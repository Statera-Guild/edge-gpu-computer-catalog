# Wave 4 merge — CMP-EGC-0021 to 0025

Prerequisite: Wave 3 commit and push complete; `git status` clean.

In Windows Anaconda Prompt, from the existing `edge-gpu-computer-catalog` repository:

```bat
xcopy "C:\Users\abc\Downloads\Wave4_Extract\edge-gpu-computer-catalog\*" "." /E /I /Y
git status --short
git add .
git diff --cached --stat
git commit -m "Add Wave 4 industrial GPU computers 0021 to 0025"
git push origin main
git status
```

Do not use this patch to overwrite previous Wave batches or change public statuses to `documented`.
