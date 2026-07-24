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
---

# Green-Ortiz et al. — Ch3-5: Trust Assessment and Policy

Ch3-5 of Green-Ortiz et al. form the trust computation and policy engine section of the book. Ch3 defines the spatial architecture — where enforcement happens and what level of trust assessment each location requires. Ch4 defines enclave design — what gets grouped together and what trust criteria justify the grouping. Ch5 operationalizes the policy development lifecycle — how trust data is collected, how policy is built from it, how it's tested, and how it survives organizational change. Together they answer: *how do you assess trust, and how do you convert that assessment into enforceable policy across an enterprise network?*

## Claim 1: Trust assessment is spatial — the architecture location determines trust data availability and granularity

**Authors' claim:** Different architectural locations (branch, campus, core, WAN, data center, cloud) present fundamentally different trust signals, different enforcement capabilities, and different blind spots. Trust assessment must be tailored to the location, not applied uniformly. The branch is the "easiest" to assess but has consumer-grade enforcement; the campus has richer enforcement but greater endpoint diversity; the data center's virtualized nature creates identity and enforcement gaps; the cloud requires adapting on-premises trust models.

**Evidence presented:** The chapter-by-location walkthrough in Ch3 provides specific trust assessment capabilities for each architectural area:
- **Branch:** Identity via RADIUS to policy server, posture via installed/ephemeral agents, traffic analysis via NetFlow/taps. Classification by business priority and impact. Key limitation: consumer/prosumer-grade network access devices with limited security features.
- **Campus:** Richer ID enforcement at access layer, MACSec for switch-to-switch authenticated encryption, external scanners for non-PC posture. L3 enforcement at VLAN/subnet boundaries. Key advantage: large number of enforcement points enables gradual rollout.
- **Core network:** Network access device identity via loopback IP + metadata (hostname, model, location, function). TACACS+ with command-level authorization. NetFlow/taps for traffic analysis.
- **WAN:** Overlay-based trust (SD-WAN, DMVPN, GETVPN, IPsec). Segmentation tags (TrustSec) carried through tunnels. Man-in-the-middle is the primary threat.
- **Data center:** Machine identity + service accounts. Virtual server enforcement via hypervisor-hosted switches or host agents. Legacy system compensating controls via segmentation.
- **Cloud:** Metadata tagging for contextual identity. Dynamic contextual metadata. SASE/SSE for cloud-delivered security controls. Baseline audit before ZT deployment.

**Confidence:** HIGH. The spatial differentiation of trust assessment is a practical contribution that complements the abstract policy engine model of NIST 800-207 and the control-plane/data-plane model of Gilman & Barth. It addresses the question those frameworks don't: *where do trust signals come from and how do they vary by network segment?*

**What's at stake:** If trust assessment is treated as uniform, organizations either under-assess in some locations (leaving blind spots) or over-engineer in others (wasting resources). The spatial model makes trust assessment deployment-operational: you start where enforcement is easiest (branch), learn there, and scale.

**Who disagrees:** Gilman & Barth's model treats trust assessment as a property of the control plane, independent of network topology — the trust engine receives signals from agents regardless of where they are on the network. This is architecturally cleaner but less useful for brownfield migration planning. Green-Ortiz's spatial model is messier but more actionable for organizations that have a physical network infrastructure.

**Alternative reading:** The spatial model could be read as a Cisco-specific framing — the emphasis on RADIUS, TrustSec, Cisco ISE, and Cisco SD-WAN reflects the book's publisher. But the underlying principle (trust signals differ by architecture location) is vendor-neutral and widely applicable.

**My assessment:** This is the most underappreciated contribution of Green-Ortiz. Most ZT literature treats the network as an abstract hostile medium. Green-Ortiz treats it as a concrete physical infrastructure with varying capabilities — and maps ZT trust assessment onto it. For organizations with brownfield networks, this is more actionable than the abstract models.

---

## Claim 2: Enclave design is trust classification — what criteria justify grouping and what criteria justify access between groups

**Authors' claim:** Enclaves (also called zones or segments) are "a categorization of common functionality, common business impact, or common regulatory requirements" used to "provide common security policy to sets of assets where logical or physical grouping can be achieved." From a ZT perspective, "enclave design is foundational to determining trust (what criteria need to be met for an asset to be placed in an enclave) and trustworthiness (what criteria need to be met to allow assets to communicate with other assets)." Ch4 provides a comprehensive taxonomy: User Layer (corporate workstations, guests, BYOD, IoT, collaboration, lab/demo), Proximity Networks, PANs, Cloud, Enterprise (business services, DMZ, common services, PCI-DSS, facility, mainframe, legacy).

