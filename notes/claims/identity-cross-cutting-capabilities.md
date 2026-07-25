---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-identity
  - topic/zt-governance
  - topic/zt-policy
  - topic/zt-monitoring
claim_id: "cisa-ztmm-id.7"
statement: "Three cross-cutting capabilities — Visibility & Analytics, Automation & Orchestration, and Governance — operate within the Identity pillar and become increasingly automated and integrated across environments as maturity increases."
confidence: "high"
confidence_rationale: "HIGH. These are direct from the source document."
claim_type: "architectural"
source_note: "[[CISA ZTMM — Identity Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-id.7: Three cross-cutting capabilities — Visibility & Analytics, Automation & Orchestration, and Governance — operate within the Identity pillar and become increasingly automated and integrated across environments as maturity increases.

**Source:** [[CISA ZTMM — Identity Pillar]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

CISA defines three capabilities that span all pillars. Their maturity progression within Identity mirrors the broader pillar trajectory. (§5.1 — Cross-Cutting Capabilities)

## Evidence

**Visibility and Analytics:**

| Stage | Capability |
|-------|-----------|
| **Traditional** | Collects user/entity activity logs (especially privileged); some routine manual analysis. |
| **Initial** | Routine manual + some automated analysis; limited correlation between log types. |
| **Advanced** | Automated analysis across some log types; collection augmented to address gaps. |
| **Optimal** | Comprehensive visibility and situational awareness; automated analysis including behavior-based analytics (UEBA). |

**Automation and Orchestration:**

| Stage | Capability |
|-------|-----------|
| **Traditional** | Manual orchestration of self-managed identities; limited integration; regular manual review. |
| **Initial** | Manual orchestration for privileged/external identities; automated for non-privileged users. |
| **Advanced** | Manual orchestration for privileged users; automated for all other identities with cross-environment integration. |
| **Optimal** | Fully automated orchestration of all identities across all environments; driven by behaviors, enrollments, and deployment needs. |

**Governance:**

| Stage | Capability |
|-------|-----------|
| **Traditional** | Identity policies enforced via static technical mechanisms and manual review. |
| **Initial** | Enterprise-wide identity policies defined; minimal automation; manual updates. |
| **Advanced** | Enterprise-wide identity policies with automation; periodic policy updates. |
| **Optimal** | Fully automated enterprise-wide identity policies for all users/entities across all systems; continuous enforcement with dynamic updates. |

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These are direct from the source document.

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
- [[npe-person-identities-independent-confidence|Visibility & analytics feeds the independent confidence tracking; automation & orchestration enables confidence aggregat]]
- [[the-three-layer-authorization-model-reveals-why-zt-is|Cross-cutting capabilities (visibility & analytics, automation & orchestration, governance) operationalize enforcement a]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
  - "[[cross-cutting-capabilities-convergence]]"

## Assessment

_Not addressed separately in the source note._
