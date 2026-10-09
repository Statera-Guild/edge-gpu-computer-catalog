---
component_id: CMP-EGC-0012
guild: CMP
class: EGC
manufacturer: Neousys Technology
product_name: Nuvo-9166GC Series
exact_part_number: unknown
record_scope: family
status: listed
source_urls:
  - https://www.neousys-tech.com/de/product/product-lines/edge-ai-gpu-computing
last_reviewed: 2026-10-09
---

# CMP-EGC-0012 — Neousys Technology Nuvo-9166GC Series

## Identity and configuration boundary
- Product form: integrated industrial edge AI computer; not a standalone SOM or GPU card.
- Exact orderable SKU, CPU/GPU options, and included accessories: **not established**.

## CPU, GPU, memory, storage
- CPU/module: Intel 12th/13th/14th Gen Core.
- GPU support or integrated GPU: supports NVIDIA L4 discrete GPU.
- Installed GPU, dedicated VRAM, installed system RAM, SSD and software image: **unknown until SKU-specific evidence**.
- Jetson shared LPDDR must not be labeled discrete GPU VRAM.

## Power and performance
- Power input: unknown.
- Maximum supported GPU-board wattage is **not** system power draw.
- AI TOPS/TFLOPS, precision, sparsity, power mode, actual sustained robot inference throughput: **unknown or not independently reproduced**.

## I/O, mechanical and sensor integration
- Manufacturer-described headline: dual PCIe slots.
- Port pinout, PoE power budget, camera synchronization, CAN/IMU/LiDAR integration, enclosure dimensions, mass, operating temperature and thermal constraints: **requires model-specific official datasheet**.

## Software and algorithm compatibility
- OS, driver, CUDA, TensorRT, JetPack (if applicable), ROS 2, Docker, ONNX Runtime versions: **unknown at selected SKU**.
- Classification, YOLO/DETR, segmentation, MOT, VO, SLAM, Video Transformer, VLM, VLA, World Model: **unknown**; no reproducibility claim.

## Provenance and open questions
- Source: https://www.neousys-tech.com/de/product/product-lines/edge-ai-gpu-computing
- Source ID: EGC-SRC-0012; manufacturer page / family-level evidence; accessed 2026-10-09.
- Qualification: No module mapping; selected GPU and orderable SKU require verification.
- Status: `listed` only. No PAI-SG certification or validation implied.

## Graph links (proposed; S03 review required)
- No module mapping; selected GPU and orderable SKU require verification.
