---
tags:
  - source/standards
  - nist
  - zt-compliance
  - rmf
  - ficam
  - fedramp
  - oskg-zerotrust
created: 2026-07-24
source: "[[../../sources/standards/_txt/NIST_SP_800-207_Zero_Trust_Architecture]]"
chapter: 6
section_range: "6.1–6.7"
source_lines: "1640–1828"
related:
  - "[[Concepts Index]]"
  - "[[NIST 800-207 — Ch2 — Tenets]]"
  - "[[NIST 800-207 — Ch7 — Migration]]"
cross_references:
  - "[[CISA Zero Trust Maturity Model]]"
  - "[[NIST SP 800-207A — ZTA for Access Control]]"
  - "[[DoD Zero Trust Strategy]]"
---

# NIST 800-207 — Chapter 6 — Federal Guidance Interactions

> **Full title:** Zero Trust Architecture and Possible Interactions with Existing Federal Guidance
> **Pages:** 32–36 (in original pagination)

## Overview

Chapter 6 maps how a Zero Trust Architecture (ZTA) adoption intersects with seven existing federal cybersecurity frameworks, policies, and programs. The core message: ZTA does not replace these frameworks — it changes *how* they are implemented. Each framework retains its mandate; ZTA shifts the enforcement model from perimeter-based to resource-proximate.

The chapter makes two meta-claims:

1. **ZTA is complementary, not conflicting.** Existing federal guidance remains in force; ZTA changes the *locus of enforcement* (from perimeter to resource) and the *granularity of policy* (from network-segment to per-session).
2. **ZTA exposes gaps in identity and asset visibility.** Several programs (ICAM, CDM) become *prerequisites* — a ZTA cannot function without mature identity provisioning and complete asset inventory.

---

## 6.1 — NIST Risk Management Framework (RMF) [SP 800-37]

**The interaction:** ZTA changes authorization boundaries but not the RMF process itself.

- ZTA introduces new architectural components (Policy Engine, Policy Administrator, PEPs) that expand the system boundary.
- RMF's core workflow (categorize → select → implement → assess → authorize → monitor) remains unchanged.
- The key difference: risk acceptance decisions in a ZTA are *per-resource* and *per-session*, not per-network-zone. The policy engine encodes these decisions algorithmically.
- ZTA planning must integrate with the agency's existing RMF authorization lifecycle. New PEP deployments require updated Security Assessment Reports (SARs) and Plans of Action and Milestones (POA&Ms).

**Implication for OSKG-ZeroTrust:** ZTA doesn't eliminate risk management — it *automates* risk decisions at finer granularity. This is an architectural claim about the relationship between policy automation and formal risk acceptance.

---

## 6.2 — NIST Privacy Framework [NISTPRIV]

**The interaction:** ZTA's requirement to inspect and log all traffic creates privacy risks that the Privacy Framework must address.

- Core tension: ZTA mandates traffic inspection (or metadata logging when decryption is impossible), but some traffic contains PII or other private information.
- The Privacy Framework [NISTPRIV] provides the formal process to identify, measure, and mitigate privacy risks arising from ZTA operations — including biometric attributes used in access evaluations.
- Mitigations include: user notification (login banners), consent mechanisms, and user education.
- NISTIR 8062 is cited as a companion resource for privacy risk identification in network monitoring contexts.

**Implication for OSKG-ZeroTrust:** "Inspect everything" is a ZTA tenet, but it creates a privacy-compliance surface that the enterprise must formally manage. This is a tension point: security visibility vs. privacy protection.

---

## 6.3 — Federal ICAM Architecture (FICAM) [M-19-17, SP 800-63-3]

**The interaction:** ICAM is a *prerequisite* for ZTA, not a parallel effort.

- The Policy Engine cannot authorize access without sufficient subject/resource identity information. Weak identity provisioning = non-functional ZTA.
- OMB M-19-17 mandates every federal agency establish an ICAM office to govern identity issuance and management.
- NIST SP 800-63-3 (Digital Identity Guidelines) provides the technical standards for identity proofing, authentication, and federation that ZTA policy engines consume.
- Key dependency chain: **ICAM maturity → usable subject attributes → functional Policy Engine → ZTA enforcement.**

**Implication for OSKG-ZeroTrust:** ICAM is the identity substrate on which ZTA rests. An agency cannot "bolt on" ZTA without first achieving mature identity governance. This places identity at the center of the ZT architecture — consistent with the "identity-centric security" concept.

---

## 6.4 — Trusted Internet Connections 3.0 (TIC 3.0) [M-19-26]

**The interaction:** TIC is evolving from perimeter-based to distributed enforcement — converging with ZTA.

- **TIC 1.0/2.0:** Perimeter-based; assumed internal network is "trusted." Contradicted ZTA's core premise that network location ≠ trust.
- **TIC 3.0:** Recognizes that trust varies by computing context. Introduces two capability types:
  - **Universal Security Capabilities** — enterprise-level
  - **PEP Security Capabilities** — applied at multiple distributed PEPs along data flows, not at a single perimeter chokepoint
- TIC 3.0 security capabilities directly support ZTA: encrypted traffic, strong authentication, microsegmentation, network/system inventory.
- TIC 3.0 is network-focused; ZTA is broader (application, user, data). The chapter predicts a future "ZTA TIC use case" will formalize network protections at ZTA enforcement points.

**Implication for OSKG-ZeroTrust:** TIC 3.0 is the *network-security dimension* of ZTA in federal environments. Agencies don't choose between TIC and ZTA — they deploy TIC capabilities at ZTA PEPs.

