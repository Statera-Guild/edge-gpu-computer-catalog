# PAI-SG Edge GPU Computer Catalog

Public manufacturer-evidence catalog of **complete edge GPU computer systems** for robotics and Physical AI, managed by Statera-Guild. This is an engineering reference, **not** certification, benchmarking evidence, a procurement recommendation, or a description of the private PAI-SG architecture.

## Scope and separation

- `EGC` includes enclosed integrated computers with CPU/GPU, memory, practical power input, cooling and accessible external I/O. Exclude standalone GPU/SoC/SOM and bare accelerator cards.
- NVIDIA Jetson SOMs belong to [`edge-device-catalog`](https://github.com/Statera-Guild/edge-device-catalog) as `EAM`; finished systems using those SOMs belong here as `EGC`.
- Names/IDs are immutable; family-card versus specific purchasable SKU must be explicit. A family record does not certify every listed option.
- Public statuses: `listed` (identified with primary manufacturer evidence) or `documented` (major technical facts supported by manufacturer documents). Neither implies independent verification.
- Public repo: official product facts, citations, uncertainty and research questions only. Confidential quotations, purchase terms, internal BOM, restricted test evidence and internal architecture live in private Core SSOT.

## Initial 10 records (Wave 1)

| Component ID | Manufacturer | Product / product family | Status | Card |
|---|---|---|---|---|
| CMP-EGC-0001 | Advantech | MIC-733-AO | listed | [Open](component_cards/CMP-EGC-0001.md) |
| CMP-EGC-0002 | Advantech | MIC-711-OX | listed | [Open](component_cards/CMP-EGC-0002.md) |
| CMP-EGC-0003 | AAEON | BOXER-8641AI | listed | [Open](component_cards/CMP-EGC-0003.md) |
| CMP-EGC-0004 | AAEON | BOXER-8641AI-PLUS | listed | [Open](component_cards/CMP-EGC-0004.md) |
| CMP-EGC-0005 | AAEON | BOXER-8653AI | listed | [Open](component_cards/CMP-EGC-0005.md) |
| CMP-EGC-0006 | ADLINK | DLAP-411-Orin | listed | [Open](component_cards/CMP-EGC-0006.md) |
| CMP-EGC-0007 | ADLINK | DLAP-411-Orin Supreme | listed | [Open](component_cards/CMP-EGC-0007.md) |
| CMP-EGC-0008 | ADLINK | DLAP-211-Orin Series | listed | [Open](component_cards/CMP-EGC-0008.md) |
| CMP-EGC-0009 | ADLINK | DLAP-211-Orin NX 16GB | listed | [Open](component_cards/CMP-EGC-0009.md) |
| CMP-EGC-0010 | Advantech | MIC-736 | listed | [Open](component_cards/CMP-EGC-0010.md) |

## Validation principle

Every material claim must point to a source; additional evidence levels belong to the *claim*, not the public card status. `candidate`, `vendor_claim`, `reproduced`, `failed`, and `unknown` are **algorithm compatibility claim statuses**, not Component Card statuses. Zero PAI-SG execution benchmarks are asserted for Wave 1.

Graph predicates such as `USES_MODULE` or `SUPPORTS_ALGORITHM` are provisional until reconciled against PAI-SG S03.

See `COMPONENT_CARD_SCHEMA.md`, `validation_framework/docs/EVIDENCE_POLICY.md`, `validation_framework/schemas/*.json` and `validation_framework/wave_a/`.

Last research review: 2026-10-09.
