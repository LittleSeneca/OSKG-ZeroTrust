---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-policy
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-governance
  - topic/zt-sdn
claim_id: "dod-ra-cap.7"
statement: "Orchestration and Policy Management (Use Cases 7–9) — centralized orchestration through a four-layer hierarchy (Global SDE Orchestrator → Cybersecurity Domain Orchestrator → ZT Policy Controller → PEPs) resolves siloed policy conflicts, and the dynamic adaptive policy feedback loop enables ZT policy to improve over time rather than being static, evolving from out-of-band AI (human review) to in-band AI (automated within acceptable risk bounds)."
confidence: "high"
confidence_rationale: "HIGH for the architecture; MEDIUM for the AI evolution timeline. The feedback loop is well-defined but the AI evolution (out-of-band → in-band) is"
claim_type: "architectural"
source_note: "[[DoD ZT Reference Architecture — Capabilities and Use Cases]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-cap.7: Orchestration and Policy Management (Use Cases 7–9) — centralized orchestration through a four-layer hierarchy (Global SDE Orchestrator → Cybersecurity Domain Orchestrator → ZT Policy Controller → PEPs) resolves siloed policy conflicts, and the dynamic adaptive policy feedback loop enables ZT policy to improve over time rather than being static, evolving from out-of-band AI (human review) to in-band AI (automated within acceptable risk bounds).

**Source:** [[DoD ZT Reference Architecture — Capabilities and Use Cases]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

Administrators apply configuration and policy changes within their own domains with little regard to other control areas, producing non-cohesive policies. ZT requires centralized orchestration of policy creation, deployment, and continued validation. (§4.7–4.9)

## Evidence

| Layer | Component | Role |
|---|---|---|
| **Global** | SDE Global Orchestrator | Provides desired/target state of the environment |
| **Domain** | Cybersecurity Domain Orchestrator (CDO) | Compares desired state to security policies, resolves conflicts, pushes policy to controllers |
| **Controller** | ZT Policy Controller | Disseminates policy to enforcement points specific to each area of influence |
| **Enforcement** | Policy Enforcement Points (PEPs) | Execute policy at the point of access |

**The adaptive feedback loop (4.9 — most architecturally significant use case):**

```
Policy Created → Deployed to PEPs → Monitored → Analyzed → Changes Identified
                                                                    ↓
                        (future: AI generates policy for review/stopgap)
                                                                    ↓
           Changes Approved → Reapplied to PEPs → Cycle repeats
```

**Cross-reference — NIST 800-207:**

NIST's trust algorithm (Ch3) is the *calculation engine*. DoD's adaptive feedback loop is the *continuous improvement mechanism* that refines the trust algorithm over time. NIST defines the static comparison; DoD adds the dynamic refinement dimension.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH for the architecture; MEDIUM for the AI evolution timeline. The feedback loop is well-defined but the AI evolution (out-of-band → in-band) is aspirational without a timeline or decision criteria.

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
- [[top-down-business-aligned-and-bottom-up-traffic-aligned-design-approaches-are|Centralized orchestration through a four-layer hierarchy operationalizes the complementary top-down/bottom-up approach —]]
- [[the-policy-decision-matrix-mapping-source-entities-to|The four-layer orchestration hierarchy (Global SDE → CDO → Policy Controller → PEPs) distributes and enforces the policy]]

## Assessment

_Not addressed separately in the source note._
