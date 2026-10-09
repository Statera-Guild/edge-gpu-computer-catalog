# CMP-EGC-0060 — Neousys Technology Nuvo-10000 Series

## Public record

- **Manufacturer:** Neousys Technology
- **Product / family:** Nuvo-10000 Series
- **Catalog category:** Edge GPU Computer (EGC); integrated industrial computer or GPU-capable host
- **Public status:** `listed` (not a procurement recommendation)
- **Record scope:** `family`; exact orderable SKU and GPU option not confirmed
- **Platform:** Expandable industrial GPU-capable computer
- **Wave:** 11 (0056–0060)

## Manufacturer evidence

- **Source ID:** `SRC-EGC-0060-01`
- **Source type:** Manufacturer manual
- **Manufacturer URL:** https://neousys.eu/images/uploaded/nuvo-10000_manual_ver_1-2.pdf
- **Evidence scope:** Product identity and GPU-capable family only. GPU compatibility matrices are vendor claims, not measured performance.

## Technical interpretation and review

GPU is optional; exact PCIe expansion/GPU configuration must be verified. A discrete GPU may be optional, and GPU capability must not be misrepresented as a shipped GPU configuration. No independent PAI-SG test, system power measurement, inference benchmark, software compatibility, safety certification or procurement qualification has been performed.

### Open verification items

- Confirm exact orderable SKU, current lifecycle, regional availability and revision.
- Confirm whether GPU is installed, its model, memory, power budget, cooling and supported drivers.
- Confirm camera/network interfaces and mechanical/electrical fit of the final configuration.
- Verify algorithm compatibility with reproducible on-device tests.

## PAI-SG compatibility status

Algorithm rows are `candidate` / `not_tested`, not verified support. Graph edges remain provisional pending S03 mapping.

## Public / private boundary

Confidential BOM, restricted commercial terms and internal engineering evidence remain in private Core SSOT.
