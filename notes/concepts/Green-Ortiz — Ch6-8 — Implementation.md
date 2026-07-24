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
---

# Green-Ortiz — Ch6–8: Implementation Patterns

The three implementation chapters of Green-Ortiz et al.'s Cisco-centric Zero Trust book. Chapter 6 defines segmentation models and technologies; Chapter 7 enumerates the common challenges organizations face in practice, with concrete solutions for each; Chapter 8 provides the planning and deployment frameworks for turning analysis into action. Together they form a complete implementation methodology — the "how" of ZT networking — with a distinctive emphasis on **layered enforcement** and **contextual identity** as the engine of segmentation policy.

---

## Ch6: Segmentation — Models, Technologies, and Methodology

### Claim 1: True ZT segmentation requires enforcement at every OSI layer — layering is not optional but the ideal-world answer, pushing back against the firewall-centric mindset that considers one enforcement point sufficient.

**Author's claim:** "In an ideal world, which segmentation methodology works best? The answer, simply put, is all of them." Green-Ortiz organizes segmentation across all seven OSI layers from physical cabling through application logic, arguing that no single technology is sufficient.

**Evidence presented:** A comprehensive OSI-layer mapping: Layer 1 (Physical) — separate cabling, air-gapped networks for defense/manufacturing; Layer 2 (Data Link) — VLAN assignment, TrustSec SGT embedding in frame headers, private VLANs for east-west control; Layer 3 (Network) — IP-based ACLs, routing policies, VRF isolation; Layer 4 (Transport) — stateful firewalling, ACLs, cloud security groups, SGT-based policy; Layer 5 (Session) — dedicated control channels, protocol validation; Layer 6 (Presentation) — checksums, encryption, message integrity; Layer 7 (Application) — containers, application sandboxing, process isolation. The authors' emphasis is that the firewall-centric mindset considers one enforcement point sufficient — this is explicitly rejected.

**Confidence:** HIGH — The all-layers position is a specific, well-articulated thesis supported by detailed OSI-layer mapping. It distinguishes Green-Ortiz from sources that focus primarily on Layer 3/4 enforcement.

### Claim 2: East-west segmentation — controlling traffic within the same VLAN/subnet — is the harder problem that most distinguishes ZT from traditional perimeter security, requiring Layer 2 identity-based enforcement that doesn't depend on routing.

**Author's claim:** The most important architectural distinction in Ch6: north-south segmentation (between security zones, with natural enforcement points at routers/firewalls) vs. east-west segmentation (within the same VLAN, where no intermediary performs path selection). East-west is where malware spreads laterally, and solving it requires either breaking every device into its own VLAN (hitting the 4094-VLAN limit) or using Layer 2 identity-based enforcement.

**Evidence presented:** TrustSec / Security Group Tags (SGT) is presented as the Cisco solution: a 16-bit SGT embedded in the Ethernet frame header (Cisco Meta Data field), assigned dynamically by ISE at authentication time, independent of VLAN/IP/MAC, traveling with every frame. Enforcement at egress by the network access device. Key capability: two adjacent devices in the same VLAN can be prevented from communicating; policy granularity ranges from specific ports/protocols per SGT pair to simple permit/deny. Two critical considerations: (1) applying Layer 2 segmentation could block a device from reaching its IP gateway — requiring complete understanding of all required traffic before enforcement; (2) the SGT taxonomy must not become too granular — the authors warn against overcomplicating, which "hinders operations teams by overcomplicating troubleshooting."

**Confidence:** HIGH — The east-west problem is a well-defined technical challenge acknowledged across the ZT literature. The 4094-VLAN limit and operational chaos from per-device VLANs are concrete constraints. The TrustSec solution is Cisco-specific but the architectural problem is universal.

### Claim 3: The five-pillar methodology for segmentation operationalizes ZT by making contextual identity the engine of policy — but organizations must start with 5–7 broad enclaves and refine iteratively, treating segmentation as "eating an elephant — one small step at a time."

**Author's claim:** The chapter operationalizes segmentation through the book's five ZT pillars: (1) Understand Contextual Identity (who/what/where/when/how + vulnerability posture via RADIUS + ISE profiling); (2) Understand External Resource Consumption (PXGrid + NetFlow for identity-injected flow data); (3) Validate Vulnerabilities to External Sites (Layer 7 firewall for application discovery + IPS); (4) Understand Internal Communication (NetFlow + identity integration for internal flows); (5) Understand Communication Within the Broadcast Domain/VLAN (hardest step, requires contextual identity first). The authors warn: "Far too many organizations start with too many segments based on contextual identity, attempting to replace primarily authentication-based mechanisms, such as Active Directory, with TrustSec tags."

