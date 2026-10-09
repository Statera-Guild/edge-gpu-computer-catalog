# Final expansion wave; run from clean Wave 14 Git repository root.
from pathlib import Path
import csv,io,re,sys
root=Path.cwd()
old=root/'validation_framework/integration/master_catalog_0001_0075.csv'
new=root/'validation_framework/integration/master_catalog_0001_0080.csv'
readme=root/'README.md'
if not (root/'.git').is_dir() or not old.is_file() or not readme.is_file():sys.exit('ERROR: run from Git repository root with 75-record baseline')
if new.exists():sys.exit('ERROR: 80-record master already exists; refusing overwrite')
with old.open(encoding='utf-8-sig',newline='') as f:
 r=csv.DictReader(f);headers=r.fieldnames;rows=list(r)
if len(rows)!=75 or sorted(x['component_id'] for x in rows)!=[f'CMP-EGC-{i:04d}' for i in range(1,76)]:sys.exit('ERROR: baseline not 75 unique contiguous IDs')
items=[('0076', 'ADLINK', 'DLAP-701', 'NVIDIA Jetson Thor T5000/T4000 compact edge AI computer', 'https://www.adlinktech.com/Products/Deep_Learning_Accelerator_Platform_and_Server/Inference_Platform/DLAP-701?lang=en', 'manufacturer_product_page', 'Confirm orderable Jetson T5000/T4000 SKU, thermal profile and software image', 'published'), ('0077', 'ADLINK', 'DLAP-711 Series', 'NVIDIA Jetson Thor robotics edge AI platform with GMSL2 interfaces', 'https://www.adlinktech.com/Products/Deep_Learning_Accelerator_Platform_and_Server/Inference_Platform/DLAP-711_Series?lang=ko', 'manufacturer_product_page', 'Manufacturer labels preliminary; confirm release, GMSL2 module and orderable SKU', 'preliminary'), ('0078', 'ADLINK', 'DLAP-IGX', 'NVIDIA IGX Thor industrial edge AI platform', 'https://www.adlinktech.com/en/dlap', 'manufacturer_family_page', 'Manufacturer labels preliminary; exact system identity, released SKU and lifecycle pending', 'preliminary'), ('0079', 'ADLINK', 'DLAP-401-Xavier', 'NVIDIA Jetson AGX Xavier fanless edge AI inference platform', 'https://www.adlinktech.com/Products/Deep_Learning_Accelerator_Platform_and_Server/Inference_Platform/DLAP-401-Xavier', 'manufacturer_product_page', 'Manufacturer marks END OF LIFE; exact SKU and retirement/replacement details require verification', 'end_of_life'), ('0080', 'ADLINK', 'RQX-71G', 'NVIDIA Jetson Thor robotic edge AI controller platform', 'https://www.adlinktech.com/kr/dlap', 'manufacturer_family_page', 'Manufacturer labels preliminary; verify controller availability, interfaces and orderable SKU', 'preliminary')]
for n,m,name,platform,url,stype,note,phase in items:
 if not (root/f'component_cards/CMP-EGC-{n}.md').is_file():sys.exit(f'ERROR: missing card {n}')
 if any(x['manufacturer'].strip().casefold()==m.casefold() and x['product_name'].strip().casefold()==name.casefold() for x in rows):sys.exit(f'ERROR: duplicate manufacturer/model {m} {name}')
