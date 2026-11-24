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

The thresholds in `RULES` are examples. The minimum-events rule guards against noise; it is not
a significance test.
