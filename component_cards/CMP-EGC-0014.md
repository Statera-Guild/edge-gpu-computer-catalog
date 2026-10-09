---
component_id: CMP-EGC-0014
guild: CMP
class: EGC
manufacturer: Neousys Technology
product_name: NRU-230V-AWP
exact_part_number: unknown
record_scope: family
status: listed
source_urls:
  - https://www.neousys-tech.com/de/core-technologies/neousys-nvidia-jetson-rugged-embedded-computers
last_reviewed: 2026-10-09
---

# CMP-EGC-0014 — Neousys Technology NRU-230V-AWP

## Identity and configuration boundary
- Product form: integrated industrial edge AI computer; not a standalone SOM or GPU card.
- Exact orderable SKU, CPU/GPU options, and included accessories: **not established**.

## CPU, GPU, memory, storage
- CPU/module: NVIDIA Jetson AGX Orin.
- GPU support or integrated GPU: integrated Jetson GPU; shared module memory.
- Installed GPU, dedicated VRAM, installed system RAM, SSD and software image: **unknown until SKU-specific evidence**.
- Jetson shared LPDDR must not be labeled discrete GPU VRAM.

## Power and performance
- Power input: vendor NRU family 8–35V DC; exact model verify.
- Maximum supported GPU-board wattage is **not** system power draw.
- AI TOPS/TFLOPS, precision, sparsity, power mode, actual sustained robot inference throughput: **unknown or not independently reproduced**.

## I/O, mechanical and sensor integration
- Manufacturer-described headline: 8 GMSL2; 1 10GbE; 4 PoE+ GbE; IP66.
- Port pinout, PoE power budget, camera synchronization, CAN/IMU/LiDAR integration, enclosure dimensions, mass, operating temperature and thermal constraints: **requires model-specific official datasheet**.

## Software and algorithm compatibility
- OS, driver, CUDA, TensorRT, JetPack (if applicable), ROS 2, Docker, ONNX Runtime versions: **unknown at selected SKU**.
- Classification, YOLO/DETR, segmentation, MOT, VO, SLAM, Video Transformer, VLM, VLA, World Model: **unknown**; no reproducibility claim.

## Provenance and open questions
- Source: https://www.neousys-tech.com/de/core-technologies/neousys-nvidia-jetson-rugged-embedded-computers
- Source ID: EGC-SRC-0014; manufacturer page / family-level evidence; accessed 2026-10-09.
- Qualification: Provisional CMP-EAM-0003 module-family mapping; exact module option unresolved.
- Status: `listed` only. No PAI-SG certification or validation implied.

## Graph links (proposed; S03 review required)
- Provisional CMP-EAM-0003 module-family mapping; exact module option unresolved.
