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

## Claim 1: The user pillar operationalizes ICAM for Zero Trust — and ICAM is the non-negotiable substrate

**NSA's claim:** The user pillar "expands and refines the capabilities associated with the FICAM framework to address the enhanced threat to identity, credentials, and access management." Without mature ICAM, ZTA cannot function.

**Evidence presented:** The document frames the entire user pillar around five FICAM capability areas: Identity Management, Credential Management, Access Management, Federation, and Governance. This is not an arbitrary structure — it mirrors the Federal ICAM Architecture directly (GSA, 2021). The NSA's contribution is adding the *threat-centric maturity model* on top: preparation → basic → intermediate → advanced for each capability.

The stakes are established through two canonical breach examples:

1. **OPM 2015 breach:** Leveraged compromised credentials. MFA was available but not fully deployed. 21.5 million personnel records exfiltrated.
2. **Colonial Pipeline 2021 ransomware:** Exploited a legacy VPN without MFA. Attackers gained access via a compromised complex password. Economic disruption across the US Southeast.

Both incidents exploited *immature ICAM capabilities* — exactly the gaps the user pillar maturity model is designed to close.

**Confidence:** HIGH. This claim is consistent with NIST 800-207 Chapter 6.3 (which states that FICAM is a "critical dependency" for ZTA) and with OMB M-22-09 (which requires agencies to adopt phishing-resistant MFA and consolidate identity systems). The NSA, NIST, CISA, and OMB are all aligned: mature ICAM is prerequisite to ZTA.

**What's at stake:** If ICAM is the non-negotiable substrate, identity maturity drives the ZTA implementation roadmap. You cannot skip identity and start with network microsegmentation — access decisions depend on authenticated identity. The user pillar is the logical starting point for any ZT adoption program.

**Who disagrees:** Nobody credible. The debate is about *how* to mature ICAM (phishing-resistant MFA mandate timing, centralized vs. federated identity stores, PIV vs. FIDO2) not *whether* it's required. Even vendor-driven ZTNA implementations depend on identity integration.

**Alternative reading:** The ICAM-first framing could be read as NSA's institutional preference — defense and intelligence agencies already have strong ICAM programs (CAC/PIV, PKI, clearance-based attributes). For commercial organizations without this infrastructure, the "start with identity" prescription may be more aspirational and take longer. But even in that case, the direction of travel is the same.

**My assessment:** The user pillar is the most foundational of the seven NSA pillars because identity is the *axis of access decisions*. Without it, nothing else in ZT works. The document's decision to lead with the user pillar is correct, and the ICAM framing gives it an architecture it can mature against. The CISA ZTMM Identity pillar ([CISA ZTMM — Identity Pillar]) covers the same territory with a slightly different taxonomy (Authentication, Identity Stores, Risk Assessments, Access Management as separate functions rather than ICAM sub-capabilities), but both converge on the same destination.

---

## Claim 2: Identity management maturity is about attribute authority, not just identity inventory

**NSA's claim:** Identity management "begins with establishing a current and accurate inventory of all users, including person and non-person entities, ensuring those with access to critical resources are vetted and registered." But that's just preparation. Real maturity means attributes at every level — from standard to locally-defined to risk-based — all integrated directly into access control mechanisms.

**Evidence presented:** The four-phase maturity progression for Identity Management:

| Phase | Capability | Key Shift |
|-------|-----------|-----------|
| **Preparation** | Enterprise repositories for person-entities only; NPEs managed ad-hoc locally; in-person vetting per NIST FIPS 201. | *Get everyone registered.* |
| **Basic** | Enterprise attribute standards defined; all local attributes documented; attribute claims validated during vetting or via approved remote methods; standard attributes integrated into access control. | *Standardize attributes enterprise-wide.* |
| **Intermediate** | Standardized attributes with authoritative sources identified; locally-defined attributes for highly sensitive resources; standardized issuance processes. | *Attribute authority becomes formal — you know who owns each attribute.* |
| **Advanced** | Risk-based attributes defined and standardized; risk indicators associated with entities alert resource managers; responses may be resource-specific; ALL user attributes relevant to a resource integrated directly into access mechanisms. | *Risk becomes a first-class identity attribute.* |

