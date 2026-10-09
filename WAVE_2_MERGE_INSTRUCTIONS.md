# Wave 2 patch merge (Windows Anaconda Prompt)

This patch intentionally does not replace the Wave 1 README, master list, schemas, or inventory. After extraction, verify with `git status --short` and `git diff --stat`.

For the next integration step, update the root README and master inventory only after confirming all five product identities and reconciling the existing CSV/JSON structure. Do not claim that the root index automatically includes Wave 2.

```bat
cd /d C:\Users\abc\Downloads\PAI_SG_Edge_GPU_Computer_Catalog_Wave1_20261009\edge-gpu-computer-catalog
git pull --ff-only origin main
git status --short
```

Extract the ZIP at the **parent** folder `C:\Users\abc\Downloads\PAI_SG_Edge_GPU_Computer_Catalog_Wave1_20261009`, merge the inner `edge-gpu-computer-catalog` directory, and do not overwrite existing files. Then:

```bat
git status --short
git add component_cards/CMP-EGC-0011.md component_cards/CMP-EGC-0012.md component_cards/CMP-EGC-0013.md component_cards/CMP-EGC-0014.md component_cards/CMP-EGC-0015.md validation_framework/wave_a/batch_0011_0015 WAVE_2_MERGE_INSTRUCTIONS.md
git diff --cached --stat
git commit -m "Add Neousys Edge GPU Computer Wave 2 records 0011 to 0015"
git push origin main
git status
```
