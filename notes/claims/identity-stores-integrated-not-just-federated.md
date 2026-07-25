---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-identity
  - topic/zt-implementation
  - topic/zt-governance
  - topic/zt-cloud
  - topic/zt-federation
claim_id: "cisa-ztmm-id.4"
statement: "Identity stores must be integrated across environments, not just federated — the maturity progression from siloed on-premises to securely integrated across all partners and environments is a significant architectural undertaking, not achievable through SSO alone."
confidence: "high"
confidence_rationale: "HIGH. The integration requirement is explicit, but the operational difficulty is understated."
claim_type: "implementation"
source_note: "[[CISA ZTMM — Identity Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-id.4: Identity stores must be integrated across environments, not just federated — the maturity progression from siloed on-premises to securely integrated across all partners and environments is a significant architectural undertaking, not achievable through SSO alone.

**Source:** [[CISA ZTMM — Identity Pillar]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

Identity store maturity moves from *siloed, on-premises* to *securely integrated across all partners and environments*. (§5.1 — Identity Stores)

## Evidence

| Stage | Capability |
|-------|-----------|
| **Traditional** | Self-managed, on-premises identity stores only. |
| **Initial** | Mix of self-managed and hosted (cloud/other agency) identity stores; minimal integration (e.g., basic SSO). |
| **Advanced** | Secure consolidation and integration of some self-managed and hosted identity stores. |
| **Optimal** | Identity stores securely integrated across all partners and environments, as appropriate. |

**NSA cross-reference:**

Maps to NSA's *Identity Management* capability. Key difference: CISA emphasizes *where* the stores live and *how well they're integrated* (architectural); NSA emphasizes *what attributes are in them* and *how authoritative they are* (governance). Both converge at the optimal/advanced level — integrated, attribute-rich, risk-informed.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The integration requirement is explicit, but the operational difficulty is understated.

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
- [[identity-federation-hard-problem|Extends beyond federation to secure integration — the architectural undertaking that federation alone cannot achieve.]]

## Assessment

_Not addressed separately in the source note._