**Confidence:** HIGH. This progression is the most granular in federal guidance. CISA's version (Identity Stores function) focuses more on *where* identity data lives (on-prem → cloud → integrated across partners); NSA focuses on *what attributes exist* and *how authoritative they are*. Both are necessary. NSA's emphasis on NPEs (non-person entities — services, devices, automated processes) is distinctive and reflects defense environments where service accounts and machine identities are as critical as user identities.

**What's at stake:** Attribute authority is the difference between *having* identity data and *trusting* it for access decisions. If your identity store says a user has clearance X but you don't know who asserted that or how it was validated, the attribute is useless for security decisions. This is why the intermediate phase's "authoritative sources identified for each attribute" is the critical inflection point.

**Who disagrees:** This is less a disagreement and more a gap. Commercial identity providers (Okta, Azure AD/Entra ID, Ping) don't natively support the "clearance" and "releasability" attributes NSA references for NSS. The commercial world models identity as HR attributes + group membership; the defense world adds classification, community-of-interest, and formal access approvals. The ABAC model (covered in Claim 4) is designed to bridge this gap.

**My assessment:** The identity management maturity model is NSA at its most practical. The progression from "ad-hoc NPE registration" to "risk-based attributes driving automated access decisions" is a realistic multi-year roadmap. The emphasis on NPEs is forward-looking — in cloud-native environments, service identities often outnumber user identities 10:1, and the same attribute-authority principles apply.

---

## Claim 3: Credential management is defined by phishing resistance — MFA is the floor, AAL3 is the ceiling

**NSA's claim:** "Compliance with EO 14028 requires MFA techniques for all users. Organizations should select strong MFA products that are validated to meet the desired AAL." But the document goes further: phishing-resistant MFA (AAL3) is the recommended target, and credential lifecycle management — especially rapid revocation — distinguishes mature implementations from basic ones.

**Evidence presented:**

**MFA and Authenticator Assurance Levels:** The document maps authentication strength to NIST SP 800-63-3's AAL scale:
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

**Confidence:** HIGH. The MFA guidance is consistent with CISA's Binding Operational Directive 22-01 (which mandates phishing-resistant MFA for agency systems) and aligns with the CISA ZTMM Authentication function at the Advanced and Optimal levels. The NPE guidance addresses a gap that CISA's ZTMM doesn't cover in as much depth.

**What's at stake:** The jump from "we have MFA" (Basic) to "our MFA is phishing-resistant AND we can revoke credentials at scale in hours" (Intermediate/Advanced) is where credential management actually prevents breaches. Colonial Pipeline had no MFA at all; OPM had MFA deployed but not universally enforced. Both would have been caught by the Basic phase — but sophisticated adversaries sidestep weaker MFA (push fatigue, SIM swap, adversary-in-the-middle). Phishing-resistant MFA closes that gap.

**Who disagrees:** The debate between PIV-derived credentials and FIDO2 is ongoing. PIV/CAC is the defense standard and provides AAL3 with existing PKI infrastructure. FIDO2 is simpler, easier to deploy at scale, and more accessible to commercial organizations. NSA recommends both — the choice depends on existing infrastructure. Some argue that PIV's complexity slows adoption compared to FIDO2's consumer-friendly UX. The market is moving toward FIDO2/passkeys for broad deployment with PIV retained for high-assurance defense environments.

**My assessment:** The credential management section is the strongest part of the document for operational guidance. The four-phase maturity model gives organizations a clear path: (1) inventory what you have, (2) get everyone on strong MFA, (3) make it phishing-resistant with lifecycle management, (4) automate revocation with risk-based triggers. The NPE guidance is essential and often overlooked — service accounts and API keys are the credentials attackers most often target for lateral movement.

---

## Claim 4: Access management is where least privilege becomes operational — through ABAC, JIT/JEA, PAM, and privileged access workstations

**NSA's claim:** Access management progresses from broad, role-based policies to fine-grained, risk-adaptive, attribute-based decisions — with specific tools and practices at each maturity level. The goal is attribute-based access control (ABAC) integrated with risk-based indicators, supported by Just-in-Time/Just-Enough Access (JIT/JEA), Privileged Access Management (PAM) tools, and dedicated privileged access workstations.

