# PyCharm Setup — Consolidated Workspace

## What you need

- Python interpreter — already installed on the learner's computer.
- PyCharm — already installed and used for this project.
- A project-local virtual environment (`.venv`) — recommended to isolate future dependencies.
- Git — recommended later for history/recovery, but not required for the first lesson.
- No third-party Python libraries are needed yet. SQLite is part of Python's standard library and can be introduced later if/when we choose local database storage.

## Install this consolidated working folder once

1. Keep the project folder as a backup.
2. Rename the existing `Project_02_SME_Management_System` folder to a backup name, such as `Project_02_SME_Management_System_backup_before_v1.0`. Do not delete it yet.
3. Extract the new ZIP into the same `04_Projects` parent folder. It should create a single `Project_02_SME_Management_System` folder containing `main.py`, `START_HERE.md`, `requirements.txt`, `.gitignore` and `docs/`.
4. In PyCharm select **File → Open** and select that extracted `Project_02_SME_Management_System` folder. Do not select the ZIP or the parent folder.
5. Check that `main.py` is at the project root and that `docs/` contains the consolidated active documents.
6. Open **File → Settings → Project → Python Interpreter** (the wording may vary slightly by PyCharm version). Select your installed Python 3.14.8 interpreter. If the project has no interpreter, create a project-local `.venv` based on that interpreter.
7. Open `main.py` and run it. The Run console should display the system name and the starter milestone text.
8. Keep the backup until the new folder opens and runs successfully. Afterwards, the old project may be removed from PyCharm's Recent Projects list; that list entry is separate from the files on disk.

#  Note
if there is another IDE you have beside Pycharm (VScode), make sure to download the python extentions from microsoft package.
## Important

- Never extract a new ZIP over the active project folder. That can mix old and new documents.
- Do not put `.venv/`, interpreter binaries or machine-specific PyCharm settings inside a ZIP. Create the virtual environment locally; `.gitignore` excludes it.
- A ZIP cannot contain or configure the PyCharm application installed on your computer. It contains the code and project files PyCharm opens.
- Do not install packages until a lesson explains why one is needed.
- The first implementation should be a small console prototype. A graphical interface, database and cloud deployment are later decisions.

## Ongoing workflow — no ZIP per lesson

Keep the same working folder. Edit the code and the relevant single-source documents in place. Use Git . Export a new ZIP only at a meaningful milestone or before a risky set of changes.
