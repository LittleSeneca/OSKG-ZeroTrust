---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-identity
  - topic/zt-authentication
  - topic/zt-governance
  - topic/zt-device
claim_id: "dod-ra-cap.2"
statement: "Continuous authentication and identity validation are common to all pillars — every access transaction requires it regardless of what pillar the capability falls under — and three enterprise-scale enablers (federated enterprise identity service, enterprise analytics, enterprise orchestration) are prerequisites, not optional."
confidence: "high"
confidence_rationale: "HIGH. These are direct assertions from the capability taxonomy section."
claim_type: "implementation"
source_note: "[[DoD ZT Reference Architecture — Capabilities and Use Cases]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-cap.2: Continuous authentication and identity validation are common to all pillars — every access transaction requires it regardless of what pillar the capability falls under — and three enterprise-scale enablers (federated enterprise identity service, enterprise analytics, enterprise orchestration) are prerequisites, not optional.

**Source:** [[DoD ZT Reference Architecture — Capabilities and Use Cases]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

Key dynamics within the capability taxonomy. (§3.1)

## Evidence

- Continuous authentication and identity validation are common to all pillars — every access transaction requires it.
- Capabilities point to multiple pillars — white arrows in Figure 6 show which aggregated capability acts on which pillar.
- Enterprise-scale enablers are required: a federated enterprise identity service, enterprise analytics, and enterprise orchestration are prerequisites.
- Data discovery and labeling must precede implementation — proper attributes and data labeling during the discovery process are prerequisites for a ZT architecture to function.

**Cross-reference — CISA ZTMM:**

CISA's maturity model organizes capabilities differently — by *maturity stage* within each pillar rather than as a taxonomy. Where DoD provides the capability inventory (what must exist), CISA provides the maturity progression (how advanced each capability should be). See [[CISA ZTMM — Identity Pillar]] and [[CISA ZTMM — Device Network App Data Pillars]].

**Cross-reference — NIST 800-207 Ch3:**

NIST's logical component model (PE, PA, PEP) is the abstract architectural pattern. DoD's capability taxonomy is the concrete instantiation — it specifies *which* capabilities populate the control plane and data plane. DoD's "Analytics & Confidence Scoring" capability maps to NIST's trust algorithm; DoD's "Automation & Orchestration" maps to NIST's Policy Administrator function. See [[NIST 800-207 — Ch3 — Logical Components]].

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These are direct assertions from the capability taxonomy section.

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
- [[authentication-keystone-identity-function|Extends the authentication keystone from an identity-pillar function to a cross-cutting requirement common to all ZT pil]]

## Assessment

_Not addressed separately in the source note._
