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
claims_status: extracted
claims_extracted: 2026-07-24
---

# CISA ZTMM — Identity Pillar

> **Full title:** Zero Trust Maturity Model v2.0 — Section 5.1: Identity
> **Agency:** Cybersecurity and Infrastructure Security Agency (CISA)
> **Date:** April 2023
> **Scope:** Federal Civilian Executive Branch (FCEB) agencies; applicable to all organizations

## Overview

The Identity pillar defines how an agency should mature its capabilities for ensuring that *the right users and entities access the right resources at the right time for the right purpose without excessive access.* Identity is the foundational pillar — without it, a ZTA cannot make access decisions.

---

**Claim 1 —** Identity is the foundational pillar of ZTA — without mature identity capabilities, a ZTA cannot make access decisions, and ICAM serves as the substrate beneath the entire pillar, as established by both CISA's maturity model and NIST 800-207 Chapter 6. → [[identity-foundational-zta-pillar]]
---

**Claim 2 —** CISA defines four maturity stages — Traditional (manual, static, perimeter-based), Initial (automation begins, some cloud integration, MFA required), Advanced (phishing-resistant MFA, dynamic risk assessments, session-based access), and Optimal (fully automated, continuous validation, JIT/JEA, behavior-based analytics) — that apply across all pillars. → [[cisa-four-maturity-stages]]
---

**Claim 3 —** Authentication is the keystone function of the Identity pillar — the jump from Traditional (passwords) to Advanced/Optimal (phishing-resistant MFA + continuous validation) is the largest single capability gap and the one most directly tied to breach prevention. → [[authentication-keystone-identity-function]]
---

**Claim 4 —** Identity stores must be integrated across environments, not just federated — the maturity progression from siloed on-premises to securely integrated across all partners and environments is a significant architectural undertaking, not achievable through SSO alone. → [[identity-stores-integrated-not-just-federated]]
---

**Claim 5 —** Risk assessment evolves from a static, periodic checkbox activity to a real-time, continuous feed into every access decision — a structural shift that CISA treats as a first-class function with its own maturity track, whereas NSA treats it as a property of the access management system. → [[risk-assessment-static-to-continuous]]
---

**Claim 6 —** Access management operationalizes least privilege through the progression from permanent access → expiring access → need-based/session-based → automated JIT/JEA, with NSA providing the tactical implementation layer (PAM tools, privileged access workstations, ABAC, risk-adaptive policies). → [[access-management-permanent-to-jit-jea]]
---

**Claim 7 —** Three cross-cutting capabilities — Visibility & Analytics, Automation & Orchestration, and Governance — operate within the Identity pillar and become increasingly automated and integrated across environments as maturity increases. → [[identity-cross-cutting-capabilities]]
---

**Claim 8 —** CISA and NSA identity frameworks are complementary, not redundant — CISA provides the maturity model framework (what to measure, what "good" looks like for FCEB agencies), while NSA provides the implementation roadmap (how to get there, tailored for national security systems but broadly applicable), and together they form the most complete federal guidance for identity maturity in a ZTA context. → [[cisa-nsa-identity-complementary]]
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
