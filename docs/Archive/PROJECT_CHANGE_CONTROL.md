# Project Change Control

This is a lightweight process for changing this learning project. It is **not** an application module for end users.

## Baseline and scope

The current direction is a modular management information system, beginning with a fictional stationery shop and a purchasing/receiving/usable-stock/exception workflow. Exception management is part of this workflow; a generic business change-management module is out of the current product scope.

The first-workflow design checkpoint is closed. Do not reopen broad feature brainstorming just because a new idea appears. A change is considered when implementation/tests reveal a genuine gap, learning scope becomes unreasonable, a material requirement appears, or an instructor requirement requires it.

## Change process

1. Describe the scenario and the reason for the change.
2. Record the proposal and status: `Proposed`, `Accepted`, `Deferred` or `Rejected`.
3. Check effects on stock accuracy, record history, the data model, requirements, tests and learning scope.
4. Decide before editing; mentioning an idea is not approval.
5. Update the one authoritative document for the affected topic rather than creating a duplicate version.
6. Add or adjust a test scenario that proves the expected behavior.
7. Verify the code and record substantial changes in `CHANGELOG.md`.
8. Use Git commits for checkpoints once Git is configured. Create a ZIP only at a meaningful milestone or before a risky change—not for every lesson.

## Confirmed change records

- **Wrong item/variant (accepted for design):** record the actual variant; separate order/receipt lines; distinguish acceptance/hold/rejection; use a formal amendment to change the original requirement. Implementation and tests remain pending.
- **International partners/locations (accepted long-term direction):** reuse `BusinessPartner`; keep registered address, dispatch origin, delivery destination and our operating sites distinct. Detailed location routing and country-specific rules are deferred.

## Domain distinction

An **exception case** tracks an operational discrepancy such as missing/damaged goods through evidence, follow-up and resolution. **Project change control** tracks a proposed change to this software or its rules. They are related but not interchangeable.
