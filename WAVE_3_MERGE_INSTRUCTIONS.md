# Wave 3 patch — merge safely

This ZIP contains only new files. Extract, then copy the inner `edge-gpu-computer-catalog` folder contents into the existing local Git worktree. Do not copy a `.git` folder.

From existing worktree (Windows Anaconda Prompt):

```bat
git status
git pull --ff-only origin main
xcopy "C:\Users\abc\Downloads\Wave3_Extract\edge-gpu-computer-catalog\*" "." /E /I /Y
git status --short
git add component_cards/CMP-EGC-0016.md component_cards/CMP-EGC-0017.md component_cards/CMP-EGC-0018.md component_cards/CMP-EGC-0019.md component_cards/CMP-EGC-0020.md validation_framework/wave_a/batch_0016_0020 WAVE_3_MERGE_INSTRUCTIONS.md
git diff --cached --stat
git commit -m "Add Wave 3 high-performance Edge GPU Computers 0016 to 0020"
git push origin main
git status
```

Do not proceed with Wave 3 push until Wave 2 is committed and pushed.
