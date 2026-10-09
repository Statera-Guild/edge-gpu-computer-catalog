# CMP-EGC-0076 — ADLINK DLAP-701

## Public record

- **Manufacturer:** ADLINK
- **Product / family:** DLAP-701
- **Catalog category:** Edge GPU Computer (EGC); integrated AI computer or controller
- **Public status:** `listed` (not certified, tested, or procurement-approved)
- **Record scope:** `family`; exact orderable SKU and lifecycle unverified
- **Manufacturer release marker:** `published` (as described by source at cataloging)
- **Platform:** NVIDIA Jetson Thor T5000/T4000 compact edge AI computer
- **Wave:** 15 (0076–0080); final catalog expansion wave

## Manufacturer evidence

- **Source ID:** `SRC-EGC-0076-01`
- **Source type:** `manufacturer_product_page`
- **Manufacturer URL:** https://www.adlinktech.com/Products/Deep_Learning_Accelerator_Platform_and_Server/Inference_Platform/DLAP-701?lang=en
- **Evidence scope:** Manufacturer identity/platform family only; family listing is not proof of current commercial availability

## Technical interpretation and review

Confirm orderable Jetson T5000/T4000 SKU, thermal profile and software image. Exact GPU configuration, SKU, software stack, lifecycle and real-world performance require further verification.

## Open verification items

- Confirm manufacturer datasheet revision, orderable SKU, official product page, release and lifecycle.
- Confirm installed GPU/module, memory, thermal/power envelope and I/O.
- Validate JetPack/CUDA/TensorRT or relevant IGX software stack, driver versions and ROS 2 support.
- Run reproducible detection, segmentation, tracking, SLAM and model inference tests on a physical device.

## PAI-SG compatibility status

All algorithm entries are `candidate` / `not_tested`. No compatibility certification or benchmark is implied.

## Public/private boundary

Confidential BOM, vendor pricing and internal design/evidence remain in private Core SSOT.
