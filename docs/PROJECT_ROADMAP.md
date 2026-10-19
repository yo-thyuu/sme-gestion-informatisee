# Project Roadmap — Working Milestones

These milestones describe our project, not official ILEIC semesters or module names. A phase is complete when its outcomes can be explained and tested, not merely when documentation or code exists.

## Phase 0 — Project framing: established
- [x] Define long-term vision and separate learning/product-exploration goals.
- [x] Choose the fictional stationery and office-supplies pilot.
- [x] Choose the first purchasing/receiving/usable-stock/exception workflow.
- [x] Keep exception management inside the larger system.
- [ ] Confirm school/PFE requirements with the instructor when appropriate.

## Phase 1 — Requirements and business rules: checkpoint closed
- [x] Practise full/partial delivery, damage, missing quantity and replacement scenarios.
- [x] Distinguish physical receipt, accepted stock, disposition and outstanding requirements.
- [x] Distinguish actual from expected timestamps.
- [x] Confirm independent cases and preserved history.
- [x] Confirm that substitution does not cancel the original requirement without the owner's formal amendment.
- [x] Accept the finite set of recommended design defaults.

## Phase 2 — Data modelling: conceptual baseline accepted
- [x] Model partner identity, product variants, multi-line orders and actual receipt lines.
- [x] Model formal order amendments separately from original requirements.
- [x] Model stock movements and duplicate-posting/correction safeguards.
- [x] Model exception cases and dated case history.
- [x] Record future international location requirements without expanding the first executable slice.
- [ ] Validate the model through implementation and tests; adjust only for a genuine contradiction or gap.

## Phase 3 — First working Python prototype: current
- [x] Open the consolidated project in PyCharm and run `main.py`.
- [x] Understand the entry point, function call and `if __name__ == "__main__"` guard.
- [x] Represent one purchase order and one line in Python.
- [ ] Add simple validation and clear output.
- [ ] Add physical receipt, actual variant and disposition.
- [ ] Calculate accepted stock and prevent duplicate posting.
- [ ] Add exception cases/history and authorised amendments in small increments.

## Phase 4 — Testing and improvement
- [ ] Test full/partial deliveries, damaged goods, delayed items and replacement receipts.
- [ ] Test wrong-variant receipt and accepted substitute without cancelling the original requirement.
- [ ] Test formal amendments and outstanding-quantity calculations.
- [ ] Test duplicate posting, correction/reversal and case-closure rules.
- [ ] Test overdue follow-up and retained history.

## Phase 5 — Progressive expansion
- [ ] Add richer partner locations/shipment routing when a workflow needs it.
- [ ] Explore returns, stock exits/sales and reports after receiving is reliable.
- [ ] Consider invoices, payments and accounting-related workflows only when requirements/coursework justify them.
- [ ] Study backups, security, permissions, multi-user needs and deployment before implementing them.

## Phase 6 — Documentation and presentation
- [ ] Prepare a user guide and technical explanation.
- [ ] Demonstrate the business need, workflow, output, test evidence and limitations.
- [ ] Confirm school-specific report, PFE and presentation requirements with the instructor.

## Phase 7 — Product validation and deployment exploration
- [ ] Interview potential users and study their current workarounds.
- [ ] Test whether the solution helps other kinds of organisations and identify what is genuinely reusable.
- [ ] Evaluate commercial viability and secure deployment only after validating user needs.

## Teaching guardrail

Teach the required concept before code, let the learner type and explain it, and test realistic behavior. Do not restart broad design questioning. Revisit the model only when implementation/testing finds a genuine contradiction or material gap.
