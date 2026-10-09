# CMP-EGC-0079 — ADLINK DLAP-401-Xavier

## Public record

- **Manufacturer:** ADLINK
- **Product / family:** DLAP-401-Xavier
- **Catalog category:** Edge GPU Computer (EGC); integrated AI computer or controller
- **Public status:** `listed` (not certified, tested, or procurement-approved)
- **Record scope:** `family`; exact orderable SKU and lifecycle unverified
- **Manufacturer release marker:** `end_of_life` (manufacturer product page explicitly states END OF LIFE)
- **Platform:** NVIDIA Jetson AGX Xavier fanless edge AI inference platform
- **Wave:** 15 (0076–0080); final catalog expansion wave

## Manufacturer evidence

- **Source ID:** `SRC-EGC-0079-01`
- **Source type:** `manufacturer_product_page`
- **Manufacturer URL:** https://www.adlinktech.com/Products/Deep_Learning_Accelerator_Platform_and_Server/Inference_Platform/DLAP-401-Xavier
- **Evidence scope:** Manufacturer product identity, GPU platform and EOL marker; not proof of orderable inventory

## Technical interpretation and review

Manufacturer product page explicitly marks END OF LIFE. Preserve as historical edge GPU platform; do not claim current availability. Confirm exact historical SKU, lifecycle dates, successor, software stack and real-world performance.

## Open verification items

- Confirm manufacturer datasheet revision, historical SKU, EOL date, replacement model and support status.
- Confirm installed GPU/module, memory, thermal/power envelope and I/O.
- Validate JetPack/CUDA/TensorRT or relevant IGX software stack, driver versions and ROS 2 support.
- Run reproducible detection, segmentation, tracking, SLAM and model inference tests on a physical device.

## PAI-SG compatibility status

All algorithm entries are `candidate` / `not_tested`. No compatibility certification or benchmark is implied.

## Public/private boundary

Confidential BOM, vendor pricing and internal design/evidence remain in private Core SSOT.