**Evidence presented:** Ch4 enumerates enclave categories with detailed trust criteria for each:
- **Corporate workstations:** Two identities combined — machine identity (device profile + attributes) + user identity. Posture checks: anti-malware running, recent definitions, patching status, NAC integration. Combined identity via 802.1X EAP-TEAP or service account + user interrogation.
- **Guests:** Limited posture assessment (agent-based controls infeasible). Network-based controls and visibility critical. Regular audits, penetration testing. Segmented from internal resources.
- **BYOD:** MDM for credential + posture management. Agent-based posture. Opt-in management for limited corporate resource access.
- **IoT:** Headless, limited patching, no agent-based controls. Network segmentation + behavior analytics. Profiling for identity. Regular vulnerability scans (carefully, due to limited error handling).
- **Collaboration:** Access governance: who can connect, what features, what access needed, how content consumed, how provisioned.
- **Lab/Demo:** Centralized policy, firewall between test segments, periodic registration/authentication.
- **Cloud:** Native tools + external tools. Contextually relevant identity data. Privileged access management. Defense-in-depth even with cloud provider tools.
- **Enterprise applications:** Development → Testing → Production → Customer/Partner facing. Each segment has distinct trust criteria.
- **Mainframe:** Segmentation, PAM (keystroke logging), session behavior monitoring (UAM), automated monitoring/response.
- **Legacy systems:** Compensating controls — segmentation, IDS/IPS, firewalls.

**Confidence:** HIGH. This is the most comprehensive enclave taxonomy in the ZT literature. Gilman & Barth's agent model is more architecturally elegant but doesn't address the diversity of device types and trust assessment methods needed at enterprise scale. NIST 800-207 abstracts enclave design entirely — it's an implementation detail from the standards perspective.

**What's at stake:** Enclave design determines the scope of policy: what gets enforced together, what's isolated, what's the blast radius of a compromise. Bad enclave design either over-segments (policy management overhead explodes) or under-segments (enforcement is too coarse to prevent lateral movement).

**Who disagrees:** The cloud-native community argues that enclave design is a legacy concept — in a fully identity-based, agent-enforced model, enclaves are unnecessary because every connection is individually authorized. Green-Ortiz's position is pragmatic: enterprises have brownfield networks and cannot deploy agents on every device (IoT, legacy, guests), so network-based enclave enforcement remains necessary.

**My assessment:** Ch4 is the most practically useful chapter in Green-Ortiz for enterprise architects. The enclave-by-enclave trust criteria serve as a readiness checklist: for each enclave type, here's what trust data you need, what posture checks are feasible, and what enforcement mechanisms apply. It bridges the gap between abstract ZT principles and operational deployment.

---

## Claim 3: Trust assessment is multi-layered — identity, posture, and behavior combine to produce an enforcement decision

**Authors' claim:** Trust in Green-Ortiz is not a single score (as in Gilman & Barth) but a multi-dimensional assessment drawing from the five ZT pillars: Identity (who/what is this?), Vulnerability Management (is it secure right now?), Policy & Governance (what are the rules?), Enforcement (what can I control?), and Analytics (what does behavior look like?). The combination determines access. Ch5 makes this explicit: "the conditions for allowing data access should incorporate both the current aspects of an identity, including the user or asset based on the data collected by the various discovery mechanisms used."

**Evidence presented:** Ch5's segmentation policy development procedure reveals the trust data pipeline:
1. **NAC consumes identity data** from flow logs to attribute communications to specific identities.
2. **DNS lookup** resolves external entities to names, adding context.
3. **IPAM/asset management** fills gaps for devices without dynamic identity (static addresses, legacy devices).
4. **Database of known endpoints** is built from all sources, with continual updates.
5. **Continual trust updates** from NAC, posture, XDR, and behavioral systems feed the enforcement policy.
6. **Integrations pass conclusions between systems** — when "an anomaly is detected, the integrations are leveraged to allow that conclusion to pass from one system to the other so that policy can be applied to provide an alert, perform mitigation and enforcement on a particular user or asset."
7. **Enforcement adjusts dynamically** — from "requiring another factor of authentication" to "complete network isolation."

**Confidence:** MEDIUM. The pipeline is conceptually sound and aligns with the NIST PDP model, but Green-Ortiz doesn't provide a computational model for combining these signals — it's a framework for what data to feed into policy, not how to compute a trust decision from it. Gilman & Barth's variable trust score model is more computationally explicit but less operationally comprehensive.

**What's at stake:** If trust assessment is only as good as its weakest data source, organizations need to understand which signals are load-bearing and which are supplementary. Green-Ortiz doesn't provide that prioritization — all five pillars are treated as equally important, which may not be practically achievable.

