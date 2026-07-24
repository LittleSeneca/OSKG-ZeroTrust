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

The Identity pillar defines how an agency should mature its capabilities for ensuring that *the right users and entities access the right resources at the right time for the right purpose without excessive access.* Identity is the foundational pillar — without it, a ZTA cannot make access decisions.

---

### Claim 1: Identity is the foundational pillar of ZTA — without mature identity capabilities, a ZTA cannot make access decisions, and ICAM serves as the substrate beneath the entire pillar, as established by both CISA's maturity model and NIST 800-207 Chapter 6.

**Author's claim:** Identity is the foundational pillar — without it, a ZTA cannot make access decisions. The pillar covers authentication, identity stores, risk assessments, and access management, each with four maturity levels: **Traditional**, **Initial**, **Advanced**, and **Optimal**.

**Evidence presented:**
- The pillar is organized around four operational functions (Authentication, Identity Stores, Risk Assessments, Access Management) plus three cross-cutting capabilities (Visibility & Analytics, Automation & Orchestration, Governance).
- The maturity progression mirrors the NSA User Pillar's four-phase framework (Preparation → Basic → Intermediate → Advanced), though CISA uses different labels and organizes around operational *functions* rather than ICAM sub-capabilities.
- As NIST 800-207 Chapter 6 makes explicit: *without mature ICAM, ZTA cannot function.* The Identity pillar is essentially a maturity framework for that ICAM substrate.

**Confidence:** HIGH. The foundational status of Identity is cross-validated by NIST, CISA, NSA, and DoD frameworks.

---

### Claim 2: CISA defines four maturity stages — Traditional (manual, static, perimeter-based), Initial (automation begins, some cloud integration, MFA required), Advanced (phishing-resistant MFA, dynamic risk assessments, session-based access), and Optimal (fully automated, continuous validation, JIT/JEA, behavior-based analytics) — that apply across all pillars.

**Author's claim:** CISA defines four maturity stages that apply across all pillars. (§5.1)

**Evidence presented:**

| Stage | Core Characteristic |
|-------|-------------------|
| **Traditional** | Manual processes, static policies, perimeter-based trust, legacy infrastructure. Passwords or basic MFA only. |
| **Initial** | Automation begins. Attribute-based policies, some cloud identity integration, MFA required but not necessarily phishing-resistant. |
| **Advanced** | Phishing-resistant MFA deployed; identity stores consolidated across environments; dynamic risk assessments inform access decisions; session-based and need-based access. |
| **Optimal** | Fully automated, continuous validation; just-in-time/just-enough access; real-time risk-based decisions; comprehensive cross-pillar interoperability; behavior-based analytics. |

**Confidence:** HIGH. These are direct definitions from the source document.

---

### Claim 3: Authentication is the keystone function of the Identity pillar — the jump from Traditional (passwords) to Advanced/Optimal (phishing-resistant MFA + continuous validation) is the largest single capability gap and the one most directly tied to breach prevention.

**Author's claim:** Authentication maturity moves from *static, password-based* to *continuous, phishing-resistant validation*. (§5.1 — Authentication)

**Evidence presented:**

| Stage | Capability |
|-------|-----------|
| **Traditional** | Passwords or basic MFA; static, one-time access grant. |
| **Initial** | MFA required; validates multiple entity attributes (e.g., locale, activity); passwords may still be one factor. |
| **Advanced** | Phishing-resistant MFA deployed for all identities (FIDO2, PIV); password-less MFA implementation begins. |
| **Optimal** | Continuous identity validation with phishing-resistant MFA — not just at initial access, but throughout the session. |

**Confidence:** HIGH. CISA and NSA are fully aligned on this progression. The phishing-resistant MFA gap is well-documented in breach data.

