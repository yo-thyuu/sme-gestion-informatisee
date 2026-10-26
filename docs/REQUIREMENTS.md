# Requirements — Purchasing, Receiving, Stock and Exception Tracking

**Status:** current functional baseline for implementation planning. These are project requirements, not official ILEIC requirements. Use fictional data.

## Functional requirements

- **EF-01 — Business partner identity:** record a reusable business partner with a unique ID and role(s), including supplier and/or customer. Keep registered country/address distinct from future shipment/operating locations.
- **EF-02 — Product/variant identity:** identify stock-controlled variants with unique SKUs/references and readable names/attributes.
- **EF-03 — Multi-line purchase order:** record an order with one or more lines, each linked to a required variant and original quantity; record order date and expected delivery when known.
- **EF-04 — Formal order amendment:** preserve the original requirement and separately record every authorised amendment with affected line, previous/new requirement, reason, approver and date/time.
- **EF-05 — Actual goods receipt:** record each physical receipt separately, including partial/replacement receipts, event time, entry time, order link and delivery-note reference when available.
- **EF-06 — Actual variant on receipt:** identify the variant physically received separately from the ordered variant. A mismatch is visible and does not silently fulfil the original requirement.
- **EF-07 — Classify receipt quantity:** at finalisation, reconcile the physical quantity into non-overlapping dispositions (accepted, damaged, held pending decision, rejected/for return).
- **EF-08 — Post usable stock once:** only accepted quantities enter usable stock through traceable stock movements linked to receipt lines. Prevent duplicate posting.
- **EF-09 — Preserve correction history:** drafts can be corrected before posting. After posting, record linked reversals/corrections/adjustments with reasons, actor and timestamp; retain the original movement.
- **EF-10 — View stock history:** show variant, signed quantity, movement type/reason, time and relevant source reference.
- **EF-11 — Detect and confirm discrepancies:** suggest cases for likely problems such as missing quantity, damage or variant mismatch; allow a person to confirm/edit the case.
- **EF-12 — One case per distinct issue:** create one exception case per distinct problem, linked to the order and relevant receipt when available.
- **EF-13 — Case actions/history:** retain current status and dated history of significant status changes, actions, decisions, follow-up and resolution. Record actor name in the first prototype; defer real authentication.
- **EF-14 — Link related receipts:** link later replacement/return receipts to the case they address while retaining the original receipt.
- **EF-15 — Explicit resolution:** a related receipt does not close a case automatically. An authorised person confirms and records the resolution; cases on the same order remain independent.
- **EF-16 — Correct time semantics:** distinguish event, record-entry, expected, expectation-confirmation and resolution times. Unknown dates remain unknown.
- **EF-17 — Separate operational states:** display usable stock, exact required-variant quantity still awaiting delivery after amendments, held/damaged/rejected quantities needing action, and open cases separately.
- **EF-18 — Substitution handling:** record the actual substitute separately. Keeping a substitute does not satisfy/cancel the original requirement; only a separate owner-authorised amendment changes it.
- **EF-19 — Overdue follow-up:** identify open cases whose expected action dates have passed, and distinguish confirmed expectations from estimates.
- **EF-20 — International partner foundation:** plan reusable supplier/customer identity across countries. Registered address, dispatch origin, delivery destination and our own sites are distinct. Detailed location/routing behavior is phased in.

## Acceptance scenarios

### A. Partial delivery with damage
Given 10 green pens ordered, 8 green pens arrive, 7 are accepted and 1 is damaged: record 8 received, classify 7 accepted and 1 damaged, post +7 green pens once, show 2 green pens awaiting delivery, and create separate missing-quantity (2) and damage (1) cases.

### B. Missing quantity arrives later
When the remaining 2 green pens arrive and are accepted, record a new receipt, post +2 green pens, reduce the original green requirement awaiting physical delivery to zero, and resolve only the missing-quantity case after authorised confirmation. A separate damage case can remain open.

### C. Replacement arrives
When one accepted replacement for the damaged pen arrives, record a new receipt linked to the damage case and post +1 usable green pen. Preserve the original damaged receipt. The damage case may close after authorised confirmation.

### D. Wrong variant received
Given an order for 10 green pens, if 10 red pens arrive, record red as the actual variant and create/confirm a variant-mismatch case. Do not count red as green. If red is authorised into usable stock, post it as red. The green requirement remains outstanding unless the owner separately authorises a formal amendment.

### E. Explicit amendment
If the owner later cancels the original green-pen requirement, preserve the original order line and create a separate amendment showing the previous/new requirement, reason, approver and timestamp. The displayed remaining requirement reflects the amendment while history remains available.

### F. Duplicate posting/correction
Posting the same accepted receipt line twice must not increase stock twice. If a posted movement is wrong, preserve it and create a linked traceable correction/reversal.

### G. Expected date passes
An open case with an expected action date in the past is shown as overdue. No stock changes until real accepted goods are posted.

## Deliberately deferred

Detailed multi-location shipment routing and warehouse transfers; currency conversion and national identifiers; customs/tax/legal automation; full sales, invoicing, payments, accounting and reporting modules; user login and secure permissions; multi-user synchronisation and notifications; database selection beyond a local-first approach; desktop GUI, cloud/SaaS hosting and deployment.

Validate future product features with real potential users rather than assuming the design defaults prove market demand.
