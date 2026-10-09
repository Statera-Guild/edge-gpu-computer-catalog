# Neousys Wave 2 review notes

- All records are `listed`, not `documented`, verified, certified or approved.
- 0011–0013 are discrete-GPU-capable computers; a supported GPU is not necessarily shipped installed.
- 0014–0015 are Jetson integrated systems. Shared memory is not discrete VRAM.
- Nuvo-10108GC manufacturer text contains differing memory headlines (64 GB and 128 GB): **do not normalize maximum RAM until current datasheet revision and order guide are reconciled**.
- NRU-162S-AWP NX/Nano variants need exact module reference before emitting an unqualified `USES_MODULE` graph edge.
- Nuvo-8240GC generation and current orderability require vendor confirmation.
- Power input, full system wattage, software stacks, actual camera drivers, thermal performance, and benchmark conditions remain unresolved.
- S03 edge vocabulary not yet reconciled; do not ingest these records as normative graph assertions.
- Do not edit or replace the 31 files committed in Wave 1. This is an additive batch.
