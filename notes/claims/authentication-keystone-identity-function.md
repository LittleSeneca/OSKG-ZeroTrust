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
- [[access-mgmt-abac-least-privilege|Access management decisions in C9 require authentication to establish subject identity first; C7's authentication keysto]]

**Supports:**
- [[ztmm-operationalizes-nist-seven-tenets|C7 describes the authentication maturity progression (Traditional→Optimal) within ZTMM, providing a concrete example of]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[continuous-authentication-common-all-pillars|C6 broadly asserts continuous auth is common to all pillars; C7 identifies authentication as the keystone function with]]
- [[icam-non-negotiable-substrate|C7 names authentication as the keystone within the ICAM/FICAM framework C3 establishes as substrate, identifying the hig]]
- [[identity-foundational-zta-pillar|C1 claims identity is foundational; C7 identifies authentication as the keystone function within the identity pillar, ad]]

## Assessment

_Not addressed separately in the source note._
