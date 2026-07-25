---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-zt-user-pillar
  - topic/zt-identity
  - topic/zt-authentication
  - topic/zt-governance
  - topic/zt-device
claim_id: "nsa-user.3"
statement: "Credential management is defined by phishing resistance — MFA is the floor, AAL3 is the ceiling"
confidence: "high"
confidence_rationale: "HIGH. The MFA guidance is consistent with CISA's Binding Operational Directive 22-01 (which mandates phishing-resistant MFA for agency systems) and"
claim_type: "implementation"
source_note: "[[NSA — User Pillar]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nsa-user.3: Credential management is defined by phishing resistance — MFA is the floor, AAL3 is the ceiling

**Source:** [[NSA — User Pillar]] — National Security Agency, *Advancing Zero Trust Maturity Throughout the User Pillar*, 2023

## The Claim

"Compliance with EO 14028 requires MFA techniques for all users. Organizations should select strong MFA products that are validated to meet the desired AAL." But the document goes further: phishing-resistant MFA (AAL3) is the recommended target, and credential lifecycle management — especially rapid revocation — distinguishes mature implementations from basic ones.

## Evidence

**MFA and Authenticator Assurance Levels:**

The document maps authentication strength to NIST SP 800-63-3's AAL scale:
- **AAL 1**: Single-factor or weak MFA (not recommended for critical resources).
- **AAL 2**: Two-factor with cryptographic protection of the authentication secret.
- **AAL 3**: Hardware-based cryptographic authenticators with phishing resistance. CAC/PIV cards and FIDO2 hardware tokens are the gold standard.

**Phishing-resistant MFA** is specifically called out: "Multifactor cryptographic device authenticators, like the common access card (CAC) and personal identity verification (PIV) card, as well as multifactor hardware tokens implementing FIDO2 mechanisms, are the most robust mechanisms commercially available, providing AAL 3 with phishing resistance."

**Non-person entity (NPE) authenticators** must be hardware-protected: "An NPE would ideally be represented by a public key certificate whose associated private key is under the strict control of the entity it represents." NPEs that only support passwords must use long, randomly generated passwords stored in hardware-protected vaults. Default passwords must be changed; unnecessary system accounts must be disabled.

**Credential lifecycle maturity:**

| Phase | Key Capability |
|-------|---------------|
| **Preparation** | Enterprise-approved credential providers per FICAM; inventory all credentials associated with each user. |
| **Basic** | All users use enterprise-approved, highly-assured authenticators compliant with NIST SP 800-63; lifecycle managed via defined methods or enterprise PKI. |
| **Intermediate** | Plans to update credentials per NSS standards (NSM-10, CNSSP 15); all credentials independently managed and rapidly revocable on compromise notification. |
| **Advanced** | Established processes to rapidly revoke AND replace credentials at scale; authoritative risk-based attribute sources interface directly with credential revocation systems. |

**Cryptographic agility** is a special concern: "Enterprises should be able to respond to [a cryptographic method becoming weak] by rapidly revoking obsolete or compromised mechanisms and deploying new credentials using secure methods, potentially to large numbers of users in a short period of time."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The MFA guidance is consistent with CISA's Binding Operational Directive 22-01 (which mandates phishing-resistant MFA for agency systems) and aligns with the CISA ZTMM Authentication function at the Advanced and Optimal levels. The NPE guidance addresses a gap that CISA's ZTMM doesn't cover in as much depth.

## Stakes

The jump from "we have MFA" (Basic) to "our MFA is phishing-resistant AND we can revoke credentials at scale in hours" (Intermediate/Advanced) is where credential management actually prevents breaches. Colonial Pipeline had no MFA at all; OPM had MFA deployed but not universally enforced. Both would have been caught by the Basic phase — but sophisticated adversaries sidestep weaker MFA (push fatigue, SIM swap, adversary-in-the-middle). Phishing-resistant MFA closes that gap.

## Disagreement

**Who disagrees:**

The debate between PIV-derived credentials and FIDO2 is ongoing. PIV/CAC is the defense standard and provides AAL3 with existing PKI infrastructure. FIDO2 is simpler, easier to deploy at scale, and more accessible to commercial organizations. NSA recommends both — the choice depends on existing infrastructure. Some argue that PIV's complexity slows adoption compared to FIDO2's consumer-friendly UX. The market is moving toward FIDO2/passkeys for broad deployment with PIV retained for high-assurance defense environments.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**
- [[access-mgmt-abac-least-privilege|Least-privilege access enforcement in C9 depends on C10's strong credential management; weak credentials undermine acces]]

**Supports:**
- [[continuous-authentication-common-all-pillars|C10 defines initial authentication strength (MFA floor, AAL3 ceiling, phishing resistance) which, together with C6's con]]
- [[ztmm-operationalizes-nist-seven-tenets|C10 describes credential management maturity within ZTMM, exemplifying C5's operationalization claim.]]
- [[authentication-keystone-identity-function|Phishing-resistant credential management directly strengthens the authentication keystone against the largest capability]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**
  - "[[authentication-keystone-identity-function]]"

**Extends:**
- [[authentication-keystone-identity-function|C10 specifies the credential management approach (phishing-resistant MFA, AAL levels) as the mechanism for achieving C7']]
- [[icam-non-negotiable-substrate|C10 details how the Credential Management FICAM capability area (established by C3) is defined by phishing resistance wi]]
- [[identity-foundational-zta-pillar|C10 specifies credential management as defined by phishing resistance (MFA floor, AAL3 ceiling), adding operational spec]]
- [[the-strongest-user-authentication-binds-identity-to-hardware|Phishing resistance (MFA→AAL3 scale) extends hardware binding by defining the credential management progression that har]]

## Assessment

The credential management section is the strongest part of the document for operational guidance. The four-phase maturity model gives organizations a clear path: (1) inventory what you have, (2) get everyone on strong MFA, (3) make it phishing-resistant with lifecycle management, (4) automate revocation with risk-based triggers. The NPE guidance is essential and often overlooked — service accounts and API keys are the credentials attackers most often target for lateral movement.
