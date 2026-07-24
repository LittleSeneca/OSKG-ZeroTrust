---
tags:
  - source/standards
  - cisa
  - zt-identity
  - zt-maturity
  - oskg-zerotrust
created: 2026-07-24
source: "[[../../sources/standards/_txt/CISA_Zero_Trust_Maturity_Model_v2]]"
section: "5.1"
source_lines: "462–687"
related:
  - "[[Concepts Index]]"
  - "[[CISA ZTMM — Devices Pillar]]"
  - "[[CISA ZTMM — Networks Pillar]]"
  - "[[CISA ZTMM — Applications and Workloads Pillar]]"
  - "[[CISA ZTMM — Data Pillar]]"
cross_references:
  - "[[NSA ZT — User Pillar]]"
  - "[[NIST 800-207 — Ch6 — Federal Guidance]]"
  - "[[NIST SP 800-63-3 — Digital Identity Guidelines]]"
  - "[[FICAM Architecture]]"
---

# CISA ZTMM — Identity Pillar

> **Full title:** Zero Trust Maturity Model v2.0 — Section 5.1: Identity
> **Agency:** Cybersecurity and Infrastructure Security Agency (CISA)
> **Date:** April 2023
> **Scope:** Federal Civilian Executive Branch (FCEB) agencies; applicable to all organizations

## Overview

The Identity pillar defines how an agency should mature its capabilities for ensuring that *the right users and entities access the right resources at the right time for the right purpose without excessive access.* Identity is the foundational pillar — without it, a ZTA cannot make access decisions. The pillar covers authentication, identity stores, risk assessments, and access management, each with four maturity levels: **Traditional**, **Initial**, **Advanced**, and **Optimal**.

The maturity progression mirrors the NSA User Pillar's four-phase framework (Preparation → Basic → Intermediate → Advanced), though CISA uses different labels and splits the capability areas slightly differently. Where the NSA framework organizes around ICAM sub-capabilities (Identity Management, Credential Management, Access Management, Federation), CISA structures around operational *functions* (Authentication, Identity Stores, Risk Assessments, Access Management) plus the three cross-cutting capabilities (Visibility & Analytics, Automation & Orchestration, Governance).

---

## Maturity Stages (General Definition)

CISA defines four maturity stages that apply across all pillars:

| Stage | Core Characteristic |
|-------|-------------------|
| **Traditional** | Manual processes, static policies, perimeter-based trust, legacy infrastructure. Passwords or basic MFA only. |
| **Initial** | Automation begins. Attribute-based policies, some cloud identity integration, MFA required but not necessarily phishing-resistant. |
| **Advanced** | Phishing-resistant MFA deployed; identity stores consolidated across environments; dynamic risk assessments inform access decisions; session-based and need-based access. |
| **Optimal** | Fully automated, continuous validation; just-in-time/just-enough access; real-time risk-based decisions; comprehensive cross-pillar interoperability; behavior-based analytics. |

---

## Function-by-Function Maturity Progression

### 1. Authentication

The core mechanism by which an agency validates that a user or entity is who they claim to be. The maturity trajectory moves from *static, password-based* to *continuous, phishing-resistant validation*.

| Stage | Capability |
|-------|-----------|
| **Traditional** | Passwords or basic MFA; static, one-time access grant. |
| **Initial** | MFA required; validates multiple entity attributes (e.g., locale, activity); passwords may still be one factor. |
| **Advanced** | Phishing-resistant MFA deployed for all identities (FIDO2, PIV); password-less MFA implementation begins. |
| **Optimal** | Continuous identity validation with phishing-resistant MFA — not just at initial access, but throughout the session. |

**NSA cross-reference:** The NSA User Pillar's *Credential Management* capability maps directly to CISA's Authentication function. NSA's maturity phases align tightly:
- **Preparation (NSA)** ≈ **Traditional (CISA):** Passwords or basic MFA; credentials may be locally managed.
- **Basic (NSA)** ≈ **Initial (CISA):** Enterprise-approved highly-assured authenticators per NIST SP 800-63. All users use enterprise credentials.
- **Intermediate (NSA)** ≈ **Advanced (CISA):** Plans for credential lifecycle management; all credentials independently managed and rapidly revocable. Phishing-resistant MFA (CAC/PIV, FIDO2) becomes standard.
- **Advanced (NSA)** ≈ **Optimal (CISA):** Rapid credential revocation and replacement processes; risk-based attributes interface with credential revocation systems. Continuous validation, not point-in-time.

