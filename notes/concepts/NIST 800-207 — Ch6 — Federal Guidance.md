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

### Claim 1: ZTA is complementary to existing federal frameworks, not a replacement — it changes the locus of enforcement (from perimeter to resource) and the granularity of policy (from network-segment to per-session), but every existing program remains in force.

**Author's claim:** ZTA changes *how* frameworks are implemented, not *whether* they apply. The chapter identifies seven federal programs that all remain in force under ZTA.

**Evidence presented:** The chapter systematically maps seven programs (RMF, Privacy Framework, ICAM, TIC 3.0, EINSTEIN/NCPS, CDM, Cloud Smart) and shows how each adapts to ZTA rather than being replaced by it. The pattern is consistent across all seven: the program's mandate stays the same; ZTA changes where and how enforcement occurs.

**Confidence:** HIGH. NIST is authoritative on federal guidance interactions — the chapter is a direct statement of NIST's position on compliance continuity.

---

### Claim 2: ZTA exposes two hard prerequisites in existing programs — mature ICAM (identity) and CDM (asset inventory) — without which ZTA cannot function, because the Policy Engine cannot authorize access without sufficient subject/resource identity information and complete asset visibility.

**Author's claim:** ICAM and CDM are *prerequisites* for ZTA, not parallel efforts. Weak identity provisioning = non-functional ZTA. Incomplete asset inventory = blindly enforcing policy on unknown assets.

**Evidence presented:** The chapter identifies two dependency chains:
- **ICAM maturity → usable subject attributes → functional Policy Engine → ZTA enforcement** (§6.3)
- **CDM/HWAM → asset visibility → device posture assessment → PEP enforcement** (§6.6)

This is not stated as a single claim by NIST but emerges across two sections — it's this note's analytical synthesis.

**Confidence:** HIGH. The dependency is explicit in §6.3 and §6.6. NIST states both programs are foundational to ZTA operation.

---

### Claim 3: RMF — ZTA changes authorization boundaries but not the RMF process itself; risk acceptance decisions become per-resource and per-session, encoded algorithmically in the Policy Engine rather than assessed per-network-zone.

**Author's claim:** ZTA introduces new architectural components (Policy Engine, Policy Administrator, PEPs) that expand the system boundary, but RMF's core workflow (categorize → select → implement → assess → authorize → monitor) remains unchanged. (§6.1)

**Evidence presented:**
- New PEP deployments require updated Security Assessment Reports (SARs) and Plans of Action and Milestones (POA&Ms).
- ZTA planning must integrate with the agency's existing RMF authorization lifecycle.
- The key difference: risk acceptance decisions are now *per-resource* and *per-session*, not per-network-zone.

**Confidence:** HIGH. This is a direct mapping exercise — NIST is describing how RMF applies to its own ZTA model.

**Implication for OSKG-ZeroTrust:** ZTA doesn't eliminate risk management — it *automates* risk decisions at finer granularity. This is an architectural claim about the relationship between policy automation and formal risk acceptance.

---

### Claim 4: Privacy Framework — ZTA's "inspect everything" tenet creates an explicit tension with privacy obligations; traffic inspection and metadata logging may capture PII, requiring formal privacy risk management via the NIST Privacy Framework [NISTPRIV].

**Author's claim:** ZTA mandates traffic inspection (or metadata logging when decryption is impossible), but some traffic contains PII or other private information. The Privacy Framework provides the formal process to identify, measure, and mitigate these risks. (§6.2)

**Evidence presented:**
- Core tension: security visibility vs. privacy protection.
- Mitigations include: user notification (login banners), consent mechanisms, and user education.
- NISTIR 8062 is cited as a companion resource for privacy risk identification in network monitoring contexts.
- Biometric attributes used in access evaluations are flagged as a specific privacy concern.

**Confidence:** HIGH. The tension is architecturally inevitable — more inspection means more privacy exposure. NIST acknowledges this explicitly.

**Implication for OSKG-ZeroTrust:** "Inspect everything" is a ZTA tenet, but it creates a privacy-compliance surface that the enterprise must formally manage. This is a tension point, not a resolved tradeoff.

---

### Claim 5: ICAM (FICAM) is the identity substrate on which ZTA rests — an agency cannot "bolt on" ZTA without first achieving mature identity governance, including identity proofing, authentication, and federation per SP 800-63-3.

