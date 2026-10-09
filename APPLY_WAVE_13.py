# Wave 13 integration: run in Git repository root.
from pathlib import Path
import csv,io,re,sys
root=Path.cwd()
old=root/'validation_framework/integration/master_catalog_0001_0065.csv'
new=root/'validation_framework/integration/master_catalog_0001_0070.csv'
readme=root/'README.md'
if not (root/'.git').is_dir() or not old.is_file() or not readme.is_file(): sys.exit('ERROR: run from Git repository root with 65-record master catalog')
with old.open(encoding='utf-8-sig',newline='') as f:
 r=csv.DictReader(f); headers=r.fieldnames; rows=list(r)
if len(rows)!=65 or sorted(x['component_id'] for x in rows)!=[f'CMP-EGC-{i:04d}' for i in range(1,66)]: sys.exit('ERROR: baseline is not 65 unique contiguous Component IDs')
items=[('0066', 'PE3000N', 'Jetson Thor integrated GPU; exact module SKU and revision pending'), ('0067', 'PE1103N', 'Orin NX/Nano family; selected SoM and GMSL expansion must be verified'), ('0068', 'PE1102N', 'Orin NX/Nano family; exact configuration and I/O must be verified'), ('0069', 'PE1100N V2', 'V2 distinct from PE1100N; verify revision and SoM'), ('0070', 'PE2100N', 'AGX Orin configuration and PoE capabilities require SKU validation')]
for n,name,note in items:
 if not (root/f'component_cards/CMP-EGC-{n}.md').is_file(): sys.exit(f'ERROR: missing card {n}')
 if any(x['manufacturer'].strip().lower()=='asus iot' and x['product_name'].strip().casefold()==name.casefold() for x in rows): sys.exit(f'ERROR: duplicate manufacturer/model in baseline: {name}')
rows_new=[dict(component_id=f'CMP-EGC-{n}',manufacturer='ASUS IoT',product_name=name,wave='13',card_path=f'component_cards/CMP-EGC-{n}.md',record_status='listed',record_scope_review='needs SKU verification',identity_review='pending',evidence_review='pending',integration_note=note) for n,name,note in items]
if any(set(x)-set(headers) for x in rows_new): sys.exit('ERROR: master header incompatible')
t=readme.read_text(encoding='utf-8-sig')
if 'CMP-EGC-0066' in t or 'CMP-EGC-0065' not in t or '## Scope and status' not in t: sys.exit('ERROR: README baseline invalid or already updated')
if '## Product index (65 records; Wave 1–12)' not in t: sys.exit('ERROR: README index header differs from expected')
if '[Master Catalog — 0001–0065](validation_framework/integration/master_catalog_0001_0065.csv) (current index)' not in t: sys.exit('ERROR: current master link not found')
needle='- [Wave 12 evidence — 0061–0065](validation_framework/wave_a/batch_0061_0065/README.md)'
if needle not in t: sys.exit('ERROR: Wave 12 evidence link missing')
head,tail=t.split('## Scope and status',1)
head=head.rstrip()
for n,name,_ in items: head+=f'\n| `CMP-EGC-{n}` | ASUS IoT | {name} | listed | [View](component_cards/CMP-EGC-{n}.md) |'
t=head+'\n\n## Scope and status'+tail
t=t.replace('## Product index (65 records; Wave 1–12)','## Product index (70 records; Wave 1–13)')
t=t.replace('- [Master Catalog — 0001–0065](validation_framework/integration/master_catalog_0001_0065.csv) (current index)','- [Master Catalog — 0001–0070](validation_framework/integration/master_catalog_0001_0070.csv) (current index)\n- [Previous Master Catalog — 0001–0065](validation_framework/integration/master_catalog_0001_0065.csv) (historical snapshot)')
t=t.replace(needle,needle+'\n- [Wave 13 evidence — 0066–0070](validation_framework/wave_a/batch_0066_0070/README.md)')
t=t.replace('## Validation and contribution','Wave 13 adds ASUS IoT Jetson integrated-GPU systems. Exact SKU, lifecycle and algorithm performance require validation. Cross-wave identity audit is pending; RUC-1000G is listed under two existing Component IDs (0019 and 0065).\n\n## Validation and contribution')
ids=re.findall(r'^\| `CMP-EGC-(\d{4})` \|',t,re.M)
if sorted(ids)!=[f'{i:04d}' for i in range(1,71)]: sys.exit(f'ERROR: README IDs invalid: {len(ids)}')
out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=headers,lineterminator='\n');w.writeheader();w.writerows(rows+rows_new)
new.write_text(out.getvalue(),encoding='utf-8')
readme.write_text(t,encoding='utf-8')
(root/'validation_framework/integration/INTEGRATION_README.md').write_text('# Integrated master catalog — 70 Component IDs\n\nCurrent public snapshot: `master_catalog_0001_0070.csv` (Waves 1–13, 70 unique Component IDs). Earlier snapshots are retained.\n\nManufacturer-sourced `listed` entries are not certifications, verified SKUs or benchmarks. Cross-wave product identity audit is pending: RUC-1000G occurs under CMP-EGC-0019 and CMP-EGC-0065. Do not claim 70 distinct hardware models before deduplication. Public evidence is in `validation_framework/wave_a/`; confidential engineering and commercial information remain in private Core SSOT.\n',encoding='utf-8')
print('SUCCESS: Master Catalog records=70; unique IDs=70; README index=70')
print('NOTICE: cross-wave identity audit pending; RUC-1000G duplicate model names (0019 and 0065)')
