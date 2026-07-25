---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-architecture
  - topic/zt-implementation
  - topic/zt-cloud
  - topic/zt-network
claim_id: "dod-ra-cap.1"
statement: "The Seven Pillars serve as the organizing taxonomy for all ZT capabilities, with seven aggregated capabilities (Continuous Authentication, Conditional Authorization, Enabling Infrastructure, Securing Application & Workload, Securing Data, Analytics, Automation & Orchestration) each nesting into sub-capabilities that extend the entire taxonomy."
confidence: "high"
confidence_rationale: "HIGH. This is the direct capability taxonomy from the DoD RA."
claim_type: "architectural"
source_note: "[[DoD ZT Reference Architecture — Capabilities and Use Cases]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-cap.1: The Seven Pillars serve as the organizing taxonomy for all ZT capabilities, with seven aggregated capabilities (Continuous Authentication, Conditional Authorization, Enabling Infrastructure, Securing Application & Workload, Securing Data, Analytics, Automation & Orchestration) each nesting into sub-capabilities that extend the entire taxonomy.

**Source:** [[DoD ZT Reference Architecture — Capabilities and Use Cases]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

Each capability is "the ability to achieve a desired effect under specified (performance) standards and conditions through combinations of ways and means (activities and resources)." The entire taxonomy is subject to change as technologies evolve. (§3.1, CV-2)

## Evidence

| Aggregate Capability | Description | Maps To |
|---|---|---|
| **Continuous Authentication** | Validating identity of entities during all access transactions, enhanced with behavioral metrics and additional identifying factors | User, Device |
| **Conditional Authorization** | Granting access contingent on continued trustworthiness — influenced by device hygiene, user/NPE behavior, and other factors | User, Device, Data |
| **Enabling Infrastructure** | Network/environment segmentation (macro and micro), Software Defined Perimeters, cloud resources | Network/Environment |
| **Securing Application & Workload** | Preventing lateral movement, validating software practices, segmenting applications, API standardization | Applications & Workload |
| **Securing Data** | Tagging, sensitive data identification, exfiltration protections, encryption at rest and in transit | Data |
| **Analytics** | Continuous entity monitoring, sensors, logging, event-driven analytics, machine learning for baselining | Visibility & Analytics |
| **Automation & Orchestration** | Automated policy deployment, ingestion of desired target state from SDE, AI/RPA augmentation (future) | Automation & Orchestration |

**Three enabling cross-cutting domains:**

1. **Data Governance** — Processes, tools, and frameworks for managing data from creation to disposition.
2. **Risk Management (RMF)** — Interdependent with ZT: ZT provides discovery content to feed RMF; RMF's prepare/assess/monitor steps adapt to DevSecOps practices.
3. **Software-Defined Enterprise (SDE)** — As compute, network, and storage are virtualized and software-defined, data and applications can be isolated at scale.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is the direct capability taxonomy from the DoD RA.

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
- [[the-nist-pdppep-model-is-the-correct-foundation|The DoD's seven-pillar capability taxonomy complements the NIST PDP/PEP model by organizing functional capabilities that]]
- [[dod-seven-ra-principles-bridge|The seven pillars taxonomy provides the functional capability domains that the seven RA principles bridge to implementat]]

## Assessment

_Not addressed separately in the source note._
