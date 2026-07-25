---
tags:
  - source/books
  - green-ortiz
  - zt-implementation
  - zt-segmentation
  - zt-access
  - oskg-zerotrust
created: 2026-07-24
confidence: high
source:
  title: "Zero Trust Architecture: Networking Technology Security"
  authors: "Cindy Green-Ortiz, Brandon Fowler, David Houck, Hank Hensel, Patrick Lloyd, Andrew McDonald, Jason Frazier"
  year: 2024
  publisher: "Cisco Press"
  local_file: "sources/books/_txt/Zero_Trust_Architecture_Networking_Technology_Security.txt"
  chapter_lines: "5901–9034"
related:
  - "[[Garbis and Chapman — Network and Access Technologies]]"
  - "[[Gilman and Barth — Ch7-8 — Applications and Traffic]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
  - "[[Concepts Index]]"
claims_status: extracted
claims_extracted: 2026-07-24
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-identity
---

# Green-Ortiz — Ch6–8: Implementation Patterns

The three implementation chapters of Green-Ortiz et al.'s Cisco-centric Zero Trust book. Chapter 6 defines segmentation models and technologies; Chapter 7 enumerates the common challenges organizations face in practice, with concrete solutions for each; Chapter 8 provides the planning and deployment frameworks for turning analysis into action. Together they form a complete implementation methodology — the "how" of ZT networking — with a distinctive emphasis on **layered enforcement** and **contextual identity** as the engine of segmentation policy.

---

## Ch6: Segmentation — Models, Technologies, and Methodology

**Claim 1 —** True ZT segmentation requires enforcement at every OSI layer — layering is not optional but the ideal-world answer, pushing back against the firewall-centric mindset that considers one enforcement point sufficient. → [[true-zt-segmentation-requires-enforcement-at-every-osi]]

**Claim 2 —** East-west segmentation — controlling traffic within the same VLAN/subnet — is the harder problem that most distinguishes ZT from traditional perimeter security, requiring Layer 2 identity-based enforcement that doesn't depend on routing. → [[east-west-segmentation-controlling-traffic-within-the-same-vlansubnet]]

**Claim 3 —** The five-pillar methodology for segmentation operationalizes ZT by making contextual identity the engine of policy — but organizations must start with 5–7 broad enclaves and refine iteratively, treating segmentation as "eating an elephant — one small step at a time." → [[the-five-pillar-methodology-for-segmentation-operationalizes-zt-by]]

---

## Ch7: Common Challenges and Practical Solutions

**Claim 4 —** True contextual identity is never just a device type — a displayless hardware phone used after hours by Facilities has a fundamentally different identity than a director's hardware phone at home during business hours, and this multi-dimensional profiling is the foundation of all ZT enforcement. → [[true-contextual-identity-is-never-just-a-device]]

**Claim 5 —** The firewall-is-enough belief is mathematically disproven — a network with 2,046 VLANs passing through a firewall requires a minimum of 12,000 initial rules just for shared services, not counting business-specific rules. → [[the-firewall-is-enough-belief-is-mathematically-disproven-a-network]]

**Claim 6 —** External access for IoT/endpoints requires baseline creation through multiple collection points — edge firewall logs, Internet proxy logs, NetFlow, endpoint agents, and DNS analytics — because vendor documentation of network interactions is unreliable. → [[external-access-for-iotendpoints-requires-baseline-creation-through]]

**Claim 7 —** New endpoint onboarding ("Day 2 Operations") requires a centralized receiving process — a secured, isolated network segment with lenient NAC policy, separate Internet access, and full NetFlow collection, followed by a structured onboarding checklist. → [[new-endpoint-onboarding-day-2-operations-requires-a]]

---

## Ch8: Developing a Successful Segmentation Plan

**Claim 8 —** Top-down (business-aligned) and bottom-up (traffic-aligned) design approaches are complementary, not competing — use top-down for high-level architecture and bottom-up for validation and detailed policy creation. → [[top-down-business-aligned-and-bottom-up-traffic-aligned-design-approaches-are]]

**Claim 9 —** The policy decision matrix — mapping source entities to destination entities with per-cell permit/deny, port/protocol, and directionality — is the output artifact of ZT planning, and multiple matrices will be needed across intra-data center, inter-site, and per-business-unit contexts. → [[the-policy-decision-matrix-mapping-source-entities-to]]

