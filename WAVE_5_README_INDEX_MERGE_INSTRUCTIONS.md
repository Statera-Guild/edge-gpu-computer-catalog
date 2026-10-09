# README index + Wave 5 merge

Prerequisite: Commit/push Wave 4 (confirmed 7ad71fe). The integration patch files in `validation_framework/integration/` are currently untracked locally; **do not delete them**.

1. Extract ZIP under `C:\Users\abc\Downloads\Wave5_Extract`.
2. From the existing repository root, run `xcopy "C:\Users\abc\Downloads\Wave5_Extract\edge-gpu-computer-catalog\*" "." /E /I /Y`.
3. This **intentionally updates root README.md** to index all 30 records. It does not modify existing cards 0001–0025.
4. Run `git status --short`, `git diff -- README.md`, and verify the 5 new cards.
5. Stage and commit the integration directory plus README and Wave 5 together only after checking diff.

README master index links to integration files from the previous patch, which must be included in the commit. Manufacturer assertions and software compatibility remain unverified until tested.
