# Edge GPU Computer Component Card Schema

Guild `CMP`; class `EGC`; immutable IDs `CMP-EGC-0001` onward. Only `listed` / `documented` are allowed as **public card** status.

Required fields: `component_id`, `guild`, `class`, `manufacturer`, `product_name`, `exact_part_number`, `record_scope`, `status`, `source_urls`, `last_reviewed`. Use `unknown` (never fabricated specs) for absent facts. `exact_part_number: unknown` is permitted for family records; do not confuse model name with orderable SKU.

`record_scope` = `family` or `configuration`. Family records describe options, not a verified specific as-shipped SKU. Full-system features must never be inherited automatically from the underlying module, and module TOPS are never real model latency. GPU VRAM is distinct from Jetson shared system memory and flash-backed model capacity.

## Required technical sections

1. Identity and scope / product form / variant boundary.
2. CPU/GPU and module association, memory vs dedicated GPU VRAM, storage.
3. AI compute claims with precision, sparsity, power-mode, model/variant provenance.
4. Whole system input and consumption vs module TDP; cooling/thermal throttling.
5. Ports, connectors, sensor/camera feasibility, PoE supply budget.
6. Mechanical/environmental claims, test conditions, lifecycle.
7. OS/BSP/JetPack/drivers and candidate algorithm workloads.
8. Citations, unknowns, compatibility evidence and PAI-SG graph crosslinks.

Compatible assertions: `candidate`, `vendor_claim`, `reproduced`, `failed`, `unknown`; `reproduced` requires workload, software versions, test host configuration, dataset, commands, metrics and traceable evidence. No card should advertise certified/verified/approved status absent governance.