---

## Synthesis: The Green-Ortiz Implementation Model

The three chapters together define a coherent implementation methodology:

```
Contextual Identity → Traffic Baseline → Vulnerability Assessment → Layered Enforcement → Monitoring/Refinement
       ↑                                                                                          ↓
       └──────────────────────────── Continuous feedback loop ─────────────────────────────────────┘
```

**Distinctive positions in the ZT literature:**

1. **Layered is the only correct answer.** Where Garbis & Chapman define deployment models and Gilman & Barth describe architectural primitives, Green-Ortiz insists that all enforcement mechanisms must be used simultaneously — VLAN, ACL, SGT, firewall, application control. No single technology is sufficient.

2. **East-west is the hard problem that defines ZT.** The authors' emphasis on intra-VLAN control (TrustSec, private VLANs, host-based firewalls) is more detailed than any other source. The recognition that most organizations have no mechanism to control peer-to-peer traffic within a VLAN is the book's sharpest diagnostic insight.

3. **Contextual identity drives everything.** The five-fold identity model (who/what/where/when/how) is not just an authentication concept — it is the engine of segmentation policy, traffic baseline creation, vulnerability assessment, and enforcement. Identity is the common thread connecting every ZT pillar.

4. **Start with 5–7 enclaves and refine.** The empirically grounded recommendation (from Cisco's services and business group experience) provides a concrete starting point that other ZT frameworks leave abstract. The warning against over-granular SGT taxonomies is a valuable corrective to the "microsegment everything" impulse.

5. **The firewall is not dead — it's been reassigned.** The authors preserve the firewall for advanced features (IPS, malware detection, DLP, VPN termination) while stripping it of its role as the sole enforcement point. This is more pragmatic than the "firewalls are obsolete" position and more ZT-aligned than the "firewalls are enough" position.

**Comparison with related sources:**

- **vs. NIST 800-207 Ch4 (Deployment Scenarios):** NIST describes five abstract scenarios (satellite, multi-cloud, contracted services, cross-enterprise, public-facing). Green-Ortiz provides deployment templates (site-based, endpoint-category, service-type) that map to specific organizational structures. NIST says *what* the scenarios are; Green-Ortiz says *how to plan for them*.

- **vs. Gilman & Barth Ch9 (Realizing a ZT Network):** Gilman & Barth's implementation chapter is requirements-driven (MUST/SHOULD prioritized list, flow enumeration, controller-less architecture). Green-Ortiz's is methodology-driven (top-down vs. bottom-up, the five-pillar process, deployment templates). The two are complementary: Gilman & Barth for the network engineer building the control plane; Green-Ortiz for the security architect planning the enterprise rollout.

- **vs. Garbis & Chapman (Network and Access Technologies):** Garbis & Chapman evaluate existing technologies against ZT principles (Replace/Persist/Adapt verdicts). Green-Ortiz provides the Cisco-specific implementation of those technologies. The Garbis & Chapman note asks "does this technology fit ZT?" The Green-Ortiz chapters answer "here's exactly how to deploy it."

**Open questions:**
- How much of the methodology is tied to Cisco's product ecosystem (ISE, TrustSec, Secure Network Analytics, Secure Workload) vs. generalizable principles? The concepts (contextual identity, layered enforcement, blast zone analysis) are vendor-neutral; the specific protocol implementations (SGT in CMD field, PXGrid, downloadable ACLs via RADIUS) are Cisco-specific.
- The "5–7 enclaves" starting point is Cisco's empirical finding — does it generalize across industries and network sizes?
- The chapter's treatment of application-level ZT is thin compared to its depth on network segmentation — is this because the book is network-focused, or because application-level ZT is genuinely less mature?

**Strongest sections:**
- Ch6's layered enforcement model (VLAN → Firewall → dACL → TrustSec) — the book's most prescriptive and actionable framework
- Ch7's contextual identity profiling methodology — the most detailed practical guide to device identification in the ZT literature
- Ch8's top-down vs. bottom-up planning framework — resolves the "where do we start?" question that paralyzes most organizations

**Weakest sections:**
- Ch6's OSI model review is a CCNA-level primer that advanced readers will skim
- Ch7's external communication mapping tools section (Taps, NetFlow, ERSPAN) is a catalog with limited synthesis
- Ch8's deployment templates are healthcare-heavy and may not resonate with other verticals
