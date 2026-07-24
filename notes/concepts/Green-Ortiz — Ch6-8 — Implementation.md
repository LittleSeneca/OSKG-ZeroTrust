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

### The OSI-Layer Segmentation Framework

Green-Ortiz organizes segmentation by OSI layer, arguing that true ZT requires enforcement at **every layer** — from physical cabling up through application logic. While the chapter's focus is Layers 2–4 (the network-centric layers), it establishes the principle that segmentation is not one technology but a **layered set of controls** deployed in concert:

| OSI Layer | Segmentation Mechanism | Typical Use |
|-----------|----------------------|-------------|
| **Layer 7 (Application)** | Containers, application sandboxing, process isolation | Preventing apps on the same host from interfering with each other |
| **Layer 6 (Presentation)** | Checksums, encryption, dedicated exchange channels, message integrity validation | Preventing man-in-the-middle manipulation of session data or encoding |
| **Layer 5 (Session)** | Dedicated control channels, authentication of session initiators, protocol validation embedded in application source code | Ensuring communication methodology matches expected patterns |
| **Layer 4 (Transport)** | Stateful firewalling, ACLs, cloud security groups, SGT-based policy on protocol/port | The most common enforcement point — protocol, source/destination port filtering |
| **Layer 3 (Network)** | IP-based ACLs, routing policies, VRF isolation, firewall zone rules | Controlling which IP subnets can reach which destinations via routing enforcement |
| **Layer 2 (Data Link)** | VLAN assignment, TrustSec SGT embedding in frame headers, MAC-based filtering, private VLANs | East-west control within a broadcast domain; the hardest problem in ZT segmentation |
| **Layer 1 (Physical)** | Separate cabling, cable colors, air-gapped networks, distinct physical switches | Defense/manufacturing environments where device interaction must be physically impossible |

**Key claim:** The authors' position is that **layering is not optional — it is the ideal-world answer.** "In an ideal world, which segmentation methodology works best? The answer, simply put, is all of them." This directly pushes back against the firewall-centric mindset that considers one enforcement point sufficient.

### Two Directional Models: North-South vs. East-West

The most important architectural distinction in the chapter:

- **North-South Segmentation:** Traffic that traverses between different security zones or routing segments, passing through an intermediary device (router, firewall, cloud gateway). The intermediary provides a natural enforcement point for Layer 3/4 ACLs. This is the traditional model — firewalls between zones with a default-deny policy. **Limitation:** Devices within the same zone/VLAN/subnet can communicate freely without touching the enforcement point.

- **East-West Segmentation:** Traffic between devices **within the same VLAN, subnet, or security zone** — the traffic that never routes. Without an intermediary device performing path selection, there is no natural point to apply Layer 3/4 ACLs. This is where malware spreads laterally. **The solution** requires Layer 2 enforcement mechanisms (TrustSec, private VLANs, host-based firewalls) that can control communication within a broadcast domain.

**Why this matters:** The authors argue that east-west segmentation is the harder problem — and the one that most distinguishes ZT from traditional perimeter security. East-west control requires either (a) breaking every device into its own VLAN (hitting the 4094-VLAN limit and creating operational chaos), or (b) using Layer 2 identity-based enforcement that doesn't depend on routing.

### Core Segmentation Technologies

**VLAN Segmentation (Layer 2/3):** The foundational, widely deployed method. VLANs break large broadcast domains into smaller segments, forcing inter-VLAN traffic through a routing device where policy can be applied. **Challenges:** VLAN sprawl (how many is too many?), policy explosion at the firewall aggregating all VLANs (each VLAN requires DNS, DHCP, auth, management, and domain rules — a set of 6 × N VLANs), and the fundamental limitation that VLANs alone cannot control intra-VLAN peer-to-peer communication.

**Access Control Lists (Layer 3/4):** Familiar, widely supported, but with three critical flaws: (1) syntax-only error checking — no validation that a higher-priority rule doesn't override a lower one, (2) no built-in lifecycle tracking — ownership, purpose, and expiration are typically relegated to comments or forgotten, (3) ACLs only control routed (Layer 3) traffic — devices in the same VLAN are unaffected. The authors' solution: dynamically applied, centrally managed ACLs via Cisco ISE that are downloaded to the access switch per session, distributing enforcement and offloading firewalls.

