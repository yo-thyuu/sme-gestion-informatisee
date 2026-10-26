# Business Rules — Orders, Receiving, Stock and Exceptions

**Baseline:** current design rules for the fictional pilot. These are project decisions, not legal, tax or accounting advice.

## Products, partners and orders

- **RG-01 — Reusable partner:** an order references a `BusinessPartner`; a partner may be a supplier, customer or both.
- **RG-02 — Distinct variant:** each stock-controlled `ProductVariant` has a unique reference/SKU. Green and red pens are different variants.
- **RG-03 — Multiple order lines:** an order can contain multiple lines, each with its own required variant and original quantity.
- **RG-04 — Preserve original requirement:** the original order line remains historical fact. A formal change is an authorised, append-only amendment that records the old and new requirement, approver, time and reason.

## Receiving and stock

- **RG-05 — An order is not stock:** placing an order or receiving an expected-date promise does not increase usable stock.
- **RG-06 — Actual receipt facts:** record the physical receipt and the actual variant that arrived, even when it differs from the ordered variant.
- **RG-07 — Classify without double-counting:** finalised physical receipt quantities must have non-overlapping dispositions (accepted, damaged, held pending decision, or rejected/for return) that reconcile to the received quantity.
- **RG-08 — Accepted stock only:** only properly accepted and posted goods increase usable stock, under the actual variant.
- **RG-09 — No duplicate posting:** posting an accepted receipt-line quantity twice must not increase stock twice.
- **RG-10 — Explain movements:** movements include product variant, signed quantity, timestamp, movement type/reason and source reference.
- **RG-11 — Trace correction:** after posting, correct through linked reversal/adjustment records; preserve the original movement and record reason, actor and time where known.
- **RG-12 — Separate quantities:** ordered, physically received, accepted, damaged/held/rejected and still-outstanding values are distinct; disposition buckets cannot double-count units.

## Substitutions and amendments

- **RG-13 — A substitute is its actual variant:** a different item never enters stock under the ordered variant's identity.
- **RG-14 — Substitution is not amendment:** authorising the shop to keep a substitute does not satisfy or cancel the original requirement.
- **RG-15 — Owner-authorised change:** the original requirement changes only after a separate formal amendment explicitly approved by the owner and retained in history.
- **RG-16 — Outstanding calculation:** a wrong variant does not reduce the original variant's required quantity unless a formal amendment changes that requirement.

## Exceptions and history

- **RG-17 — One case per distinct issue:** missing quantity, damage and wrong-variant discrepancies may be separate cases on the same order.
- **RG-18 — Link evidence:** cases link to the order, the receipt that revealed the issue when available, and later related receipts such as replacements or returns.
- **RG-19 — Case history:** retain dated significant actions, status changes, decisions, follow-up and resolution. The first prototype records actor names; it does not provide secure authentication.
- **RG-20 — Independent case status:** resolving one case does not resolve another case automatically.
- **RG-21 — Explicit case resolution:** a related receipt may suggest resolution, but an authorised person must confirm the outcome before closing the case.
- **RG-22 — Case state does not change stock:** opening, updating or resolving a case does not itself create stock movements.
- **RG-23 — Actual versus expected time:** distinguish event, entry, expected, expectation-confirmed and resolution timestamps. Unknown dates remain unknown.
- **RG-24 — Overdue follow-up:** open cases whose expected dates have passed can be identified, and confirmed expectations are distinguished from estimates.

## International partner future requirement

- **RG-25 — Separate location meanings:** partner registered address/country, shipment dispatch origin, delivery destination and our own operating locations are distinct. Detailed routing is phased in.
- **RG-26 — Verify regulated rules:** currency, tax, customs, accounting and legal automation must be studied and verified before implementation.

## Stock example

The shop orders 10 green pens and 10 red pens arrive. If the owner authorises keeping the red pens, any accepted stock movement records **red pens**. The 10 green pens remain outstanding unless the owner separately approves and the system records a formal amendment. If an amendment later cancels the green requirement, preserve both the original requirement and the amendment history.
