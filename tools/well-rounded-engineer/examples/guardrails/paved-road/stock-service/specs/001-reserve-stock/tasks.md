# Tasks for 001 (from the approved plan, not included here; [P] = can run in parallel)
T1      schema.sql: stock, reservation (unique idempotency_key)        AC-1..8
T2 [P]  tests AC-1, AC-2, AC-6, AC-8 over HTTP; see them fail          AC-1, AC-2, AC-6, AC-8
T3 [P]  tests AC-3 retry and same-key race, AC-5 release; see fail     AC-3, AC-5
T4 [P]  test AC-4: 20 racers, one unit; see it fail                     AC-4
T5 [P]  test AC-7: key reused for a different request; see it fail     AC-7
T6      ReservationService: claim key, then conditional UPDATE         after T1..T5
T7      ReservationController: 201/200/404/409/422/400, problem details after T6
T8      gates: mvn test, trace_check.py; reviewer agent against spec   after T7
