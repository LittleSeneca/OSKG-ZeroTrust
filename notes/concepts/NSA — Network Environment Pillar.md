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

## Claim 1: Lateral movement prevention is the pillar's *raison d'être*

**NSA's claim:** "The Zero Trust network and environment pillar curtails adversarial lateral movement by employing controls and capabilities to logically and physically segment, isolate, and control access (on-premises and off-premises) through granular policy restrictions." The pillar works in concert with the other ZT pillars as part of a holistic model that "assumes adversary breaches occur inside the network, and so limits, verifies, and monitors activities throughout the network."

**Evidence presented:** The document opens with the 2013 Target breach as its central case study — HVAC vendor credentials used to pivot from an HVAC network segment to point-of-sale systems, compromising 40 million payment cards. The NSA uses this as a recurring anchor: macro segmentation appears as the preventive control ($5 of "could have prevented this"), and micro segmentation appears as the blast-radius limiter ($8 of "might have limited the impact"). This is a deliberate rhetorical structure — the problem statement (lateral movement) → a real-world failure → the solution (segmentation at multiple layers).

**Confidence:** HIGH. This framing is consistent across NSA publications and reflects the agency's threat-informed approach. Lateral movement is the attack phase that ZT network controls are uniquely positioned to stop — identity controls prevent initial access, device controls prevent endpoint compromise, but it's network segmentation that prevents the pivot from initial foothold to critical assets.

**What's at stake:** If lateral movement isn't the primary threat, then the network pillar's emphasis on segmentation is overengineered relative to other controls. If lateral movement IS the primary threat (as incident response data consistently shows), then segmentation is the single most important network control in ZT.

**Cross-reference to NIST 800-207:** NIST frames micro-segmentation as one of three ZTA approaches (§3.1.2), with the key observation that "stateless firewalls are a very poor choice" for PEPs due to administration cost and slow adaptation. NSA's maturity model operationalizes this: Intermediate-level macro segmentation demands "access policies restricting lateral movement between segments are defined and written into firewall rules based on security policies." The NSA and NIST framings are complementary — NIST provides the architectural rationale, NSA provides the implementation roadmap.

**My assessment:** The Target breach is now 11 years old, and it's telling that NSA still leads with it. Either network segmentation has not improved enough in a decade to retire the case study, or it's simply the best-documented example of segmentation failure at scale. Both are plausible, and both support NSA's core argument.

---

## Claim 2: Data flow mapping is the foundational capability — you can't segment what you don't understand

**NSA's claim:** "Data flow mapping identifies the route data travels within an organization and describes how that data transforms from one location or application to another." It is "foundational for other network activities, such as macro and micro segmentation," and "aids in efficiently identifying anomalous traffic behavior via analytics."

**Evidence presented:** Four-phase maturity progression:

| Phase | Capability |
|-------|-----------|
| **Preparation** | Identify locations where data is stored and processed, and in which state the data components are stored. |
| **Basic** | Begin mapping physical and logical data flows. Mapping is primarily manual. Transition unencrypted flows to encrypted flows or within encrypted tunnels/protocols. |
| **Intermediate** | Complete list of applications; critical data flows identified. Some automation maintains mapping accuracy. Anomalous data flows isolated or eliminated. |
| **Advanced** | Complete inventory of all data flows. Automation monitors for controls and mitigates all current, new, or anomalous data flows. |

**Confidence:** HIGH. This claim is logically sound and practically validated — data flow mapping is a prerequisite for any network segmentation effort. The maturity model correctly identifies the manual-to-automated trajectory and the critical Intermediate milestone of identifying anomalous flows.

**What's at stake:** If data flow mapping is incomplete, segmentation boundaries will be wrong — either too permissive (leaving lateral movement paths open) or too restrictive (breaking legitimate workflows). The NSA's emphasis on encryption discovery during mapping is particularly important: flows that aren't encrypted in transit represent a compounding risk (data exposed + lateral movement path available).

**Cross-reference to CISA:** CISA's Network pillar does not explicitly separate "data flow mapping" as a standalone function — it's embedded within the Network Segmentation function's maturity progression. NSA's treatment is more granular. CISA's cross-cutting Visibility & Analytics capability covers the monitoring dimension that NSA ties directly to data flow mapping: at the Optimal level, CISA calls for "visibility into communication across all agency networks and environments."

**My assessment:** This is the most underappreciated capability in the document. Every organization that has attempted network segmentation has discovered that their data flow documentation is incomplete — and that discovering actual flows (vs. documented flows) reveals shadow IT, legacy interconnections, and forgotten VPN tunnels. NSA's placement of data flow mapping as Capability #1, before any discussion of segmentation, is architecturally correct.

---

## Claim 3: Macro segmentation prevents lateral movement between business functions

