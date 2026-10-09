---
component_id: CMP-EGC-0020
guild: CMP
class: EGC
manufacturer: ASUS IoT
product_name: EBS-4U1000
exact_part_number: unknown
record_scope: family
status: listed
source_urls:
  - https://www.asus.com/content/asus-iot-edge-ai-systems/
last_reviewed: 2026-10-09
---

# CMP-EGC-0020 — ASUS IoT EBS-4U1000

## Product boundary
Integrated GPU-capable industrial edge computer. This is a product-family entry, not a fixed fully configured and tested SKU. GPU card, VRAM, CPU selection, RAM, storage, PSU and accessories are not assumed included.

## Manufacturer-described capabilities
- CPU platform: unknown.
- GPU accommodation: up to three discrete 450W GPU cards.
- Input power: unknown (check configuration-specific operating constraints).
- Interfaces / enclosure: 4U system; exact orderable configuration and chassis interfaces pending.
- Installed GPU, dedicated VRAM, RAM, storage, GPU software stack and exact orderable SKU: **unknown**.

## Evidence and interpretation
- Official manufacturer evidence: https://www.asus.com/content/asus-iot-edge-ai-systems/
- The supported GPU-board power is **not** total system input power, guaranteed sustained GPU power, installed GPU configuration, or measured AI throughput.
- Product-family capabilities and ordering-option compatibility require SKU-specific datasheet confirmation. Manufacturer web claims may change; check datasheet revision.

## PAI-SG algorithm compatibility
Classification, YOLO/DETR, segmentation, multi-object tracking, visual odometry, SLAM, video transformer, VLM, VLA and world model: **unknown** pending selected GPU, driver/runtime versions and reproducible benchmarks. No test has been performed.

## Validation gaps
- Exact GPU compatibility list, GPU count, VRAM, card physical dimensions and slot topology.
- Total system power, DC supply sizing, transient peaks, cooling and thermal derating with GPU(s) installed.
- Ethernet/USB/PCIe/CAN/serial, sensor synchronization, ROS 2 and container runtime versions.
- Operating temperature with GPU load, dimensions, mass, mount, lifecycle and certifications.

## Proposed graph edges (not S03 approved)
- EdgeGPUComputer -> HAS_GPU -> GPU (only after GPU configuration is established).
- EdgeGPUComputer -> SUPPORTS_ALGORITHM -> Algorithm (only via evidence-backed compatibility assertion).

**Status:** `listed` — manufacturer-referenced entry only, not independently validated or certified.
