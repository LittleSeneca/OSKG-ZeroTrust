---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-user-pillar
  - topic/zt-identity
  - topic/zt-governance
claim_id: "nsa-user.6"
statement: 'The NSA and CISA identity frameworks are complementary — NSA provides the "how" for the defense context, CISA provides the "what to measure"'
confidence: "high"
confidence_rationale: "HIGH. The complementarity is well-established. The CISA ZTMM Identity Pillar note already cross-references extensively with the NSA User Pillar. NIST"
claim_type: "governance"
source_note: "[[NSA — User Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-user.6: The NSA and CISA identity frameworks are complementary — NSA provides the "how" for the defense context, CISA provides the "what to measure"

**Source:** [[NSA — User Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the User Pillar*, 2023

## The Claim

The user pillar maturity model is designed for NSS environments where attributes like clearance, classification, and community-of-interest are first-class access decision inputs, and where adversaries are nation-state actors. This distinguishes it from CISA's FCEB-focused maturity model.

## Evidence

The structural differences between the two frameworks:

| Dimension | NSA User Pillar | CISA ZTMM Identity Pillar |
|-----------|----------------|--------------------------|
| **Structure** | 4 ICAM sub-capabilities (Identity Mgmt, Credential Mgmt, Access Mgmt, Federation) | 4 functions (Authentication, Identity Stores, Risk Assessments, Access Management) + 3 cross-cutting capabilities |
| **Maturity labels** | Preparation → Basic → Intermediate → Advanced | Traditional → Initial → Advanced → Optimal |
| **Primary audience** | NSS owners/operators, DoD, DIB | FCEB agencies; general applicability |
| **Distinctive emphasis** | NPEs, clearance/releasability attributes, cryptographic agility, cross-domain solutions, PAM as attack surface | UEBA, automation/orchestration, governance as first-class function, identity store integration architecture |
| **Auth target** | Phishing-resistant MFA (AAL3): CAC/PIV, FIDO2 hardware tokens | Phishing-resistant MFA (Advanced level); password-less at Optimal |
| **Access control** | ABAC with NSS-specific attributes (clearance, classification, releasability, citizenship, COI) | ABAC implied; JIT/JEA at Optimal |

But they converge at the destination: both want phishing-resistant MFA, continuous validation, attribute-based access decisions, risk-informed policies, and JIT/JEA for privileged access.

**The NSA's added value for defense environments:**

- **NPE guidance** (service accounts, machine identities, API keys) at a level of detail CISA doesn't match. In classified environments, a compromised NPE credential can be as catastrophic as a compromised user credential.
- **Cryptographic agility** as a distinct concern — the ability to revoke and replace credentials at scale when a cryptographic method becomes obsolete. This is a defense-specific concern driven by CNSSP 15 and NSM-10 compliance timelines.
- **PAM as an attack surface** — the explicit warning that PAM implementations must be "tightly controlled and monitored" because they control the privileged functions that shape the environment. This operational paranoia is distinctively NSA.
- **Cross-domain solutions** — the acknowledgment that ZT doesn't eliminate the need for CDS when sharing across security domains with different sensitivity levels.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The complementarity is well-established. The CISA ZTMM Identity Pillar note already cross-references extensively with the NSA User Pillar. NIST 800-207 Ch 6 references both.

## Stakes

Organizations that use only one framework will have gaps. CISA alone underinvests in NPE credentials and cryptographic agility. NSA alone underinvests in governance as a first-class function and risk assessments as a distinct capability track. Together they're complete.

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
  - "[[cisa-nsa-identity-complementary]]"

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

This is one of the most productive cross-references in the entire OSKG-ZeroTrust graph. The frameworks don't conflict — they address different audiences with different threat models and different operational constraints. The fact that both were published in 2023 (CISA v2 in April, NSA v1.1 in April) and align without contradiction suggests coordination, not competition. For any organization doing both defense and civilian work (common in the DIB), both frameworks should be referenced.