**Evidence presented:** The document identifies five core access management capabilities and maps them across maturity phases:

### Core Capabilities

1. **Least Privilege:** "Implementing least privilege access policies minimizes the damage a malicious actor can cause." For highly privileged users: separate devices, credentials, and accounts isolated from high-risk activities (email, web browsing).

2. **Just-in-Time (JIT) / Just-Enough Access (JEA):** Privileges are granted only when needed, only at the level needed, and revoked automatically after the task. "Access to highly privileged functions are segregated both logically and chronologically."

3. **Privileged Access Management (PAM) Tools:** Centralized management for fine-grained privileges, proxying access to resources that don't support strong authenticators, enforcing workflow constraints and role separation. Critical warning: "PAM implementations should be tightly controlled and monitored, since they control the highly privileged functions that shape the environment, making them an attractive target."

4. **Privileged Access Workstations:** Dedicated physical or virtual devices for administrative functions. "It is important that administrative workstations only have access to essential applications required to perform administrative actions and do not allow high-risk activities, such as email or web browsing."

5. **Fine-grained, risk-adaptive access policies (ABAC):** Access decisions consider multiple attributes per request — user identity, device posture, resource sensitivity, data classification, risk-based indicators. "Attribute-based access control (ABAC) models provide the flexibility required to meet these goals." NIST SP 800-162 is the authoritative reference for ABAC implementation.

### Maturity Phases for Access Management

| Phase | Key Capability |
|-------|---------------|
| **Preparation** | Inventory user entitlements and access policies; remove outdated/inappropriate entitlements; identify attributes implicit in existing policies; update legacy applications to use modern methods. |
| **Basic** | Review against least privilege; implement PAM for all highly privileged users; identify authoritative sources for user attributes; implement data tagging for critical resources; ensure access logging for forensics; limit authentication assertions in time and scope. |
| **Intermediate** | Segregate highly privileged functions logically and chronologically using dedicated workstations + PAM with JIT/JEA; access policies reflect authentication strength (weaker auth = less access); differentiate access for MFA types. |
| **Advanced** | Granular access per specific resource considering user, device, application sensitivity, and data attributes; risk-based indicators from authoritative sources; user activity assessed against roles and behavior patterns (continuous authentication); risk responses triggered automatically; credential revocation interfaces with risk-based attributes. |

**The ABAC model is the architecture that makes all of this possible.** Traditional RBAC is static — a user's role determines their access, period. ABAC adds dimensions: *this* user, on *this* device, at *this* time, with *this* risk score, requesting *this* specific resource with *these* data attributes. For NSS, the attributes include classification, clearance, releasability, citizenship, community-of-interest, and need-to-know — attributes that don't exist in standard commercial IAM products but are life-or-death for defense systems.

**Confidence:** HIGH. The access management section is the longest and most detailed in the document, reflecting NSA's operational focus. The progression from "inventory your mess" (Preparation) to "risk-based automated access decisions with continuous authentication" (Advanced) is realistic and well-defined.

**What's at stake:** Access management is where identity credentials meet resources. The most common attacker technique — compromised credentials → lateral movement → privilege escalation — exploits gaps at every phase: no least privilege (too much access), no PAM (privileged accounts unmonitored), no JIT/JEA (standing privileges always on), no privileged workstations (admin browses web, gets phished). The four capabilities together close this kill chain.

**Who disagrees:** The practical challenge is that ABAC at NSA's Advanced level requires significant investment in attribute infrastructure, policy authoring, and enforcement mechanisms. NIST 800-162 acknowledges this: "ABAC implementations can be complex and resource-intensive to initially establish." CISA's ZTMM Access Management function sets the same destination (JIT/JEA at Optimal) but is less prescriptive about the ABAC path. Commercial ZTNA vendors (Zscaler, Palo Alto) tend to implement resource-level access controls without the full ABAC attribute framework that defense environments require.

**My assessment:** The access management section is the most practical part of the document for implementers. The five capabilities (least privilege, JIT/JEA, PAM, privileged workstations, ABAC) form a coherent strategy. The order matters: you can't do JIT/JEA without PAM, you shouldn't do PAM without privileged workstations (else the PAM console itself becomes a target), and ABAC is the long-term architecture that makes risk-adaptive decisions possible. The NSA's explicit warning that PAM itself is an attractive target is a critical operational insight that most guidance omits.

