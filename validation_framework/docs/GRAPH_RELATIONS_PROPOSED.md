# Proposed cross-repository knowledge graph relations — NOT RATIFIED

`EdgeGPUComputer -> USES_MODULE -> EdgeAIModule` (e.g. CMP-EGC-0001 to CMP-EAM-0003, provisional family-resolution link)

`EdgeGPUComputer -> HAS_GPU -> GPU`

`EdgeGPUComputer -> HAS_INTERFACE -> Interface`

`EdgeGPUComputer -> RUNS_SOFTWARE -> SoftwareRelease`

`EdgeGPUComputer -> SUPPORTS_ALGORITHM -> Algorithm` **only with CompatibilityAssertion and supporting source/test**

`CompatibilityAssertion -> SUPPORTED_BY_SOURCE -> SourceDocument`

IDs of uncreated GPU, interface, software or algorithm nodes are **not invented**. Reconcile relation names, cardinality, provenance and graph node namespace with PAI-SG S03 prior to publication of normative edge data.
