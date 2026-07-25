---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-monitoring
  - topic/zt-implementation
claim_id: "dod-ra-cap.6"
statement: "Analytics and AI (Use Cases 5–6) — ZT must unify siloed domain data through a pipeline (Sensors → SIEM → SOAR + AI → ZT Controller → ML/AI storage) to enable consistent policies, user/NPE confidence scoring, advanced threat detection, and automated threat mitigation, collecting far more data than traditional architectures to power automation."
confidence: "medium"
confidence_rationale: "MEDIUM-HIGH. The pipeline is architecturally sound but the DoD's claim that it makes siloed domains \"obsolete\" is aspirational — most organizations"
claim_type: "implementation"
source_note: "[[DoD ZT Reference Architecture — Capabilities and Use Cases]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-cap.6: Analytics and AI (Use Cases 5–6) — ZT must unify siloed domain data through a pipeline (Sensors → SIEM → SOAR + AI → ZT Controller → ML/AI storage) to enable consistent policies, user/NPE confidence scoring, advanced threat detection, and automated threat mitigation, collecting far more data than traditional architectures to power automation.

**Source:** [[DoD ZT Reference Architecture — Capabilities and Use Cases]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

Siloed domains create inconsistent policies, data, logs, and analytics. ZT makes siloed domains obsolete through unified analytics and AI. (§4.5–4.6)

## Evidence

```
Sensors → SIEM (initial processing, threat detection) → SOAR + AI (advanced analysis)
                                                            ↓
                                                     ZT Controller (automated mitigation)
                                                            ↓
                              ML/AI storage (confidence scoring, baselining, external intel)
```

**What this enables:**

- Systematic data collection identifying data types and finding correlations between datasets
- Accelerated automation of data preparation (gather → discover → assess → clean → structure → transform → enrich → publish)
- Consistent policies, data, logs, and analytics across the architecture
- User/NPE confidence scoring, advanced threat detection, and automated threat mitigation

**Scale difference:**

A ZT model collects far more data than traditional architecture — required to power automation. This demands advanced tools beyond traditional SIEM.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM-HIGH. The pipeline is architecturally sound but the DoD's claim that it makes siloed domains "obsolete" is aspirational — most organizations have significant data integration debt.

## Stakes

_Not addressed separately in the source note._

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