**Who disagrees:** Gilman & Barth propose a unified trust score computed by a trust engine — a quantitative model. Green-Ortiz proposes a multi-dimensional assessment consumed by policy rules — a qualitative model. Both can produce equivalent enforcement outcomes, but the operational trade-offs differ: a single trust score is simpler to implement but harder to debug; multi-dimensional rules are more transparent but harder to manage at scale.

**My assessment:** Green-Ortiz's approach is the pragmatic enterprise answer to "how do you compute trust?" The answer is: you don't compute a single number. You collect identity, posture, and behavior data; you define policy rules that combine them; and you let the enforcement system apply those rules. It's less elegant than a unified trust engine but more aligned with how enterprises actually operate — with multiple security tools, each providing partial signals, integrated through a policy orchestration layer.

---

## Claim 4: Policy creation is data-driven — discovery before enforcement, log before block

**Authors' claim:** Policy should be built from observed traffic patterns, not from documentation or human assumptions. Ch5's recommended logic proceeds from identity attribution (NAC on flow logs) → DNS resolution → IPAM lookup → endpoint database → classification into enclaves. The entire process is designed to produce policy from empirical communication patterns. Ch3 reinforces this: "continual analysis will contribute to an ever-evolving policy being applied." Ch5 warns against enforcement without discovery: even "full participation from all relevant stakeholders" may miss use cases "not well understood or known by their owners."

**Evidence presented:**
- Ch3 branch analysis: "combined with a traffic collection or analysis mechanism, such as NetFlow or traffic taps, both mechanisms are used to determine the impact of policy on a set number of devices."
- Ch3 campus analysis: "traffic monitoring and identity enforcement, for example, can be done on singular switches that still have a larger variety of connected endpoints" — breaking the campus into small analysis areas for iterative learning.
- Ch5 explicit procedure: NAC → DNS → IPAM → endpoint database → classification.
- Ch5 testing: model and test policy, monitor for an "extended period to collect more data and ensure users are not negatively impacted in completing their business functions."
- Ch5 monitoring: explicit warning against the common workaround — "the complete removal or bypass of enforcement from the port or session through which the entity connects" — because it "precludes the ability to actively troubleshoot."

**Confidence:** HIGH. The discover-then-enforce pattern is validated by every major ZT migration case study (Gilman & Barth's log-then-enforce, Google BeyondCorp's observe phase). Green-Ortiz operationalizes it with specific data sources and a sequenced procedure.

**What's at stake:** The discover-then-enforce model is what makes ZT migration safe. Without it, policy is written from assumptions and breaks production workloads. The operational discipline to avoid bypassing enforcement during troubleshooting is a cultural challenge that Green-Ortiz correctly identifies as critical.

**Who disagrees:** The disagreement isn't about the principle but about the feasibility. Organizations with thousands of applications and millions of flows may find exhaustive discovery impractical. Green-Ortiz's answer is automation (orchestration solutions) and gradual rollout (one segment at a time), but the scalability of this approach at very large enterprises is not proven in the book.

**My assessment:** The "log before block" pattern is the single most important operational insight in ZT migration literature, and Green-Ortiz provides the most detailed data pipeline for implementing it. The emphasis on building an endpoint database — a living inventory with identity, location, owner, and communication patterns — is practical and hard-won advice. In real deployments, the absence of such an inventory is the first and hardest obstacle.

---

## Claim 5: Policy survives organizational change through the Policy & Governance pillar — but mergers, acquisitions, and shadow IT constantly challenge it

**Authors' claim:** The Policy & Governance pillar is the organizational anchor for ZT. Ch5 details two major threats to policy integrity: mergers/acquisitions (Ch5: "Onboarding: The Challenge of Merger Activity") and independent purchasing decisions (Ch5: "Onboarding: The Challenge of Independent Purchasing Decisions"). In both cases, the solution is formal policy enforced through the governance pillar: "Policies should be created and adhered to, and they should entail replacing equipment at the end of its useful life cycle" and "a well-defined policy allowing for purchase of devices so long as they are onboarded in a consistent manner and in alignment with organizational standards."

