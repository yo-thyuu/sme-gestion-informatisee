# Business Process — Receiving Goods and Resolving Delivery Exceptions

**Baseline:** accepted process design for the fictional pilot. This describes project behavior, not a substitute for checking legal/accounting requirements.

## Purpose

Record the supplier order, the goods that physically arrive, accepted usable stock and the resolution of each discrepancy without erasing original facts.

## Workflow

1. Select or create the supplier from reusable `BusinessPartner` records.
2. Record a purchase order with one or more lines. Each line identifies the required product variant and original quantity.
3. When goods physically arrive, create a new `GoodsReceipt` and its receipt lines. Record the actual variant, physical quantity, event time and entry time; keep delivery-document references where available.
4. Classify received units into non-overlapping current dispositions: accepted, damaged, held pending a decision, or rejected/for return. The categories must reconcile to the physical quantity without double-counting.
5. Compare actual variants and quantities with the order lines. The system may flag a likely discrepancy and suggest a case; a person confirms or edits the case.
6. Only accepted quantities can be posted to usable stock. Each stock movement records the actual variant and its source receipt line. Prevent duplicate posting.
7. Create separate cases for distinct problems. Link each case to the order and, when available, the receipt that exposed the problem. Preserve dated history, actions, expected dates, decisions and actor names.
8. For an incorrect variant, an authorised person decides whether to hold, return, exchange or keep it as a substitute. Record the actual variant received.
9. If the owner formally changes the original requirement, create a separate `OrderAmendment`; do not rewrite the original order line. Without a formal amendment, the original variant requirement remains outstanding.
10. Record later deliveries and replacements as new receipts. Link relevant receipts to their cases.
11. Correct posted stock mistakes with linked reversals/corrections/adjustments. Do not silently delete or rewrite the original stock movement.
12. Close a case only after an authorised person confirms and records the actual resolution. A receipt or a status change alone never changes usable stock.

## Quantity and time distinctions

Keep original ordered quantity, actual physical receipt, current receipt disposition, accepted posted stock and the required-variant quantity still awaiting delivery after authorised amendments separate. Also distinguish event time, entry time, expected date/time, expectation confirmation and resolution time.

## International partner foundation

A supplier's registered country/address must not stand in for the shipment's dispatch origin or delivery destination. The future model must also represent our own operating sites separately. Detailed location and routing behavior belongs to a later phase; it does not delay the first receiving workflow.