**TrustSec / Security Group Tags (Layer 2):** The Cisco-specific technology for east-west control. A 16-bit Security Group Tag (SGT) is embedded in the Ethernet frame header (the Cisco Meta Data field), assigned dynamically by ISE at authentication time. The SGT is an **overlay identity** — independent of VLAN, IP, or MAC — that travels with every frame. Enforcement is done at egress (closest to the destination endpoint) by the network access device, which downloads only the policies relevant to locally connected devices from the TrustSec matrix. **Key capabilities:** Two adjacent devices in the same VLAN can be prevented from communicating; policy can be as granular as specific ports/protocols per SGT pair or as simple as permit/deny.

**Two critical TrustSec considerations:** (1) Applying Layer 2 segmentation to a device could block it from reaching its IP gateway — requiring complete understanding of all required traffic before enforcement, and (2) the tagging structure must not become too granular — the authors warn against overcomplicating the SGT taxonomy, which "hinders operations teams by overcomplicating troubleshooting due to huge policies that, in many cases, have identical policy rules."

### The Layered Enforcement Model

The authors prescribe a specific stacking order:

1. **VLAN** — Dynamic assignment at authentication for broad logical segmentation
2. **Firewall** — Inter-VLAN traversal control plus advanced features (IPS, malware detection, TCP normalization, VPN termination)
3. **Downloadable ACLs** — Distributed to access switches to offload Layer 3/4 permit/deny from the centralized firewall, localizing enforcement to the network access device
4. **TrustSec SGTs** — Intra-VLAN peer-to-peer control, identity-based upstream firewall policy differentiation

**Beyond the campus:** For data centers, the authors acknowledge that virtual switches in hypervisors often don't support TrustSec. The recommended alternative: host-based agents (Cisco Secure Workload or Secure Endpoint) that write IP tables / local firewall rules based on centrally managed policy, overcoming the RADIUS limitation of the campus model.

### The Five-Pillar Methodology for Segmentation

The chapter operationalizes segmentation through the book's five Zero Trust pillars:

1. **Understand Contextual Identity** — Who (user), What (device type), Where (location), When (time), How (connection medium), plus vulnerability posture. Enabled by RADIUS + ISE profiling (DHCP, HTTP headers, NMAP, CDP/LLDP, SNMP).

2. **Understand External Resource Consumption** — Map what external destinations each identity communicates with. Use PXGrid to inject identity into NetFlow/Secure Network Analytics. Discover baseline behavior.

3. **Validate Vulnerabilities to External Sites** — Layer 7 firewall (Cisco Secure Firewall) for application discovery and IPS. Policies applied as close to the endpoint as possible.

4. **Understand Communication Within the Organization** — NetFlow + identity integration for internal flows. Internal firewalls (between VRFs) for cross-business-unit control. Offload edge firewall processing.

5. **Understand Communication Within the Broadcast Domain/VLAN** — The hardest step. Requires contextual identity first, then traffic collection within the VLAN. Enforcement refined from broad permit/deny to port/protocol specificity. **Warning:** "Far too many organizations start with too many segments based on contextual identity, attempting to replace primarily authentication-based mechanisms, such as Active Directory, with TrustSec tags."

**Bottom line:** Treat segmentation as "eating an elephant — one small step at a time." Start with 5–7 broad enclaves, get operational, then refine. The endpoint segmentation plan (Figure 6-6) maps device types → business units → required restrictions → enforcement mechanisms.

---

## Ch7: Common Challenges and Practical Solutions

Chapter 7 is the book's most operationally grounded chapter — a catalog of the real obstacles organizations hit and how to overcome them. Each challenge is paired with a concrete solution methodology.

### Challenge 1: Gaining Visibility into Unknown Endpoints

**The problem:** Legacy networks lack documentation; application owners resist scrutiny; leadership sees visibility work as impedance to implementation speed; the team feels overwhelmed by scope. Distributed purchasing (anyone with a corporate credit card can buy and connect devices) compounds the problem.

**The solution — Contextual Identity:** The authors expand the familiar "who, what, where, when, how" framework with specific profiling techniques:

- **Who:** Directory services integration for domain-joined devices; asset management databases for headless devices. The greatest challenge: devices without users, where onboarding processes are bypassed due to "arbitrarily chosen timelines or loudly complaining consumers."

- **What (Active Profiling):** NMAP scanning (with caution — legacy medical/manufacturing devices may crash from intensive scans), OS fingerprinting via TCP/UDP response patterns, SNMP queries, vulnerability scanner integration. **Rule:** determine at least partial device identity before initiating active profiling.

- **What (Passive Profiling):** RADIUS probe data (MAC, OUI, username, switch/port), DHCP options and hostname, HTTP User-Agent headers, DNS queries, CDP/LLDP advertisements, MUD (Manufacturer Usage Description) URLs for IoT. **Validation principle:** DHCP should be weighted higher than MAC address because it's harder to spoof; matching attributes across probes increases certainty.