**NSA cross-reference:** The NSA User Pillar's *Credential Management* capability maps directly:
- **Preparation (NSA)** ≈ **Traditional (CISA):** Passwords or basic MFA; credentials may be locally managed.
- **Basic (NSA)** ≈ **Initial (CISA):** Enterprise-approved highly-assured authenticators per NIST SP 800-63.
- **Intermediate (NSA)** ≈ **Advanced (CISA):** Phishing-resistant MFA (CAC/PIV, FIDO2) becomes standard.
- **Advanced (NSA)** ≈ **Optimal (CISA):** Continuous validation, not point-in-time; risk-based attributes interface with credential revocation.

---

### Claim 4: Identity stores must be integrated across environments, not just federated — the maturity progression from siloed on-premises to securely integrated across all partners and environments is a significant architectural undertaking, not achievable through SSO alone.

**Author's claim:** Identity store maturity moves from *siloed, on-premises* to *securely integrated across all partners and environments*. (§5.1 — Identity Stores)

**Evidence presented:**

| Stage | Capability |
|-------|-----------|
| **Traditional** | Self-managed, on-premises identity stores only. |
| **Initial** | Mix of self-managed and hosted (cloud/other agency) identity stores; minimal integration (e.g., basic SSO). |
| **Advanced** | Secure consolidation and integration of some self-managed and hosted identity stores. |
| **Optimal** | Identity stores securely integrated across all partners and environments, as appropriate. |

**Confidence:** HIGH. The integration requirement is explicit, but the operational difficulty is understated.

**NSA cross-reference:** Maps to NSA's *Identity Management* capability. Key difference: CISA emphasizes *where* the stores live and *how well they're integrated* (architectural); NSA emphasizes *what attributes are in them* and *how authoritative they are* (governance). Both converge at the optimal/advanced level — integrated, attribute-rich, risk-informed.

---

### Claim 5: Risk assessment evolves from a static, periodic checkbox activity to a real-time, continuous feed into every access decision — a structural shift that CISA treats as a first-class function with its own maturity track, whereas NSA treats it as a property of the access management system.

**Author's claim:** Risk assessment maturity moves from *manual, static* to *real-time, continuous, dynamic*. (§5.1 — Risk Assessments)

**Evidence presented:**

| Stage | Capability |
|-------|-----------|
| **Traditional** | Limited determinations for identity risk. |
| **Initial** | Manual methods and static rules for risk determination; supports basic visibility. |
| **Advanced** | Some automated analysis; dynamic rules inform access decisions and response activities. |
| **Optimal** | Real-time identity risk determination based on continuous analysis and dynamic rules; delivers ongoing protection. |

**Confidence:** MEDIUM-HIGH. The progression is well-defined but the operational requirements for real-time continuous risk assessment are significant and under-described.

**NSA cross-reference:** This is a notable structural difference: CISA treats risk as a first-class function with its own maturity track; NSA treats it as a property of the access management system. Both agree on the destination: real-time, continuous, behavior-informed risk assessment.

---

### Claim 6: Access management operationalizes least privilege through the progression from permanent access → expiring access → need-based/session-based → automated JIT/JEA, with NSA providing the tactical implementation layer (PAM tools, privileged access workstations, ABAC, risk-adaptive policies).

**Author's claim:** Access management maturity moves from *permanent, periodically-reviewed* to *just-in-time, just-enough, automated*. (§5.1 — Access Management)

**Evidence presented:**

| Stage | Capability |
|-------|-----------|
| **Traditional** | Permanent access with periodic manual review (privileged and unprivileged). |
| **Initial** | Access that expires; automated review; includes privileged access requests. |
| **Advanced** | Need-based and session-based access; tailored to specific actions and resources; includes privileged access. |
| **Optimal** | Automated just-in-time (JIT) and just-enough access (JEA); tailored to individual actions and individual resource needs. |

**Confidence:** HIGH. The JIT/JEA progression is well-defined and broadly agreed across frameworks.

