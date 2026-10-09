# Wave 11 — run once from existing Git repository root.
from pathlib import Path
import csv,io,re,sys
root=Path.cwd()
old=root/'validation_framework/integration/master_catalog_0001_0055.csv'
new=root/'validation_framework/integration/master_catalog_0001_0060.csv'
readme=root/'README.md'
if not (root/'.git').is_dir() or not old.is_file() or not readme.is_file():
 sys.exit('ERROR: run from repository root with 55-record baseline')
if new.exists(): sys.exit('ERROR: 60-record master already exists; refusing overwrite')
with old.open(encoding='utf-8-sig',newline='') as f:
 reader=csv.DictReader(f);headers=reader.fieldnames;rows=list(reader)
if len(rows)!=55 or sorted(r['component_id'] for r in rows)!=[f'CMP-EGC-{i:04d}' for i in range(1,56)]:
 sys.exit('ERROR: expected unique contiguous 0001–0055 master baseline')
items=[('0056', 'Nuvo-9160GC', 'Discrete NVIDIA GPU expansion platform', 'GPU is optional; exact compatible GPU SKU, power, thermal envelope pending'), ('0057', 'SEMIL-2000GC', 'Rugged discrete GPU computer', 'Confirm model variant, GPU configuration, ruggedization and lifecycle'), ('0058', 'RGS-8805GC', 'Rugged GPU computer', 'Confirm exact GPU configuration, operating limits and SKU'), ('0059', 'GT-92GC', 'GPU computing platform', 'Confirm exact GPU option, cooling and orderable SKU'), ('0060', 'Nuvo-10000 Series', 'Expandable industrial GPU-capable computer', 'GPU is optional; exact PCIe expansion/GPU configuration must be verified')]
text=readme.read_text(encoding='utf-8-sig')
if 'CMP-EGC-0056' in text or 'CMP-EGC-0055' not in text or '## Scope and status' not in text:
 sys.exit('ERROR: README baseline unexpected or Wave 11 already present')
for n,name,platform,note in items:
 if not (root/f'component_cards/CMP-EGC-{n}.md').is_file():sys.exit(f'ERROR: missing card {n}')
for n,name,platform,note in items:
 rows.append(dict(component_id=f'CMP-EGC-{n}',manufacturer='Neousys Technology',product_name=name,wave='11',card_path=f'component_cards/CMP-EGC-{n}.md',record_status='listed',record_scope_review='needs SKU verification',identity_review='pending',evidence_review='pending',integration_note=note))
head,tail=text.split('## Scope and status',1)
head=head.rstrip()
for n,name,_,_ in items:head+=f'\n| `CMP-EGC-{n}` | Neousys Technology | {name} | listed | [View](component_cards/CMP-EGC-{n}.md) |'
text=head+'\n\n## Scope and status'+tail
text=text.replace('## Product index (55 records; Wave 1–10)','## Product index (60 records; Wave 1–11)')
oldnav='- [Master Catalog — 0001–0055](validation_framework/integration/master_catalog_0001_0055.csv) (current index)'
if oldnav not in text:sys.exit('ERROR: expected master navigation not found')
text=text.replace(oldnav,'- [Master Catalog — 0001–0060](validation_framework/integration/master_catalog_0001_0060.csv) (current index)\n- [Previous Master Catalog — 0001–0055](validation_framework/integration/master_catalog_0001_0055.csv) (historical snapshot)')
needle='- [Wave 10 evidence — 0051–0055](validation_framework/wave_a/batch_0051_0055/README.md)'
if needle not in text:sys.exit('ERROR: Wave 10 navigation missing')
text=text.replace(needle,needle+'\n- [Wave 11 evidence — 0056–0060](validation_framework/wave_a/batch_0056_0060/README.md)')
text=text.replace('## Validation and contribution','Wave 11 adds Neousys GPU-capable industrial systems. Optional discrete GPU configurations must be distinguished from a shipped GPU; SKU and lifecycle verification remain pending.\n\n## Validation and contribution')
ids=re.findall(r'^\| `CMP-EGC-(\d{4})` \|',text,re.M)
if sorted(ids)!=[f'{i:04d}' for i in range(1,61)]:sys.exit(f'ERROR: README index inconsistent ({len(ids)} rows)')
s=io.StringIO();w=csv.DictWriter(s,fieldnames=headers,lineterminator='\n');w.writeheader();w.writerows(rows)
new.write_text(s.getvalue(),encoding='utf-8')
readme.write_text(text,encoding='utf-8')
(root/'validation_framework/integration/INTEGRATION_README.md').write_text('# Integrated master catalog — 60 records\n\nCurrent public snapshot: `master_catalog_0001_0060.csv` (Waves 1–11, 60 unique Component IDs). Earlier snapshots are retained.\n\nRecords are manufacturer-evidence `listed` entries, not certification or performance benchmarks. Exact SKUs, lifecycle and GPU configurations require review. Wave 11 includes GPU-capable hosts whose discrete GPUs may be optional. Public evidence resides in `validation_framework/wave_a/`; confidential engineering and commercial data remain in Core SSOT.\n',encoding='utf-8')
print('SUCCESS: Master Catalog records=60; unique IDs=60; README index=60')
