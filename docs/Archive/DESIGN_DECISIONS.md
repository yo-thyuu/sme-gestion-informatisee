# Accepted Design Decisions — First Workflow

**Decision checkpoint:** 17 October 2026  
**Status:** recommended defaults accepted; implementation and tests still pending.  
**Scope:** first purchasing/receiving/stock/exception workflow.

The learner approved these recommendations as the best-fit starting defaults. They are the current design baseline, not immutable laws. Revisit them only if implementation/testing exposes a real contradiction, the learning scope becomes unreasonable, or a material real-user requirement justifies a change. Approval does not prove market demand.

## Accepted decisions

1. **Multiple order lines:** one purchase order can contain multiple product/variant lines. Learning still proceeds one line at a time.
2. **Variant identity:** every stock-controlled variant has a unique SKU/reference, display name and relevant attributes.
3. **Actual received item:** every receipt line records the actual variant received and links to the intended order line where applicable. A mismatch never silently satisfies the original requirement.
4. **Receipt classification:** finalised physical quantities have a clear, non-overlapping disposition: accepted, damaged, held pending decision, or rejected/for return. Totals must reconcile to the physical quantity. Only accepted quantities can be posted to usable stock.
5. **Case suggestion:** software flags likely discrepancies and suggests a case; a person confirms/edits the case and makes the business decision.
6. **Exception history:** retain the current case state plus dated history for significant actions, status changes, decisions and resolution. First prototype records actor names, not authenticated identities.
7. **Case links:** link cases to the order, the receipt that exposed the problem when available, and later related receipts such as replacements/returns.
8. **Manual resolution confirmation:** a related receipt may suggest resolution but does not close a case automatically; an authorised person records the outcome.
9. **Separate amendment:** keeping a substitute and formally amending an order are different. A formal amendment preserves the original order and records old/new requirements, reason, approver and timestamp.
10. **Separate quantities:** distinguish required-variant quantity still awaiting delivery, accepted usable stock, quantities damaged/held/rejected for action, and open cases. Cases do not define order completion.
11. **Traceable corrections:** drafts may be corrected before posting; after posting, preserve the original movement and add a linked reversal/correction/adjustment with reason, actor and timestamp. Prevent duplicate posting.
12. **Minimum fields:** use the proposed minimum/optional fields in the design closure. Do not invent unknown expected dates. Record entry times automatically; require resolution details when closing a case.
13. **Actor representation:** defer full login and permission management in the first console prototype. Explicitly record the responsible/approving person's name and action; design proper authentication later.
14. **International partner architecture:** a reusable `BusinessPartner` can be a supplier, customer or both. Distinguish registered identity/address, dispatch origin, delivery destination and our own operating sites. Implement the minimum partner identity first; detailed locations and country-specific automation are deferred.

## Consequences

- The conceptual model contains `BusinessPartner`, `Product`, `ProductVariant`, `PurchaseOrder`, `PurchaseOrderLine`, `OrderAmendment`, `OrderAmendmentLine`, `GoodsReceipt`, `GoodsReceiptLine`, `StockMovement`, `ExceptionCase` and `ExceptionHistory`.
- Detailed location/shipment routing is a long-term requirement, not part of the first executable slice.
- The finite design-closure questionnaire is complete; we do not repeat it or restart broad feature brainstorming.
- The first prototype records names but does not claim names are secure authentication.
- Market validation remains a later phase. The project must not claim that potential users want all proposed features until feedback supports it.
