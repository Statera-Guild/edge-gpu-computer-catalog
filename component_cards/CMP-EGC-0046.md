# CMP-EGC-0046 — Neousys Technology NRU-220S

## Public record

- **Manufacturer:** Neousys Technology
- **Product / family:** NRU-220S
- **Catalog category:** Edge GPU Computer (EGC); integrated system
- **Public status:** `listed`
- **Record scope:** `family`; exact orderable SKU not confirmed
- **Platform:** NVIDIA Jetson AGX Orin (manufacturer-described; variant to verify)
- **Wave:** 9 (0046–0050)

## Manufacturer evidence

- **Source ID:** `SRC-EGC-0046-01`
- **Source type:** `manufacturer_product_page` / `manufacturer_technology_overview` (see source registry)
- **Official manufacturer URL:** https://www.neousys-tech.com/en/product/product-lines/edge-ai-gpu-computing/nru-220s-nru-222s
- **Evidence scope:** Product family identity, platform class and stated application/interface category; datasheet and exact SKU review pending.

## Technical interpretation and review

AI NVR; 4 shared PoE+ GbE and 2 2.5GbE ports. Manufacturer-described features are not independently reproduced PAI-SG results. Exact installed Jetson module, firmware, environmental rating, connector option, region, availability and lifecycle are unverified.

### Open verification items

- Confirm exact orderable SKU, hardware revision, region and lifecycle.
- Verify installed compute module, memory, storage, power and thermal limits against dated datasheet.
- Verify camera interfaces and connector count for the selected SKU.
- Validate JetPack, CUDA, TensorRT, ROS 2 and target algorithms on hardware before claiming support.

## PAI-SG compatibility status

Algorithm entries are `candidate` / `not_tested`; no hardware performance, latency, power or certification claim is asserted. Graph edges remain provisional pending PAI-SG S03 mapping.

## Public / private boundary

This public card excludes confidential BOM, supplier pricing, private PAI-SG architecture and unpublished test evidence.
