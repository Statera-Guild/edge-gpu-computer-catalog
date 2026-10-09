# Wave 8 installation

1. Extract ZIP to `C:\Users\abc\Downloads\Wave8_Extract`.
2. Change directory to the **Git repository root** (not Downloads).
3. Copy the `edge-gpu-computer-catalog` patch tree into the repository.
4. Run `python APPLY_WAVE_8.py` from the repository root. This validates the existing 40-record master and creates `master_catalog_0001_0045.csv`, updates README and integration notes.
5. Verify output before git add/commit/push.

Never run the installer from Downloads. No independent PAI-SG benchmark is implied.