**Author's claim:** The Policy Engine cannot authorize access without sufficient subject/resource identity information. OMB M-19-17 mandates every federal agency establish an ICAM office to govern identity issuance and management. (§6.3)

**Evidence presented:**
- NIST SP 800-63-3 (Digital Identity Guidelines) provides the technical standards for identity proofing, authentication, and federation that ZTA policy engines consume.
- Key dependency chain: **ICAM maturity → usable subject attributes → functional Policy Engine → ZTA enforcement.**

**Confidence:** VERY HIGH. This dependency is explicit and broadly agreed across all ZT frameworks — CISA, NSA, and DoD all make the same point.

**Implication for OSKG-ZeroTrust:** ICAM is the identity substrate on which ZTA rests. This places identity at the center of the ZT architecture — consistent with the "identity-centric security" concept.

---

### Claim 6: TIC 3.0 is converging with ZTA — TIC evolved from perimeter-based (1.0/2.0) to distributed enforcement (3.0) with PEP Security Capabilities applied at multiple enforcement points, making TIC 3.0 the network-security dimension of ZTA in federal environments.

**Author's claim:** TIC 3.0 recognizes that trust varies by computing context and introduces PEP Security Capabilities applied at distributed enforcement points rather than a single perimeter chokepoint. (§6.4)

**Evidence presented:**
- **TIC 1.0/2.0:** Perimeter-based; assumed internal network is "trusted." Contradicted ZTA's core premise.
- **TIC 3.0:** Introduces Universal Security Capabilities (enterprise-level) and PEP Security Capabilities (applied at multiple distributed PEPs).
- TIC 3.0 security capabilities directly support ZTA: encrypted traffic, strong authentication, microsegmentation, network/system inventory.
- The chapter predicts a future "ZTA TIC use case" will formalize network protections at ZTA enforcement points.

**Confidence:** HIGH. TIC 3.0's distributed PEP model is documented and aligns structurally with ZTA. The convergence is recognized by both NIST and CISA.

**Implication for OSKG-ZeroTrust:** TIC 3.0 is the *network-security dimension* of ZTA in federal environments. Agencies don't choose between TIC and ZTA — they deploy TIC capabilities at ZTA PEPs.

---

### Claim 7: EINSTEIN/NCPS must evolve its perimeter-situational-awareness model to ingest cloud-based telemetry and ZTA-generated data — ZTA improves detection data quality but requires NCPS to adapt its sensor model from perimeter-based to resource-proximate.

**Author's claim:** NCPS (EINSTEIN) delivers intrusion detection, advanced analytics, information sharing, and intrusion prevention for federal networks. Current NCPS sensor placement assumes perimeter defense; ZTA moves protections to the resource level. (§6.5)

**Evidence presented:**
- NCPS must evolve to (a) ingest cloud-based traffic telemetry, (b) receive expanded situational awareness data from ZTA systems, and (c) inform policy enforcement at both legacy NCPS locations and new ZTA PEPs.
- **Upside for incident response:** ZTA generates richer authentication, inspection, and logging data that can improve event impact quantification, feed ML-based detection, and support after-the-fact forensic analysis.

**Confidence:** MEDIUM. The evolution path is logically sound but NIST is describing a desired future state — NCPS adaptation to ZTA was not operationally realized at time of publication.

**Implication for OSKG-ZeroTrust:** NCPS is the legacy detection backbone. ZTA improves detection data quality but requires NCPS to adapt its sensor model. The chapter frames this as evolution, not replacement.

---

### Claim 8: CDM is the visibility prerequisite for ZTA — without CDM's four foundational questions answered (what is connected, who is on the network, what is happening, how is data protected), ZTA cannot evaluate device posture or make informed access decisions.

**Author's claim:** The CDM program answers four foundational questions that ZTA depends on. DHS Hardware Asset Management (HWAM) enables the "first steps" toward ZTA. (§6.6)

**Evidence presented — CDM-to-ZTA dependency mapping:**

| CDM Question | ZTA Dependency |
|---|---|
| **What is connected?** (devices, apps, services) | PEP needs complete asset inventory to evaluate device posture |
| **Who is on the network?** (users, NPEs) | Policy Engine needs subject identity and role attributes |
| **What is happening?** (traffic patterns, messages) | Continuous monitoring and anomaly detection feed dynamic policy |
| **How is data protected?** (at rest, in transit, in use) | Data classification informs access policy and encryption requirements |

- Key dependency chain: **CDM/HWAM → asset visibility → device posture assessment → PEP enforcement.**

