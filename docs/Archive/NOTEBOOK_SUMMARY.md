# Notebook Summary — Système Modulaire de Gestion Informatisée

**Project folder:** `Project_02_SME_Management_System`  
**Workspace baseline:** 1.0 (consolidated documentation plus minimal Python starter)  
**Current phase:** begin the first working Python prototype

## 1. Project identity and purpose

The project is called **Système Modulaire de Gestion Informatisée** (*Modular Management Information System*). Its long-term purpose is to develop a modular system that helps small and medium-sized organisations manage operational information, records, stock, documents, follow-up and reports while preserving traceable history.

This project has two connected goals:

1. **Learning goal:** learn to analyse, model, build, test and improve business software by writing and understanding the code rather than copying a finished application.
2. **Product exploration goal:** find out later whether the resulting solution helps real organisations. Commercial success and market demand have not been established; they must be tested with potential users.

This ILEIC project stays separate from Continuity Workspace and the personal IT learning roadmap.

## 2. Long-term vision and boundaries

The system may eventually support different modules for different organisations—for example, purchasing and stock for a shop, enrolments for a training centre, membership records for an association, or purchases and sales for a cooperative. These are examples of future possibilities, not a promise to build every module.

The architecture should distinguish a partner's identity and registered address from where goods are dispatched, where they are delivered, and where our own branches, shops, offices or warehouses operate. For example, a supplier may be registered in China, goods may be dispatched from Germany, and the delivery may arrive in Morocco. These are different facts.

A reusable `BusinessPartner` record for suppliers/customers is accepted in the conceptual design. Detailed multiple locations and shipment routing will be implemented later, only when a workflow needs them. Currency conversion, customs/tax/legal automation, payroll, full accounting, advanced access permissions, multi-user synchronisation and cloud/SaaS hosting are outside the first prototype. International partners do not require cloud storage; local-first storage remains an option.

## 3. Pilot organisation and first workflow

The pilot is a **fictional stationery and office-supplies shop** (*papeterie et fournitures de bureau*). We use fictional data only. The first workflow is:

**Purchase order → physical goods receipt → disposition/acceptance → usable-stock movement → exception follow-up and resolution.**

Supplier discrepancy tracking is one workflow within the larger system, not the identity of the entire project. The initial scenarios include full and partial deliveries, missing quantities, damaged goods, wrong variants, substitutions, replacements and authorised order amendments.

## 4. Confirmed business rules

- Preserve original orders, receipts and posted stock movements. Record authorised amendments and post-entry corrections separately.
- A substitute does not automatically fulfil or cancel the original requirement. The original product/variant remains outstanding until the owner explicitly authorises a formal amendment.
- Record the actual product/variant received. Red pens received instead of green pens remain red pens in stock.
- A purchase order or expected delivery does not add usable stock. Only properly accepted and posted quantities affect usable stock.
- Prevent duplicate stock posting. Correct an already-posted mistake with a traceable reversal/correction instead of silently deleting the original movement.
- Each distinct problem has its own exception case. A case's status does not itself change stock, and one case's resolution does not automatically resolve another.
- A replacement is a new receipt linked to the relevant case. A related receipt does not automatically close the case.
- Keep event time, record-entry time, expected time and resolution time distinct. Unknown information stays unknown.
- International partner identity, registered address, dispatch origin, destination and our own operating locations are separate concepts.

## 5. Accepted conceptual design

The accepted conceptual model includes:

- `BusinessPartner` — supplier, customer or both;
- `Product` and `ProductVariant` — variants have distinct stock references/SKUs;
- `PurchaseOrder` and `PurchaseOrderLine` — orders support multiple lines;
- `OrderAmendment` and `OrderAmendmentLine` — separately record authorised changes;
- `GoodsReceipt` and `GoodsReceiptLine` — record what physically arrived and its actual variant;
- `StockMovement` — traceable change to usable stock;
- `ExceptionCase` and `ExceptionHistory` — distinct issues and dated history.

The accepted recommendations are documented in `DESIGN_DECISIONS.md`, with the current conceptual structure in `DATA_MODEL.md`. They are design defaults for this learning project—not evidence that potential customers have validated every feature. If implementation/testing exposes a genuine contradiction or a material missing rule, we can make a controlled change.

## 6. How we will learn and build

For each implementation slice:

1. Understand the business rule and the problem it solves.
2. Learn the relevant Python concept before writing it.
3. Predict what the code should do.
4. Type the code in PyCharm and run it.
5. Test normal and failure scenarios, observe errors and debug them.
6. Explain what the code does and change it yourself.
7. Expand only when the current slice is understood and tested.

A document is not proof that software works, and a program that runs is not proof that the business rules are correct. We need both understanding and tests. A milestone is complete when I can explain the behavior, apply it to a new scenario and verify it—not merely because I watched a course or the program starts.

## 7. Project phases

These are project milestones, **not official ILEIC semester/module names**.

1. **Project framing — established:** purpose, long-term direction, boundaries and fictional pilot.
2. **Requirements and business rules — checkpoint closed:** partial deliveries, damage, missing goods, replacements, stock rules, exceptions, substitutions and history.
3. **Data modelling — conceptual baseline accepted:** variants, order/receipt lines, amendments, stock movements, cases/history and partner foundation. Validate through coding and tests.
4. **First Python prototype — current phase:** build the console entry point and then model one purchase-order line at a time.
5. **Testing and improvement:** verify partial/damaged deliveries, wrong variants, duplicate posting, correction history, amendments and case resolution.
6. **Progressive expansion:** add richer location handling, stock exits/sales, documents, invoices or reports only when the first workflow works and real requirements justify them.
7. **Documentation and presentation:** produce a user explanation, test evidence and limitations; confirm PFE/report/presentation requirements with the instructor.
8. **Product validation and deployment exploration:** consult potential users, study security/backups/maintenance and evaluate deployment only after validating actual needs.

## 8. Current status and next step

The project vision, pilot workflow, finite design questionnaire and recommended design defaults are established. The ZIP now contains one authoritative file per design topic and a minimal runnable `main.py`. The purchasing/receiving workflow itself is **not implemented yet**.

**Next:** open `main.py` in PyCharm, run the starter and inspect its output. Then learn the parts of the program and make the first small change before introducing purchase-order data. See `PROJECT_STATUS.md` for the immediate learning checkpoint and `PROJECT_ROADMAP.md` for the full sequence.
