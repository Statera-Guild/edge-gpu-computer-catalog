---
component_id: CMP-EGC-0031
guild: CMP
class: EGC
manufacturer: AAEON
product_name: BOXER-8640AI
exact_part_number: unknown
record_scope: family
status: listed
source_urls:
  - https://www.aaeon.com/en/news/detail/ces-orin-product-announcement
last_reviewed: 2026-10-09
---

# CMP-EGC-0031 — AAEON BOXER-8640AI

## Identity and configuration boundary
- Finished industrial edge AI computer; not a standalone Jetson module.
- Product form: fanless embedded AI system.
- Exact orderable SKU, shipping configuration, lifecycle and region-specific availability: **unverified**.

## Manufacturer-published evidence
- Processor family: NVIDIA Jetson AGX Orin 32GB (module option and revision require SKU verification).
- Manufacturer statement: AAEON lists AGX Orin 32GB; verify exact module and SKU.
- Manufacturer source: https://www.aaeon.com/en/news/detail/ces-orin-product-announcement
- Evidence class: manufacturer announcement or manufacturer catalog listing, **not** independent measurement.

## Hardware and integration gaps
- Exact CPU/GPU clocks, installed shared LPDDR, storage, I/O, sensor timing, CAN, PoE budget, and power-input requirements: **not normalized from an SKU-specific datasheet**.
- Jetson memory is shared LPDDR; do not report it as discrete dedicated GPU VRAM.
- Module power mode, board power budget, full-system measured watts, ambient operating envelope, dimensions, thermal throttling, and shock/vibration evidence: **unknown / needs official datasheet and testing**.
- JetPack/BSP, CUDA, TensorRT, ROS 2, kernel, camera drivers and software image versions: **not verified at selected SKU**.

## PAI-SG algorithm assessment
- Candidate workloads: classification, YOLO/DETR, segmentation, multi-object tracking, visual odometry/SLAM, Video Transformer, VLM, VLA, and World Model evaluation.
- All algorithm mappings are `candidate`, **not** `reproduced` or benchmarked.
- Actual FPS, latency, throughput, memory ceiling, thermal sustainability and robotic deployment qualification: **unknown**.

## Evidence and review
- Official source: https://www.aaeon.com/en/news/detail/ces-orin-product-announcement
- Registry ID: `EGC-SRC-0031`.
- Public status: `listed`. No PAI-SG certification or recommendation implied.
- Check the manufacturer catalog for lifecycle changes and resolve exact SKU before raising status.
- S03 Knowledge Graph relationships are provisional; no definitive `USES_MODULE` edge without variant evidence.
