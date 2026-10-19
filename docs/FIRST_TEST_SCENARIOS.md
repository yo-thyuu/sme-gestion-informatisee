# First Workflow Test Scenarios

These are expected-behavior examples to use as the implementation grows. They are not automated tests yet.

1. **Partial and damaged delivery:** order 10 green pens; receive 8; accept 7 and classify 1 as damaged. Stock increases by 7 green pens once; 2 green pens remain physically outstanding; separate missing and damage cases are tracked.
2. **Remaining goods arrive:** receive and accept the 2 missing green pens in a new receipt. Stock increases by 2; the missing case can be closed after authorised confirmation while the damage case may remain open.
3. **Replacement arrives:** receive one accepted replacement as a new receipt linked to the damage case; increase stock by 1; preserve the original damaged receipt.
4. **Wrong variant:** order 10 green pens but receive 10 red pens. Record red as the actual variant. Accepted red pens enter red stock; green stays outstanding until a formal owner-authorised amendment changes the requirement.
5. **Duplicate posting:** posting the accepted quantity of one receipt line twice must not create a second stock increase.
6. **Posted correction:** preserve an incorrect posted movement and add a traceable correction/reversal.
7. **No automatic case closure:** a related receipt may support resolution but does not close a case without an authorised confirmation.
8. **Overdue case:** an open case whose expected action date has passed can be flagged overdue; a date estimate must not be described as a confirmed supplier promise.
