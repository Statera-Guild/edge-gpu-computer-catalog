---
component_id: CMP-EGC-0004
guild: CMP
class: EGC
manufacturer: AAEON
product_name: BOXER-8641AI-PLUS
exact_part_number: unknown
record_scope: family
status: listed
source_urls:
  - https://www.aaeon.com/en/product/detail/ai-edge-solutions-boxer-8641ai-plus/specification
last_reviewed: 2026-10-09
---

# CMP-EGC-0004 — AAEON BOXER-8641AI-PLUS

## Product identity and configuration boundary

- System product form: Industrial fanless AI system.
- Record scope: product family or model; orderable SKU and configuration not yet resolved.
- Underlying processor/module: Jetson AGX Orin. Proposed cross-catalog module reference: `CMP-EAM-0003`. Check the variant before treating this as exact installed hardware.

## CPU, GPU, memory and storage

- Hardware baseline: AGX Orin 32GB/64GB options; 12–19V DC.
- CPU cores/clock, GPU core count, module memory capacities, storage interfaces and options: **consult exact configuration datasheet and order guide before normalizing**.
- **Dedicated GPU VRAM:** Not established; Jetson products generally use shared LPDDR system memory. Do not treat shared LPDDR or flash extensions as discrete VRAM.

## AI performance and energy

- Vendor/module headline: AGX Orin 32GB/64GB options; 12–19V DC.
- Quantization precision, sparsity, clock/power mode and variant for any TOPS claim: **requires explicit source and normalization**.
- Measured inference performance on PAI-SG algorithms: **unknown / not tested**.
- Module TDP: unknown at exact orderable configuration; **whole-system power (W): unknown / not measured**.
- Power input and camera/PoE power budget: **requires model-specific check**.

## Physical I/O and sensor feasibility

- Manufacturer described I/O: 1 GbE; 1 10GbE; 4 USB 3.2 Gen 2; serial.
- Camera interface mapping, aggregate bandwidth, synchronization, PoE total budget, ROS camera drivers, LiDAR ports, CAN and IMU support: **not verified end-to-end**.

## Mechanical, cooling and lifetime

- Vendor form/cooling: Fanless; wall mount.
- Dimensions, mass, ambient range, vibration/shock qualification, airflow constraints, mounting and life-cycle / LTS support: check official mechanical and ordering docs before marking `documented`.

## Software and workloads

- JetPack/BSP/Linux and CUDA/TensorRT exact version matrix: **unknown at this configuration**, except vendor headline information in official source.
- Classification, YOLO/DETR, segmentation, MOT, VO, SLAM, Video Transformer, VLM, VLA, World Model: **compatibility state `unknown`** pending execution/evidence. Neither NVIDIA hardware nor advertised TOPS establishes validated runnability.

## Manufacturer source and research questions

- Official page: https://www.aaeon.com/en/product/detail/ai-edge-solutions-boxer-8641ai-plus/specification
- Source ID: `EGC-SRC-0004` (manufacturer product page; accessed 2026-10-09).
- Verify: exact SKU, GPU configuration, memory/storage as-shipped, full-system power, thermal throttle behavior, software version support, camera counts, supply/availability and official PDF datasheet revision.
- Public record status: `listed` (not verified, qualified, recommended or certified).

## Knowledge graph (proposed; pending S03)

`CMP-EGC-0004 -> USES_MODULE -> CMP-EAM-0003` is a provisional family-level relationship; no normative graph ingestion until S03 reconciliation.
