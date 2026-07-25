---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-user-pillar
  - topic/zt-identity
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-authentication
  - topic/zt-federation
claim_id: "nsa-user.1"
statement: "The user pillar operationalizes ICAM for Zero Trust — and ICAM is the non-negotiable substrate"
confidence: "high"
confidence_rationale: 'HIGH. This claim is consistent with NIST 800-207 Chapter 6.3 (which states that FICAM is a "critical dependency" for ZTA) and with OMB M-22-09 (which'
claim_type: "definitional"
source_note: "[[NSA — User Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-user.1: The user pillar operationalizes ICAM for Zero Trust — and ICAM is the non-negotiable substrate

**Source:** [[NSA — User Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the User Pillar*, 2023

## The Claim

The user pillar "expands and refines the capabilities associated with the FICAM framework to address the enhanced threat to identity, credentials, and access management." Without mature ICAM, ZTA cannot function.

## Evidence

The document frames the entire user pillar around five FICAM capability areas: Identity Management, Credential Management, Access Management, Federation, and Governance. This is not an arbitrary structure — it mirrors the Federal ICAM Architecture directly (GSA, 2021). The NSA's contribution is adding the *threat-centric maturity model* on top: preparation → basic → intermediate → advanced for each capability.

The stakes are established through two canonical breach examples:

1. **OPM 2015 breach:** Leveraged compromised credentials. MFA was available but not fully deployed. 21.5 million personnel records exfiltrated.
2. **Colonial Pipeline 2021 ransomware:** Exploited a legacy VPN without MFA. Attackers gained access via a compromised complex password. Economic disruption across the US Southeast.

Both incidents exploited *immature ICAM capabilities* — exactly the gaps the user pillar maturity model is designed to close.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This claim is consistent with NIST 800-207 Chapter 6.3 (which states that FICAM is a "critical dependency" for ZTA) and with OMB M-22-09 (which requires agencies to adopt phishing-resistant MFA and consolidate identity systems). The NSA, NIST, CISA, and OMB are all aligned: mature ICAM is prerequisite to ZTA.

## Stakes

If ICAM is the non-negotiable substrate, identity maturity drives the ZTA implementation roadmap. You cannot skip identity and start with network microsegmentation — access decisions depend on authenticated identity. The user pillar is the logical starting point for any ZT adoption program.

## Disagreement

**Who disagrees:**

Nobody credible. The debate is about *how* to mature ICAM (phishing-resistant MFA mandate timing, centralized vs. federated identity stores, PIV vs. FIDO2) not *whether* it's required. Even vendor-driven ZTNA implementations depend on identity integration.

**Alternative reading:**

The ICAM-first framing could be read as NSA's institutional preference — defense and intelligence agencies already have strong ICAM programs (CAC/PIV, PKI, clearance-based attributes). For commercial organizations without this infrastructure, the "start with identity" prescription may be more aspirational and take longer. But even in that case, the direction of travel is the same.

## Edges

**Depends on:**

**Supports:**
- [[ztmm-operationalizes-nist-seven-tenets|ICAM as the non-negotiable substrate provides the identity infrastructure that the ZTMM operationalizes into measurable]]
- [[user-identity-and-device-identity-are-separate-trust|ICAM as the non-negotiable substrate must accommodate separate trust domains for users and devices with independent auth]]
- [[identity-foundational-zta-pillar|Both establish ICAM as the non-negotiable substrate for ZTA identity — CISA's maturity model explicitly names ICAM as th]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[identity-foundational-zta-pillar|C1 asserts ICAM serves as substrate beneath the identity pillar; C3 specifies how the user pillar operationalizes ICAM t]]
- [[true-contextual-identity-is-never-just-a-device|The ICAM substrate is operationalized through multi-dimensional contextual profiling that captures who, what device, and]]

## Assessment

The user pillar is the most foundational of the seven NSA pillars because identity is the *axis of access decisions*. Without it, nothing else in ZT works. The document's decision to lead with the user pillar is correct, and the ICAM framing gives it an architecture it can mature against. The CISA ZTMM Identity pillar ([CISA ZTMM — Identity Pillar]) covers the same territory with a slightly different taxonomy (Authentication, Identity Stores, Risk Assessments, Access Management as separate functions rather than ICAM sub-capabilities), but both converge on the same destination.
