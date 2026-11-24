# Agents to Production: the release gate

The script behind <https://enrichmeai.com/well-rounded-engineer/agentprod/>. Python 3, no
dependencies. The data in `data/` is **synthetic**: results for a stand-in agent on 30
regression and 10 capability tasks, 3 trials each. No model was called.

```bash
python3 release_gate.py data/baseline.json data/candidate_good.json                       # PASS offline (exit 0)
python3 release_gate.py data/baseline.json data/candidate_regresses.json                  # HOLD: newly failing R07, R19 (exit 1)
python3 release_gate.py data/baseline.json data/candidate_good.json data/canary_ok.json    # PROMOTE (exit 0)
python3 release_gate.py data/baseline.json data/candidate_good.json data/canary_bad.json   # ROLL BACK: 1.65x hand-offs (exit 1)
python3 release_gate.py data/baseline.json data/candidate_good.json data/canary_small.json # CANNOT DECIDE, treated as HOLD (exit 2)
```

Tests: `python3 -m unittest test_release_gate` (21 tests). Each tries a way to fool the gate (mismatched
or duplicate tasks, a misspelled or moved suite, empty or non-boolean trials, NaN or negative numbers,
a tiny or silent canary, missing keys) and requires a refusal, never a pass. 11 of them failed on the
version before this one.

The thresholds in `RULES` are examples. The canary comparison waits until the control's rate predicts
at least 30 events in the canary; that guards against noise, and it is not a significance test.
