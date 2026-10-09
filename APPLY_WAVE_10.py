# Apply Wave 10 from the existing repository root.
from pathlib import Path
import csv,io,re,sys
root=Path.cwd();old=root/'validation_framework/integration/master_catalog_0001_0050.csv';new=root/'validation_framework/integration/master_catalog_0001_0055.csv';readme=root/'README.md';integration=root/'validation_framework/integration/INTEGRATION_README.md'
if not (root/'.git').is_dir() or not old.is_file() or not readme.is_file() or not integration.is_file():sys.exit('ERROR: run from existing Git repository root with 50-record catalog')
with old.open(encoding='utf-8-sig',newline='') as f:r=csv.DictReader(f);headers=r.fieldnames;rows=list(r)
ids=[x['component_id'] for x in rows]
if len(rows)!=50 or sorted(ids)!=[f'CMP-EGC-{i:04d}' for i in range(1,51)]:sys.exit('ERROR: baseline 0001-0050 invalid; no changes made')
items=[('0051','BOXER-8621AI','Verify Orin Nano variant and Super Mode SKU'),('0052','BOXER-8224AI','Carrier/module/heatsink assembly: confirm EGC category and legacy lifecycle'),('0053','BOXER-8253AI','Legacy Xavier NX; verify lifecycle'),('0054','BOXER-8250AI','Manufacturer End-of-Life Products category'),('0055','BOXER-8230AI','EOL; last buy date 2024-06-28 per manufacturer')]
for n,name,note in items:
 if not (root/f'component_cards/CMP-EGC-{n}.md').is_file():sys.exit(f'ERROR: missing card {n}; no changes made')
 if not (root/f'validation_framework/wave_a/batch_0051_0055/source_registry_wave_a_0051_0055.csv').is_file():sys.exit('ERROR: evidence files missing; no changes made')
 rows.append(dict(component_id=f'CMP-EGC-{n}',manufacturer='AAEON',product_name=name,wave='10',card_path=f'component_cards/CMP-EGC-{n}.md',record_status='listed',record_scope_review='needs SKU verification',identity_review='pending',evidence_review='pending',integration_note=note))
t=readme.read_text(encoding='utf-8-sig')
if 'CMP-EGC-0051' in t or '## Product index (50 records; Wave 1–9)' not in t or '## Scope and status' not in t:sys.exit('ERROR: README baseline mismatch or duplicate; no changes made')
needle='- [Wave 9 evidence — 0046–0050](validation_framework/wave_a/batch_0046_0050/README.md)'
if needle not in t:sys.exit('ERROR: Wave 9 navigation missing; no changes made')
if '[Master Catalog — 0001–0050](validation_framework/integration/master_catalog_0001_0050.csv) (current index)' not in t:sys.exit('ERROR: current master link missing; no changes made')
t=t.replace('[Master Catalog — 0001–0050](validation_framework/integration/master_catalog_0001_0050.csv) (current index)','[Master Catalog — 0001–0055](validation_framework/integration/master_catalog_0001_0055.csv) (current index)\n- [Previous Master Catalog — 0001–0050](validation_framework/integration/master_catalog_0001_0050.csv) (historical snapshot)')
t=t.replace(needle,needle+'\n- [Wave 10 evidence — 0051–0055](validation_framework/wave_a/batch_0051_0055/README.md)')
t=t.replace('## Product index (50 records; Wave 1–9)','## Product index (55 records; Wave 1–10)')
pos=t.index('## Scope and status');head=t[:pos].rstrip();tail=t[pos:]
for n,name,_ in items:head+=f'\n| `CMP-EGC-{n}` | AAEON | {name} | listed | [View](component_cards/CMP-EGC-{n}.md) |'
t=head+'\n\n'+tail
rows_in_readme=re.findall(r'^\| `CMP-EGC-(\d{4})` \|',t,re.M)
if sorted(rows_in_readme)!=[f'{i:04d}' for i in range(1,56)]:sys.exit('ERROR: README index invalid; no changes made')
t=t.replace('## Validation and contribution','Wave 10 includes legacy Jetson models and manufacturer end-of-life notices. A `listed` entry is not an availability claim or procurement recommendation.\n\n## Validation and contribution')
o=io.StringIO(newline='');w=csv.DictWriter(o,fieldnames=headers,lineterminator='\n');w.writeheader();w.writerows(rows)
new.write_text(o.getvalue(),encoding='utf-8');readme.write_text(t,encoding='utf-8')
integration.write_text('# Integrated master catalog — 55 records\n\nCurrent public snapshot: `master_catalog_0001_0055.csv` (Waves 1–10; 55 unique Component IDs). Earlier snapshots remain unchanged.\n\nEntries are manufacturer-sourced `listed` records with pending identity/evidence review, not certifications or benchmarks. Wave 10 includes legacy and EOL devices; confirm exact SKU and lifecycle. Public evidence is under `validation_framework/wave_a/`, while private engineering and commercial information remains in Core SSOT.\n',encoding='utf-8')
print('SUCCESS: Master Catalog records=55; unique IDs=55; README index=55')
