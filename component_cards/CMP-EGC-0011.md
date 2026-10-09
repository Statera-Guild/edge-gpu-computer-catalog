---
component_id: CMP-EGC-0011
guild: CMP
class: EGC
manufacturer: Neousys Technology
product_name: Nuvo-10108GC
exact_part_number: unknown
record_scope: family
status: listed
source_urls:
  - https://www.neousys-tech.com/ja/product/processor/intel-ipc/intel-14th-13th-12th-gen-core/nuvo-10108gc-intel-13th-350w-rtx-gpu-computing-platform
last_reviewed: 2026-10-09
---

# CMP-EGC-0011 — Neousys Technology Nuvo-10108GC

## Identity and configuration boundary
- Product form: integrated industrial edge AI computer; not a standalone SOM or GPU card.
- Exact orderable SKU, CPU/GPU options, and included accessories: **not established**.

## CPU, GPU, memory, storage
- CPU/module: Intel 12th/13th/14th Gen Core.
- GPU support or integrated GPU: single discrete NVIDIA RTX GPU, up to 350W GPU support.
- Installed GPU, dedicated VRAM, installed system RAM, SSD and software image: **unknown until SKU-specific evidence**.
- Jetson shared LPDDR must not be labeled discrete GPU VRAM.

## Power and performance
- Power input: 8–48V DC; higher load requires >=13.8V.
- Maximum supported GPU-board wattage is **not** system power draw.
- AI TOPS/TFLOPS, precision, sparsity, power mode, actual sustained robot inference throughput: **unknown or not independently reproduced**.

## I/O, mechanical and sensor integration
- Manufacturer-described headline: 3 additional PCIe expansion slots.
- Port pinout, PoE power budget, camera synchronization, CAN/IMU/LiDAR integration, enclosure dimensions, mass, operating temperature and thermal constraints: **requires model-specific official datasheet**.

## Software and algorithm compatibility
- OS, driver, CUDA, TensorRT, JetPack (if applicable), ROS 2, Docker, ONNX Runtime versions: **unknown at selected SKU**.
- Classification, YOLO/DETR, segmentation, MOT, VO, SLAM, Video Transformer, VLM, VLA, World Model: **unknown**; no reproducibility claim.

## Provenance and open questions
- Source: https://www.neousys-tech.com/ja/product/processor/intel-ipc/intel-14th-13th-12th-gen-core/nuvo-10108gc-intel-13th-350w-rtx-gpu-computing-platform
- Source ID: EGC-SRC-0011; manufacturer page / family-level evidence; accessed 2026-10-09.
- Qualification: No module mapping; exact RTX GPU and VRAM depend on selected option.
- Status: `listed` only. No PAI-SG certification or validation implied.

## Graph links (proposed; S03 review required)
- No module mapping; exact RTX GPU and VRAM depend on selected option.
