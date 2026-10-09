# CMP-EGC-0074 — Advantech MIB-741-AT

## Public record

- **Manufacturer:** Advantech
- **Product / family:** MIB-741-AT
- **Catalog category:** Edge GPU Computer (EGC); integrated AI computer
- **Public status:** `listed` (not certified, tested or procurement-approved)
- **Record scope:** `family`; exact orderable SKU and lifecycle not confirmed
- **Platform:** NVIDIA Jetson Thor T4000; AI inference system
- **Wave:** 14 (0071–0075)

## Manufacturer evidence

- **Source ID:** `SRC-EGC-0074-01`
- **Source type:** Manufacturer product/catalog page
- **Manufacturer URL:** https://www.advantech.com/ko-kr/products/f8c8792f-5837-421d-b268-f40a8fc1e484/mib-741-at/mod_68d73d71-4805-4925-b59c-cd067364b41c
- **Evidence scope:** Model identity and platform family; not independent measured performance

## Technical interpretation and review

Confirm orderable SKU, GMSL2 accessories and current lifecycle. Manufacturer platform information is not proof of a particular orderable configuration, performance, long-term availability or PAI-SG algorithm compatibility.

### Open verification items

- Confirm exact SKU, manufacturer datasheet revision, lifecycle and regional availability.
- Confirm installed NVIDIA module, GPU memory, thermal envelope, power and interfaces.
- Confirm software/driver stack, JetPack/CUDA/TensorRT and ROS 2 compatibility for the actual device.
- Execute reproducible PAI-SG detection, segmentation, tracking, SLAM and model-inference tests.

## PAI-SG compatibility status

All algorithm rows are `candidate` / `not_tested`; no tested or certified support is asserted. Graph edges remain provisional pending S03 mapping.

## Public / private boundary

Confidential BOM, internal engineering evidence, restricted pricing and supplier terms remain in private Core SSOT.