---

## Claim 5: Identity federation is the hard problem — maturity amplifies complexity, not reduces it

**NSA's claim:** "Federation between partner organizations is complicated, and will depend on the partner agreements, the capabilities and maturity of each partner's system, and the assessed risk associated with each system." ZT does not remove requirements for cross-domain solutions.

**Evidence presented:** Unlike the other three ICAM sub-capabilities, the NSA does not provide detailed maturity phases for federation. Instead, it identifies the persistent challenges:

- Partners have varying ICAM maturity levels and distinct implementations that "complicate sharing."
- FICAM requirements for federation apply at all maturity levels: confidence in partner identity/credential management, mapping authentication assertions from multiple sources, aligning attributes, reconciling access policy differences.
- At higher maturity, federation requirements intensify: sharing risk-based attributes, access to back-end credential and inventory repositories, detailed system access logs.
- "Zero Trust mechanisms do not remove requirements for cross-domain solutions, especially when information sensitivity differences create excessive risk or when maturity levels vary widely."

**Implementation guidance for federation:**
1. Inventory partner identities (PEs and NPEs) your systems need to support.
2. Map partner identity and credential assurance levels; map partner-issued attributes to local equivalents.
3. Map access policy differences and establish mitigating controls for interoperability gaps.
4. Negotiate formatting, equivalency, and interface specifications at the IT security leadership level.

**Confidence:** MEDIUM. The admission that federation is complicated and ZT doesn't simplify it is honest, but the document is thin on *how* to address these challenges. This is a known hard problem — NISTIR 8149 (Developing Trust Frameworks to Support Identity Federations) is an entire publication on it.

**What's at stake:** Federation is where most ZT implementations hit the wall. Internal ICAM maturity can be achieved through organizational authority (mandate CAC/PIV, enforce MFA, deploy PAM). External federation requires *negotiation* with partners who have different risk tolerances, different technology stacks, and different timelines. The DoD's mission partner environment is the canonical hard case: sharing classified information with coalition partners whose ICAM maturity may be at the Preparation phase.

**Who disagrees:** This is not a disagreement but a gap. NIST's work on trust frameworks (NISTIR 8149, NIST SP 800-63-C) provides more detailed guidance. The DoD ZT Reference Architecture addresses federation as a core capability with more specificity (attribute-based access control across security domains via the ABAC model). CISA's ZTMM touches on federation indirectly through the "identity stores" function at Optimal ("securely integrated across all partners and environments").

**My assessment:** The document's honesty about federation complexity is more valuable than a superficial maturity model would be. The four-step implementation guidance is practical if high-level. The key insight is that ZT doesn't magically solve the cross-domain problem — it raises the bar for internal security, which makes the federation boundary the new weak point. Mitigating controls for partner maturity gaps should be an explicit part of any federation agreement.

---

## Claim 6: The NSA and CISA identity frameworks are complementary — NSA provides the "how" for the defense context, CISA provides the "what to measure"

**NSA's claim (implicit):** The user pillar maturity model is designed for NSS environments where attributes like clearance, classification, and community-of-interest are first-class access decision inputs, and where adversaries are nation-state actors. This distinguishes it from CISA's FCEB-focused maturity model.

**Evidence presented:** The structural differences between the two frameworks:

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

**Confidence:** HIGH. The complementarity is well-established. The CISA ZTMM Identity Pillar note already cross-references extensively with the NSA User Pillar. NIST 800-207 Ch 6 references both.

**What's at stake:** Organizations that use only one framework will have gaps. CISA alone underinvests in NPE credentials and cryptographic agility. NSA alone underinvests in governance as a first-class function and risk assessments as a distinct capability track. Together they're complete.

**My assessment:** This is one of the most productive cross-references in the entire OSKG-ZeroTrust graph. The frameworks don't conflict — they address different audiences with different threat models and different operational constraints. The fact that both were published in 2023 (CISA v2 in April, NSA v1.1 in April) and align without contradiction suggests coordination, not competition. For any organization doing both defense and civilian work (common in the DIB), both frameworks should be referenced.

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