- **Where:** Geographic location narrows device identity when models are deployed only to specific sites.

- **When:** Time-of-day patterns — a device connecting at 3 AM may indicate compromise.

- **How:** Connection medium — an iPad connecting via wired Ethernet should trigger additional scrutiny.

**Reducing complexity:** Break network into functional elements, use agile methodologies for incremental value, create reusable documentation, invite vendors/contractors to validate dependencies, solicit leadership buy-in by advertising value outside of ZT. "Minimum viable products provide value in accelerating implementation planning."

### Challenge 2: Understanding Expected Endpoint Behavior

**The solution:** A six-part endpoint evaluation framework:

1. **OS/firmware protections** — Signed software images, authentication mechanisms (even default credentials are better than none), netstat/ps inspection for unknown processes
2. **Anti-malware/anti-X software** — Presence, central management, definition currency
3. **Posture agents** (Cisco AnyConnect Posture, Duo) — Validate installed applications, services, keys, definitions against baseline; trigger remediation on noncompliance
4. **Internal communication baseline** — NetFlow/sFlow/OpenFlow + identity integration to map identity-to-identity communication; tools: Cisco Secure Network Analytics
5. **External communication baseline** — Cloud controller destinations, update servers, geographically distributed redundancy points; tools: edge firewalls, Internet proxies, Cisco Umbrella DNS analytics
6. **Change in baseline behavior** — Document what a device *can* do vs. what it *is currently doing*; maintain a repository of device capabilities for future business needs — enabling both security and capex savings

**The contextual identity decision tree (Figure 7-1):** A framework showing that "phone" is never just "phone." A displayless hardware phone used after hours by Facilities has a different contextual identity than a director's hardware phone at home during business hours. The authors make the provocative point: "True contextual identity is never just 'phone,' 'printer,' 'laptop,' or 'camera.'"

### Challenge 3: External Access Requirements

**The problem:** IoT devices rely on elastic cloud infrastructure with dynamically updated DNS names. Vendor documentation of network interactions is unreliable. The binary choice appears to be "allow anything to *.vendor.com" or exhaustively track every destination.

**The solution:** Baseline creation through multiple collection points — edge firewall logs + identity injection, Internet proxy logs, NetFlow (Cisco Secure Network Analytics), endpoint agents (Network Traffic Analysis module), and DNS analytics (Cisco Umbrella). The key insight: "resources to run the business... will be longer lived and more commonly accessed than malware-infected resources, which will need to change servers, hosting providers, or cloud services on a regular basis to avoid detection."

**The firewall rule lifecycle problem:** The authors observe that external access rules are rarely audited or retired. In environments without audit processes, "it's common to have hundreds of thousands of rules, with large percentages representing overlaps in address and purpose." The ZT approach — distributing policy to the access layer based on contextual identity — creates a side benefit: it forces cleanup of poorly managed centralized firewall rules.

### Challenge 4: Macrosegmentation vs. Microsegmentation

**The problem:** How granular is too granular? The VLAN-as-microsegment approach hits hard limits: 4094 maximum VLANs, operational overhead of managing N×(N−1) policy pairs, and firewall throughput scaling issues.

**The solution — Distributed enforcement:** Dynamic VLAN assignment + TrustSec SGTs within VLANs + downloadable ACLs + firewalls for external access. This layered model means the firewall is no longer the sole enforcement point.

**The blast zone calculus:** The authors introduce the concept of "acceptable blast zones" — how many devices can exist between the control point and the endpoints before risk exceeds tolerance? The answer depends on:
- Risk being mitigated
- Data showing how contextual identities interact
- Operational overhead of the proposed segmentation
- Access device capabilities

**The Cisco empirical finding:** "Customers who use dynamic application of enforcement policy have the best likelihood of success when they start with no more than five to seven groups or enclaves." Start broad, get progressively granular over time. Grouping devices that share ports/protocols carries little risk if the devices wouldn't respond to exploits on non-included ports. But grouping mission-critical servers with overlapping ports *without* considering risk of exploitation can be "disastrous."

### Challenge 5: New Endpoint Onboarding ("Day 2 Operations")

**The problem:** Organizations focus on segmenting what's already on the network but neglect the process for new devices. The old model — firewall admins receive tickets requesting "allow our IP range to access these DNS names" without explanation — is incompatible with ZT.

