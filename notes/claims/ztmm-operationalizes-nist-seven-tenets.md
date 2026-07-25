---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-governance
  - topic/zt-definition
  - topic/zt-identity
  - topic/zt-architecture
claim_id: "cisa-ztmm-ov.9"
statement: "The ZTMM operationalizes all seven NIST 800-207 tenets into measurable capabilities"
confidence: "high"
confidence_rationale: "HIGH. The tenets are directly quoted and the ZTMM structure demonstrably covers them. What the ZTMM adds is NOT the tenets themselves but the"
claim_type: "governance"
source_note: "[[CISA ZTMM — Overview and Framework]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-ov.9: The ZTMM operationalizes all seven NIST 800-207 tenets into measurable capabilities

**Source:** [[CISA ZTMM — Overview and Framework]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

"This model reflects the seven tenets of zero trust as outlined in NIST SP 800-207." The document reproduces all seven tenets verbatim and maps the maturity model structure to them.

## Evidence

The seven tenets are listed explicitly (lines 257-267):

1. All data sources and computing services are considered resources.
2. All communication is secured regardless of network location.
3. Access to individual enterprise resources is granted on a per-session basis.
4. Access to resources is determined by dynamic policy.
5. The enterprise monitors and measures the integrity and security posture of all owned and associated assets.
6. All resource authentication and authorization are dynamic and strictly enforced before access is allowed.
7. The enterprise collects as much information as possible about the current state of assets, network infrastructure, and communications and uses it to improve its security posture.

The mapping is implicit (the document doesn't provide a tenet-to-pillar matrix), but the alignment is clear: Tenet 1 → Data pillar; Tenet 2 → Networks pillar; Tenet 3 → Identity + Applications pillars; Tenet 4 → all pillars via cross-cutting capabilities; Tenet 5 → Devices pillar; Tenet 6 → Identity pillar; Tenet 7 → Visibility and Analytics cross-cutting capability.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The tenets are directly quoted and the ZTMM structure demonstrably covers them. What the ZTMM adds is NOT the tenets themselves but the operationalization: NIST says "access is determined by dynamic policy" (aspirational); the ZTMM says "at Advanced level, policy is automated with cross-pillar coordination; at Optimal, policy is fully dynamic based on automated triggers" (measurable).

## Stakes

If the ZTMM fails to cover a tenet, there's a gap in the federal ZTA assessment framework. If it covers all tenets but some are weaker than others, agencies will under-invest in those areas. The implicit mapping (no explicit tenet-to-function traceability) creates audit risk — an agency could claim compliance without demonstrating tenet coverage.

## Disagreement

**Who disagrees:**

No one disagrees that the seven tenets are the right foundation. The debate is over whether a maturity model is the right way to assess compliance with them. NSA prefers a threat-model-driven assessment ("does your architecture stop this attack pattern?"), while CISA prefers a capability-driven assessment ("do you have phishing-resistant MFA?"). Both approaches can cover the same tenets.

**Alternative reading:**

The ZTMM's claim to reflect all seven tenets could be read as aspirational — it covers them at the framework level, but the specific function tables may not fully address every tenet. For example, Tenet 3 (per-session access) is partially covered by Identity's Access Management function, but per-session access to individual resources (as opposed to per-session authentication) isn't a distinct function in any pillar.

## Edges

**Depends on:**

**Supports:**
  - "[[ztmm-nist-800-207-definition-foundation]]"

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The ZTMM successfully operationalizes the tenets, but the mapping is imperfect. The framework would benefit from an explicit tenet-to-function traceability matrix, which would make gaps visible and closeable. In its absence, agencies should perform this mapping themselves as part of their ZTA planning. The implicit coverage is good enough for assessment purposes but not rigorous enough for auditing.