---

## 6.5 — EINSTEIN / NCPS (National Cybersecurity Protection System)

**The interaction:** NCPS is perimeter-situational-awareness — ZTA pushes enforcement closer to assets. The two must reconcile.

- NCPS (EINSTEIN) delivers intrusion detection, advanced analytics, information sharing, and intrusion prevention for federal networks.
- Current NCPS sensor placement assumes perimeter defense; ZTA moves protections to the resource level.
- The program must evolve to (a) ingest cloud-based traffic telemetry, (b) receive expanded situational awareness data from ZTA systems, and (c) inform policy enforcement at both legacy NCPS locations and new ZTA PEPs.
- **Upside for incident response:** ZTA generates richer authentication, inspection, and logging data that can improve event impact quantification, feed ML-based detection, and support after-the-fact forensic analysis.

**Implication for OSKG-ZeroTrust:** NCPS is the legacy detection backbone. ZTA improves detection data quality but requires NCPS to adapt its sensor model. The chapter frames this as evolution, not replacement.

---

## 6.6 — DHS Continuous Diagnostics and Mitigation (CDM) Program

**The interaction:** CDM is another *prerequisite* — ZTA cannot operate without the visibility CDM provides.

The CDM program answers four foundational questions that ZTA depends on:

| CDM Question | ZTA Dependency |
|---|---|
| **What is connected?** (devices, apps, services) | PEP needs complete asset inventory to evaluate device posture |
| **Who is on the network?** (users, NPEs) | Policy Engine needs subject identity and role attributes |
| **What is happening?** (traffic patterns, messages) | Continuous monitoring and anomaly detection feed dynamic policy |
| **How is data protected?** (at rest, in transit, in use) | Data classification informs access policy and encryption requirements |

- DHS Hardware Asset Management (HWAM) program is specifically cited as enabling the "first steps" toward ZTA: agencies must discover and inventory all physical and virtual assets before they can categorize, configure, and monitor them.
- **Key dependency chain: CDM/HWAM → asset visibility → device posture assessment → PEP enforcement.**

**Implication for OSKG-ZeroTrust:** CDM is the *visibility prerequisite*. Without CDM, a ZTA is blindly enforcing policy on unknown assets — undermining the entire "verify explicitly" tenet.

---

## 6.7 — Cloud Smart Strategy & Federal Data Strategy

**The interaction:** Cloud/data inventory drives ZTA prioritization. Cloud-hosted and remote-accessed resources are the best ZTA candidates.

- **Cloud Smart** (successor to Cloud First) and the Data Center Optimization Initiative [M-19-19] require agencies to inventory and assess data collection, storage, and access — on-premises and in cloud.
- This inventory answers: *which business processes would benefit most from ZTA?*
- **Best ZTA candidates:** cloud-based applications/services and resources primarily accessed by remote workers — because subjects and resources both sit outside the traditional network perimeter. These see the most benefit in usability, scalability, and security.
- The **Federal Data Strategy** adds a cross-agency dimension: agencies must make data assets accessible to other agencies or the public. This maps to the ZTA "cross-enterprise collaboration" use case (Section 4.4). ZTA deployment for these assets must account for publication/collaboration requirements.

**Implication for OSKG-ZeroTrust:** Cloud migration and ZTA adoption are mutually reinforcing. Remote-access and cloud-resident resources are the natural starting point for ZTA implementation — they already operate outside the perimeter model.

---

## Cross-References to Related Guidance

### CISA Zero Trust Maturity Model
The CISA ZT Maturity Model operationalizes many of the interactions described in this chapter. CISA's five pillars (Identity, Device, Network, Application/Workload, Data) map directly to the federal programs discussed here — ICAM maps to the Identity pillar, CDM to Device, TIC 3.0 to Network, and the Federal Data Strategy to Data. The maturity model provides the *progression framework* that this chapter's policy interactions enable.

### NIST SP 800-207A — ZTA for Access Control
SP 800-207A extends the architectural concepts from Chapter 6 by providing technical implementation guidance for the access control components that ICAM policy and CDM asset data feed into. While Chapter 6 addresses *policy alignment*, 800-207A addresses *technical realization* of those policies in the PEP/policy engine access decision flow.

### DoD Zero Trust Strategy
The DoD ZT Strategy translates Chapter 6's federal civilian guidance into the defense context. The DoD strategy inherits the same compliance landscape (RMF, ICAM, CDM equivalents) but adds classification and mission-assurance dimensions that Chapter 6 does not address. The DoD's "Target ZT" and "Advanced ZT" capability levels correspond to maturity progressions that the federal programs in this chapter enable.

---

## Key Takeaways

1. **ZTA is a compliance *complement*, not a replacement.** RMF, Privacy Framework, ICAM, TIC, NCPS, CDM, and Cloud Smart all remain in force. ZTA changes where and how their controls are enforced.

2. **Identity and asset visibility are hard prerequisites.** Without mature ICAM (identity) and CDM (asset inventory), ZTA cannot function. These are not optional accelerators — they are foundational dependencies.

3. **The convergence trend is real.** TIC 3.0's distributed PEP model, CDM's continuous monitoring, and Cloud Smart's inventory requirements all push federal IT in directions that align with — and enable — ZTA.

4. **ZTA generates better data for existing programs.** Richer authentication logs, per-session inspection, and continuous device posture assessment improve the detection and response capabilities of NCPS/EINSTEIN and incident response teams.

5. **Privacy is an explicit tension.** "Inspect everything" collides with privacy obligations. Organizations must use the NIST Privacy Framework to formally manage this tension.