if len({(m.casefold(),name.casefold()) for _,m,name,*_ in items}) != len(items):sys.exit('ERROR: duplicate manufacturer/model within Wave 15')
rows_new=[dict(component_id=f'CMP-EGC-{n}',manufacturer=m,product_name=name,wave='15',card_path=f'component_cards/CMP-EGC-{n}.md',record_status='listed',record_scope_review='needs SKU verification',identity_review='pending',evidence_review='pending',integration_note=note) for n,m,name,platform,url,stype,note,phase in items]
if any(set(x)-set(headers) for x in rows_new):sys.exit('ERROR: master header incompatible')
t=readme.read_text(encoding='utf-8-sig')
if 'CMP-EGC-0076' in t or 'CMP-EGC-0075' not in t or '## Scope and status' not in t:sys.exit('ERROR: README baseline invalid/already updated')
if '## Product index (75 records; Wave 1–14)' not in t:sys.exit('ERROR: README index header differs')
oldnav='- [Master Catalog — 0001–0075](validation_framework/integration/master_catalog_0001_0075.csv) (current index)'
if oldnav not in t:sys.exit('ERROR: current master link missing')
needle='- [Wave 14 evidence — 0071–0075](validation_framework/wave_a/batch_0071_0075/README.md)'
if needle not in t:sys.exit('ERROR: Wave 14 evidence link missing')
head,tail=t.split('## Scope and status',1);head=head.rstrip()
for n,m,name,_,_,_,_,_ in items:head+=f'\n| `CMP-EGC-{n}` | {m} | {name} | listed | [View](component_cards/CMP-EGC-{n}.md) |'
t=head+'\n\n## Scope and status'+tail
t=t.replace('## Product index (75 records; Wave 1–14)','## Product index (80 records; Wave 1–15)')
t=t.replace(oldnav,'- [Master Catalog — 0001–0080](validation_framework/integration/master_catalog_0001_0080.csv) (current index)\n- [Previous Master Catalog — 0001–0075](validation_framework/integration/master_catalog_0001_0075.csv) (historical snapshot)')
t=t.replace(needle,needle+'\n- [Wave 15 evidence — 0076–0080](validation_framework/wave_a/batch_0076_0080/README.md)')
t=t.replace('## Validation and contribution','**Catalog expansion freeze:** Wave 15 concludes registration at 80 Component IDs. Unique IDs do not imply 80 distinct orderable SKUs; manufacturer identity, duplicates, evidence, lifecycle and on-device algorithm compatibility remain under audit. Known RUC-1000G duplicate IDs: 0019 and 0065.\n\n## Validation and contribution')
ids=re.findall(r'^\| `CMP-EGC-(\d{4})` \|',t,re.M)
if sorted(ids)!=[f'{i:04d}' for i in range(1,81)]:sys.exit(f'ERROR: README IDs invalid: {len(ids)}')
out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=headers,lineterminator='\n');w.writeheader();w.writerows(rows+rows_new)
new.write_text(out.getvalue(),encoding='utf-8');readme.write_text(t,encoding='utf-8')
(root/'validation_framework/integration/INTEGRATION_README.md').write_text('# Integrated master catalog — 80 Component IDs (Wave 15 expansion freeze)\n\nCurrent public snapshot: `master_catalog_0001_0080.csv` (Waves 1–15, 80 unique Component IDs). Earlier snapshots are retained. No further product expansion until evidence-quality review is complete.\n\nRecords are manufacturer-sourced `listed` candidates, not certified SKUs, independently measured benchmarks or procurement endorsements. Duplicate identity pending: ASUS RUC-1000G under CMP-EGC-0019 and CMP-EGC-0065. Wave 14 evidence follow-ups: BOXER-8658AI-PLUS and MIC-741-AT. Wave 15 preliminary ADLINK systems require orderability and release checks; CMP-EGC-0079 DLAP-401-Xavier is manufacturer-marked END OF LIFE.\n\nNext audit: identity/duplicate aliases; manufacturer primary sources; SKU configuration; active/EOL/EOS lifecycle; on-device algorithm runtime and reproducibility. Confidential BOM, supplier terms and internal evidence remain private Core SSOT.\n',encoding='utf-8')
print('SUCCESS: Master Catalog records=80; unique IDs=80; README index=80')
print('NOTICE: EXPANSION FROZEN; verification audit pending (duplicate model identity, preliminary products, SKU, lifecycle, algorithm tests)')
