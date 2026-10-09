# CMP-EGC-0024 — ADLINK DLAP-4000 Series

## Identity
- Component ID: `CMP-EGC-0024`
- Manufacturer: ADLINK
- Product / configuration: DLAP-4000 Series
- Catalog category: Edge GPU Computer
- Subcategory: industrial single GPU workstation
- Public documentation status: `listed`
- Registration wave: Wave 4 (0021–0025)
- Evidence level: manufacturer web-page claim; not independently reproduced

## Manufacturer-published characteristics
| Property | Claim / qualification |
|---|---|
| CPU | 8th/9th Gen Intel Core |
| GPU capability | FHFL dual-width PEG; NVIDIA Quadro cards in vendor recommendation |
| System memory | Up to 32 GB DDR4 non-ECC |
| Interfaces | DVI HDMI DP; mini PCIe |
| Notes | 300 W / 500 W Flex ATX PSU options; older generation |

## PAI-SG integration assessment
- Potential workload classes: object detection, segmentation, multi-object tracking, visual SLAM, multi-camera inference, VLM/VLA evaluation, subject to GPU and software configuration.
- Compatibility status for every workload: `candidate`, **not** a confirmed successful run.
- Benchmark results, latency, sustained FPS, model capacity, and deployment temperature: `unknown`.
- GPU support rating, installed GPU TDP, PSU nameplate, measured wall power, and sustained workload power are different fields and must not be conflated.
- Operating system, driver, CUDA, TensorRT, ROS 2, and kernel versions require SKU-specific confirmation.

## Evidence
- Manufacturer source: https://www.adlinktech.com/Products/Industrial_PCs_Fanless_Embedded_PCs/IPCSystems/DLAP-4000_Series
- Evidence class: `manufacturer_product_page`
- Verification: web-page level, reviewed 2026-10-09; no hardware testing
- Supporting registers: `validation_framework/wave_a/batch_0021_0025/`

## Review / open questions
- Confirm orderable SKU and exact GPU model(s), PCIe lane allocation, power supply and cooling.
- Confirm mechanical, shock/vibration, temperature, certification and lifecycle requirements for robotics use.
- Verify exact system configuration before claiming software compatibility.
