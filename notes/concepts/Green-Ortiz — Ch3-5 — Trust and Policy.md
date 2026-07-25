---
tags:
  - source/books
  - green-ortiz
  - zt-trust
  - zt-policy
  - trust-engine
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
claims_status: extracted
claims_extracted: 2026-07-24
confidence: high
source:
  title: "Zero Trust Architecture: Theory, Implementation, Maintenance, and Growth"
  authors: "Cindy Green-Ortiz, Brandon Fowler, David Houck"
  year: 2024
  publisher: "Cisco Press"
  local_file: "sources/books/_txt/Zero_Trust_Architecture_Networking_Technology_Security.txt"
  chapters: "3-5"
  line_range: "3743-5901"
related:
  - "[[Gilman and Barth — Ch2 — Managing Trust]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[Garbis and Chapman — Practice IAM Policy]]"
  - "[[Books Index]]"
  - "[[Concepts Index]]"
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-definition
---

# Green-Ortiz et al. — Ch3-5: Trust Assessment and Policy

Ch3-5 of Green-Ortiz et al. form the trust computation and policy engine section of the book. Ch3 defines the spatial architecture — where enforcement happens and what level of trust assessment each location requires. Ch4 defines enclave design — what gets grouped together and what trust criteria justify the grouping. Ch5 operationalizes the policy development lifecycle — how trust data is collected, how policy is built from it, how it's tested, and how it survives organizational change. Together they answer: *how do you assess trust, and how do you convert that assessment into enforceable policy across an enterprise network?*

**Claim 1 —** Trust assessment is spatial — the architecture location determines trust data availability and granularity → [[trust-assessment-is-spatial-the-architecture-location-determines]]

---

**Claim 2 —** Enclave design is trust classification — what criteria justify grouping and what criteria justify access between groups → [[enclave-design-is-trust-classification-what-criteria-justify]]

---

**Claim 3 —** Trust assessment is multi-layered — identity, posture, and behavior combine to produce an enforcement decision → [[trust-assessment-is-multi-layered-identity-posture-and-behavior]]

---

**Claim 4 —** Policy creation is data-driven — discovery before enforcement, log before block → [[policy-creation-is-data-driven-discovery-before-enforcement-log]]

---

**Claim 5 —** Policy survives organizational change through the Policy & Governance pillar — but mergers, acquisitions, and shadow IT constantly challenge it → [[policy-survives-organizational-change-through-the-policy-governance]]

---

**Claim 6 —** Automation bridges the gap between trust assessment and enforcement at scale — continuous, not occasional, evaluation → [[automation-bridges-the-gap-between-trust-assessment-and]]

---

## Chapter 3-5 Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| Trust assessment is spatial — location determines signals | HIGH | Cloud-native/agent-only models claiming location is irrelevant |
| Enclave design is trust classification | HIGH | Fully identity-based enforcement making enclave design unnecessary |
| Trust assessment is multi-layered (identity + posture + behavior) | MEDIUM | Lack of computational model for combining signals |
| Policy creation is data-driven (discover → log → enforce) | HIGH | Scalability questions at very large enterprises |
| Policy survives through governance — mergers and shadow IT | MODERATE | Thin governance prescription; aspiration vs. reality gap |
| Automation bridges assessment and enforcement at scale | HIGH (principle), MODERATE (specificity) | Vendor-specific implementation guidance |

**Strongest section:** The data-driven policy creation pipeline (Claim 4) — the NAC → DNS → IPAM → endpoint database → classification → policy procedure. It's the most detailed operational prescription in ZT literature for building policy from observed network behavior, and it bridges the gap between "monitor first" (everyone agrees) and "here's exactly how" (nobody else provides).

**Weakest section:** The governance discussion (Claim 5). Identifying mergers and shadow IT as threats to policy integrity is correct and important, but the governance mechanisms are underdeveloped — templates and checklists rather than tested operational patterns. This is a gap across the entire ZT literature, not unique to Green-Ortiz.

**What's missing from Ch3-5:**
1. **No trust scoring algorithm.** Unlike Gilman & Barth (Ch2), Green-Ortiz never defines a computational model for combining identity, posture, and behavior into a trust score. Trust is assessed through multiple dimensions but never reduced to a single value. This is a design choice, not a gap — but it means Green-Ortiz's model is harder to compare quantitatively with other ZT implementations.
2. **No explicit control-plane/data-plane separation.** The NIST 800-207 and Gilman & Barth models both distinguish the policy decision point from the policy enforcement point. Green-Ortiz collapses this distinction into the five-pillar model, which is comprehensive but loses the architectural clarity of the split-plane model.
3. **No treatment of trust decay or renewal.** Gilman & Barth's "trust is temporary" principle (leased tokens, short-lived credentials) is absent from Green-Ortiz's treatment. The five-pillar model implies continuous reassessment but doesn't specify temporal properties of trust decisions.
4. **Cisco-specific implementation bias.** RADIUS, TrustSec, Cisco ISE, Cisco SD-WAN, and Cisco Secure Network Analytics are the implementing technologies. The principles are vendor-neutral, but the implementation path is Cisco-prescribed. Organizations using non-Cisco infrastructure will need to map the principles to their own tools.

**Unique contribution to OSKG-ZeroTrust:** Green-Ortiz Ch3-5 provides the operational layer that NIST 800-207 (architectural principles) and Gilman & Barth (computational model) both lack. NIST says "collect identity, device, and environmental data for policy decisions." Gilman & Barth say "compute a trust score from continuously monitored attributes." Green-Ortiz says "here's where the data comes from at each architecture location, here's how to design enclaves that group assets by trust criteria, here's the data pipeline that converts discovery into policy, and here's how to keep it all working through mergers and shadow IT." It's the most operational treatment of trust assessment and policy in the ZT literature — less elegant than Gilman & Barth, but more directly implementable in a brownfield enterprise.

**Cross-references:**
- **NIST 800-207 Ch3:** The PDP/PEP model is the abstract architecture. Green-Ortiz Ch3-5 is the concrete deployment guide for the same pattern. The five pillars (Policy & Governance, Identity, Vulnerability Management, Enforcement, Analytics) map roughly to NIST's data sources (ID management, device security, asset management, etc.).
- **Gilman & Barth Ch2:** The variable trust score model and the trust engine are the computational equivalents of Green-Ortiz's multi-dimensional assessment. Gilman & Barth provide the algorithm; Green-Ortiz provides the data pipeline and the spatial deployment model.
- **Garbis & Chapman Ch4-5:** The IAM + policy model in Garbis & Chapman (Subject Criteria → Action → Target + Condition, with four-component triggers) is the policy evaluation engine that would consume Green-Ortiz's trust data. The two books are complementary: Green-Ortiz tells you how to gather trust data and build policy; Garbis & Chapman tell you how to structure and evaluate policy rules.
