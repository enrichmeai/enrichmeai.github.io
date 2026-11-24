"""Every way the gate can be fooled must end in HOLD, ROLL BACK or CANNOT DECIDE, never PASS or PROMOTE."""
import copy, json, math, subprocess, sys, unittest
from pathlib import Path

HERE = Path(__file__).parent
DATA = HERE / "data"
load = lambda n: json.loads((DATA / n).read_text())


def run(tmp, base, cand, canary=None):
    files = []
    for name, obj in (("b.json", base), ("c.json", cand), ("k.json", canary)):
        if obj is not None:
            p = Path(tmp) / name
            p.write_text(json.dumps(obj))
            files.append(str(p))
    r = subprocess.run([sys.executable, "-I", str(HERE / "release_gate.py"), *files], capture_output=True, text=True)
    return r.returncode, r.stdout + r.stderr


class Gate(unittest.TestCase):
    def setUp(self):
        import tempfile
        self.tmp = tempfile.mkdtemp()
        self.base, self.good = load("baseline.json"), load("candidate_good.json")
        self.ok = load("canary_ok.json")

    def assertRefuses(self, base, cand, canary=None):
        code, out = run(self.tmp, base, cand, canary)
        self.assertNotEqual(code, 0, out)
        self.assertNotIn("Traceback", out)

    # the documented paths
    def test_good_candidate_passes_offline(self):
        self.assertEqual(run(self.tmp, self.base, self.good)[0], 0)

    def test_good_canary_promotes(self):
        self.assertEqual(run(self.tmp, self.base, self.good, self.ok)[0], 0)

    def test_bad_canary_rolls_back(self):
        self.assertEqual(run(self.tmp, self.base, self.good, load("canary_bad.json"))[0], 1)

    def test_regression_is_held(self):
        self.assertEqual(run(self.tmp, self.base, load("candidate_regresses.json"))[0], 1)

    # inputs that once slipped through
    def test_task_sets_must_match(self):
        self.assertRefuses(self.base[1:], self.good)

    def test_empty_trials_fail(self):
        c = copy.deepcopy(self.good); c[0]["trials"] = []
        self.assertRefuses(self.base, c)

    def test_string_trials_are_rejected(self):
        c = copy.deepcopy(self.good); c[0]["trials"] = ["false", "false", "false"]
        self.assertRefuses(self.base, c)

    def test_nan_cost_is_rejected(self):
        c = copy.deepcopy(self.good); c[0]["cost_usd"] = math.nan
        self.assertRefuses(self.base, c)

    def test_nan_latency_is_rejected(self):
        c = copy.deepcopy(self.good)
        for r in c: r["latency_s"] = math.nan
        self.assertRefuses(self.base, c)

    def test_negative_values_are_rejected(self):
        c = copy.deepcopy(self.good); c[0]["latency_s"] = -5; c[1]["cost_usd"] = -1
        self.assertRefuses(self.base, c)

    def test_unknown_suite_is_rejected(self):
        c = copy.deepcopy(self.good); c[0]["suite"] = "regresion"
        self.assertRefuses(self.base, c)

    def test_task_may_not_change_suite(self):
        c = copy.deepcopy(self.good); c[0]["suite"] = "capability"
        self.assertRefuses(self.base, c)

    def test_duplicate_task_ids_are_rejected(self):
        c = copy.deepcopy(self.good); c.append(copy.deepcopy(c[0]))
        self.assertRefuses(self.base, c)

    def test_missing_suite_is_refused(self):
        self.assertRefuses([r for r in self.base if r["suite"] == "regression"],
                           [r for r in self.good if r["suite"] == "regression"])

    def test_zero_baseline_cost_is_refused_not_crashed(self):
        b = copy.deepcopy(self.base)
        for r in b: r["cost_usd"] = 0
        self.assertRefuses(b, self.good)

    # canary
    def test_tiny_canary_waits(self):
        self.assertRefuses(self.base, self.good, load("canary_small.json"))

    def test_zero_traffic_waits(self):
        k = copy.deepcopy(self.ok); k["canary"]["requests"] = 0
        self.assertRefuses(self.base, self.good, k)

    def test_zero_control_events_waits(self):
        k = copy.deepcopy(self.ok); k["control"]["errors"] = 0
        self.assertRefuses(self.base, self.good, k)

    def test_negative_canary_counts_are_rejected(self):
        k = copy.deepcopy(self.ok); k["canary"]["errors"] = -100
        self.assertRefuses(self.base, self.good, k)

    def test_nan_canary_counts_are_rejected(self):
        k = copy.deepcopy(self.ok); k["canary"]["errors"] = math.nan
        self.assertRefuses(self.base, self.good, k)

    def test_more_events_than_requests_is_rejected(self):
        k = copy.deepcopy(self.ok); k["canary"]["errors"] = 7000
        self.assertRefuses(self.base, self.good, k)

    def test_fewer_trials_than_baseline_is_refused(self):
        c = copy.deepcopy(self.good)
        for r in c: r["trials"] = r["trials"][:1]
        self.assertRefuses(self.base, c)

    def test_missing_task_id_is_refused(self):
        b = copy.deepcopy(self.base); c = copy.deepcopy(self.good)
        del b[0]["task"]; del c[0]["task"]
        self.assertRefuses(b, c)

    def test_non_object_entry_is_refused_not_crashed(self):
        self.assertRefuses(self.base, [1] + self.good[1:])

    def test_silent_canary_is_refused(self):
        k = copy.deepcopy(self.ok); k["canary"]["errors"] = 0; k["canary"]["escalations"] = 0
        self.assertRefuses(self.base, self.good, k)

    def test_missing_canary_key_is_refused_not_crashed(self):
        k = copy.deepcopy(self.ok); del k["canary"]["escalations"]
        self.assertRefuses(self.base, self.good, k)


if __name__ == "__main__":
    unittest.main()