**The solution — Centralized receiving and onboarding:** A secured, isolated network segment with lenient NAC policy, separate Internet access, and full NetFlow collection. The onboarding checklist:
1. Create contextual identity (active + passive profiling)
2. Collect traffic patterns (local switch NetFlow, upstream firewall logs)
3. Document architecture and device capabilities
4. Evaluate authentication capability (802.1X, posture, management enrollment)
5. Assign to a static group in the NAC server → authorization result → distributed enforcement policy

### Challenge 6: Edge/Remote Network Policy Ubiquity

**The problem:** Remote users must receive the same restrictions as on-campus users, but technologies focus on one medium or the other. VPN is seen as a performance impediment, driving interest in VPN-less architectures.

**The solution — Ubiquitous policy through contextual identity:** The location attribute of contextual identity changes (network access device → remote network), but the remaining four attributes should drive the same policy. The authors evaluate three VPN models:

| Model | Strengths | Weaknesses |
|-------|-----------|------------|
| **Client-based VPN** | OS hooks for posture/identity; DNS enforcement; packet redirection for inspection | User friction; client deployment overhead |
| **Clientless VPN (browser-only)** | Low overhead; identity-based tunnel establishment | Only browser traffic encrypted; minimal use cases for non-web apps |
| **Distributed VPN ("branch in a box")** | True office experience; hardware phone/video/test units; same switch configs as in-office; easier vulnerability scanning | Higher cost; hardware provisioning needed; may save money long-term vs. software licensing |

**Identity gateways** (Cisco Duo Access Gateway): A fourth option — redirect web requests to an application gateway that queries a user agent for posture validation before granting access, without a full VPN tunnel. The authors also endorse **MDM-based provisioning** (Meraki Systems Manager) for pushing VPN/client configurations with minimal user steps.

### Challenge 7: The Belief That a Firewall Is Enough

**The problem:** Organizations with large firewall estates believe firewalls alone constitute sufficient segmentation. The math disproves this: a network with 2,046 VLANs passing through a firewall requires a minimum of 12,000 initial rules just for shared services (DNS, DHCP, authentication, remote access protocols, domain controller traffic × 6 per VLAN), not counting business-specific rules.

**The solution — Defense in depth, modeled on universities:** University/research networks treat every endpoint as a threat by default — a model the authors argue all enterprises should adopt:

1. Treat every endpoint as a threat to the network
2. Segment endpoints from everything except critical services
3. Require users to agree to policy stating explicit access requirements
4. Require the level of contextual identity the organization can facilitate
5. Apply enforcement and vulnerability management at network ingress

**The firewall's retained role:** Even in distributed enforcement, the firewall still provides **advanced features that access switches cannot** — intrusion prevention, malware detection, TCP normalization, data loss prevention, VPN termination. But it becomes one layer among many rather than the sole enforcement point. The firewall for external access can typically be a smaller, lower-throughput model because it handles only the subset of traffic actually destined for the Internet.

### Application Security as a ZT Layer

The authors extend defense-in-depth to the application itself:
- **Identity:** External identity providers (social login) or internal SSO with 2FA; token-based session validation to reduce login frequency
- **Vulnerability Management:** Header/body validation, schema enforcement, cross-site scripting and SQL injection prevention, DNS-based origin lookup and geolocation filtering
- **Enforcement:** Role-based access control within the application, with full logging (identity, what was accessed, how, for how long) sent to centralized SIEM

**The cloud implication:** The move of applications from on-premises to cloud, exposed directly to the Internet, means application-level ZT controls become *the* enforcement mechanism — there is no hardware firewall, IPS, or DLP in front. This drives adoption of "as a service" security models.

---

## Ch8: Developing a Successful Segmentation Plan

Chapter 8 is the book's planning and deployment methodology — the bridge between analysis and action.

### Planning: Defining Goals and Objectives

Four business drivers that define the segmentation charter:

1. **Risk Assessments and Compliance:** CMMC, PCI, ISO requirements mapped directly to the five ZT pillars. The authors quote specific CMMC assessment criteria for each pillar (Policy & Governance, Identity, Vulnerability Management, Enforcement, Analytics) to demonstrate regulatory alignment.

2. **Threat Mapping:** Understanding probability × impact of threats (ransomware, malware, phishing, DDoS) on critical systems. The output may influence policy — e.g., the convenience of allowing personal devices may be offset by ransomware likelihood, driving corporate-device-only policies.

3. **Data Protection:** Confidentiality, integrity, availability as the trifecta. For R&D organizations, protecting data access patterns drives the ZT architecture.

