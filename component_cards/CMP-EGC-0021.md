# CMP-EGC-0021 — ADLINK DLAP-8100 Series

## Identity
- Component ID: `CMP-EGC-0021`
- Manufacturer: ADLINK
- Product / configuration: DLAP-8100 Series
- Catalog category: Edge GPU Computer
- Subcategory: industrial GPU workstation
- Public documentation status: `listed`
- Registration wave: Wave 4 (0021–0025)
- Evidence level: manufacturer web-page claim; not independently reproduced

## Manufacturer-published characteristics
| Property | Claim / qualification |
|---|---|
| CPU | Intel Core Series 2 / 14th/13th/12th Gen |
| GPU capability | NVIDIA RTX A6000E up to 350 W; PCIe Gen4 x16 |
| System memory | Up to 196 GB DDR5; four SODIMM slots |
| Interfaces | 3 x 2.5GbE; 4 x COM; digital I/O |
| Notes | NVIDIA Qualified System; 4 hot-swappable SATA trays |

## PAI-SG integration assessment
- Potential workload classes: object detection, segmentation, multi-object tracking, visual SLAM, multi-camera inference, VLM/VLA evaluation, subject to GPU and software configuration.
- Compatibility status for every workload: `candidate`, **not** a confirmed successful run.
- Benchmark results, latency, sustained FPS, model capacity, and deployment temperature: `unknown`.
- GPU support rating, installed GPU TDP, PSU nameplate, measured wall power, and sustained workload power are different fields and must not be conflated.
- Operating system, driver, CUDA, TensorRT, ROS 2, and kernel versions require SKU-specific confirmation.

## Evidence
- Manufacturer source: https://www.adlinktech.com/Products/industrial_pcs_fanless_embedded_pcs/IPCSystems/DLAP-8100_Series
- Evidence class: `manufacturer_product_page`
- Verification: web-page level, reviewed 2026-10-09; no hardware testing
- Supporting registers: `validation_framework/wave_a/batch_0021_0025/`

## Review / open questions
- Confirm orderable SKU and exact GPU model(s), PCIe lane allocation, power supply and cooling.
- Confirm mechanical, shock/vibration, temperature, certification and lifecycle requirements for robotics use.
- Verify exact system configuration before claiming software compatibility.
