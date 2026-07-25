---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-identity
  - topic/zt-authentication
  - topic/zt-governance
  - topic/zt-access-mgmt
claim_id: "cisa-ztmm-id.3"
statement: "Authentication is the keystone function of the Identity pillar — the jump from Traditional (passwords) to Advanced/Optimal (phishing-resistant MFA + continuous validation) is the largest single capability gap and the one most directly tied to breach prevention."
confidence: "high"
confidence_rationale: "HIGH. CISA and NSA are fully aligned on this progression. The phishing-resistant MFA gap is well-documented in breach data."
claim_type: "implementation"
source_note: "[[CISA ZTMM — Identity Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-id.3: Authentication is the keystone function of the Identity pillar — the jump from Traditional (passwords) to Advanced/Optimal (phishing-resistant MFA + continuous validation) is the largest single capability gap and the one most directly tied to breach prevention.

**Source:** [[CISA ZTMM — Identity Pillar]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

Authentication maturity moves from *static, password-based* to *continuous, phishing-resistant validation*. (§5.1 — Authentication)

## Evidence

| Stage | Capability |
|-------|-----------|
| **Traditional** | Passwords or basic MFA; static, one-time access grant. |
| **Initial** | MFA required; validates multiple entity attributes (e.g., locale, activity); passwords may still be one factor. |
| **Advanced** | Phishing-resistant MFA deployed for all identities (FIDO2, PIV); password-less MFA implementation begins. |
| **Optimal** | Continuous identity validation with phishing-resistant MFA — not just at initial access, but throughout the session. |

**NSA cross-reference:**

The NSA User Pillar's *Credential Management* capability maps directly:
- **Preparation (NSA)** ≈ **Traditional (CISA):** Passwords or basic MFA; credentials may be locally managed.
- **Basic (NSA)** ≈ **Initial (CISA):** Enterprise-approved highly-assured authenticators per NIST SP 800-63.
- **Intermediate (NSA)** ≈ **Advanced (CISA):** Phishing-resistant MFA (CAC/PIV, FIDO2) becomes standard.
- **Advanced (NSA)** ≈ **Optimal (CISA):** Continuous validation, not point-in-time; risk-based attributes interface with credential revocation.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. CISA and NSA are fully aligned on this progression. The phishing-resistant MFA gap is well-documented in breach data.

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
