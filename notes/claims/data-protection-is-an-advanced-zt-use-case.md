---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-data
  - topic/zt-maturity
claim_id: "gc-soc-data-iot.3"
statement: "Data protection is an advanced ZT use case — classification maturity and platform capabilities are prerequisites, making it unsuitable for early ZT projects."
confidence: "high"
confidence_rationale: "HIGH — Consistent with the broader ZT literature which consistently treats data as the most mature and hardest pillar. The explicit characterization"
claim_type: "maturity"
source_note: "[[Garbis and Chapman — SOC Data IoT]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-soc-data-iot.3: Data protection is an advanced ZT use case — classification maturity and platform capabilities are prerequisites, making it unsuitable for early ZT projects.

**Source:** [[Garbis and Chapman — SOC Data IoT]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

Garbis & Chapman explicitly state that "data protection is an advanced ZT use case — not ideal for early projects. Classification maturity and platform capabilities are prerequisites."

## Evidence

The chapter describes data as a resource protected by PEPs, just like applications. Two integration models are defined: (1) Enclave model — data resources sit inside a resource enclave behind a PEP, with a Data Access Governance (DAG) solution feeding labels/tags into the PDP; policies like "only Customer Care Team can access resources tagged 'Customer Records'" are enforced at the PEP. (2) Local device model — variants where DAG informs PDP → local agent PEP enforces controls based on data labels, or DLP acts as a mini-PEP consuming ZT-provided identity/session context for data residency enforcement. The authors cover FIPS Pub 199 classification levels (Low/Moderate/High), three classification methods (automated, user-based, discovery), and the full data lifecycle from creation through destruction.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — Consistent with the broader ZT literature which consistently treats data as the most mature and hardest pillar. The explicit characterization of data as "advanced" provides useful prioritization guidance.

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
