# Project Status and Learning Handoff

**Last consolidated:** 17 October 2026  
**Active folder:** `Project_02_SME_Management_System`  
**Current phase:** first Python console prototype

## Learning already completed

The learner has practised:

- distinguishing purchase orders from physical goods receipts;
- partial deliveries and accepted vs. damaged quantities;
- calculating quantities outstanding and accepted stock;
- replacement deliveries as new receipts;
- separate exception cases with independent status;
- linking a case to its purchase order and relevant receipt (for example, `EX-002` links to `PO-001` and `GR-001`);
- distinguishing expected dates from actual events and event time from entry time;
- understanding that a case status does not itself change stock;
- keeping a substitute distinct from the originally ordered variant and requiring an owner-authorised formal amendment to alter the original requirement.

## Design checkpoint

The finite design-closure questionnaire was completed and its recommended defaults accepted. `DESIGN_DECISIONS.md`, `DATA_MODEL.md`, `REQUIREMENTS.md`, `BUSINESS_PROCESS.md` and `BUSINESS_RULES.md` are the single active sources for their respective topics. The older overlapping versions have been removed from this consolidated workspace to prevent conflicting instructions.

## Current implementation status

- `main.py` exists and is a minimal runnable console starter.
- The purchasing/receiving workflow is **not implemented**.
- Automated tests are **not yet included**; we will write them when we have a small behavior worth testing.
- No third-party libraries are needed at this stage.
- Python is already installed on the learner's computer. Configure/select the local interpreter in PyCharm; never include `.venv` in a ZIP.

## Immediate next step

Run `main.py` in PyCharm and check that the console displays the project title and starter message. The first lesson is to understand the entry point, `main()` function, `print()` calls and main guard. Then make one small change and explain what it does before we model a purchase order.

## Teaching and continuity instructions

- This chat/project is exclusively for ILEIC Gestion Informatisée. Do not merge it with Continuity Workspace or the personal IT roadmap.
- Use English explanations; include French business vocabulary when useful.
- Explain a concept before asking the learner to type code. Do not paste the complete application.
- Work one implementation slice at a time. Ask the learner to predict, run, inspect, debug, modify and explain behavior.
- Do not ask settled design questions again or restart feature brainstorming.
- Never claim a feature is implemented just because it exists in a design document.
- Use fictional data and confirm formal academic/PFE requirements with the instructor.
- Do not create a new ZIP for every lesson. Keep editing the same working folder and export a snapshot only at a meaningful milestone or before a risky change.
