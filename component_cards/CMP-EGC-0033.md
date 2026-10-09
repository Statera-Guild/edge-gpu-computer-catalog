---
component_id: CMP-EGC-0033
guild: CMP
class: EGC
manufacturer: AAEON
product_name: BOXER-8646AI
exact_part_number: unknown
record_scope: family
status: listed
source_urls:
  - https://www.aaeon.com/en/news/detail/ces-orin-product-announcement
last_reviewed: 2026-10-09
---

# CMP-EGC-0033 — AAEON BOXER-8646AI

## Identity and configuration boundary
- Finished industrial edge AI computer; not a standalone Jetson module.
- Product form: PoE multi-camera edge system.
- Exact orderable SKU, shipping configuration, lifecycle and region-specific availability: **unverified**.

## Manufacturer-published evidence
- Processor family: NVIDIA Jetson AGX Orin (module option and revision require SKU verification).
- Manufacturer statement: AAEON announced 12 PoE RJ-45 LAN ports and 10GbE; check SKU and power budget.
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
- Registry ID: `EGC-SRC-0033`.
- Public status: `listed`. No PAI-SG certification or recommendation implied.
- Check the manufacturer catalog for lifecycle changes and resolve exact SKU before raising status.
- S03 Knowledge Graph relationships are provisional; no definitive `USES_MODULE` edge without variant evidence.
