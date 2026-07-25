---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-architecture
  - topic/zt-policy
  - topic/zt-implementation
  - topic/zt-governance
claim_id: "dod-ra-cap.3"
statement: "The Fit-for-Purpose (FFP) mapping instantiates a chain of five decision points — not NIST's single PDP — extending from Authentication through Authorization, Resource, Application, to Data, with each building on the previous and independently evaluating confidence levels."
confidence: "high"
confidence_rationale: "HIGH. The five-decision-point chain is documented in the FFP mapping."
claim_type: "architectural"
source_note: "[[DoD ZT Reference Architecture — Capabilities and Use Cases]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-cap.3: The Fit-for-Purpose (FFP) mapping instantiates a chain of five decision points — not NIST's single PDP — extending from Authentication through Authorization, Resource, Application, to Data, with each building on the previous and independently evaluating confidence levels.

**Source:** [[DoD ZT Reference Architecture — Capabilities and Use Cases]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

Figure 11 (CV-7) provides an operational view of how security measures are implemented within the architecture, organized around decision points placed at key enforcement locations. (§3.2)

## Evidence

| Decision Point | What It Evaluates | Capability |
|---|---|---|
| **Authentication Decision Point** | Credential issuance, user/NPE identity, device managed/unmanaged state | Continuous Authentication, ICAM Service |
| **Authorization Decision Point** | User and device confidence levels against policy | Conditional Authorization, C2C Service |
| **Resource Authorization Decision Point** | Combined NPE + user confidence level for resource access | Securing Application Workload |
| **Application Authorization Decision Point** | Combined user + NPE for application-specific access | Securing Application Workload, Securing Supply Chain |
| **Data Authorization Decision Point** | Data tagging, classification, owner-defined policies | Securing Data, Data Discovery & Classification, Dynamic Data Masking |

**Cross-reference — NIST 800-207:**

The DoD's multi-decision-point architecture extends NIST's single PDP/PEP model. NIST defines one Policy Decision Point; the DoD instantiates a chain of *five* decision points, each with independent confidence evaluation. This reflects the scale and classification requirements unique to defense environments.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The five-decision-point chain is documented in the FFP mapping.

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
