# Wave 12 integration: run in Git repository root.
from pathlib import Path
import csv,io,re,sys
root=Path.cwd()
old=root/'validation_framework/integration/master_catalog_0001_0060.csv'
new=root/'validation_framework/integration/master_catalog_0001_0065.csv'
readme=root/'README.md'
if not (root/'.git').is_dir() or not old.is_file() or not readme.is_file(): sys.exit('ERROR: run from Git repository root with 60-record master catalog')
with old.open(encoding='utf-8-sig',newline='') as f:
 r=csv.DictReader(f); headers=r.fieldnames; rows=list(r)
if len(rows)!=60 or sorted(x['component_id'] for x in rows)!=[f'CMP-EGC-{i:04d}' for i in range(1,61)]: sys.exit('ERROR: baseline is not 60 unique contiguous records')
items=[('0061', 'PE3100G', 'GPU module optional; confirm module SKU and thermal rating'), ('0062', 'PE3000G', 'GPU module optional; verify MXM compatibility'), ('0063', 'PE4000G', 'GPU not necessarily installed; power is GPU support limit, not measured system consumption'), ('0064', 'PE5101D', 'GPU optional; verify GPU SKU and current manufacturer datasheet'), ('0065', 'RUC-1000G', 'Rack system; 600W denotes supported GPU capacity not measured consumption')]
for n,name,note in items:
 if not (root/f'component_cards/CMP-EGC-{n}.md').is_file(): sys.exit(f'ERROR: missing card {n}')
rows_new=[dict(component_id=f'CMP-EGC-{n}',manufacturer='ASUS IoT',product_name=name,wave='12',card_path=f'component_cards/CMP-EGC-{n}.md',record_status='listed',record_scope_review='needs SKU verification',identity_review='pending',evidence_review='pending',integration_note=note) for n,name,note in items]
if any(set(x)-set(headers) for x in rows_new): sys.exit('ERROR: master header incompatible')
t=readme.read_text(encoding='utf-8-sig')
if 'CMP-EGC-0061' in t or 'CMP-EGC-0060' not in t or '## Scope and status' not in t: sys.exit('ERROR: README baseline invalid or already updated')
if '## Product index (60 records; Wave 1–11)' not in t: sys.exit('ERROR: README index header differs from expected')
if '[Master Catalog — 0001–0060](validation_framework/integration/master_catalog_0001_0060.csv) (current index)' not in t: sys.exit('ERROR: current master link not found')
needle='- [Wave 11 evidence — 0056–0060](validation_framework/wave_a/batch_0056_0060/README.md)'
if needle not in t: sys.exit('ERROR: Wave 11 evidence link missing')
head,tail=t.split('## Scope and status',1)
head=head.rstrip()
for n,name,_ in items: head+=f'\n| `CMP-EGC-{n}` | ASUS IoT | {name} | listed | [View](component_cards/CMP-EGC-{n}.md) |'
t=head+'\n\n## Scope and status'+tail
t=t.replace('## Product index (60 records; Wave 1–11)','## Product index (65 records; Wave 1–12)')
t=t.replace('- [Master Catalog — 0001–0060](validation_framework/integration/master_catalog_0001_0060.csv) (current index)','- [Master Catalog — 0001–0065](validation_framework/integration/master_catalog_0001_0065.csv) (current index)\n- [Previous Master Catalog — 0001–0060](validation_framework/integration/master_catalog_0001_0060.csv) (historical snapshot)')
t=t.replace(needle,needle+'\n- [Wave 12 evidence — 0061–0065](validation_framework/wave_a/batch_0061_0065/README.md)')
t=t.replace('## Validation and contribution','Wave 12 adds ASUS IoT GPU-capable systems; GPU installation, exact SKU, lifecycle and performance require verification.\n\n## Validation and contribution')
ids=re.findall(r'^\| `CMP-EGC-(\d{4})` \|',t,re.M)
if sorted(ids)!=[f'{i:04d}' for i in range(1,66)]: sys.exit(f'ERROR: README IDs invalid: {len(ids)}')
out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=headers,lineterminator='\n');w.writeheader();w.writerows(rows+rows_new)
new.write_text(out.getvalue(),encoding='utf-8')
readme.write_text(t,encoding='utf-8')
(root/'validation_framework/integration/INTEGRATION_README.md').write_text('# Integrated master catalog — 65 records\n\nCurrent public snapshot: `master_catalog_0001_0065.csv` (Waves 1–12, 65 unique Component IDs). Earlier snapshots are retained.\n\nManufacturer-sourced `listed` entries are not certifications, verified configurations or benchmarks. Wave 12 GPU-ready systems require confirmation of installed GPU and exact SKU. Public evidence is in `validation_framework/wave_a/`; confidential engineering and commercial information remain in private Core SSOT.\n',encoding='utf-8')
print('SUCCESS: Master Catalog records=65; unique IDs=65; README index=65')
