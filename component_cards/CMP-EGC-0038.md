# CMP-EGC-0038 — Advantech MIC-713-OX

## Public record

- **Manufacturer:** Advantech
- **Product / family:** MIC-713-OX
- **Catalog category:** Edge GPU Computer (EGC); integrated system
- **Public status:** `listed`
- **Record scope:** `family`; exact orderable SKU not confirmed
- **Platform:** NVIDIA Jetson Orin NX (manufacturer-described family; verify variant)
- **Wave:** 7 (0036–0040)

## Manufacturer evidence

- **Source ID:** `SRC-EGC-0038-01`
- **Source type:** `manufacturer_product_page`
- **Official manufacturer URL:** https://www.advantech.com/en-us/products/965e4edb-fb98-429e-89ed-9a0a8435a7be/mic-713-ox/mod_6d301c11-8606-44ce-8179-b31753b59c23
- **Evidence scope:** Product identity and platform family. Detailed specifications must be checked against a dated datasheet and exact SKU.

## Technical interpretation and review

Compact fanless inference computer; memory and module variant unresolved. No independent PAI-SG test, power measurement, latency benchmark, software compatibility, safety certification or procurement qualification has been performed.

### Open verification items

- Confirm orderable part number, hardware revision, lifecycle and region.
- Confirm installed Jetson variant, RAM, storage, power and thermal configuration.
- Confirm camera/network I/O and robotics middleware support for the exact configuration.
- Reconcile supported algorithms only after deployment and reproducible testing.

## PAI-SG compatibility status

Algorithm rows in the batch compatibility file are **candidates**, not verified support. Graph relations remain provisional pending PAI-SG S03 mapping.

## Public / private boundary

This public card excludes private architecture, BOM, commercial terms and unpublished validation evidence.
