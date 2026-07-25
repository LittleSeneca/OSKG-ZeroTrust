---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-data
  - topic/zt-access-mgmt
claim_id: "dod-ra-cap.5"
statement: "Data-Centric Security (Use Cases 1–4) — data protection must shift from network-centric RBAC to attribute-based ABAC with four coordinating protection mechanisms (Data Tagging, DRM, DLP, DDM) operating around the Data Store, and encryption decisions made by the ZT policy engine rather than as a separate concern."
confidence: "high"
confidence_rationale: "HIGH. The data-centric security model is well-specified with defined mechanisms and flows."
claim_type: "implementation"
source_note: "[[DoD ZT Reference Architecture — Capabilities and Use Cases]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-cap.5: Data-Centric Security (Use Cases 1–4) — data protection must shift from network-centric RBAC to attribute-based ABAC with four coordinating protection mechanisms (Data Tagging, DRM, DLP, DDM) operating around the Data Store, and encryption decisions made by the ZT policy engine rather than as a separate concern.

**Source:** [[DoD ZT Reference Architecture — Capabilities and Use Cases]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

Data is protected by network-centric policies — username/password, device-based access, encryption only at rest, and static RBAC rarely updated or validated. The ZT solution is a unified framework with data-centric policies coordinated through continuous assessment. (§4.1–4.4)

## Evidence

**Four protection mechanisms:**

| Mechanism | Function |
|---|---|
| **Data Tagging** | On creation/import, categorize data with attributes for PII/sensitivity classification; feeds DRM and DLP |
| **DRM (Data Rights Management)** | Allow/block access, editing, or copying of data based on tags and policy |
| **DLP (Data Loss Prevention)** | Block access and transmission of data; monitor for exfiltration |
| **DDM (Dynamic Data Masking)** | Mask and alter data while being accessed/transmitted — column-level security at query time |

**RBAC → ABAC evolution:**

Data tagging enables Attribute-Based Access Control (ABAC), which creates dynamic policies based on attributes rather than static roles. RBAC answers "what role are you?" ABAC answers "what are the attributes of this access request?" — and can change in real time.

**Encryption integration (4.3):**

Encryption and access control are not separate concerns. The decision to decrypt is itself a policy decision made by the ZT policy engine. The flow: request → PEPs → check policy → if allowed, decrypt; simultaneously, SIEM analyzes the request and can trigger SOAR to terminate sessions and re-encrypt data.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The data-centric security model is well-specified with defined mechanisms and flows.

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
