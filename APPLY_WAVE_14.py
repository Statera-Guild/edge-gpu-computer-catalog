# Wave 14 integration; run once from repository root after Wave 13 push.
from pathlib import Path
import csv,io,re,sys
root=Path.cwd()
old=root/'validation_framework/integration/master_catalog_0001_0070.csv'
new=root/'validation_framework/integration/master_catalog_0001_0075.csv'
readme=root/'README.md'
if not (root/'.git').is_dir() or not old.is_file() or not readme.is_file():sys.exit('ERROR: run from Git repository root with 70-record master catalog')
if new.exists():sys.exit('ERROR: 75-record master already exists; refusing overwrite')
with old.open(encoding='utf-8-sig',newline='') as f:
 r=csv.DictReader(f);headers=r.fieldnames;rows=list(r)
if len(rows)!=70 or sorted(x['component_id'] for x in rows)!=[f'CMP-EGC-{i:04d}' for i in range(1,71)]:sys.exit('ERROR: baseline is not 70 unique contiguous Component IDs')
items=[('0071', 'AAEON', 'BOXER-8655AI', 'NVIDIA Jetson Orin NX; fanless embedded AI system; GMSL2 cameras', 'https://www.aaeon.com/en/product/detail/ai-edge-solutions-boxer-8655ai', '8GB/16GB SKU selection and GMSL2 camera interoperability require validation'), ('0072', 'AAEON', 'BOXER-8658AI', 'NVIDIA Jetson Orin NX; fanless PoE in-vehicle AI system', 'https://www.aaeon.com/en/product/detail/ai-edge-solutions-boxer-8658ai', 'Verify PoE power budget, 8GB/16GB ordering SKU and lifecycle'), ('0073', 'AAEON', 'BOXER-8658AI-PLUS', 'NVIDIA Jetson Orin NX; PoE embedded AI system variant', 'https://catalog.aaeon.com.tw/Systems/files/basic-html/page3.html', '2025 manufacturer catalog identity only; PLUS distinctions and exact SKU require primary product datasheet'), ('0074', 'Advantech', 'MIB-741-AT', 'NVIDIA Jetson Thor T4000; AI inference system', 'https://www.advantech.com/ko-kr/products/f8c8792f-5837-421d-b268-f40a8fc1e484/mib-741-at/mod_68d73d71-4805-4925-b59c-cd067364b41c', 'Confirm orderable SKU, GMSL2 accessories and current lifecycle'), ('0075', 'Advantech', 'MIC-741-AT', 'NVIDIA Jetson Thor; AI inference system', 'https://www.advantech.com/ko-kr/products/f8c8792f-5837-421d-b268-f40a8fc1e484/mib-741-at/mod_68d73d71-4805-4925-b59c-cd067364b41c', 'Linked in manufacturer product-family navigation; exact product page, specs and SKU require verification')]
for n,m,name,platform,url,note in items:
 if not (root/f'component_cards/CMP-EGC-{n}.md').is_file():sys.exit(f'ERROR: missing card {n}')
 if any(x['manufacturer'].strip().casefold()==m.casefold() and x['product_name'].strip().casefold()==name.casefold() for x in rows):sys.exit(f'ERROR: duplicate manufacturer/model in baseline: {m} {name}')
rows_new=[dict(component_id=f'CMP-EGC-{n}',manufacturer=m,product_name=name,wave='14',card_path=f'component_cards/CMP-EGC-{n}.md',record_status='listed',record_scope_review='needs SKU verification',identity_review='pending',evidence_review='pending',integration_note=note) for n,m,name,platform,url,note in items]
if any(set(x)-set(headers) for x in rows_new):sys.exit('ERROR: master header incompatible')
t=readme.read_text(encoding='utf-8-sig')
if 'CMP-EGC-0071' in t or 'CMP-EGC-0070' not in t or '## Scope and status' not in t:sys.exit('ERROR: README baseline invalid or already updated')
if '## Product index (70 records; Wave 1–13)' not in t:sys.exit('ERROR: README index header differs from expected')
oldnav='- [Master Catalog — 0001–0070](validation_framework/integration/master_catalog_0001_0070.csv) (current index)'
if oldnav not in t:sys.exit('ERROR: current master link not found')
needle='- [Wave 13 evidence — 0066–0070](validation_framework/wave_a/batch_0066_0070/README.md)'
if needle not in t:sys.exit('ERROR: Wave 13 evidence link missing')
head,tail=t.split('## Scope and status',1);head=head.rstrip()
for n,m,name,_,_,_ in items:head+=f'\n| `CMP-EGC-{n}` | {m} | {name} | listed | [View](component_cards/CMP-EGC-{n}.md) |'
t=head+'\n\n## Scope and status'+tail
t=t.replace('## Product index (70 records; Wave 1–13)','## Product index (75 records; Wave 1–14)')
t=t.replace(oldnav,'- [Master Catalog — 0001–0075](validation_framework/integration/master_catalog_0001_0075.csv) (current index)\n- [Previous Master Catalog — 0001–0070](validation_framework/integration/master_catalog_0001_0070.csv) (historical snapshot)')
t=t.replace(needle,needle+'\n- [Wave 14 evidence — 0071–0075](validation_framework/wave_a/batch_0071_0075/README.md)')
t=t.replace('## Validation and contribution','Wave 14 adds AAEON and Advantech Jetson systems. SKU, lifecycle, evidence and algorithm verification remain pending. Known cross-wave RUC-1000G duplicate model names (0019 and 0065) require identity audit.\n\n## Validation and contribution')
ids=re.findall(r'^\| `CMP-EGC-(\d{4})` \|',t,re.M)
if sorted(ids)!=[f'{i:04d}' for i in range(1,76)]:sys.exit(f'ERROR: README IDs invalid: {len(ids)}')
out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=headers,lineterminator='\n');w.writeheader();w.writerows(rows+rows_new)
new.write_text(out.getvalue(),encoding='utf-8');readme.write_text(t,encoding='utf-8')
(root/'validation_framework/integration/INTEGRATION_README.md').write_text('# Integrated master catalog — 75 Component IDs\n\nCurrent public snapshot: `master_catalog_0001_0075.csv` (Waves 1–14, 75 unique Component IDs). Earlier snapshots are retained.\n\nManufacturer-sourced `listed` records are not certifications, verified SKUs or benchmarks. Identity audit pending: RUC-1000G occurs under CMP-EGC-0019 and CMP-EGC-0065. Wave 14 BOXER-8658AI-PLUS and MIC-741-AT require direct manufacturer product-page/datasheet validation. Public evidence resides in `validation_framework/wave_a/`; confidential data remains in private Core SSOT.\n',encoding='utf-8')
print('SUCCESS: Master Catalog records=75; unique IDs=75; README index=75')
print('NOTICE: identity audit pending; RUC-1000G duplicates (0019 and 0065); two Wave 14 evidence follow-ups')
