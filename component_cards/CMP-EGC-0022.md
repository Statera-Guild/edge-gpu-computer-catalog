# CMP-EGC-0022 — ADLINK DLAP-5200 Series

## Identity
- Component ID: `CMP-EGC-0022`
- Manufacturer: ADLINK
- Product / configuration: DLAP-5200 Series
- Catalog category: Edge GPU Computer
- Subcategory: fanless MXM GPU IPC
- Public documentation status: `listed`
- Registration wave: Wave 4 (0021–0025)
- Evidence level: manufacturer web-page claim; not independently reproduced

## Manufacturer-published characteristics
| Property | Claim / qualification |
|---|---|
| CPU | Intel Core Series 2 / 14th/13th/12th Gen |
| GPU capability | MXM 3.1 Type A/B module; GPU depends on orderable SKU |
| System memory | Up to 196 GB DDR5 |
| Interfaces | Front-accessible I/O; exact ports depend on SKU |
| Notes | Order examples RTX3000 and A2000; Linux Ubuntu 22.04 listed |

## PAI-SG integration assessment
- Potential workload classes: object detection, segmentation, multi-object tracking, visual SLAM, multi-camera inference, VLM/VLA evaluation, subject to GPU and software configuration.
- Compatibility status for every workload: `candidate`, **not** a confirmed successful run.
- Benchmark results, latency, sustained FPS, model capacity, and deployment temperature: `unknown`.
- GPU support rating, installed GPU TDP, PSU nameplate, measured wall power, and sustained workload power are different fields and must not be conflated.
- Operating system, driver, CUDA, TensorRT, ROS 2, and kernel versions require SKU-specific confirmation.

## Evidence
- Manufacturer source: https://www.adlinktech.com/Products/industrial_pcs_fanless_embedded_pcs/IPCSystems/DLAP-5200_Series
- Evidence class: `manufacturer_product_page`
- Verification: web-page level, reviewed 2026-10-09; no hardware testing
- Supporting registers: `validation_framework/wave_a/batch_0021_0025/`

## Review / open questions
- Confirm orderable SKU and exact GPU model(s), PCIe lane allocation, power supply and cooling.
- Confirm mechanical, shock/vibration, temperature, certification and lifecycle requirements for robotics use.
- Verify exact system configuration before claiming software compatibility.
