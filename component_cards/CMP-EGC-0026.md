---
component_id: CMP-EGC-0026
guild: CMP
class: EGC
manufacturer: AAEON
product_name: BOXER-8642AI
exact_part_number: unknown
record_scope: family
status: listed
source_urls:
  - https://www.aaeon.com/en/news/detail/boxer_8642_news
last_reviewed: 2026-10-09
---

# CMP-EGC-0026 — AAEON BOXER-8642AI

## Identity and product boundary

- Integrated Edge AI computer, not a standalone GPU, accelerator, or bare SOM.
- CPU/GPU platform: Jetson AGX Orin.
- Orderable SKU, shipped configuration, firmware revision, and included power accessories: **unverified**.

## Manufacturer evidence

- Manufacturer-described headline: 32GB/64GB module options; eight independent 10Gbps USB; 12–24V DC.
- Source: https://www.aaeon.com/en/news/detail/boxer_8642_news
- Evidence class: `manufacturer_announcement`; source ID `EGC-SRC-0026`.
- This is a vendor claim, **not an independently reproduced specification**. Exact data-sheet revision and SKU are pending.

## Hardware and power qualification

- Installed GPU/SoC variant, system RAM, storage, exact I/O mapping and mechanical tolerances require SKU-specific verification.
- For Jetson models, LPDDR is shared system memory, not discrete GPU VRAM.
- For PCIe GPU-capable hosts, support for a GPU model does not establish that it is included in the shipped system.
- Module TOPS, GPU board power, power-input rating, PSU capacity and measured whole-system consumption are separate claims.

## PAI-SG algorithm assessment

- Classification, YOLO/DETR, segmentation, multi-object tracking, VO/SLAM, Video Transformer, VLM, VLA, and World Model: **candidate only**, subject to runtime and hardware qualification.
- No PAI-SG measured latency, throughput, power, sustained thermal stability or algorithm validation is asserted.
- ROS 2, BSP/JetPack (if relevant), Linux, CUDA, TensorRT and driver version matrix remains unverified.

## Open verification tasks

- Obtain exact manufacturer datasheet, orderable part number and supported OS/BSP versions.
- Verify camera bandwidth and synchronization, Ethernet/PoE budgets, serial/CAN, mounting, vibration, thermal derating and supply lifecycle.
- Record tested GPU configuration and test artifact before upgrading any compatibility assertion.

## Knowledge graph

- Graph links are provisional; do not ingest normative `USES_MODULE` or `SUPPORTS_ALGORITHM` edges until PAI-SG S03 reconciliation.
