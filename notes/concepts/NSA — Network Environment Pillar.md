---
tags:
  - source/standards
  - nsa
  - zt-network
  - segmentation
  - sdn
  - lateral-movement
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
claims_status: extracted
claims_extracted: 2026-07-24
confidence: high
source:
  title: "Advancing Zero Trust Maturity Throughout the Network and Environment Pillar"
  authors: "National Security Agency"
  year: 2024
  publisher: "NSA"
  report_no: "U/OO/125052-24 | PP-24-0689"
  version: "1.0"
  date: "MAR 2024"
  local_file: "sources/standards/_txt/NSA_ZT_Network_Environment_Pillar.txt"
  pages: 12
related:
  - "[[Concepts Index]]"
  - "[[NSA — Embracing a Zero Trust Security Model]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[CISA ZTMM — Device Network App Data Pillars]]"
  - "[[CISA ZTMM — Identity Pillar]]"
  - "[[NSA ZT User Pillar]]"
  - "[[NSA ZT Device Pillar]]"
---

# NSA — Network and Environment Pillar

> **Significance:** This is the NSA's definitive guidance on the network dimension of Zero Trust. Published March 2024, it provides the most operationally detailed treatment of network segmentation for lateral movement prevention in the federal ZT canon — more tactical than CISA's maturity model, more network-specific than NIST 800-207's architectural abstractions. The document is built around four capabilities (data flow mapping, macro segmentation, micro segmentation, software-defined networking), each with a four-phase maturity model (Preparation → Basic → Intermediate → Advanced).

---

**Claim 1 —** Lateral movement prevention is the pillar's *raison d'être* → [[lateral-movement-prevention-raison-detre]]
---

**Claim 2 —** Data flow mapping is the foundational capability — you can't segment what you don't understand → [[data-flow-mapping-foundational-capability]]
---

**Claim 3 —** Macro segmentation prevents lateral movement between business functions → [[macro-segmentation-cross-function]]
---

**Claim 4 —** Micro segmentation limits blast radius within segments — it's the granular layer → [[micro-segmentation-blast-radius]]
---

**Claim 5 —** SDN is the enabling technology that makes micro segmentation manageable at scale → [[sdn-enables-scalable-micro-segmentation]]
---

**Claim 6 —** The four capabilities form an integrated, sequential maturity journey → [[sequential-network-maturity-journey]]
---

## Cross-Framework Alignment

| NSA Capability | CISA ZTMM Network Pillar (§5.3) | NIST 800-207 Ch.3 |
|---|---|---|
| Data Flow Mapping | Embedded in Network Segmentation function + cross-cutting Visibility & Analytics | Implicit in data source inventory (§3.0, data sources #4, #8) |
| Macro Segmentation | Network Segmentation function: Traditional (large perimeter/macro) → Initial (critical workload isolation) → Advanced (micro-perimeters) → Optimal (fully distributed) | Enclave-Based deployment model (§3.2.2) |
| Micro Segmentation | Network Segmentation function: endpoint/application isolation, ingress/egress micro-perimeters, service-specific interconnections | Micro-Segmentation ZTA approach (§3.1.2): "individual resources or resource groups on unique network segments protected by gateway devices" |
| SDN | Implicit in "dynamic just-in-time and just-enough connectivity" at Optimal level | SDP approach (§3.1.3): "overlay networks with PA acting as network controller" |
| Lateral Movement Testing | Not explicitly modeled | Not explicitly modeled |

**Key structural difference:** NSA's model has four maturity phases (Preparation → Basic → Intermediate → Advanced). CISA's model has four maturity levels (Traditional → Initial → Advanced → Optimal). They align substantively but use different labels:

| NSA Phase | CISA Level | Characteristic |
|-----------|-----------|---------------|
| Preparation | Traditional | Manual, static, perimeter-focused |
| Basic | Initial | Automation begins, formal policies, initial segmentation |
| Intermediate | Advanced | Enterprise-wide, dynamic policies, service-specific interconnections |
| Advanced | Optimal | Fully automated, continuous, risk-adaptive, centrally managed |

**NSA's unique contributions relative to CISA and NIST:**
1. **Adversarial testing of segmentation** — the Advanced SDN requirement to "test which network paths would allow lateral movement" has no equivalent in CISA or NIST.
2. **SDN controller security** — the detailed SDNC hardening guidance (separate API admin roles, mutual authentication, encrypted API calls) is NSA-specific.
3. **Recurring case study** — the Target breach as a pedagogical anchor across multiple capability sections.
4. **Encryption discovery during data flow mapping** — identifying and remediating unencrypted flows as a prerequisite to segmentation.

---

## Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| Lateral movement as pillar's primary purpose | HIGH | Depends on assumption that lateral movement is the threat — perimeter-focused organizations may disagree |
| Data flow mapping as foundational | HIGH | Organizations may attempt to skip this step, but the evidence of failure when they do is strong |
| Macro segmentation prevents cross-function lateral movement | HIGH | Undisputed; the challenge is implementation completeness, not conceptual validity |
| Micro segmentation limits intra-function blast radius | HIGH | Operational cost without SDN; the "test and refine" acknowledgment is honest |
| SDN enables scalable micro segmentation | HIGH (capability), MEDIUM (necessity) | SDNC as single point of compromise; host-based alternatives not discussed |
| Sequential capability maturity | HIGH (logical), MEDIUM (practical) | Real-world implementations rarely follow a strict sequence |

**Strongest sections:** The maturity tables for each capability — they are the most operationally actionable content in the federal ZT network guidance corpus. The Target breach as a recurring case study effectively grounds abstract segmentation concepts in a concrete failure.

**Weakest section:** The SDN treatment assumes SDN as the primary path to micro segmentation at scale and does not discuss host-based micro segmentation (agent-based isolation) as an alternative. This may reflect NSA's bias toward network infrastructure controls (consistent with their institutional focus) rather than a comprehensive evaluation of alternatives.

**Biggest gap:** The document does not address how the network pillar's controls interact with cloud-native environments where the organization doesn't control the underlying network infrastructure. The assumption throughout is an enterprise-owned network — a reasonable scope limitation given the NSS/DoD/DIB audience, but a gap for organizations with significant cloud workloads.

**Historical significance:** Published March 2024, this is one of the most recent NSA ZT pillar guidance documents and represents the current state of the NSA's Zero Trust maturity framework. It complements the 2021 "Embracing a Zero Trust Security Model" foundational document with pillar-specific implementation guidance. Together with the CISA ZTMM v2 (April 2023) and NIST 800-207 (2020), it completes the federal ZT network guidance triad.

---

## Inline Cross-References

- **[[CISA ZTMM — Device Network App Data Pillars]]** — §2 (Network/Environment Pillar) for the CISA maturity levels that NSA's phases map to. See especially the Network Segmentation, Network Traffic Management, and Traffic Encryption functions.
- **[[NIST 800-207 — Ch3 — Logical Components]]** — §§3.1.2–3.1.3 for micro-segmentation and SDP approaches; §3.2 for deployment models; §3.4 for control plane / data plane separation.
- **[[NSA — Embracing a Zero Trust Security Model]]** — The foundational NSA ZT document (2021) that established the threat-centric "assume breach" framing and the preparation → basic → intermediate → advanced maturity structure that this pillar guidance follows.
- **[[Concepts Index]]** — Concept-level entries for microsegmentation, lateral movement prevention, SDP, and ZTNA.

---

*Notes prepared for the OSKG-ZeroTrust knowledge graph. This note will generate approximately 12–16 claim nodes during Phase 2 extraction. See [[Concepts Index]] for related concept notes.*