**Evidence presented:**
- **Mergers:** Organizational debt increases, technical debt accrues, skill gaps appear. The acquiring organization "has the responsibility, by utilizing the analysis tools and capabilities found within the respective pillar, to evaluate how organizational debt will be affected by the merger." Feedback from all pillars is critical. Due diligence questions include: "Does the organization have well-defined policies?" "Do competing policies, processes, and procedures create unresolvable conflicts?" "How will data be protected as it migrates across infrastructures?"
- **Shadow IT:** Two scenarios — the first (policy failure) where devices "do not allow for discovery" and create "shadow IT" blind spots; the second (political pressure) where "the decision comes down to when and not if the network can be ready for them." Solution: "a well-defined policy allowing for purchase of devices so long as they are onboarded in a consistent manner."
- **Onboarding process:** Three steps: (1) policy exception process with security level approval; (2) acquisition with bill of materials + test plan documenting operational modes; (3) policy creation addressing visibility, identity, context, and enforcement, with operational testing before sign-off.

**Confidence:** MODERATE. The role of governance in maintaining ZT policy is underdeveloped in the broader ZT literature (NIST's migration chapter mentions it, Gilman & Barth don't address it). Green-Ortiz's treatment is more extensive than most, but it's still aspirational — actual governance implementations in complex organizations are far messier than the three-step onboarding process suggests.

**What's at stake:** Policy integrity over time is the single biggest threat to a ZT deployment. A perfectly enforced ZT architecture can be eroded by one merger that introduces thousands of unmanaged devices, or by shadow IT that creates undocumented access paths. Green-Ortiz correctly identifies this as a governance problem, not a technology problem — but the governance prescription is thin.

**Who disagrees:** Some argue that the solution to shadow IT and merger complexity is to make ZT enforcement so lightweight and automated that new devices can be onboarded without friction — making governance unnecessary. Green-Ortiz's position is that governance is unavoidable because business decisions (mergers, budget allocations, vendor selection) create trust boundary changes that technology alone cannot adjudicate.

**My assessment:** This is the most important and least developed claim in Ch3-5. The governance problem is real and underappreciated. Green-Ortiz identifies the right threats but the solutions are templates rather than battle-tested patterns. The due diligence questions for mergers are the most actionable part — they can serve as a practical checklist for any organization undergoing M&A.

---

## Claim 6: Automation bridges the gap between trust assessment and enforcement at scale — continuous, not occasional, evaluation

**Authors' claim:** Automation is "a key focus area for organizations as they attempt to reduce complexity and increase productivity." The specific ZT value of automation is that it enables "constantly evaluating trust rather than the common implicit trust or single evaluation of trust at entry to the network." Automation turns trust assessment from a periodic check into a continuous process: "Automation assists an organization where detection within this network behavior platform can automatically cause the execution of changes to other security controls" — such as "firewall rule changes to prevent data exfiltration or a DNS security update to block identified suspect domains."

**Evidence presented:**
- Ch5 retail example: attacks that bypass NAC "often attempt to reside in a retail environment" and "have shown difficulty in both identifying the cause and scope of the attack. With a Zero Trust architecture focus on visibility, the time to identify and resolve these attacks is shortened."
- Ch5 policy orchestration: "It is recommended that an organization implement a solution that automates and orchestrates network security policy management on-premises and in the cloud."
- Ch5 PCI-DSS benefit: Automated documentation reduces the labor for Reports on Compliance (ROC) — "hundreds of employees and thousands of hours of labor" reduced through maintained, accurate policy data.
- Ch5 feedback loop: "Iterative feedback and consumption of outputs from other pillars within the Zero Trust architecture ensures that the policy continues to adapt to changes in the environment."

**Confidence:** HIGH in principle, MODERATE in specificity. The "automation is essential" claim is widely validated — no one disputes that manual ZT enforcement doesn't scale. But the specific automation mechanisms Green-Ortiz describes (ISE, Cisco Secure Network Analytics, policy orchestration tools) are vendor-specific, and the generic claim "use automation" is not particularly actionable.

**What's at stake:** Without automation, ZT reduces to a static set of policies that are checked at connection time — which is basically a more complex firewall. The continuous, adaptive nature of ZT — the property that makes it genuinely different — requires automation to be feasible at enterprise scale. The gap between "use automation" and a fully automated trust assessment-to-enforcement pipeline is enormous.

**Who disagrees:** Gilman & Barth's agent model embeds automation into the architecture itself — agents report trust signals, the trust engine computes scores, the control plane enforces. Green-Ortiz's approach layers automation on top of existing infrastructure. The former is architecturally cleaner; the latter is more realistic for brownfield deployments.

**My assessment:** This connects back to the trust assessment pipeline in Claim 3. The pipeline (NAC → DNS → IPAM → endpoint database → classification → policy → enforcement) IS the automation specification for trust assessment. Green-Ortiz describes it as a sequence of data sources, but the real insight is that it must be automated — you can't do this manually for thousands of endpoints. The PCI-DSS ROC example is particularly valuable: it shows that automation pays for itself in compliance cost reduction, not just security improvement.

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