**NSA cross-reference:** NSA's *Access Management* capability maps closely and provides much more tactical detail: PAM tools, privileged access workstations, ABAC models, fine-grained risk-adaptive access policies. CISA provides the maturity *targets*; NSA provides the *how-to* for defense environments.

---

### Claim 7: Three cross-cutting capabilities — Visibility & Analytics, Automation & Orchestration, and Governance — operate within the Identity pillar and become increasingly automated and integrated across environments as maturity increases.

**Author's claim:** CISA defines three capabilities that span all pillars. Their maturity progression within Identity mirrors the broader pillar trajectory. (§5.1 — Cross-Cutting Capabilities)

**Evidence presented:**

**Visibility and Analytics:**
| Stage | Capability |
|-------|-----------|
| **Traditional** | Collects user/entity activity logs (especially privileged); some routine manual analysis. |
| **Initial** | Routine manual + some automated analysis; limited correlation between log types. |
| **Advanced** | Automated analysis across some log types; collection augmented to address gaps. |
| **Optimal** | Comprehensive visibility and situational awareness; automated analysis including behavior-based analytics (UEBA). |

**Automation and Orchestration:**
| Stage | Capability |
|-------|-----------|
| **Traditional** | Manual orchestration of self-managed identities; limited integration; regular manual review. |
| **Initial** | Manual orchestration for privileged/external identities; automated for non-privileged users. |
| **Advanced** | Manual orchestration for privileged users; automated for all other identities with cross-environment integration. |
| **Optimal** | Fully automated orchestration of all identities across all environments; driven by behaviors, enrollments, and deployment needs. |

**Governance:**
| Stage | Capability |
|-------|-----------|
| **Traditional** | Identity policies enforced via static technical mechanisms and manual review. |
| **Initial** | Enterprise-wide identity policies defined; minimal automation; manual updates. |
| **Advanced** | Enterprise-wide identity policies with automation; periodic policy updates. |
| **Optimal** | Fully automated enterprise-wide identity policies for all users/entities across all systems; continuous enforcement with dynamic updates. |

**Confidence:** HIGH. These are direct from the source document.

---

### Claim 8: CISA and NSA identity frameworks are complementary, not redundant — CISA provides the maturity model framework (what to measure, what "good" looks like for FCEB agencies), while NSA provides the implementation roadmap (how to get there, tailored for national security systems but broadly applicable), and together they form the most complete federal guidance for identity maturity in a ZTA context.

**Author's claim:** This is a synthesis claim by this note's author comparing the two frameworks.

**Evidence presented:**
- CISA's four functions (Authentication, Identity Stores, Risk Assessments, Access Management) map to NSA's four ICAM sub-capabilities (Credential Management, Identity Management, Access Management, Federation) with tight alignment at each maturity level.
- NSA provides much more tactical detail: PAM tools, privileged access workstations, ABAC models, fine-grained risk-adaptive access policies.
- CISA provides the maturity *targets*; NSA provides the *how-to*.

**Confidence:** MEDIUM-HIGH. The complementary relationship is visible when the two documents are compared side-by-side, but neither document explicitly frames itself as complementary to the other. This is an analytical observation.

**Key takeaways from the synthesis:**

1. **Authentication is the keystone function.** The jump from Traditional (passwords) to Advanced/Optimal (phishing-resistant MFA + continuous validation) is the largest single capability gap.

2. **Identity stores must be integrated, not just federated.** Optimal means identity data flows seamlessly between on-prem, cloud, and partner systems.

3. **Risk assessment evolves from static → dynamic → continuous.** At Optimal, it's a real-time feed into every access decision.

4. **Access management is where least privilege becomes operational.** CISA's progression (permanent → expiring → session-based → JIT/JEA) operationalizes the principle. NSA adds the tactical layer.

5. **ICAM is the substrate beneath this entire pillar.** As NIST 800-207 Chapter 6 makes explicit: *without mature ICAM, ZTA cannot function.*

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
