---
tags:
  - source/standards
  - nsa
  - zt-user
  - zt-identity
  - icam
  - ficam
  - mfa
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
claims_status: extracted
claims_extracted: 2026-07-24
confidence: high
source:
  title: "Advancing Zero Trust Maturity Throughout the User Pillar"
  authors: "National Security Agency"
  year: 2023
  version: "v1.1, April 2023"
  publisher: "NSA"
  report_id: "U/OO/127344-23 | PP-23-0208"
  local_file: "sources/standards/_txt/NSA_ZT_User_Pillar.txt"
related:
  - "[[NSA — Embracing a Zero Trust Security Model]]"
  - "[[CISA ZTMM — Identity Pillar]]"
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[NIST 800-207 — Ch6 — Federal Guidance]]"
  - "[[Concepts Index]]"
---

# NSA — User Pillar: Advancing Zero Trust Maturity

The NSA's pillar-specific guidance for the user/identity pillar. Published April 2023 (v1.1), it is the most operationally detailed document in the NSA Zero Trust series. 22 pages. It builds on the FICAM (Federal Identity, Credential, and Access Management) architecture and defines maturity phases across four ICAM sub-capabilities: Identity Management, Credential Management, Access Management, and Identity Federation. The guidance is tailored for National Security System (NSS) owners and operators but broadly applicable to any organization defending against sophisticated adversaries.

**Claim 1 —** The user pillar operationalizes ICAM for Zero Trust — and ICAM is the non-negotiable substrate → [[icam-non-negotiable-substrate]]
---

**Claim 2 —** Identity management maturity is about attribute authority, not just identity inventory → [[identity-mgmt-attribute-authority]]
---

**Claim 3 —** Credential management is defined by phishing resistance — MFA is the floor, AAL3 is the ceiling → [[credential-mgmt-phishing-resistance]]
---

**Claim 4 —** Access management is where least privilege becomes operational — through ABAC, JIT/JEA, PAM, and privileged access workstations → [[access-mgmt-abac-least-privilege]]
---

**Claim 5 —** Identity federation is the hard problem — maturity amplifies complexity, not reduces it → [[identity-federation-hard-problem]]
---

**Claim 6 —** The NSA and CISA identity frameworks are complementary — NSA provides the "how" for the defense context, CISA provides the "what to measure" → [[nsa-cisa-identity-frameworks-complementary]]
---

## Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| ICAM as ZT substrate | HIGH | Overestimating commercial orgs' existing ICAM maturity |
| Identity management as attribute authority | HIGH | NPE attribute management remains immature industry-wide |
| Credential management = phishing resistance + lifecycle | HIGH | Cryptographic agility hasn't been tested at scale in most orgs |
| Access management = operationalized least privilege | HIGH | ABAC implementation complexity may stall at Intermediate |
| Federation is the hard problem | MEDIUM | Thin guidance; implementation depends on partner negotiations |
| NSA + CISA complementarity | HIGH | Risk of orgs choosing one framework and missing the other's strengths |

**Strongest sections:** Credential Management (MFA, phishing resistance, NPE authenticators) and Access Management (least privilege, JIT/JEA, PAM, privileged workstations, ABAC). These provide the most immediately actionable operational guidance.

**Weakest section:** Identity Federation. The document acknowledges the complexity honestly but provides minimal "how to" beyond high-level steps. This reflects the genuine difficulty of the problem more than a failure of the document — but anyone implementing federation will need NISTIR 8149 and the DoD ZT RA for deeper guidance.

**Historical significance:** This document, published alongside CISA's ZTMM v2, completes the federal identity maturity picture for Zero Trust. CISA defines the maturity targets for FCEB agencies; NSA defines the implementation roadmap for defense environments. Together they operationalize the ICAM requirements that NIST 800-207 and EO 14028 established. For the OSKG-ZeroTrust project, this document and the CISA Identity Pillar note form a linked pair — read both for a complete picture of federal identity maturity in a ZT context.

---

## Cross-References

- **[[CISA ZTMM — Identity Pillar]]** — The complementary maturity model for FCEB agencies. Includes detailed cross-walk between NSA and CISA frameworks.
- **[[NSA — Embracing a Zero Trust Security Model]]** — The foundational NSA ZT document that this pillar guidance extends.
- **[[NIST 800-207 — Ch2 — Zero Trust Basics]]** — The seven tenets and the definition that both NSA and CISA build on.
- **[[NIST 800-207 — Ch6 — Federal Guidance]]** — Sections 6.3 (FICAM), 6.4 (Trust Frameworks), and 6.6 (CDM) provide the architectural context for ICAM as a ZTA dependency.
- **[[NIST SP 800-63-3 — Digital Identity Guidelines]]** — The AAL framework that defines MFA strength (future note).
- **[[FICAM Architecture]]** — The GSA architecture that the NSA User Pillar builds on (future note).