**NSA's claim:** Macro segmentation "provides high-level control over traffic moving between various areas of an organization's network by breaking up a network into multiple discrete components with each supporting a different security requirement." It can be thought of as "the separation of sub-organizations within a company." These boundaries, "coupled with access controls, provide security by shrinking the attack surface to prevent lateral movement."

**Evidence presented:** Four-phase maturity progression:

| Phase | Capability |
|-------|-----------|
| **Preparation** | Define different security levels on the network. Map the logical distinctions in network structure. |
| **Basic** | Segment networks based on business functions, locations, and asset criticality. Strengthen internal security controls within existing segments (e.g., VLANs). |
| **Intermediate** | Access policies restricting lateral movement between segments are defined and written into firewall rules based on security policies. |
| **Advanced** | Network further segmented into more granular components. Automated central management system integrated and configured to manage network growth. |

**Confidence:** HIGH. Macro segmentation is a mature concept (VLANs, VRFs, security zones) that predates Zero Trust by decades. NSA's contribution is positioning it as the *first layer* of a multi-layer segmentation strategy, not the only layer.

**What's at stake:** Many organizations stop at macro segmentation and consider their networks "segmented." The NSA's model makes clear that macro is necessary but insufficient — micro segmentation is the next required layer. The maturity progression from Basic (VLANs) to Intermediate (firewall-enforced access policies) to Advanced (automated central management) defines the gap between traditional network segmentation and ZT-grade macro segmentation.

**Cross-reference to NIST 800-207 §3.2.2 (Enclave-Based Deployment):** NIST's enclave-based model is essentially macro segmentation applied at the resource level — a gateway protects a collection of resources serving a single business function. NIST correctly identifies the key downside: "subjects may see resources they don't have access to." NSA's micro segmentation layer addresses exactly this limitation.

**My assessment:** The key insight in NSA's maturity model is at the Intermediate level — the shift from "segment the network" (Basic) to "write access policies that restrict lateral movement between segments" (Intermediate). Many organizations have VLANs but no explicit lateral movement prevention rules between them. That gap is where the Target breach occurred.

---

## Claim 4: Micro segmentation limits blast radius within segments — it's the granular layer

**NSA's claim:** Micro segmentation "provides security at a granular level by breaking down a portion of the network into smaller components to limit how data flows laterally through strict access policies." It can be thought of as "the network separation within a sub-organization; employees in the same department should not have access to each other's resources unless explicitly required." This "provides for additional security enforcement closer to applications and resources, augmenting policies already established at the network perimeter."

**Evidence presented:** Four-phase maturity progression:

| Phase | Capability |
|-------|-----------|
| **Preparation** | Define different security levels on the network based on identity and application access. |
| **Basic** | Begin transitioning toward service-specific interconnections and isolation of critical data flows. |
| **Intermediate** | Deploy endpoint and application isolation mechanisms to more of the network architecture with ingress/egress controls between micro segments. Controls tested and refined as needed. |
| **Advanced** | Extensive micro segmentation based on application profiles and data flows, with continuous authentication of connectivity for service-specific interconnections. Central management platforms refined to provide automated and optimal visibility and security monitoring, including alerting on anomalous behavior. |

**Confidence:** HIGH. Micro segmentation is the capability most directly associated with Zero Trust networking, and NSA's maturity model captures the progression from "we define different security levels" (Preparation) to "continuous authentication of connectivity" (Advanced).

**What's at stake:** Micro segmentation is operationally expensive without automation. The NSA addresses this by tying micro segmentation maturity to SDN maturity — the Advanced level for micro segmentation presumes SDN-based central management. Organizations that attempt micro segmentation with traditional tools (manual firewall rules per workload) discover that the combinatorial explosion of rules is unmanageable. The document's structure — SDN as Capability #4, directly following micro segmentation — is not coincidental.

**Key nuance:** NSA distinguishes between endpoint/application isolation (Intermediate) and continuous authentication of connectivity (Advanced). The difference is temporal: Intermediate micro segmentation sets up static isolation boundaries; Advanced dynamically re-authenticates connectivity, meaning that even within a micro segment, a session that changes risk profile can be terminated. This maps directly to NIST 800-207's "contextual trust algorithm" concept (§3.3).

**Cross-reference to CISA Network Pillar:** CISA's segmentation function describes: "Fully distributed ingress/egress micro-perimeters; extensive micro-segmentation based on application profiles; dynamic just-in-time and just-enough connectivity for service-specific interconnections" at the Optimal level. This maps directly to NSA's Advanced level. NSA's Intermediate level maps to CISA's Advanced level ("expands deployment of endpoint and application profile isolation mechanisms; ingress/egress micro-perimeters"). The two models are substantially aligned.

**My assessment:** The most operationally significant line is at the Intermediate level: "controls are tested and refined as needed." This acknowledges that micro segmentation is iterative — you will break things, you will need to tune. No other ZT standard is this honest about the operational reality of micro segmentation deployment.

