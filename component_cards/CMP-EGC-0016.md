---
component_id: CMP-EGC-0016
guild: CMP
class: EGC
manufacturer: Neousys Technology
product_name: Nuvo-10208GC
exact_part_number: unknown
record_scope: family
status: listed
source_urls:
  - https://www.neousys-tech.com.cn/cn/product/processor/intel-ipc/nuvo-10208gc-intel-13th-nvidia-rtx-gpu-computing-platform
last_reviewed: 2026-10-09
---

# CMP-EGC-0016 — Neousys Technology Nuvo-10208GC

## Product boundary
Integrated GPU-capable industrial edge computer. This is a product-family entry, not a fixed fully configured and tested SKU. GPU card, VRAM, CPU selection, RAM, storage, PSU and accessories are not assumed included.

## Manufacturer-described capabilities
- CPU platform: Intel 14th/13th/12th Gen Core.
- GPU accommodation: dual discrete NVIDIA RTX GPUs, up to 350W per GPU.
- Input power: 8–48V DC (check configuration-specific operating constraints).
- Interfaces / enclosure: dual 2.5GbE, 1GbE, optional 10GbE, additional PCIe slots.
- Installed GPU, dedicated VRAM, RAM, storage, GPU software stack and exact orderable SKU: **unknown**.

## Evidence and interpretation
- Official manufacturer evidence: https://www.neousys-tech.com.cn/cn/product/processor/intel-ipc/nuvo-10208gc-intel-13th-nvidia-rtx-gpu-computing-platform
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
