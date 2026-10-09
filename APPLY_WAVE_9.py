# Apply from the repository root after copying Wave 9 patch.
from pathlib import Path
import csv,io,re,sys
root=Path.cwd()
old=root/'validation_framework/integration/master_catalog_0001_0045.csv'
new=root/'validation_framework/integration/master_catalog_0001_0050.csv'
readme=root/'README.md'
if not (root/'.git').is_dir() or not old.is_file() or not readme.is_file():
 sys.exit('ERROR: run from existing Git repository root with 45-record master catalog')
with old.open(encoding='utf-8-sig',newline='') as f:
 reader=csv.DictReader(f); headers=reader.fieldnames; rows=list(reader)
ids=[x['component_id'] for x in rows]
if len(rows)!=45 or sorted(ids)!=[f'CMP-EGC-{i:04d}' for i in range(1,46)]:
 sys.exit('ERROR: baseline master is not exactly 0001-0045; no changes made')
items=[('0046','NRU-220S','AI NVR; confirm PoE and 2.5GbE configuration'),('0047','NRU-222S','M12-connector AI NVR; confirm variant'),('0048','NRU-240S-AWP','IP66 AGX Orin PoE system; distinct from NRU-230V-AWP'),('0049','NRU-171V-PPC','IP66 integrated GMSL2 panel PC; confirm module and SKU'),('0050','NRU-172S-PPC','IP66 integrated PoE panel PC; confirm module and SKU')]
for n,name,note in items:
 card=root/f'component_cards/CMP-EGC-{n}.md'
 if not card.is_file():sys.exit(f'ERROR: missing {card}; no changes made')
 rows.append(dict(component_id=f'CMP-EGC-{n}',manufacturer='Neousys Technology',product_name=name,wave='9',card_path=f'component_cards/CMP-EGC-{n}.md',record_status='listed',record_scope_review='needs SKU verification',identity_review='pending',evidence_review='pending',integration_note=note))
text=readme.read_text(encoding='utf-8-sig')
if 'CMP-EGC-0046' in text or 'CMP-EGC-0045' not in text or '## Scope and status' not in text:
 sys.exit('ERROR: README baseline not recognized or already includes Wave 9; no changes made')
index_end=text.index('## Scope and status')
head=text[:index_end].rstrip();tail=text[index_end:]
for n,name,_ in items:
 head+=f'\n| `CMP-EGC-{n}` | Neousys Technology | {name} | listed | [View](component_cards/CMP-EGC-{n}.md) |'
text=head+'\n\n'+tail
text=text.replace('## Product index (45 records; Wave 1–8)','## Product index (50 records; Wave 1–9)')
needle='[Master Catalog — 0001–0045](validation_framework/integration/master_catalog_0001_0045.csv) (current index)'
if needle not in text:sys.exit('ERROR: current master README link missing; no changes made')
text=text.replace(needle,'[Master Catalog — 0001–0050](validation_framework/integration/master_catalog_0001_0050.csv) (current index)\n- [Previous Master Catalog — 0001–0045](validation_framework/integration/master_catalog_0001_0045.csv) (historical snapshot)')
needle='- [Wave 8 evidence — 0041–0045](validation_framework/wave_a/batch_0041_0045/README.md)'
if needle not in text:sys.exit('ERROR: Wave 8 evidence link missing; no changes made')
text=text.replace(needle,needle+'\n- [Wave 9 evidence — 0046–0050](validation_framework/wave_a/batch_0046_0050/README.md)')
text=text.replace('## Validation and contribution','Wave 9 adds Neousys AGX Orin NVR/PoE systems and Orin NX/Nano panel PCs. Panel PCs are integrated systems; lifecycle and exact SKU require review.\n\n## Validation and contribution')
row_ids=re.findall(r'^\| `CMP-EGC-(\d{4})` \|',text,re.M)
if sorted(row_ids)!=[f'{i:04d}' for i in range(1,51)]:
 sys.exit(f'ERROR: README index inconsistent ({len(row_ids)} rows); no changes made')
out=io.StringIO(newline='');w=csv.DictWriter(out,fieldnames=headers,lineterminator='\n');w.writeheader();w.writerows(rows)
new.write_text(out.getvalue(),encoding='utf-8')
readme.write_text(text,encoding='utf-8')
(root/'validation_framework/integration/INTEGRATION_README.md').write_text('# Integrated master catalog — 50 records\n\nCurrent public snapshot: `master_catalog_0001_0050.csv` (Waves 1–9, 50 unique Component IDs). Historical snapshots are retained.\n\nRecords are manufacturer-sourced `listed` entries, not certifications, performance benchmarks or procurement approvals. Identity and evidence reviews remain pending. Wave 9 includes integrated Neousys panel PCs and AI NVR systems. Algorithm candidates are not tested. Public provenance is in `validation_framework/wave_a/`; confidential engineering and commercial data remain in private Core SSOT.\n',encoding='utf-8')
print('SUCCESS: Master Catalog records=50; unique IDs=50; README index=50')
