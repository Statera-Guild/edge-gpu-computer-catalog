# Vendor and Platform Risk Register — Wave 1

| Risk ID | Vendor / platform | Risk | Required mitigation |
|---|---|---|---|
| EGC-R01 | NVIDIA Jetson | Vendor TOPS depend on precision, sparsity, power mode, model and variant | Store benchmark condition; no fps claims absent reproducible test |
| EGC-R02 | All Jetson OEMs | Integrated module power/TDP confused with total computer input | Collect measured DC input including cameras and drives |
| EGC-R03 | All Jetson OEMs | Shared LPDDR memory mislabeled GPU dedicated VRAM | Distinguish unified memory from dedicated graphics VRAM |
| EGC-R04 | ADLINK | aiDAPTIV+ flash-assisted model capacity confused with GPU RAM | Record architecture, latency, endurance and vendor-only performance claims separately |
| EGC-R05 | All | Ethernet/PoE count mistaken for independently supported synchronized cameras | Verify sensor SDK, PoE budget, capture drivers, timestamps and synchronization |
| EGC-R06 | All | Linux/JetPack presence mistaken for all ROS 2 or TensorRT versions | Capture exact OS, JetPack, TensorRT, ROS distribution, container runtime and ABI |
| EGC-R07 | All | Fanless headline mistaken for sustained operation at ambient extremes | Validate airflow, power profile, enclosure and thermal throttling |
| EGC-R08 | All | Product family mistaken for purchasable orderable SKU | Require ordering table and revision before procurement |
| EGC-R09 | All | End-of-life or lead time unknown | Check official lifecycle and support channels on schedule |
| EGC-R10 | All | Internal engineering evidence accidentally published | Separate public summaries from confidential SSOT/evidence repositories |
