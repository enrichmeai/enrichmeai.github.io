"""Release gate for an agent: may this candidate replace the live version?

Stage 1 (offline): eval results for the candidate and the live baseline, each a list of
  {"task": id, "suite": "regression"|"capability", "trials": [true/false, ...],
   "cost_usd": float, "latency_s": float}
Stage 2 (canary): live metrics for a small share of traffic, canary vs control.
"""
import json, math, sys

RULES = {
    "regression_min": 0.95,     # the regression suite must stay this high (pass^k: every trial passes)
    "cost_growth_max": 0.20,    # cost per task may grow at most 20%
    "p95_latency_max_s": 8.0,
    "canary_min_events": 30,    # wait until the control's rate predicts this many events in the canary
    "canary_error_ratio_max": 1.10,       # canary error rate at most 10% above control
    "canary_escalation_ratio_max": 1.25,  # hand-offs to people at most 25% above control
}


class GateError(Exception):
    """The gate cannot decide. That is a refusal, never a pass."""


SUITES = {"regression", "capability"}


def number(x, what):
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x) or x < 0:
        raise GateError(f"{what} must be a finite number >= 0, got {x!r}")
    return x


def by_task(results):
    """Validate every result before any arithmetic: bad input is a refusal, not a number."""
    if not isinstance(results, list):
        raise GateError("results must be a list")
    out = {}
    for r in results:
        if not isinstance(r, dict):
            raise GateError(f"each result must be an object, got {r!r}")
        t = r.get("task")
        if not isinstance(t, str) or not t:
            raise GateError(f"each result needs a task id, got {t!r}")
        if t in out:
            raise GateError(f"duplicate task id {t!r}")
        if r.get("suite") not in SUITES:
            raise GateError(f"task {t!r} has unknown suite {r.get('suite')!r}")
        if not isinstance(r.get("trials"), list) or not all(isinstance(x, bool) for x in r["trials"]):
            raise GateError(f"task {t!r} trials must be a list of true/false")
        number(r.get("cost_usd"), f"task {t!r} cost_usd")
        number(r.get("latency_s"), f"task {t!r} latency_s")
        out[t] = r
    return out


def passed(r, all_trials):
    if not r["trials"]:
        return False                      # no results is a failure, not a pass
    return all(r["trials"]) if all_trials else any(r["trials"])


def rate(results, suite, all_trials):
    tasks = [r for r in results.values() if r["suite"] == suite]
    if not tasks:
        raise GateError(f"no {suite} tasks in the results")
    return sum(passed(r, all_trials) for r in tasks) / len(tasks)


def p95(xs):
    xs = sorted(xs)
    return xs[math.ceil(0.95 * len(xs)) - 1]      # nearest-rank percentile


def offline(base, cand):
    if base.keys() != cand.keys():
        raise GateError(f"task sets differ: {sorted(base.keys() ^ cand.keys())}")
    moved = sorted(t for t in base if base[t]["suite"] != cand[t]["suite"])
    if moved:
        raise GateError(f"tasks changed suite: {', '.join(moved)}")
    fewer = sorted(t for t in base if len(cand[t]["trials"]) != len(base[t]["trials"]))
    if fewer:
        raise GateError(f"trial counts differ from the baseline (pass^k needs the same k): {', '.join(fewer)}")
    reasons = []
    reg_b, reg_c = rate(base, "regression", True), rate(cand, "regression", True)
    cap_b, cap_c = rate(base, "capability", False), rate(cand, "capability", False)
    cost_b = sum(r["cost_usd"] for r in base.values()) / len(base)
    cost_c = sum(r["cost_usd"] for r in cand.values()) / len(cand)
    lat = p95([r["latency_s"] for r in cand.values()])
    if cost_b == 0:
        raise GateError("baseline cost is zero: cannot judge cost growth")
    print(f"regression pass^k  baseline {reg_b:.2f}  candidate {reg_c:.2f}")
    print(f"capability pass@k  baseline {cap_b:.2f}  candidate {cap_c:.2f}")
    print(f"cost per task      baseline ${cost_b:.4f}  candidate ${cost_c:.4f}")
    print(f"p95 latency        candidate {lat:.1f}s")
    failing = sorted(t for t, r in cand.items() if r["suite"] == "regression" and not passed(r, True))
    newly = [t for t in failing if passed(base[t], True)]
    if reg_c < RULES["regression_min"]:
        reasons.append(f"regression suite {reg_c:.2f} is below {RULES['regression_min']}")
    if newly:
        reasons.append(f"newly failing: {', '.join(newly)}")
    if cost_c > cost_b * (1 + RULES["cost_growth_max"]):
        reasons.append(f"cost per task grew {100 * (cost_c / cost_b - 1):.0f}%")
    if lat > RULES["p95_latency_max_s"]:
        reasons.append(f"p95 latency {lat:.1f}s is over {RULES['p95_latency_max_s']}s")
    return reasons


def ratio(m, key):
    can, ctl = m["canary"], m["control"]
    for side, d in (("canary", can), ("control", ctl)):
        number(d["requests"], f"{side} requests")
        if not number(d[key], f"{side} {key}") <= d["requests"]:
            raise GateError(f"{side} {key} exceed its requests")
    if can["requests"] == 0 or ctl["requests"] == 0:
        raise GateError("no canary or control traffic yet")
    expected = ctl[key] * can["requests"] / ctl["requests"]   # what the canary would see at the control's rate
    if expected < RULES["canary_min_events"]:
        raise GateError(f"too few {key} expected in the canary ({expected:.0f}) to compare yet: wait for more traffic")
    if can[key] == 0:
        raise GateError(f"canary reports no {key} where about {expected:.0f} were expected: check the metrics before trusting it")
    return (can[key] / can["requests"]) / (ctl[key] / ctl["requests"])


def canary(m):
    reasons = []
    err, esc = ratio(m, "errors"), ratio(m, "escalations")
    print(f"canary vs control  error ratio {err:.2f}  escalation-to-human ratio {esc:.2f}")
    if err > RULES["canary_error_ratio_max"]:
        reasons.append(f"canary error rate is {err:.2f}x control")
    if esc > RULES["canary_escalation_ratio_max"]:
        reasons.append(f"canary hands {esc:.2f}x as many cases to people")
    return reasons


if __name__ == "__main__":
    load = lambda p: json.load(open(p))
    try:
        reasons = offline(by_task(load(sys.argv[1])), by_task(load(sys.argv[2])))
        if reasons:
            print("HOLD (offline):", "; ".join(reasons)); sys.exit(1)
        if len(sys.argv) > 3:
            reasons = canary(load(sys.argv[3]))
            if reasons:
                print("ROLL BACK (canary):", "; ".join(reasons)); sys.exit(1)
            print("PROMOTE: widen the rollout")
        else:
            print("PASS offline: start a canary on a small share of traffic")
    except (GateError, KeyError, ValueError, TypeError, AttributeError, OSError, IndexError) as e:
        why = str(e) if isinstance(e, GateError) else f"bad input ({type(e).__name__}: {e})"
        print("CANNOT DECIDE (treated as HOLD):", why); sys.exit(2)