### 2. Identity Stores

Where an agency stores and manages identity data. The maturity trajectory moves from *siloed, on-premises* to *securely integrated across all partners and environments*.

| Stage | Capability |
|-------|-----------|
| **Traditional** | Self-managed, on-premises identity stores only. |
| **Initial** | Mix of self-managed and hosted (cloud/other agency) identity stores; minimal integration (e.g., basic SSO). |
| **Advanced** | Secure consolidation and integration of some self-managed and hosted identity stores. |
| **Optimal** | Identity stores securely integrated across all partners and environments, as appropriate. |

**NSA cross-reference:** This maps to the NSA User Pillar's *Identity Management* capability:
- **Preparation (NSA):** Local, ad-hoc identity management for NPEs; enterprise repositories for person-entities only.
- **Basic (NSA):** Enterprise attribute standards defined; all local attributes documented; validated during vetting.
- **Intermediate (NSA):** Standardized attributes with authoritative sources identified; locally-defined attributes possible for sensitive resources.
- **Advanced (NSA) ≈ Optimal (CISA):** Risk-based attributes standardized; all attributes integrated directly into access mechanisms. Full integration across partners.

The key difference: CISA emphasizes *where* the stores live and *how well they're integrated* (architectural); NSA emphasizes *what attributes are in them* and *how authoritative they are* (governance). Both converge at the optimal/advanced level — integrated, attribute-rich, risk-informed.

### 3. Risk Assessments

How an agency evaluates the likelihood that an identity is compromised. The maturity trajectory moves from *manual, static* to *real-time, continuous, dynamic*.

| Stage | Capability |
|-------|-----------|
| **Traditional** | Limited determinations for identity risk. |
| **Initial** | Manual methods and static rules for risk determination; supports basic visibility. |
| **Advanced** | Some automated analysis; dynamic rules inform access decisions and response activities. |
| **Optimal** | Real-time identity risk determination based on continuous analysis and dynamic rules; delivers ongoing protection. |

**NSA cross-reference:** The NSA User Pillar does not separate "risk assessments" as a standalone function — risk is embedded throughout its Access Management maturity progression:
- **Intermediate (NSA):** Access policies begin to reflect authentication strength. Risk indicators start to inform access.
- **Advanced (NSA) ≈ Optimal (CISA):** Risk-based attributes of user and device minimize risk. User activity assessed against behavior patterns to identify increased risk. "Continuous authentication" triggers re-authentication. Risk-based attributes interface directly with credential revocation.

This is a notable structural difference: CISA treats risk as a first-class function with its own maturity track; NSA treats it as a property of the access management system. Both agree on the destination: real-time, continuous, behavior-informed risk assessment.

### 4. Access Management

How an agency authorizes access to resources. The maturity trajectory moves from *permanent, periodically-reviewed* to *just-in-time, just-enough, automated*.

| Stage | Capability |
|-------|-----------|
| **Traditional** | Permanent access with periodic manual review (privileged and unprivileged). |
| **Initial** | Access that expires; automated review; includes privileged access requests. |
| **Advanced** | Need-based and session-based access; tailored to specific actions and resources; includes privileged access. |
| **Optimal** | Automated just-in-time (JIT) and just-enough access (JEA); tailored to individual actions and individual resource needs. |

**NSA cross-reference:** The NSA User Pillar's *Access Management* capability is the most detailed section in that document and maps closely:
- **Preparation (NSA) ≈ Traditional (CISA):** Siloed access policies; some administrative segregation; weak legacy mechanisms.
- **Basic (NSA) ≈ Initial (CISA):** PAM for all highly privileged users; authoritative attribute sources identified; data tagging for critical resources; authentication assertions limited in time/scope.
- **Intermediate (NSA) ≈ Advanced (CISA):** Refined policies with resource segregation; dedicated privileged workstations; PAM tools supporting JIT/JEA; access differentiated by authentication strength.
- **Advanced (NSA) ≈ Optimal (CISA):** Granular access to specific resources considering user, device, application sensitivity, and data attributes. Risk-based indicators from authoritative sources. User activity assessed against roles and behavior patterns. "Continuous authentication" triggers re-authentication on risk.

The NSA document provides much more tactical detail: PAM tools, privileged access workstations, ABAC models, fine-grained risk-adaptive access policies. CISA provides the maturity *targets*; NSA provides the *how-to* for defense environments.

