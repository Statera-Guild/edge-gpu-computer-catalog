# CMP-EGC-0036 — Advantech MIC-743-AT

## Public record

- **Manufacturer:** Advantech
- **Product / family:** MIC-743-AT
- **Catalog category:** Edge GPU Computer (EGC); integrated system
- **Public status:** `listed`
- **Record scope:** `family`; exact orderable SKU not confirmed
- **Platform:** NVIDIA Jetson Thor T5000 / T4000 (manufacturer-described family; verify variant)
- **Wave:** 7 (0036–0040)

## Manufacturer evidence

- **Source ID:** `SRC-EGC-0036-01`
- **Source type:** `manufacturer_product_page`
- **Official manufacturer URL:** https://www.advantech.com/emt/products/f8c8792f-5837-421d-b268-f40a8fc1e484/mic-743-at/mod_c29865e3-0dd2-4468-8fb8-2ae10add3355
- **Evidence scope:** Product identity and platform family. Detailed specifications must be checked against a dated datasheet and exact SKU.

## Technical interpretation and review

Jetson Thor edge inference system; T5000 and T4000 variants require SKU confirmation. No independent PAI-SG test, power measurement, latency benchmark, software compatibility, safety certification or procurement qualification has been performed.

### Open verification items

- Confirm orderable part number, hardware revision, lifecycle and region.
- Confirm installed Jetson variant, RAM, storage, power and thermal configuration.
- Confirm camera/network I/O and robotics middleware support for the exact configuration.
- Reconcile supported algorithms only after deployment and reproducible testing.

## PAI-SG compatibility status

Algorithm rows in the batch compatibility file are **candidates**, not verified support. Graph relations remain provisional pending PAI-SG S03 mapping.

## Public / private boundary

This public card excludes private architecture, BOM, commercial terms and unpublished validation evidence.
