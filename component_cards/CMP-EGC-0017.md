---
component_id: CMP-EGC-0017
guild: CMP
class: EGC
manufacturer: ASUS IoT
product_name: PE8000G
exact_part_number: unknown
record_scope: family
status: listed
source_urls:
  - https://www.asus.com/kr/networking-iot-servers/aiot-industrial-solutions/embedded-computers-edge-ai-systems/pe8000g/
last_reviewed: 2026-10-09
---

# CMP-EGC-0017 — ASUS IoT PE8000G

## Product boundary
Integrated GPU-capable industrial edge computer. This is a product-family entry, not a fixed fully configured and tested SKU. GPU card, VRAM, CPU selection, RAM, storage, PSU and accessories are not assumed included.

## Manufacturer-described capabilities
- CPU platform: Intel Core Series 2 or 14th/13th/12th Gen.
- GPU accommodation: dual discrete GPU cards, up to 450W per GPU.
- Input power: 8–48V DC (check configuration-specific operating constraints).
- Interfaces / enclosure: rugged dual GPU, ignition power control.
- Installed GPU, dedicated VRAM, RAM, storage, GPU software stack and exact orderable SKU: **unknown**.

## Evidence and interpretation
- Official manufacturer evidence: https://www.asus.com/kr/networking-iot-servers/aiot-industrial-solutions/embedded-computers-edge-ai-systems/pe8000g/
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
