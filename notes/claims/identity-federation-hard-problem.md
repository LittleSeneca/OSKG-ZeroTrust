---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-user-pillar
  - topic/zt-identity
  - topic/zt-federation
  - topic/zt-governance
  - topic/zt-device
claim_id: "nsa-user.5"
statement: "Identity federation is the hard problem — maturity amplifies complexity, not reduces it"
confidence: "medium"
confidence_rationale: "MEDIUM. The admission that federation is complicated and ZT doesn't simplify it is honest, but the document is thin on *how* to address these"
claim_type: "implementation"
source_note: "[[NSA — User Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-user.5: Identity federation is the hard problem — maturity amplifies complexity, not reduces it

**Source:** [[NSA — User Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the User Pillar*, 2023

## The Claim

"Federation between partner organizations is complicated, and will depend on the partner agreements, the capabilities and maturity of each partner's system, and the assessed risk associated with each system." ZT does not remove requirements for cross-domain solutions.

## Evidence

Unlike the other three ICAM sub-capabilities, the NSA does not provide detailed maturity phases for federation. Instead, it identifies the persistent challenges:

- Partners have varying ICAM maturity levels and distinct implementations that "complicate sharing."
- FICAM requirements for federation apply at all maturity levels: confidence in partner identity/credential management, mapping authentication assertions from multiple sources, aligning attributes, reconciling access policy differences.
- At higher maturity, federation requirements intensify: sharing risk-based attributes, access to back-end credential and inventory repositories, detailed system access logs.
- "Zero Trust mechanisms do not remove requirements for cross-domain solutions, especially when information sensitivity differences create excessive risk or when maturity levels vary widely."

**Implementation guidance for federation:**

1. Inventory partner identities (PEs and NPEs) your systems need to support.
2. Map partner identity and credential assurance levels; map partner-issued attributes to local equivalents.
3. Map access policy differences and establish mitigating controls for interoperability gaps.
4. Negotiate formatting, equivalency, and interface specifications at the IT security leadership level.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. The admission that federation is complicated and ZT doesn't simplify it is honest, but the document is thin on *how* to address these challenges. This is a known hard problem — NISTIR 8149 (Developing Trust Frameworks to Support Identity Federations) is an entire publication on it.

## Stakes

Federation is where most ZT implementations hit the wall. Internal ICAM maturity can be achieved through organizational authority (mandate CAC/PIV, enforce MFA, deploy PAM). External federation requires *negotiation* with partners who have different risk tolerances, different technology stacks, and different timelines. The DoD's mission partner environment is the canonical hard case: sharing classified information with coalition partners whose ICAM maturity may be at the Preparation phase.

## Disagreement

**Who disagrees:**

This is not a disagreement but a gap. NIST's work on trust frameworks (NISTIR 8149, NIST SP 800-63-C) provides more detailed guidance. The DoD ZT Reference Architecture addresses federation as a core capability with more specificity (attribute-based access control across security domains via the ABAC model). CISA's ZTMM touches on federation indirectly through the "identity stores" function at Optimal ("securely integrated across all partners and environments").

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
  - "[[identity-stores-integrated-not-just-federated]]"

## Assessment

The document's honesty about federation complexity is more valuable than a superficial maturity model would be. The four-step implementation guidance is practical if high-level. The key insight is that ZT doesn't magically solve the cross-domain problem — it raises the bar for internal security, which makes the federation boundary the new weak point. Mitigating controls for partner maturity gaps should be an explicit part of any federation agreement.
