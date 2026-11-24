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
    "canary_min_events": 30,    # below this many errors or escalations in the canary, a ratio is noise: wait
    "canary_error_ratio_max": 1.10,       # canary error rate at most 10% above control
    "canary_escalation_ratio_max": 1.25,  # hand-offs to people at most 25% above control
}


class GateError(Exception):
    """The gate cannot decide. That is a refusal, never a pass."""


def by_task(results):
    return {r["task"]: r for r in results}


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
    reasons = []
    reg_b, reg_c = rate(base, "regression", True), rate(cand, "regression", True)
    cap_b, cap_c = rate(base, "capability", False), rate(cand, "capability", False)
    cost_b = sum(r["cost_usd"] for r in base.values()) / len(base)
    cost_c = sum(r["cost_usd"] for r in cand.values()) / len(cand)
    lat = p95([r["latency_s"] for r in cand.values()])
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
    if can["requests"] == 0 or ctl["requests"] == 0:
        raise GateError("no canary or control traffic yet")
    if can[key] < RULES["canary_min_events"] and ctl[key] * can["requests"] / ctl["requests"] < RULES["canary_min_events"]:
        raise GateError(f"too few {key} to compare yet: wait for more traffic")
    ctl_rate = max(ctl[key], 1) / ctl["requests"]   # a control with 0 events is compared as if it had 1
    return (can[key] / can["requests"]) / ctl_rate


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
    except GateError as e:
        print("CANNOT DECIDE (treated as HOLD):", e); sys.exit(2)
