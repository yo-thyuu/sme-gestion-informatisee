# Conceptual Data Model — First Workflow

**Baseline:** accepted conceptual model for implementation planning. This is not a database schema yet; exact Python types and database storage will be learned gradually while coding. This document is the sole active data-model reference in this workspace.

## 1. `BusinessPartner`

A reusable organisation/contact record with a unique ID, name, role(s) (`supplier`, `customer`, or both), status, basic contact details and registered country/address when known.

**Future extension:** represent multiple partner locations, dispatch origins, delivery destinations and our own branches/warehouses separately. These detailed location/shipment concepts are not part of the first coding slice.

## 2. `Product` and `ProductVariant`

- `Product` identifies a general product, such as a pen.
- `ProductVariant` identifies each stock-controlled version, with a unique SKU/reference, readable name and relevant attributes such as colour, size or format.

Green and red pens have different variant IDs/SKUs. Stock is associated with the actual variant, not only a broad product name or free-text description.

## 3. `PurchaseOrder` and `PurchaseOrderLine`

- `PurchaseOrder`: order ID, supplier/`BusinessPartner` reference, order date/time, optional expected delivery, status and optional supporting notes/reference.
- `PurchaseOrderLine`: line ID, parent order, originally ordered `ProductVariant`, original quantity and line-level references.

One order can contain multiple lines. The original variant and quantity remain the historical baseline; do not rewrite an original line to make an amendment appear to have been the original order.

## 4. `OrderAmendment` and `OrderAmendmentLine`

`OrderAmendment` records a formal authorised change to one or more original requirements: ID, linked order, reason, approver name, approval timestamp and record-entry timestamp. Each `OrderAmendmentLine` links to the affected original order line and records the previous and new requirement (for example, reducing/cancelling a quantity or formally changing the required variant).

Amendments are append-only in the conceptual model. Further changes create further amendment records. A decision to keep red pens is not itself an amendment cancelling the green-pen requirement.

## 5. `GoodsReceipt` and `GoodsReceiptLine`

- `GoodsReceipt`: receipt ID, linked order, physical receipt time, entry time, receipt type, delivery-note reference when available and notes.
- `GoodsReceiptLine`: line ID, parent receipt, linked order line when applicable, **actual received variant**, physical received quantity and its disposition/quantity classification.

A receipt line identifies what physically arrived. It may link to an order line that requested a different variant, preserving the discrepancy. At finalisation, quantities are classified into non-overlapping dispositions: accepted, damaged, held pending decision, or rejected/for return. The disposition quantities must reconcile to the physical quantity. Only accepted quantities can be posted into usable stock.

Partial deliveries and replacement deliveries are new receipts. Never overwrite the first receipt to represent a later delivery.

## 6. `StockMovement`

A traceable entry affecting usable stock. Conceptual fields include movement ID, product-variant ID, signed quantity change, movement type/reason, event timestamp, entry timestamp, source receipt line when applicable, actor name when known, and optional reference to the movement being reversed/corrected.

Prevent duplicate posting for the same accepted receipt-line quantity. After posting, correct mistakes using linked reversal/correction/adjustment entries; preserve the original movement.

## 7. `ExceptionCase` and `ExceptionHistory`

- `ExceptionCase`: case ID, order reference, optional receipt where the issue was first exposed, problem type, description, affected quantity, current status, next action, optional responsible person, optional expected date, opening/update timestamps and resolution details.
- `ExceptionHistory`: a dated event linked to a case, with action/status/decision details, actor name when known, and related receipt/amendment references where relevant.

One distinct issue has one case. A case can exist before a receipt, so its receipt link may initially be empty. Later replacement/return receipts link to the relevant case. A related receipt does not automatically close a case; an authorised person confirms resolution. Case status alone never changes stock.

## Quantity and status concepts that must stay separate

- Original ordered quantity for each variant/line.
- Physical quantity received on each receipt line.
- Accepted quantity posted to usable stock.
- Quantity currently damaged, held or rejected and still requiring action.
- Quantity of the exact required variant still awaiting delivery after authorised amendments.
- Open exception cases and their status, independently of order completion.

A substitute does not silently reduce the outstanding quantity of the original variant. Displays should be derived from original requirements, authorised amendments and receipt facts—not from an exception status alone.

## Core relationships

- One partner can have many orders and can act as supplier and/or customer.
- One order has one or more order lines.
- One order line can have several amendment entries and receipt lines over time.
- One order can have multiple receipts, including partial and replacement receipts.
- One receipt has one or more receipt lines.
- A receipt line identifies the actual variant and may reference the order line it was intended to fulfil.
- A correctly posted accepted receipt-line quantity creates a stock movement; duplicate posting is blocked.
- One order can have multiple independent exception cases; each case can have multiple dated history events.

## Deferred international concepts

The architecture must not confuse (1) a partner's registered/legal country and address, (2) a warehouse/dispatch origin, (3) a delivery destination, and (4) our own organisation's sites. Add reusable location and shipment references when needed. Currency, national identifiers, tax/customs/legal automation, multi-user synchronisation and detailed access controls are deferred until studied and justified.

## Implementation order

Although the conceptual model supports multiple order lines, begin with one line in the exercises. Add records and basic validation, then receipt and actual variant, then disposition/stock posting, then exception/history, then authorised amendment. Test each slice before expanding.
