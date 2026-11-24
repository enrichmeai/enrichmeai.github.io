# 001 Reserve stock

Owner: the product manager. Approved by: product + tech lead, before any plan.

## Why
Two customers can each be told the last unit is theirs. Checkout must hold stock
for an order line until the order is paid or abandoned.

## User story
As the checkout service, I reserve stock for an order line,
so that no unit is sold twice.

## Acceptance criteria
- AC-1: GIVEN sku A has 5 available WHEN checkout reserves 2 THEN the reply is 201 with a reservation id AND 3 remain.
- AC-2: GIVEN sku A has 1 available WHEN checkout reserves 2 THEN the reply is 409 INSUFFICIENT_STOCK AND 1 remains.
- AC-3: GIVEN a reservation made with Idempotency-Key k WHEN the same request is retried with k, one after the other or at the same moment THEN the same reservation id comes back AND stock fell once.
- AC-4: GIVEN 1 unit left WHEN 20 reservations for it arrive at once THEN exactly one succeeds.
- AC-5: GIVEN a reservation of 2 WHEN checkout releases it THEN the 2 units are available again AND a second release changes nothing.
- AC-6: GIVEN a quantity outside 1..100 WHEN checkout reserves THEN the reply is 400.
- AC-7: GIVEN key k was used to reserve 2 of sku A WHEN k is sent with a different sku or quantity THEN the reply is 422 IDEMPOTENCY_KEY_REUSED AND stock is unchanged.
- AC-8: GIVEN no sku Z exists WHEN checkout reserves Z THEN the reply is 404 UNKNOWN_SKU.

## Non-functional
- NFR-1: any number of instances can run at once. No instance keeps state in memory; the database is the record.

## Out of scope
- Expiry of abandoned reservations, and what a retry should return after its
  reservation was released: today it returns the released reservation (spec 002).
- Validating the Idempotency-Key itself (blank keys, keys over 128 characters).

## Open questions
- [NEEDS CLARIFICATION: may one order reserve the same sku twice?] Answered by product: no, use one line with the total.
