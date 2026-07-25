---
tags:
  - source/standards
  - nist
  - zt-architecture
  - policy-engine
  - pep
  - microsegmentation
  - sdp
  - oskg-zerotrust
  - concepts
  - reading-notes
created: 2026-07-24
confidence: high
source:
  title: "NIST SP 800-207 — Zero Trust Architecture"
  author: "Scott Rose et al., NIST"
  year: 2020
  publisher: "National Institute of Standards and Technology"
  local_file: "sources/standards/_txt/NIST_SP_800-207_Zero_Trust_Architecture.txt"
  section: "Chapter 3 — Logical Components of Zero Trust Architecture"
  lines: 706–1289
related:
  - "[[Concepts Index]]"
  - "[[NIST 800-207 — Ch1-2 — Introduction and Tenets]]"
  - "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
  - "[[CISA Zero Trust Maturity Model]]"
  - "[[DoD ZT Reference Architecture v2]]"
  - "[[Gilman & Barth — Control Plane and Data Plane]]"
claims_status: extracted
claims_extracted_date: 2026-07-24
claims_count: 8
claims_files:
  - "[[zta-three-core-components-pe-pa-pep]]"
  - "[[eight-data-sources-feed-policy-engine]]"
  - "[[three-zta-approaches-identity-microseg-sdp]]"
  - "[[four-deployment-models-zta]]"
  - "[[trust-algorithm-five-input-categories]]"
  - "[[trust-algorithm-two-axes-criteria-contextual]]"
  - "[[nist-control-data-plane-separation]]"
  - "[[ten-network-requirements-zta]]"
  - topic/zt-architecture
  - topic/zt-network
  - topic/zt-implementation
---

# NIST SP 800-207 — Chapter 3: Logical Components

> **Significance:** This is the single most important architectural chapter in the Zero Trust canon. It defines the canonical ZTA component model — Policy Engine (PE), Policy Administrator (PA), Policy Enforcement Point (PEP) — that every subsequent standard, reference architecture, and vendor framework either adopts or maps to. The chapter also introduces the control plane / data plane separation, the trust algorithm concept, and the three ZTA approach variations (identity governance, micro-segmentation, SDP) and four deployment models. No other 24-page section of government prose carries more architectural weight in cybersecurity.

---

## 3.0 — Core Logical Components

**Claim 1 —** ZTA has three core decision-making components (PE, PA, PEP) → [[zta-three-core-components-pe-pa-pep]]

**Claim 2 —** Eight data sources feed the Policy Engine's access decisions → [[eight-data-sources-feed-policy-engine]]

---

## 3.1 — Variations of Zero Trust Architecture Approaches

**Claim 3 —** Three ZTA approaches exist — identity governance, micro-segmentation, and SDP → [[three-zta-approaches-identity-microseg-sdp]]

---

## 3.2 — Deployed Variations of the Abstract Architecture

**Claim 4 —** Four deployment models operationalize the logical architecture → [[four-deployment-models-zta]]

---

## 3.3 — Trust Algorithm

**Claim 5 —** The Trust Algorithm is the PE's decision-making process with five input categories → [[trust-algorithm-five-input-categories]]

**Claim 6 —** Trust algorithms vary on two axes — criteria/score-based and singular/contextual → [[trust-algorithm-two-axes-criteria-contextual]]

---

## 3.4 — Network/Environment Components

**Claim 7 —** Control plane and data plane must be logically separated → [[nist-control-data-plane-separation]]

**Claim 8 —** Ten network requirements support ZTA → [[ten-network-requirements-zta]]

---

## Chapter-Level Assessment

### What Holds Up Strongest

1. **PE/PA/PEP tripartite model.** Five years of implementation have validated this as the right abstraction level — not too granular, not too coarse.
2. **Control plane / data plane separation.** The clearest architectural differentiator between ZTA and traditional perimeter models.
3. **Trust algorithm input taxonomy.** Five categories (access request, subject, asset, resource requirements, threat intelligence) provide a durable evaluation framework.
4. **Deployment model diversity.** The four models accurately reflect real-world patterns without constraining implementation.

### What Is Most Vulnerable

1. **Contextual trust algorithms.** The "ideally contextual" aspiration understates the operational burden. The tuning phase can be indefinite, and many organizations achieve adequate security with criteria-based TAs plus strong authentication.
2. **Data source integration.** NIST assumes data sources are available and integrated. The CISA Maturity Model is more honest about how far most organizations are from this ideal.
3. **Application sandboxing as a standalone model.** This is better understood as a defense-in-depth complement, not a primary ZTA deployment pattern.

### The Single Biggest Gap

**NIST 800-207 Chapter 3 defines the WHAT (components, approaches, models) but not the HOW (interfaces, protocols, APIs).** The DoD ZT Reference Architecture and CISA Maturity Model fill this gap partially, but neither provides an interface specification between PE, PA, and PEP. This is the largest unaddressed standardization gap in ZTA — and the primary reason vendor implementations are not interoperable.

### Cross-Standard Architecture Alignment

| Concept | NIST 800-207 Ch.3 | CISA Maturity Model | DoD ZT RA v2 |
|---|---|---|---|
| Decision components | PE, PA, PEP | Implicit in all pillars | Policy Decision Point, Policy Enforcement Point |
| Control/data plane | Section 3.4 | Network pillar | Universal Control Plane |
| Identity approach | Section 3.1.1 | Identity pillar (foundational) | ICAM + ABAC |
| Micro-segmentation | Section 3.1.2 | Network pillar (maturity levels) | Network Environment pillar |
| SDP/ZTNA | Section 3.1.3 | Implicit in Network pillar | Capability 2.3 (Remote Access) |
| Trust algorithm | Section 3.3 | Cross-cutting "automation and orchestration" | Dynamic risk-based access (Capability 5.1) |
| Deployment models | Section 3.2 (4 models) | Not explicitly modeled | Reference designs (7 architectures) |

### Existential Threat to the Chapter's Authority

If any other standards body were to define a fundamentally incompatible ZT component model (e.g., merging PE/PA/PEP into a single component, or splitting control plane into three separate planes), NIST 800-207 Chapter 3's canonical status would weaken. This has not happened. The chapter's authority grows with each standard that adopts its model rather than competing with it.

---

## Inline Cross-References

- **[[CISA Zero Trust Maturity Model]]** — Operationalizes the five pillars (Identity, Device, Network, Application/Workload, Data) that map to NIST's data sources and approaches. See especially the Network pillar for micro-segmentation and SDP maturity progression.
- **[[DoD ZT Reference Architecture v2]]** — Adopts the PE/PA/PEP model and provides seven reference designs. Adds mission-criticality and operational tempo as trust-algorithm inputs. Operationalizes the "VPN replacement" requirement (Requirement 8) through Capability 2.3.
- **[[Gilman & Barth — Control Plane and Data Plane]]** — The foundational text (2017, "Zero Trust Networks") that NIST explicitly cites for control plane / data plane separation. Provides practical implementation guidance that NIST 800-207 deliberately omits, including control plane availability, latency considerations, and the PA/PE as single point of failure.
- **[[NIST 800-207 — Ch1-2 — Introduction and Tenets]]** — The ZT definition and seven tenets that Chapter 3's architecture implements.
- **[[NIST 800-207 — Ch4 — Deployment Scenarios]]** — Practical use cases that exercise the architecture defined in Chapter 3.

---

*Notes prepared for the OSKG-ZeroTrust knowledge graph. This chapter will generate approximately 15–20 claim nodes during Phase 2 extraction. See [[Concepts Index]] for related concept notes and [[METHODOLOGY]] for the claim format specification.*