---

## Cross-Cutting Capabilities (Identity Context)

CISA defines three capabilities that span all pillars. In the Identity context:

### Visibility and Analytics

| Stage | Capability |
|-------|-----------|
| **Traditional** | Collects user/entity activity logs (especially privileged); some routine manual analysis. |
| **Initial** | Routine manual + some automated analysis; limited correlation between log types. |
| **Advanced** | Automated analysis across some log types; collection augmented to address gaps. |
| **Optimal** | Comprehensive visibility and situational awareness; automated analysis including behavior-based analytics (UEBA). |

### Automation and Orchestration

| Stage | Capability |
|-------|-----------|
| **Traditional** | Manual orchestration of self-managed identities; limited integration; regular manual review. |
| **Initial** | Manual orchestration for privileged/external identities; automated for non-privileged users and self-managed entities. |
| **Advanced** | Manual orchestration for privileged users; automated for all other identities with cross-environment integration. |
| **Optimal** | Fully automated orchestration of all identities across all environments; driven by behaviors, enrollments, and deployment needs. |

### Governance

| Stage | Capability |
|-------|-----------|
| **Traditional** | Identity policies enforced via static technical mechanisms and manual review. |
| **Initial** | Enterprise-wide identity policies defined; minimal automation; manual updates. |
| **Advanced** | Enterprise-wide identity policies with automation; periodic policy updates. |
| **Optimal** | Fully automated enterprise-wide identity policies for all users/entities across all systems; continuous enforcement with dynamic updates. |

---

## Key Takeaways

1. **Authentication is the keystone function.** The jump from Traditional (passwords) to Advanced/Optimal (phishing-resistant MFA + continuous validation) is the largest single capability gap — and the one most directly tied to breach prevention. CISA and NSA are fully aligned on this.

2. **Identity stores must be integrated, not just federated.** The maturity progression is about *consolidation and integration* across environments, not just establishing SSO. Optimal means identity data flows seamlessly between on-prem, cloud, and partner systems — a significant architectural undertaking.

3. **Risk assessment evolves from static → dynamic → continuous.** At Traditional/Initial, risk is a periodic checkbox. At Optimal, it's a real-time feed into every access decision — the engine that powers continuous validation.

4. **Access management is where least privilege becomes operational.** CISA's progression (permanent → expiring → session-based → JIT/JEA) operationalizes the least-privilege principle. NSA's guidance adds the tactical layer: PAM tools, privileged access workstations, ABAC, and risk-adaptive policies.

5. **CISA and NSA are complementary, not redundant.** CISA provides the *maturity model framework* (what to measure, what "good" looks like for FCEB agencies). NSA provides the *implementation roadmap* (how to get there, tailored for national security systems but broadly applicable). Together they form the most complete federal guidance for identity maturity in a ZTA context.

6. **ICAM is the substrate beneath this entire pillar.** As NIST 800-207 Chapter 6 makes explicit: *without mature ICAM, ZTA cannot function.* The Identity pillar of CISA's ZTMM is essentially a maturity framework for exactly that ICAM substrate.

---

## Relationship to Other CISA Pillars

The Identity pillar is not independent. Key dependencies:

- **Devices:** Optimal-level access decisions incorporate device posture (what device is the user on?). Identity risk interacts with device trust scores.
- **Networks:** Microsegmentation and dynamic network policies depend on identity attributes to define trust zones.
- **Applications and Workloads:** Workload identity (NPEs, services) lives in both the Identity and Applications pillars.
- **Data:** Data classification labels are consumed by identity-based access policies at the Optimal level.

Optimal identity maturity *requires* cross-pillar interoperability — identity attributes must feed into device posture, network policy, application access, and data protection decisions simultaneously.

---

## References

- CISA Zero Trust Maturity Model v2.0 (April 2023) — Section 5.1
- NSA Advancing Zero Trust Maturity Throughout the User Pillar (April 2023)
- NIST SP 800-207 — Chapter 6 (Federal Guidance Interactions, esp. 6.3 FICAM and 6.6 CDM)
- NIST SP 800-63-3 Digital Identity Guidelines
- OMB M-22-09, "Moving the U.S. Government Toward Zero Trust Cybersecurity Principles"
- EO 14028, "Improving the Nation's Cybersecurity"
- FICAM Architecture (GSA)