**Confidence:** HIGH. The CDM-to-ZTA dependency is explicit and structural — without asset inventory, the "verify explicitly" tenet is undermined because you're verifying against an incomplete picture.

**Implication for OSKG-ZeroTrust:** CDM is the *visibility prerequisite*. Without CDM, a ZTA is blindly enforcing policy on unknown assets — undermining the entire "verify explicitly" tenet.

---

### Claim 9: Cloud Smart and the Federal Data Strategy drive ZTA prioritization — cloud-hosted and remote-accessed resources are the best ZTA candidates because they already operate outside the perimeter model, making cloud migration and ZTA adoption mutually reinforcing.

**Author's claim:** Cloud Smart (successor to Cloud First) and the Data Center Optimization Initiative [M-19-19] require agencies to inventory and assess data collection, storage, and access. This inventory answers: which business processes would benefit most from ZTA? (§6.7)

**Evidence presented:**
- **Best ZTA candidates:** cloud-based applications/services and resources primarily accessed by remote workers — because subjects and resources both sit outside the traditional network perimeter.
- The **Federal Data Strategy** adds a cross-agency dimension: agencies must make data assets accessible to other agencies or the public, mapping to the ZTA "cross-enterprise collaboration" use case (Section 4.4).

**Confidence:** MEDIUM-HIGH. The logic is sound but prioritization criteria are qualitative — NIST doesn't provide a decision framework for selecting among cloud candidates.

**Implication for OSKG-ZeroTrust:** Cloud migration and ZTA adoption are mutually reinforcing. Remote-access and cloud-resident resources are the natural starting point for ZTA implementation — they already operate outside the perimeter model.

---

### Claim 10: The chapter's seven federal program interactions reveal that ZTA is a compliance *complement*, identity and asset visibility are hard prerequisites, TIC 3.0 and CDM are converging with ZTA, ZTA generates better data for existing programs, and privacy is an explicit unresolved tension.

**Author's claim:** This synthesizes the chapter's meta-claims into a single analytical assertion about the federal compliance landscape under ZTA.

**Evidence presented** (from the chapter's key takeaways):

1. **ZTA is a compliance *complement*, not a replacement.** RMF, Privacy Framework, ICAM, TIC, NCPS, CDM, and Cloud Smart all remain in force. ZTA changes where and how their controls are enforced.

2. **Identity and asset visibility are hard prerequisites.** Without mature ICAM (identity) and CDM (asset inventory), ZTA cannot function. These are not optional accelerators — they are foundational dependencies.

3. **The convergence trend is real.** TIC 3.0's distributed PEP model, CDM's continuous monitoring, and Cloud Smart's inventory requirements all push federal IT in directions that align with — and enable — ZTA.

4. **ZTA generates better data for existing programs.** Richer authentication logs, per-session inspection, and continuous device posture assessment improve the detection and response capabilities of NCPS/EINSTEIN and incident response teams.

5. **Privacy is an explicit tension.** "Inspect everything" collides with privacy obligations. Organizations must use the NIST Privacy Framework to formally manage this tension.

**Confidence:** HIGH (as a synthesis of NIST's own framing). The five takeaways are directly supported by the chapter.

---

## Cross-References to Related Guidance

### CISA Zero Trust Maturity Model
The CISA ZT Maturity Model operationalizes many of the interactions described in this chapter. CISA's five pillars (Identity, Device, Network, Application/Workload, Data) map directly to the federal programs discussed here — ICAM maps to the Identity pillar, CDM to Device, TIC 3.0 to Network, and the Federal Data Strategy to Data. The maturity model provides the *progression framework* that this chapter's policy interactions enable.

### NIST SP 800-207A — ZTA for Access Control
SP 800-207A extends the architectural concepts from Chapter 6 by providing technical implementation guidance for the access control components that ICAM policy and CDM asset data feed into. While Chapter 6 addresses *policy alignment*, 800-207A addresses *technical realization* of those policies in the PEP/policy engine access decision flow.

### DoD Zero Trust Strategy
The DoD ZT Strategy translates Chapter 6's federal civilian guidance into the defense context. The DoD strategy inherits the same compliance landscape (RMF, ICAM, CDM equivalents) but adds classification and mission-assurance dimensions that Chapter 6 does not address. The DoD's "Target ZT" and "Advanced ZT" capability levels correspond to maturity progressions that the federal programs in this chapter enable.