**Evidence presented:** The endpoint segmentation plan (Figure 6-6) maps device types → business units → required restrictions → enforcement mechanisms. The prescribed stacking order: VLAN (dynamic assignment) → Firewall (inter-VLAN traversal + advanced features) → Downloadable ACLs (distributed to access switches) → TrustSec SGTs (intra-VLAN peer-to-peer control). For data centers where virtual switches don't support TrustSec: host-based agents (Cisco Secure Workload or Secure Endpoint) that write IP tables based on centrally managed policy.

**Confidence:** HIGH — The five-pillar methodology is the book's core framework. The "start with 5-7 enclaves" recommendation is an empirically grounded Cisco services finding that provides a concrete starting point other ZT frameworks leave abstract.

---

## Ch7: Common Challenges and Practical Solutions

### Claim 4: True contextual identity is never just a device type — a displayless hardware phone used after hours by Facilities has a fundamentally different identity than a director's hardware phone at home during business hours, and this multi-dimensional profiling is the foundation of all ZT enforcement.

**Author's claim:** The authors expand the familiar "who, what, where, when, how" framework with specific profiling techniques and make the provocative point: "True contextual identity is never just 'phone,' 'printer,' 'laptop,' or 'camera.'" The contextual identity decision tree (Figure 7-1) demonstrates that identity is the product of multiple intersecting attributes.

**Evidence presented:** Specific profiling techniques: Who — directory services for domain-joined devices, asset management databases for headless devices; What (Active) — NMAP scanning with caution for legacy devices, OS fingerprinting, SNMP, vulnerability scanner integration; What (Passive) — RADIUS probe data, DHCP options and hostname, HTTP User-Agent headers, CDP/LLDP, MUD URLs for IoT, with DHCP weighted higher than MAC address because harder to spoof; Where — geographic location narrows identity; When — time-of-day patterns, 3 AM connections may indicate compromise; How — connection medium, an iPad via wired Ethernet triggers additional scrutiny. The "minimum viable products" approach: break network into functional elements, use agile methodologies for incremental value.

**Confidence:** HIGH — The profiling methodology is the most detailed practical guide to device identification in the ZT literature. The multi-attribute identity claim is a conceptual insight with direct operational implications.

### Claim 5: The firewall-is-enough belief is mathematically disproven — a network with 2,046 VLANs passing through a firewall requires a minimum of 12,000 initial rules just for shared services, not counting business-specific rules.

**Author's claim:** Organizations with large firewall estates believe firewalls alone constitute sufficient segmentation. The math disproves this: each VLAN requires DNS, DHCP, authentication, remote access protocols, and domain controller traffic rules — a set of 6 × N VLANs = ~12,000 rules minimum for 2,046 VLANs.

**Evidence presented:** The authors propose a university/research network model where every endpoint is treated as a threat by default: (1) treat every endpoint as a threat to the network; (2) segment endpoints from everything except critical services; (3) require users to agree to policy stating explicit access requirements; (4) require the level of contextual identity the organization can facilitate; (5) apply enforcement and vulnerability management at network ingress. The firewall's retained role: advanced features that access switches cannot provide (IPS, malware detection, TCP normalization, DLP, VPN termination) — but it becomes one layer among many rather than the sole enforcement point. The firewall for external access can typically be a smaller, lower-throughput model.

**Confidence:** HIGH — The 12,000-rule calculation is a concrete, verifiable mathematical argument. The university network model provides an alternative operational paradigm with specific, enumerated principles.

### Claim 6: External access for IoT/endpoints requires baseline creation through multiple collection points — edge firewall logs, Internet proxy logs, NetFlow, endpoint agents, and DNS analytics — because vendor documentation of network interactions is unreliable.

**Author's claim:** IoT devices rely on elastic cloud infrastructure with dynamically updated DNS names, and vendor documentation of network interactions is unreliable. The binary choice appears to be "allow anything to *.vendor.com" or exhaustively track every destination — neither is acceptable.

**Evidence presented:** The solution uses multiple collection points: edge firewall logs + identity injection, Internet proxy logs, NetFlow (Cisco Secure Network Analytics), endpoint agents (Network Traffic Analysis module), and DNS analytics (Cisco Umbrella). Key insight: "resources to run the business... will be longer lived and more commonly accessed than malware-infected resources, which will need to change servers, hosting providers, or cloud services on a regular basis to avoid detection." The firewall rule lifecycle problem: without audit processes, "it's common to have hundreds of thousands of rules, with large percentages representing overlaps in address and purpose." ZT's distributed policy approach forces cleanup of poorly managed centralized firewall rules as a side benefit.

