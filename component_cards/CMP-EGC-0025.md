# CMP-EGC-0025 — Advantech MIC-770 V3 + MIC-75G20

## Identity
- Component ID: `CMP-EGC-0025`
- Manufacturer: Advantech
- Product / configuration: MIC-770 V3 + MIC-75G20
- Catalog category: Edge GPU Computer
- Subcategory: modular GPU IPC system configuration
- Public documentation status: `listed`
- Registration wave: Wave 4 (0021–0025)
- Evidence level: manufacturer web-page claim; not independently reproduced

## Manufacturer-published characteristics
| Property | Claim / qualification |
|---|---|
| CPU | 12th/13th/14th Gen Intel Core, subject to MIC-770 V3 SKU |
| GPU capability | MIC-75G20 supports NVIDIA GPU card up to 350 W, 2.75-slot |
| System memory | MIC-770 V3 memory varies by SKU |
| Interfaces | MIC-75G20: PCIe x16 + PCIe x4; dual removable 2.5-inch bays |
| Notes | Configuration, not standalone MIC-75G20 computer; host and expansion compatibility must be verified |

## PAI-SG integration assessment
- Potential workload classes: object detection, segmentation, multi-object tracking, visual SLAM, multi-camera inference, VLM/VLA evaluation, subject to GPU and software configuration.
- Compatibility status for every workload: `candidate`, **not** a confirmed successful run.
- Benchmark results, latency, sustained FPS, model capacity, and deployment temperature: `unknown`.
- GPU support rating, installed GPU TDP, PSU nameplate, measured wall power, and sustained workload power are different fields and must not be conflated.
- Operating system, driver, CUDA, TensorRT, ROS 2, and kernel versions require SKU-specific confirmation.

## Evidence
- Manufacturer source: https://www.advantech.com/en-us/products/088556da-e8d6-4502-8e67-17567a0a95b5/mic-75g20/mod_e39bfbcf-f640-4445-a411-21376c45532d
- Evidence class: `manufacturer_product_page`
- Verification: web-page level, reviewed 2026-10-09; no hardware testing
- Supporting registers: `validation_framework/wave_a/batch_0021_0025/`

## Review / open questions
- Confirm orderable SKU and exact GPU model(s), PCIe lane allocation, power supply and cooling.
- Confirm mechanical, shock/vibration, temperature, certification and lifecycle requirements for robotics use.
- Verify exact system configuration before claiming software compatibility.