---

## Claim 5: SDN is the enabling technology that makes micro segmentation manageable at scale

**NSA's claim:** "Though micro segmentation can be achieved with traditional system components and manual configuration, the centralized nature of SDN allows for dynamic implementation and management across the network. SDN enables the control of packet routing by a centralized control server via a distributed forwarding plane, provides additional visibility into the network, and enables unified policy enforcement."

**Evidence presented:** Four-phase maturity progression:

| Phase | Capability |
|-------|-----------|
| **Preparation** | Map network segments within administrative purview. Identify a roadmap for SDN component integrations. |
| **Basic** | Integrate SDN components and develop a central control plane, along with management policy, network configuration rules, and task schedule (such as updates). |
| **Intermediate** | Map SDN APIs, establish roles, and configure the SDNC to make API calls using encryption and authentication. Test interconnectedness and set configurations to employ segmentation rules at the optimal level of granularity. |
| **Advanced** | Create alert systems to notify administrators of anomalous or suspicious behavior. Employ advanced analytics and controls. Test the network to determine which network paths would allow an intruder to move between segments laterally or otherwise. Restrict the paths as appropriate with strict access controls. |

**Confidence:** HIGH on the capability description. MEDIUM on the implicit assumption that SDN is the best or only path to micro segmentation at scale — host-based micro segmentation (software agents on endpoints) is an alternative that NSA does not discuss.

**SDN Controller Risk:** NSA explicitly warns: "the SDN Controller (SDNC) itself can become a priority target that requires proper configuration and continuous monitoring." Recommended mitigations include:
- Dedicated API administrator roles with restricted privileges (separate from SDN administrators)
- SDNC should only accept API calls from authorized API administrators
- API calls secured using encrypted protocols (TLS v1.2+, SSH v2+) and mutual authentication (client and server certificates)

This is a significant operational warning — the centralized control that makes SDN powerful also makes the SDNC a single point of compromise. If an attacker compromises the SDNC, they can reconfigure the entire segmented network.

**Cross-reference to NIST 800-207 §3.1.3 (SDP):** NIST describes SDP as an overlay network approach where "the PA acts as a network controller that sets up and reconfigures the network based on PE decisions." This is essentially the same concept that NSA frames as SDN-enabled micro segmentation. NIST also references SDN and IBN (Intent-Based Networking) as enabling technologies. The two documents converge on the same architectural pattern: a central controller making policy decisions that are enforced at distributed points.

**Cross-reference to CISA Network Pillar:** CISA's "dynamic just-in-time and just-enough connectivity for service-specific interconnections" at the Optimal level is the policy outcome that NSA's SDN capability enables. CISA describes the *what*; NSA describes the *how*.

**My assessment:** The SDN maturity model's most valuable contribution is at the Advanced level: "Test the network to determine which network paths would allow an intruder to move between segments laterally or otherwise. Restrict the paths as appropriate." This is a call for adversarial testing of segmentation boundaries — essentially, red-teaming the network segmentation. No other ZT standard makes this explicit. It's a characteristically NSA addition: test your defenses against the threat you're designing against.

---

## Claim 6: The four capabilities form an integrated, sequential maturity journey

**NSA's claim:** To mature network and environment capabilities, an organization should: (1) map data flows based on usage patterns and operational business requirements; (2) properly segment the network at both macro and micro levels; (3) use SDN for centralized control and automated tasking where available and practical; (4) automate security policies to gain operational efficiency and agility; (5) use risk-based methodologies to define access rules that ensure malicious or unauthorized traffic is dropped prior to reaching network resources at the perimeter, macro, and micro boundaries.

**Evidence presented:** The sequential structure of the document (data flow mapping → macro → micro → SDN) itself argues for sequential dependency. You cannot segment without understanding flows. You cannot micro-segment effectively without macro segmentation as a foundation. You cannot manage micro segmentation at scale without SDN or equivalent automation.

**Confidence:** HIGH on the logical dependencies. MEDIUM on whether the sequence must be strictly sequential in practice — organizations with existing macro segmentation can begin micro segmentation pilots before completing comprehensive data flow mapping, and SDN adoption can begin in parallel with segmentation efforts.

**What's at stake:** The implied message is that skipping steps creates fragility. An organization that deploys SDN-enabled micro segmentation without data flow mapping will build segmentation rules based on assumptions rather than reality — and will discover broken workflows and shadow IT paths the hard way.

**My assessment:** The five summary recommendations at the end of the document form a complete implementation checklist. Combined with the maturity tables, they provide more actionable guidance than CISA's Network pillar (which describes maturity *levels* but not the *sequence* of capability development). NSA's contribution relative to CISA is making the implementation pathway explicit.

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
