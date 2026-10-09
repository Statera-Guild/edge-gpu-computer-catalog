# CMP-EGC-0071 — AAEON BOXER-8655AI

## Public record

- **Manufacturer:** AAEON
- **Product / family:** BOXER-8655AI
- **Catalog category:** Edge GPU Computer (EGC); integrated AI computer
- **Public status:** `listed` (not certified, tested or procurement-approved)
- **Record scope:** `family`; exact orderable SKU and lifecycle not confirmed
- **Platform:** NVIDIA Jetson Orin NX; fanless embedded AI system; GMSL2 cameras
- **Wave:** 14 (0071–0075)

## Manufacturer evidence

- **Source ID:** `SRC-EGC-0071-01`
- **Source type:** Manufacturer product/catalog page
- **Manufacturer URL:** https://www.aaeon.com/en/product/detail/ai-edge-solutions-boxer-8655ai
- **Evidence scope:** Model identity and platform family; not independent measured performance

## Technical interpretation and review

8GB/16GB SKU selection and GMSL2 camera interoperability require validation. Manufacturer platform information is not proof of a particular orderable configuration, performance, long-term availability or PAI-SG algorithm compatibility.

### Open verification items

- Confirm exact SKU, manufacturer datasheet revision, lifecycle and regional availability.
- Confirm installed NVIDIA module, GPU memory, thermal envelope, power and interfaces.
- Confirm software/driver stack, JetPack/CUDA/TensorRT and ROS 2 compatibility for the actual device.
- Execute reproducible PAI-SG detection, segmentation, tracking, SLAM and model-inference tests.

## PAI-SG compatibility status

All algorithm rows are `candidate` / `not_tested`; no tested or certified support is asserted. Graph edges remain provisional pending S03 mapping.

## Public / private boundary

Confidential BOM, internal engineering evidence, restricted pricing and supplier terms remain in private Core SSOT.