**Confidence:** HIGH — The multi-collection-point methodology is specific and operational. The observation about legitimate resources having longer-lived connection patterns vs. malware is a useful heuristic for baseline differentiation.

### Claim 7: New endpoint onboarding ("Day 2 Operations") requires a centralized receiving process — a secured, isolated network segment with lenient NAC policy, separate Internet access, and full NetFlow collection, followed by a structured onboarding checklist.

**Author's claim:** Organizations focus on segmenting what's already on the network but neglect the process for new devices. The old model — firewall admins receive tickets requesting "allow our IP range to access these DNS names" without explanation — is incompatible with ZT.

**Evidence presented:** The onboarding process: centralized receiving segment with secured/isolated network, lenient NAC policy, separate Internet access, full NetFlow collection. Onboarding checklist: (1) create contextual identity (active + passive profiling); (2) collect traffic patterns (local switch NetFlow, upstream firewall logs); (3) document architecture and device capabilities; (4) evaluate authentication capability (802.1X, posture, management enrollment); (5) assign to static group in NAC server → authorization result → distributed enforcement policy. For remote users, the authors endorse MDM-based provisioning (Meraki Systems Manager) for pushing VPN/client configurations with minimal user steps.

**Confidence:** HIGH — The Day 2 operations gap is a well-recognized operational failure mode. The centralized receiving segment and structured checklist provide a concrete, actionable process that addresses a gap in most ZT planning.

---

## Ch8: Developing a Successful Segmentation Plan

### Claim 8: Top-down (business-aligned) and bottom-up (traffic-aligned) design approaches are complementary, not competing — use top-down for high-level architecture and bottom-up for validation and detailed policy creation.

**Author's claim:** The chapter's core planning contribution distinguishes two design approaches: top-down (business-aligned — starts with executive buy-in and business drivers, defines segments by business function and regulatory compliance) and bottom-up (traffic-aligned — starts with traffic collection and identity mapping, determines segmentation based on observed communication patterns). "The implementation of segmentation may require that both of these strategies be utilized for the best results to be achieved."

**Evidence presented:** Top-down is best for regulated industries with clear business-unit boundaries where endpoints cleanly map to organizational units. Bottom-up is best for consulting firms (one person spans multiple BUs), shared physical servers hosting multiple BU VMs, and politically siloed organizations where cross-department communication is unknown. Three deployment templates: (1) By Site Type — classify sites, build reusable patterns (Business Services, Building IoT, Infrastructure Management, Guest, Shared Services); (2) By Endpoint Category — homogeneous populations, healthcare example mapping Imaging/Pharma/Point of Care/Labs/Clinical VDI; (3) By Service Type — policy enforcement points at organizational boundaries (Partner VPN, Employee VPN, Partner Leased Lines, DMZ, Corporate WAN, Guest Internet, Unknown). Warning: "One organization went so far as to attempt to describe endpoints based on age" — categorizations must be actionable from available contextual identity data.

**Confidence:** HIGH — The top-down/bottom-up distinction resolves the "where do we start?" question that paralyzes most organizations. The three deployment templates provide concrete organizational structures for planning.

### Claim 9: The policy decision matrix — mapping source entities to destination entities with per-cell permit/deny, port/protocol, and directionality — is the output artifact of ZT planning, and multiple matrices will be needed across intra-data center, inter-site, and per-business-unit contexts.

**Author's claim:** The segmentation planning process produces a matrix where each cell defines simple permit/deny, port/protocol policy, and directionality. The authors note multiple matrices will be needed — intra-data center, inter-site, and potentially per-business-unit.

**Evidence presented:** Four business drivers define the segmentation charter: (1) Risk Assessments and Compliance — CMMC, PCI, ISO requirements mapped directly to the five ZT pillars, with specific CMMC assessment criteria quoted for each; (2) Threat Mapping — probability × impact of threats on critical systems; (3) Data Protection — confidentiality, integrity, availability as the trifecta; (4) Reducing Attack Surfaces — self-justifying even without regulatory mandate. Implementation guidance: "Monitor mode first — the organization should implement a discovery or monitor mode for as long as possible, and in parallel to other enforcement tasks being executed." Authorization of entities is "the most important outcome of the Zero Trust journey."

**Confidence:** HIGH — The policy decision matrix is a concrete, implementable planning artifact. The monitor-mode-first mandate is consistent across all ZT sources. The claim that authorization is the most important outcome provides clear prioritization.

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
