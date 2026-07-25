---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-data
  - topic/zt-implementation
  - topic/zt-governance
  - topic/zt-device
claim_id: "gc-soc-data-iot.4"
statement: "Data classification spans a structured-to-unstructured continuum — structured data (databases) has implicit classification via schema, while unstructured data (documents, SaaS) lacks inherent metadata, making automatic classification the hardest problem."
confidence: "high"
confidence_rationale: "HIGH — The structured/unstructured distinction is a standard data management concept. The mapping of protection technologies to lifecycle phases is"
claim_type: "implementation"
source_note: "[[Garbis and Chapman — SOC Data IoT]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-soc-data-iot.4: Data classification spans a structured-to-unstructured continuum — structured data (databases) has implicit classification via schema, while unstructured data (documents, SaaS) lacks inherent metadata, making automatic classification the hardest problem.

**Source:** [[Garbis and Chapman — SOC Data IoT]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

The authors organize data protection around the structured ↔ unstructured continuum, noting that structured data benefits from column metadata for implicit classification while unstructured data lacks inherent schemas.

## Evidence

Specific technologies are mapped to phases: DLP (Data Loss Prevention) for device/content control and enforced encryption; DAG (Data Access Governance) for defining who can access what and when; DRM (Digital Rights Management) for owner-imposed controls on proprietary data. Data-at-rest is protected by full-disk or database table encryption; data-in-motion by encrypted transport (HTTPS, TLS — "simplest to secure, apply to all data"); data-in-use is the hardest phase requiring in-memory encryption, tokenization, obfuscation, CASBs, and developer toolkits. Emerging technologies include homomorphic cryptography and data tokenization.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The structured/unstructured distinction is a standard data management concept. The mapping of protection technologies to lifecycle phases is well-established.

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
- [[data-categorization-automated-labeling|The CISA ZTMM claim describes the maturity progression of data categorization; the GC SOC claim adds depth by explaining]]

## Assessment

_Not addressed separately in the source note._
