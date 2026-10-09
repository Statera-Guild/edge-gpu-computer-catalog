# Wave 6 merge instructions (Windows Anaconda Prompt)

1. Extract ZIP to `C:\Users\abc\Downloads\Wave6_Extract`.
2. From the cloned `edge-gpu-computer-catalog` root, run `xcopy "C:\Users\abc\Downloads\Wave6_Extract\edge-gpu-computer-catalog\*" "." /E /I /Y`.
3. Verify `git status --short` and `git diff -- README.md` (use `git --no-pager diff -- README.md` if needed).
4. Stage, commit, push after review. New files do not overwrite existing Component Cards or the previous 25-record master.

Expected: 5 new cards, 6 Wave 6 validation files, new 35-record master, updated integration README, updated root README, merge instructions = 15 files.
