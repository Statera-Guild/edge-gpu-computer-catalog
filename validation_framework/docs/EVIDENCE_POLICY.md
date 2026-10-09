# Manufacturer claim and compatibility evidence policy

A `source_document` record must have source ID, manufacturer-owned URL, accessed date, document type and scope. For PDF sources also preserve published revision/date where available. Do not redistribute copyrighted datasheets by default; link to the official page.

A `claim` record binds component ID, field, exact asserted value, source ID, option/variant, test conditions, assessment (`vendor_claim`/`unknown` etc.), and optional limitations. `listed` only means product identified. Promote to `documented` only after a reviewer checks individual key claims against primary docs.

Algorithm assertions must not be inferred from CUDA, JetPack, a GPU model or promotional TOPS alone. Candidate workloads are not executions. `reproduced` needs a test record, reproducible recipe, environment, model checksum, dataset split, latency throughput measurements and log/evidence digest. Public records should link to allowed evidence rather than contain restricted logs.

`USES_MODULE`, `HAS_GPU`, `HAS_INTERFACE`, `RUNS_SOFTWARE`, `SUPPORTS_ALGORITHM`, `SUPPORTED_BY_SOURCE` are provisional, unapproved predicate strings pending the PASG S03 authority review. Use `predicate_status: proposed`.
