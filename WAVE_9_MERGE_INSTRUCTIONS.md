# Wave 9 integration — 0046–0050

From repository root on Windows Anaconda Prompt:

1. Extract ZIP to `C:\Users\abc\Downloads\Wave9_Extract`.
2. `cd /d C:\Users\abc\Downloads\PAI_SG_Edge_GPU_Computer_Catalog_Wave1_20261009\edge-gpu-computer-catalog`
3. `xcopy "C:\Users\abc\Downloads\Wave9_Extract\edge-gpu-computer-catalog\*" "." /E /I /Y`
4. `python APPLY_WAVE_9.py`
5. `git status --short`

Do not commit/push until the integration checks succeed. Manufacturer claims are not independently validated.