4. **Reducing Attack Surfaces:** The default driver — even without a specific regulatory mandate, minimizing the attack surface through ZT principles is self-justifying.

### Two Design Approaches: Top-Down vs. Bottom-Up

The chapter's core planning contribution:

**Top-Down Design:** Business-aligned. Starts with executive buy-in and business drivers, defines segments by business function and regulatory compliance, collects technical artifacts to validate. **Best for:** regulated industries with clear business-unit boundaries, where endpoints cleanly map to organizational units. **Process:** Define business drivers → identify impacted teams → define use cases/workflows → gap analysis → define segments → collect technical artifacts.

**Bottom-Up Design:** Traffic-aligned. Starts with traffic collection and identity mapping, determines segmentation based on observed communication patterns. **Best for:** consulting firms (one person spans multiple business units), shared physical servers hosting multiple business unit VMs, politically siloed organizations where cross-department communication is unknown. **Process:** Collect flows → integrate identity → map identity-to-identity communication → apply enforcement aligned to business units as a secondary step.

**Practical reality:** "The implementation of segmentation may require that both of these strategies be utilized for the best results to be achieved." Use top-down for high-level architecture, bottom-up for validation and detailed policy creation.

### Three Deployment Templates

**1. By Site Type:** Classify sites into categories (technical user sites first for better feedback; revenue-generating sites later to minimize risk). Build reusable patterns/templates. Site-based segmentation might include enclaves for:
- **Business Services** — Managed workstations, BYOD, printers, phones, conferencing (lower risk, easier posture assessment)
- **Building IoT** — Physical security, badge readers, HVAC, lighting (harder to identify/interact with; same NIC make/model may conceal unique devices)
- **Infrastructure Management** — Managed power strips, UPS, environmental sensors (high risk — these are the connectivity conduit for everything else)
- **Guest** — Internet-only access, dedicated DNS/time/DHCP, no internal system interaction
- **Services/Shared Services** — DHCP, DNS, NTP, management, remote desktop (very high risk — all devices depend on these)

**2. By Endpoint Category:** Assumes endpoint categories are similar across sites. Start with homogeneous populations. **Healthcare example:** Imaging (MRI/CT/radiology — peer-to-peer backups and streaming, medium risk), Pharma (medicine stations, anesthesia — medium risk, high sensitivity), Point of Care (infusion pumps, monitors — high risk due to direct patient impact, last to receive enforcement), Labs (diagnostic instruments — low risk), Clinical VDI (thin clients — policy at VDI manager level rather than physical switch).

**Warning:** "One organization went so far as to attempt to describe endpoints based on age, a futile attempt to segment devices from one another given their need for the same access." Categorizations must be actionable from available contextual identity data.

**3. By Service Type (Boundary Services):** Focuses on policy enforcement points at organizational boundaries:
- Partner/Vendor Remote Access VPN — semi-trusted access to defined resources
- Employee Remote Access VPN — granular access based on resource categorization
- Partner Leased Lines — "trusted DMZ" for third-party access without client/VPN
- DMZ Services — public-facing web/services with secondary secured backend connections (very high risk)
- Corporate WAN — backbone circuits between locations; prime area for firewalls/IPS (very high risk)
- Employee Outbound Internet — filtering, caching, SaaS access
- Guest Outbound Internet — physically separate hardware and services (low risk)
- Unknown — initial open policy, progressively restricted as devices are identified and categorized

### The Segmentation Model (Policy Decision Matrix)

The output of the planning process: a matrix mapping source entities (rows) to destination entities (columns), with each cell defining:
- **Simple permit/deny** — All traffic allowed or blocked between the two entities
- **Port/protocol policy** — Granular control specifying which ports and protocols are permitted
- **Directionality** — Traffic is expected to be initiated in one direction only in many cases

The authors note multiple matrices will be needed — intra-data center, inter-site, and potentially per-business-unit.

### Implementation Guidance

- **Monitor mode first:** "The organization should implement a discovery or monitor mode for as long as possible, and in parallel to other enforcement tasks being executed."
- **On-site representation:** Helps determine entity identity when dynamic classification fails.
- **Distributed enforcement paradigm:** No longer a single appliance; multiple enforcement points throughout the network.
- **Brownfield vs. greenfield:** Different approaches for each; careful documentation of profiling lessons from monitor mode eases the transition to enforcement.
- **Authorization as the outcome:** "Authorization of entities should be considered the most important outcome of the Zero Trust journey." Special considerations for positively identified entities, greenfield/brownfield environments, and unified communications devices.

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
