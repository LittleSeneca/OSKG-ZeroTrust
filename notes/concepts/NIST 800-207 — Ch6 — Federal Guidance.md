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
claims_status: extracted
claims_extracted_date: 2026-07-24
claims_count: 10
claims_files:
  - "[[zta-complementary-not-replacement]]"
  - "[[zta-prerequisites-icam-cdm]]"
  - "[[rmf-zta-changes-authorization-boundaries]]"
  - "[[privacy-framework-inspect-everything-tension]]"
  - "[[ficam-identity-substrate-zta]]"
  - "[[tic-3-converging-with-zta]]"
  - "[[einstein-ncps-evolve-perimeter-model]]"
  - "[[cdm-visibility-prerequisite-zta]]"
  - "[[cloud-smart-drives-zta-prioritization]]"
  - "[[federal-program-interactions-synthesis]]"
---

# NIST 800-207 — Chapter 6 — Federal Guidance Interactions

> **Full title:** Zero Trust Architecture and Possible Interactions with Existing Federal Guidance
> **Pages:** 32–36 (in original pagination)

## Overview

Chapter 6 maps how a Zero Trust Architecture (ZTA) adoption intersects with seven existing federal cybersecurity frameworks, policies, and programs. The core message: ZTA does not replace these frameworks — it changes *how* they are implemented. Each framework retains its mandate; ZTA shifts the enforcement model from perimeter-based to resource-proximate.

**Claim 1 —** ZTA is complementary to existing federal frameworks, not a replacement — it changes the locus of enforcement (from perimeter to resource) and the granularity of policy (from network-segment to per-session), but every existing program remains in force. → [[zta-complementary-not-replacement]]

---

**Claim 2 —** ZTA exposes two hard prerequisites in existing programs — mature ICAM (identity) and CDM (asset inventory) — without which ZTA cannot function, because the Policy Engine cannot authorize access without sufficient subject/resource identity information and complete asset visibility. → [[zta-prerequisites-icam-cdm]]

---

**Claim 3 —** RMF — ZTA changes authorization boundaries but not the RMF process itself; risk acceptance decisions become per-resource and per-session, encoded algorithmically in the Policy Engine rather than assessed per-network-zone. → [[rmf-zta-changes-authorization-boundaries]]

---

**Claim 4 —** Privacy Framework — ZTA's "inspect everything" tenet creates an explicit tension with privacy obligations; traffic inspection and metadata logging may capture PII, requiring formal privacy risk management via the NIST Privacy Framework [NISTPRIV]. → [[privacy-framework-inspect-everything-tension]]

---

**Claim 5 —** ICAM (FICAM) is the identity substrate on which ZTA rests — an agency cannot "bolt on" ZTA without first achieving mature identity governance, including identity proofing, authentication, and federation per SP 800-63-3. → [[ficam-identity-substrate-zta]]

---

**Claim 6 —** TIC 3.0 is converging with ZTA — TIC evolved from perimeter-based (1.0/2.0) to distributed enforcement (3.0) with PEP Security Capabilities applied at multiple enforcement points, making TIC 3.0 the network-security dimension of ZTA in federal environments. → [[tic-3-converging-with-zta]]

---

**Claim 7 —** EINSTEIN/NCPS must evolve its perimeter-situational-awareness model to ingest cloud-based telemetry and ZTA-generated data — ZTA improves detection data quality but requires NCPS to adapt its sensor model from perimeter-based to resource-proximate. → [[einstein-ncps-evolve-perimeter-model]]

---

**Claim 8 —** CDM is the visibility prerequisite for ZTA — without CDM's four foundational questions answered (what is connected, who is on the network, what is happening, how is data protected), ZTA cannot evaluate device posture or make informed access decisions. → [[cdm-visibility-prerequisite-zta]]

---

**Claim 9 —** Cloud Smart and the Federal Data Strategy drive ZTA prioritization — cloud-hosted and remote-accessed resources are the best ZTA candidates because they already operate outside the perimeter model, making cloud migration and ZTA adoption mutually reinforcing. → [[cloud-smart-drives-zta-prioritization]]

---

**Claim 10 —** The chapter's seven federal program interactions reveal that ZTA is a compliance *complement*, identity and asset visibility are hard prerequisites, TIC 3.0 and CDM are converging with ZTA, ZTA generates better data for existing programs, and privacy is an explicit unresolved tension. → [[federal-program-interactions-synthesis]]

---

## Cross-References to Related Guidance

### CISA Zero Trust Maturity Model
The CISA ZT Maturity Model operationalizes many of the interactions described in this chapter. CISA's five pillars (Identity, Device, Network, Application/Workload, Data) map directly to the federal programs discussed here — ICAM maps to the Identity pillar, CDM to Device, TIC 3.0 to Network, and the Federal Data Strategy to Data. The maturity model provides the *progression framework* that this chapter's policy interactions enable.

### NIST SP 800-207A — ZTA for Access Control
SP 800-207A extends the architectural concepts from Chapter 6 by providing technical implementation guidance for the access control components that ICAM policy and CDM asset data feed into. While Chapter 6 addresses *policy alignment*, 800-207A addresses *technical realization* of those policies in the PEP/policy engine access decision flow.

### DoD Zero Trust Strategy
The DoD ZT Strategy translates Chapter 6's federal civilian guidance into the defense context. The DoD strategy inherits the same compliance landscape (RMF, ICAM, CDM equivalents) but adds classification and mission-assurance dimensions that Chapter 6 does not address. The DoD's "Target ZT" and "Advanced ZT" capability levels correspond to maturity progressions that the federal programs in this chapter enable.
