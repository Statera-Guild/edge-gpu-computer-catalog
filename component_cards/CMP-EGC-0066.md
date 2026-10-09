# CMP-EGC-0066 — ASUS IoT PE3000N

## Public record

- **Manufacturer:** ASUS IoT
- **Product / family:** PE3000N
- **Catalog category:** Edge GPU Computer (EGC); integrated NVIDIA Jetson GPU platform
- **Public status:** `listed` (not a procurement recommendation)
- **Record scope:** `family`; exact orderable SKU not confirmed
- **Platform:** NVIDIA Jetson Thor edge AI computer
- **Wave:** 13 (0066–0070)

## Manufacturer evidence

- **Source ID:** `SRC-EGC-0066-01`
- **Source type:** official manufacturer portfolio
- **Official manufacturer URL:** https://iot.asus.com/kr/discover/edge-ai-nvidia-jetson-series/
- **Evidence scope:** manufacturer-listed product identity and Jetson platform family. Product-level datasheet, exact module revision, availability and lifecycle remain unverified.

## Technical interpretation and review

Jetson Thor integrated GPU; exact module SKU and revision pending. Manufacturer platform descriptions are not independent benchmarks. No PAI-SG device test, software compatibility test, system power measurement or procurement qualification has been performed.

### Open verification items

- Confirm exact orderable SKU, manufacturer datasheet, lifecycle, region and revision.
- Confirm installed Jetson SoM, GPU architecture, memory and firmware/JetPack compatibility.
- Confirm power/thermal envelope and supported camera, Ethernet and sensor interfaces.
- Run reproducible algorithm, latency and thermal tests on physical hardware.

## PAI-SG compatibility status

Algorithm rows are `candidate` / `not_tested`; they do not assert working compatibility. LiDAR workflows require sensor and software stack verification.

## Public / private boundary

Confidential BOM, commercial terms and internal engineering evidence remain in private Core SSOT.
