# Anaconda Prompt — Windows 10 (cmd.exe)

1. Create an empty GitHub public repository under `Statera-Guild`, name `edge-gpu-computer-catalog`, default branch main. **Do not initialize README, .gitignore or license** (ZIP includes README/.gitignore).
2. Save and extract the delivered ZIP to `C:\Users\abc\A_RL\00_Master_Library\08_Robotics_Software`, resulting in one `edge-gpu-computer-catalog` folder.
3. Run the following commands in Anaconda Prompt:

```bat
cd /d C:\Users\abc\A_RL\00_Master_Library\08_Robotics_Software\edge-gpu-computer-catalog
gh auth status
git init -b main
git remote add origin https://github.com/Statera-Guild/edge-gpu-computer-catalog.git
git status
git add .
git diff --cached --stat
git commit -m "Initialize PAI-SG edge GPU computer catalog Wave 1"
git push -u origin main
git status
```

For a **previously initialized** repo, don't repeat `git init` or `git remote add`; instead use `git pull --ff-only origin main`, copy/merge new files without deleting existing content, then `git add .`, `git diff --cached --stat`, `git commit`, `git push`, `git status`.

No force-push. If `git pull --ff-only` fails, inspect `git status`, `git branch -vv` and `git remote -v` before modifications. LF/CRLF conversion warnings alone are not proof of file corruption. Copy final output (especially `git status` and GitHub URL) back to the conversation.
