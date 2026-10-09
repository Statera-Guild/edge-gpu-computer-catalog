---
component_id: CMP-EGC-0032
guild: CMP
class: EGC
manufacturer: AAEON
product_name: BOXER-8645AI
exact_part_number: unknown
record_scope: family
status: listed
source_urls:
  - https://www.aaeon.com/jp/news/detail/gtc-2023
last_reviewed: 2026-10-09
---

# CMP-EGC-0032 — AAEON BOXER-8645AI

## Identity and configuration boundary
- Finished industrial edge AI computer; not a standalone Jetson module.
- Product form: GMSL2 multi-camera edge system.
- Exact orderable SKU, shipping configuration, lifecycle and region-specific availability: **unverified**.

## Manufacturer-published evidence
- Processor family: NVIDIA Jetson AGX Orin (module option and revision require SKU verification).
- Manufacturer statement: AAEON announced eight GMSL2 ports and HDMI 2.1; manufacturer catalog flags product discontinuation; check lifecycle.
- Manufacturer source: https://www.aaeon.com/jp/news/detail/gtc-2023
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
- Official source: https://www.aaeon.com/jp/news/detail/gtc-2023
- Registry ID: `EGC-SRC-0032`.
- Public status: `listed`. No PAI-SG certification or recommendation implied.
- Check the manufacturer catalog for lifecycle changes and resolve exact SKU before raising status.
- S03 Knowledge Graph relationships are provisional; no definitive `USES_MODULE` edge without variant evidence.
