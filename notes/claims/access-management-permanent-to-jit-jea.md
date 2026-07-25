---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-identity
  - topic/zt-access-mgmt
claim_id: "cisa-ztmm-id.6"
statement: "Access management operationalizes least privilege through the progression from permanent access → expiring access → need-based/session-based → automated JIT/JEA, with NSA providing the tactical implementation layer (PAM tools, privileged access workstations, ABAC, risk-adaptive policies)."
confidence: "high"
confidence_rationale: "HIGH. The JIT/JEA progression is well-defined and broadly agreed across frameworks."
claim_type: "implementation"
source_note: "[[CISA ZTMM — Identity Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-id.6: Access management operationalizes least privilege through the progression from permanent access → expiring access → need-based/session-based → automated JIT/JEA, with NSA providing the tactical implementation layer (PAM tools, privileged access workstations, ABAC, risk-adaptive policies).

**Source:** [[CISA ZTMM — Identity Pillar]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

Access management maturity moves from *permanent, periodically-reviewed* to *just-in-time, just-enough, automated*. (§5.1 — Access Management)

## Evidence

| Stage | Capability |
|-------|-----------|
| **Traditional** | Permanent access with periodic manual review (privileged and unprivileged). |
| **Initial** | Access that expires; automated review; includes privileged access requests. |
| **Advanced** | Need-based and session-based access; tailored to specific actions and resources; includes privileged access. |
| **Optimal** | Automated just-in-time (JIT) and just-enough access (JEA); tailored to individual actions and individual resource needs. |

**NSA cross-reference:**

NSA's *Access Management* capability maps closely and provides much more tactical detail: PAM tools, privileged access workstations, ABAC models, fine-grained risk-adaptive access policies. CISA provides the maturity *targets*; NSA provides the *how-to* for defense environments.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The JIT/JEA progression is well-defined and broadly agreed across frameworks.

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
