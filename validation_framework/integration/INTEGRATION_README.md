# PAI-SG Edge GPU Computer Catalog — 25-record integration index

Snapshot date: 2026-10-09. Scope: CMP-EGC-0001 through CMP-EGC-0025, Waves 1–4.

## Purpose
This is an **additive, non-destructive integration patch**. It does not change existing component cards, source registries or batch inventories. `master_catalog_0001_0025.csv` is a unified identity/navigation index, **not** a verified hardware specification database.

## Evidence limitations
Entries 0001–0010 were reconstructed from the known Wave 1 registration list; their current live metadata should be checked against the GitHub cards before declaring reconciliation complete. Entries 0011–0025 were cross-checked against existing batch inventory data or a representative card. All `identity_review` and `evidence_review` flags remain pending. Product status remains `listed`.

## Validation gates
1. Verify unique IDs and card paths.
2. Check family, series, variant, SKU and composite-system distinctions.
3. Map each normalized specification to a manufacturer source and evidence claim ID.
4. Keep supported GPU-board power separate from measured whole-system power.
5. Preserve `candidate`/`unknown` algorithm compatibility until a reproducible benchmark exists.
6. Do not publish private supplier, commercial, or architecture SSOT details.
7. Do not assert normative knowledge graph edges before S03 reconciliation.

## Files
- `master_catalog_0001_0025.csv`: 25-row public navigation index
- `review_queue_0001_0025.csv`: eight cross-batch review issues

Do not mark this integration as fully verified until all source cards and registers are checked.
