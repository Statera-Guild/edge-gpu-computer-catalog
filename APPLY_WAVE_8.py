# Apply from the repository root after copying this patch.
from pathlib import Path
import csv,io,re,sys
root=Path.cwd()
old=root/'validation_framework/integration/master_catalog_0001_0040.csv'
new=root/'validation_framework/integration/master_catalog_0001_0045.csv'
readme=root/'README.md'
if not (root/'.git').is_dir() or not old.is_file() or not readme.is_file():
 sys.exit('ERROR: run from existing Git repository root containing 40-record master catalog')
with old.open(encoding='utf-8-sig',newline='') as f:
 r=csv.DictReader(f); headers=r.fieldnames; rows=list(r)
ids=[x['component_id'] for x in rows]
expected=[f'CMP-EGC-{i:04d}' for i in range(1,41)]
if len(rows)!=40 or sorted(ids)!=expected:
 sys.exit('ERROR: baseline master is not exactly 0001–0040 unique; no changes made')
items=[('0041','DLAP-212 Series','Preliminary product family; SKU and release status pending'),('0042','DLAP-211-Nano','Legacy Jetson Nano lifecycle and SKU pending'),('0043','DLAP-301-Nano','NVR-specific system; legacy lifecycle pending'),('0044','DLAP-211-JNX','Legacy Jetson Xavier NX lifecycle and SKU pending'),('0045','DLAP-301-JNX','NVR-specific system; legacy lifecycle pending')]
for n,name,note in items:
 card=root/f'component_cards/CMP-EGC-{n}.md'
 if not card.is_file(): sys.exit(f'ERROR: missing {card}; no changes made')
 rows.append(dict(component_id=f'CMP-EGC-{n}',manufacturer='ADLINK',product_name=name,wave='8',card_path=f'component_cards/CMP-EGC-{n}.md',record_status='listed',record_scope_review='needs SKU verification',identity_review='pending',evidence_review='pending',integration_note=note))
text=readme.read_text(encoding='utf-8-sig')
if 'CMP-EGC-0041' in text:
 sys.exit('ERROR: README already contains Wave 8 IDs; refusing duplicate insertion')
if 'CMP-EGC-0040' not in text or '## Scope and status' not in text:
 sys.exit('ERROR: README baseline not recognized; no changes made')
# Normalize a stray blank line in the existing markdown table before appending.
index_end=text.index('## Scope and status')
head=text[:index_end].rstrip()
tail=text[index_end:]
for n,name,_ in items:
 head+=f'\n| `CMP-EGC-{n}` | ADLINK | {name} | listed | [View](component_cards/CMP-EGC-{n}.md) |'
text=head+'\n\n'+tail
text=text.replace('## Product index (40 records; Wave 1–7)','## Product index (45 records; Wave 1–8)')
text=text.replace('[Master Catalog — 0001–0040](validation_framework/integration/master_catalog_0001_0040.csv) (current index)','[Master Catalog — 0001–0045](validation_framework/integration/master_catalog_0001_0045.csv) (current index)\n- [Previous Master Catalog — 0001–0040](validation_framework/integration/master_catalog_0001_0040.csv) (historical snapshot)')
needle='- [Wave 7 evidence — 0036–0040](validation_framework/wave_a/batch_0036_0040/README.md)'
if needle not in text: sys.exit('ERROR: Wave 7 README navigation missing; no changes made')
text=text.replace(needle,needle+'\n- [Wave 8 evidence — 0041–0045](validation_framework/wave_a/batch_0041_0045/README.md)')
if 'DLAP-212' not in text[text.index('## Scope and status'):]:
 text=text.replace('## Validation and contribution','Wave 8 includes a preliminary DLAP-212 listing and legacy Jetson Nano/Xavier NX systems; confirm current lifecycle and exact SKU before procurement.\n\n## Validation and contribution')
# Verify README row IDs (no duplicates, contiguous).
row_ids=re.findall(r'^\| `CMP-EGC-(\d{4})` \|',text,re.M)
if sorted(row_ids)!=[f'{i:04d}' for i in range(1,46)]:
 sys.exit(f'ERROR: README index inconsistent ({len(row_ids)} rows); no changes made')
out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=headers,lineterminator='\n');w.writeheader();w.writerows(rows)
new.write_text(out.getvalue(),encoding='utf-8')
readme.write_text(text,encoding='utf-8')
(root/'validation_framework/integration/INTEGRATION_README.md').write_text('# Integrated master catalog — 45 records\n\nCurrent public snapshot: `master_catalog_0001_0045.csv` (Waves 1–8, 45 unique Component IDs). Earlier snapshots are retained.\n\nRecords are manufacturer-sourced `listed` entries, not certification or performance benchmarks. Identity and evidence reviews remain pending. Wave 8 includes preliminary and legacy platform lifecycle risks. Public evidence is in `validation_framework/wave_a/`; private engineering and commercial data remain in Core SSOT.\n',encoding='utf-8')
print('SUCCESS: Master Catalog records=45; unique IDs=45; README index=45')
