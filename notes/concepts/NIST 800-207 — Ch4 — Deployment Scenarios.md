---
tags:
  - source/standards
  - nist
  - zt-deployment
  - use-cases
  - multi-cloud
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
confidence: very-high
source:
  title: "NIST SP 800-207 — Zero Trust Architecture"
  authors: "Scott Rose, Oliver Borchert, Stu Mitchell, Sean Connelly"
  year: 2020
  publisher: "National Institute of Standards and Technology"
  local_file: "sources/standards/_txt/NIST_SP_800-207_Zero_Trust_Architecture.txt"
  lines: "1290–1461"
related:
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[DoD ZT Reference Architecture v2]]"
  - "[[BeyondCorp — A New Approach]]"
  - "[[Green-Ortiz — ZT Implementation Patterns]]"
  - "[[Concepts Index]]"
---

# NIST SP 800-207 — Ch4: Deployment Scenarios

This chapter translates the abstract ZT tenets and PDP/PEP architecture (Ch 2–3) into five concrete deployment scenarios. Unlike vendor marketing that treats "Zero Trust" as a single product or deployment model, NIST shows that ZTA adapts to the specific flows of subjects, resources, and trust boundaries in each scenario. The unifying principle across all five is that the PEP should sit as close to the resource as possible, and the PA/PE should make per-request, context-aware decisions regardless of where the subject is coming from.

### Claim 1: The five scenarios are not mutually exclusive — real enterprises combine them

**NIST's claim:** "Any enterprise environment can be designed with zero trust tenets in mind... ZTA is not explicitly indicated since the enterprise likely has both perimeter-based and possibly ZTA infrastructures" (4.0). NIST acknowledges that most enterprises will operate in a hybrid state (see Ch 7.2) where ZTA and perimeter-based security coexist.

**Evidence presented:** The five scenarios are presented as lenses, not silos. An enterprise with satellite facilities (4.1) may also use multiple clouds (4.2), host contractors (4.3), collaborate with partners (4.4), and serve public-facing applications (4.5). The scenarios compound.

**Confidence:** HIGH. The chapter opens with this disclaimer explicitly. Real federal agencies combine all five scenarios daily.

**What's at stake:** Treating scenarios as silos leads to fragmented ZT deployment — a different architecture per scenario rather than a unified PDP/PA/PEP infrastructure. NIST's framing allows one policy engine to govern multiple scenarios simultaneously.

**Who disagrees:** Vendor ZTNA products often address only scenarios 4.1 and 4.4 (remote access and cross-enterprise). The other scenarios are left to different product categories (CASB for cloud, NAC for contractors, WAF for public-facing). This is a product taxonomy problem, not an architectural one — NIST shows the same logical components apply everywhere.

---

### Claim 2: For satellite facilities and remote workers, the PE/PA must be hosted as a cloud service to avoid hairpinning traffic through HQ — the MPLS link to HQ becomes a commodity transport, not a security boundary. (Scenario 4.1)

## Scenario 4.1: Enterprise with Satellite Facilities

**NIST's description:** An enterprise with a headquarters and geographically dispersed locations not joined by an enterprise-owned physical network. Remote employees may use enterprise-owned or personally-owned devices. The enterprise wants to grant access to some resources (email, calendar) while denying or restricting access to more sensitive resources (HR database). This is the most common scenario and the one closest to ZTA's historical roots.

**How ZTA applies:**

- **PE/PA hosted as a cloud service** — avoids forcing remote traffic to hairpin through the enterprise HQ network. "It may not be most responsive to have the PE/PA(s) hosted on the enterprise local network as remote offices and workers must send all traffic back to the enterprise network to reach applications/services hosted by cloud services."
- **Endpoint agent or resource portal** — subjects access resources through an installed agent (Section 3.2.1) or a web gateway portal (Section 3.2.3). Both patterns appear: agents for managed devices, portals for unmanaged or limited-use devices.
- **MPLS bandwidth constraints** — NIST flags the practical problem: an MPLS link to HQ may not have adequate bandwidth for all traffic, and the enterprise may not *want* cloud-destined traffic to traverse HQ. This is the architectural rationale for cloud-hosted PE/PA.

**Cross-references:**

| Source | How It Relates |
|--------|---------------|
| **BeyondCorp** (Google) | This IS BeyondCorp's founding use case. Google's entire architecture was built to eliminate the distinction between "on-campus" and "remote" access. BeyondCorp's access proxy sits at the edge of every application, and device trust is continuously assessed — the canonical implementation of NIST 4.1. |
| **DoD ZT Reference Architecture v2** | The DoD RA addresses this through the User Pillar and Device Pillar — Continuous Multi-Factor Authentication (CMFA) and Comply-to-Connect for endpoints. But DoD frames it through technology pillars rather than deployment topology. |
| **Green-Ortiz (Cisco Press)** | Green-Ortiz covers branch/campus ZT deployment in Ch 3–4. Their "SBC Inc." case study (Appendix A) mirrors satellite facility challenges: 175 campuses and branches with contractor access, simplified through identity-based policy rather than per-firewall IP rules. |

**Confidence:** VERY HIGH. This is the canonical ZT use case and the strongest architectural argument against VPNs.

**Operational implication:** The satellite facility scenario is where the "death of the VPN" argument is strongest. If PE/PA is cloud-hosted and resources are accessed through agents/portals, the MPLS link to HQ becomes a commodity transport, not a security boundary.

---

### Claim 3: Multi-cloud environments require the SDP server-to-server model — a PEP at each cloud-hosted service, no enterprise network hairpinning, and the enterprise perimeter is irrelevant to the security model. (Scenario 4.2)

## Scenario 4.2: Multi-cloud/Cloud-to-Cloud Enterprise

**NIST's description:** An enterprise uses two or more cloud providers to host applications and data. Sometimes the application and its data source reside in different clouds. For performance, the application in Cloud A should connect directly to the data source in Cloud B — not tunnel through the enterprise network. This is a **server-to-server** deployment.

**How ZTA applies:**

- **PEP at each application/data access point** — each cloud-hosted service gets its own PEP. The PE and PA can be services in either cloud, or even a third cloud provider. This is the Software-Defined Perimeter (SDP) model applied to cloud workloads.
- **No enterprise network hairpinning** — traffic flows directly between cloud providers. The enterprise perimeter is irrelevant to the security model.
- **CSA SDP specification** — NIST explicitly references the Cloud Security Alliance's SDP spec as the canonical implementation pattern for this scenario. "This use case is the server-server implementation of the CSA's software defined perimeter (SDP) specification [CSA-SDP]."

**Key challenge NIST identifies:** "Different cloud providers have unique ways of implementing similar functionality. Enterprise architects will need to be aware of how to implement their enterprise ZTA with each cloud provider they utilize." This is a vendor lock-in / multi-cloud complexity warning.

**Cross-references:**

| Source | How It Relates |
|--------|---------------|
| **BeyondCorp → BeyondProd** (Google) | BeyondProd extends the BeyondCorp model to service-to-service communication in cloud-native environments. It's the architectural bridge between ZTNA (user-to-app) and service mesh security (app-to-app). Google's approach: mutual TLS between services, workload identity rather than network identity, and continuous trust evaluation at the service boundary. |
| **DoD ZT Reference Architecture v2** | The DoD RA addresses cloud deployment through the Network/Environment Pillar — microsegmentation, SDP, and cloud access points aligned to DoD Cloud Computing SRG. The DoD's "Target-Level ZT" includes cloud-native workload identity. |
| **Green-Ortiz (Cisco Press)** | Ch 4 covers "cloud enclave design" — applying ZT policy at cloud ingress/egress points. Green-Ortiz's five ZT capabilities (Policy & Governance, Identity, Vulnerability Management, Enforcement, Analytics) apply identically across on-prem and cloud environments, which maps directly to NIST's point that "there should be no difference between enterprise-owned and -operated network infrastructure and infrastructure owned and operated by any other service provider." |

**Confidence:** VERY HIGH. This scenario is the theoretical death blow to perimeter-centric architectures.

**Operational implication:** The multi-cloud scenario is the strongest argument against perimeter-based security. When applications and data live in clouds the enterprise doesn't own, the enterprise perimeter is not just irrelevant — it's an architectural obstacle. ZT enforces access at the workload level, not the network level.

---

### Claim 4: Contracted services and nonemployee access should use the SDP "dark network" model — enterprise resources are obscured from network discovery, preventing lateral movement, with the PA ensuring nonenterprise assets can access the internet but cannot discover or reach enterprise resources. (Scenario 4.3)

## Scenario 4.3: Enterprise with Contracted Services and/or Nonemployee Access

**NIST's description:** On-site visitors and contracted service providers (e.g., smart HVAC technicians) need limited access to enterprise resources. The ZTA approach: allow these devices and technicians internet access while **obscuring enterprise resources** — preventing network discovery and lateral movement. This is the "untrusted guest on the enterprise LAN" problem.

**How ZTA applies:**

- **PE/PA hosted as cloud service or on LAN** — depending on cloud usage. If the enterprise primarily uses on-prem resources, the PE/PA sits on the LAN. If cloud-hosted resources dominate, PE/PA is cloud-hosted.
- **Agent or portal for enterprise assets** — enterprise-managed devices use agents; everything else can't access local resources at all. "The PA(s) ensures that all nonenterprise assets (those that do not have installed agents or cannot connect to a portal) cannot access local resources but may access the internet."
- **Network obscurity via SDP** — visitors "may not even be able to discover enterprise services via network scans (i.e., prevent active network reconnaissance/east-west movement)." This is the SDP "dark network" property: services are invisible until authenticated.

**Cross-references:**

| Source | How It Relates |
|--------|---------------|
| **BeyondCorp** (Google) | Google's "unprivileged network" is the canonical implementation of this scenario. The unprivileged network provides only internet access, DNS, NTP, and DHCP — no access to corporate applications. Contractors, guests, and BYOD devices land on the unprivileged network by default. Access to corporate resources goes through the access proxy with full device/user trust evaluation. |
| **DoD ZT Reference Architecture v2** | Addressed through the Device Pillar (Comply-to-Connect — devices must prove compliance before network access) and the User Pillar (identity-based, not IP-based, access). The DoD's "least privilege" principle maps directly to this scenario: contractors get exactly the access their role requires, nothing more. |
| **Green-Ortiz (Cisco Press)** | Appendix A (SBC Inc. case study) has extensive contractor access patterns: 350,000 firewall rules reduced to identity-based policy for contractors accessing Smart Building Central. Green-Ortiz shows the practical process: audit, identity-link, reduce, and replace IP-based rules with contextual identity policies (who, what, where, when, how). This is the operationalization of NIST's architectural prescription. |

**Confidence:** HIGH. The SDP dark network model is architecturally sound but deployment complexity can undermine the "invisible resources" property.

**Operational implication:** The contracted services scenario exposes the fragility of perimeter-based NAC solutions. If a contractor's laptop is on the LAN, NAC grants network access — but NIST's ZTA says *no* network access, only *resource-specific* access through a PEP. The contractor's device may have internet access on the same physical network without ever discovering enterprise resources.

---

### Claim 5: Cross-enterprise collaboration should use federated identity plus resource-specific PEPs — this scales linearly with partners, while the alternative (bilateral VPNs, shared AD domains, per-partner firewall rules) creates O(n²) complexity. (Scenario 4.4)

## Scenario 4.4: Collaboration Across Enterprise Boundaries

**NIST's description:** Two enterprises (e.g., federal agencies, or a federal agency and a private company — G2G or G2B) collaborate on a project. Enterprise A operates a database but must grant access to certain Enterprise B employees — without granting access to any other Enterprise A resources. This is the **federated identity** scenario.

**How ZTA applies:**

- **Federated ID management** — both organizations enrolled in a federated identity system. Enterprise B subjects authenticate through their own IdP, and Enterprise A's PEP trusts the federated assertion. No separate Enterprise A accounts needed.
- **No complex firewall rules or ACLs** — "there do not need to be complex firewall rules or enterprise-wide access control lists (ACLs) allowing certain IP addresses belonging to Enterprise B to access resources in Enterprise A based on Enterprise A's access policies."
- **Cloud-hosted PE/PA** — "a PE and PA hosted as a cloud service may provide availability to all parties without having to establish a VPN or similar." Cross-enterprise access shouldn't require bilateral network integration.
- **Agent or web gateway access** — Enterprise B employees use an installed agent or a portal, identical to Scenario 4.1.

**Cross-references:**

| Source | How It Relates |
|--------|---------------|
| **BeyondCorp** (Google) | Google's federated access model for partners and acquired companies. BeyondCorp's access proxy can consume federated identity assertions — partners authenticate at their own IdP, and Google's policy engine makes access decisions based on the federated claim. This is exactly NIST's scenario. |
| **DoD ZT Reference Architecture v2** | The DoD RA emphasizes "joint all-domain" operations requiring cross-agency and cross-classification data sharing. The User Pillar explicitly addresses federated identity and attribute-based access control (ABAC) — the mechanism for granting Enterprise B members access to specific Enterprise A resources without full network integration. |
| **Green-Ortiz (Cisco Press)** | Ch 5 ("Enclave Exploration and Consideration") covers cross-organization considerations. Green-Ortiz emphasizes that different organizations may have different ZT maturity levels, and the collaboration boundary must accommodate the least mature partner — a practical constraint NIST doesn't address. |

**Confidence:** HIGH. The federated identity pattern is well-established and the scaling argument is mathematically sound.

**Operational implication:** Cross-enterprise collaboration is the scenario where ZT pays for itself fastest. The alternative — bilateral VPNs, shared AD domains, per-partner firewall rules — creates an O(n²) complexity problem. Federated identity + resource-specific PEPs scales linearly with the number of partners. This is the pattern that enables secure government-to-contractor collaboration without network-level trust.

---

### Claim 6: Public-facing services expose ZTA's boundary — ZT tenets do not directly apply to anonymous public resources, and for registered users the enterprise is constrained in what cybersecurity policies can be enforced on nonenterprise-owned devices, limiting ZTA to behavioral monitoring and graduated enforcement. (Scenario 4.5)

## Scenario 4.5: Enterprise with Public- or Customer-Facing Services

**NIST's description:** Public-facing services that may or may not require user registration. This covers anonymous public resources (e.g., a public web page), registered customers with business relationships, and special users (e.g., employee dependents). The key constraint: **requesting assets are not enterprise-owned, and the enterprise is limited in what cybersecurity policies it can enforce.**

**How ZTA applies:**

- **Anonymous public resources**: ZT tenets "do not directly apply." The enterprise cannot control the state of requesting assets, and anonymous resources don't require credentials. NIST is honest here: ZT has limits.
- **Registered public users**: The enterprise can enforce password policies, MFA, and credential lifecycle management. But it "is constrained as to what internal cybersecurity polices can be enforced on nonenterprise-owned devices."
- **Behavioral monitoring for attack detection**: "A sudden increase in access requests from unknown browser types or known outdated versions could indicate an automated attack of some kind, and the enterprise could take steps to limit requests from these identified clients." This is ZT-adjacent — using telemetry from incoming requests for threat detection, even without device trust.
- **Legal/regulatory constraints**: "The enterprise should also be aware of any statutes or regulations regarding what information can be collected and recorded about the requesting users and assets." Privacy limitations on user/device data collection constrain ZT telemetry in this scenario.

**Cross-references:**

| Source | How It Relates |
|--------|---------------|
| **BeyondCorp** (Google) | Google's public-facing services (Gmail, G Suite) use the same access proxy infrastructure as internal services. Registered users (customers) authenticate and the proxy evaluates device/browser signals. Anonymous services (google.com) don't route through the proxy. This mirrors NIST's split: registered = ZT applies, anonymous = ZT doesn't apply. |
| **DoD ZT Reference Architecture v2** | The DoD RA's Data Pillar addresses public-facing data access through encryption, DRM, and DLP. For registered users accessing DoD data portals (e.g., veteran benefits), attribute-based access control and continuous monitoring apply — but DoD can mandate CAC/PIV for military users, while public users can't be required to use government-issued hardware. |
| **Green-Ortiz (Cisco Press)** | Ch 9 ("Zero Trust Enforcement") addresses graduated enforcement: different policy strictness for managed vs. unmanaged devices. For registered public users with unmanaged devices, Green-Ortiz would apply baseline policies (MFA, geolocation checks, behavioral analytics) without requiring device agents. This is the practical implementation of NIST's "limited to what can be enforced." |

**Confidence:** VERY HIGH. NIST's honesty about ZTA's limits here is as important as its prescriptions — this is the boundary condition that prevents ZT overreach claims.

**Operational implication:** Scenario 4.5 is NIST's admission that ZT has a boundary. You can't enforce device trust on a customer's personal laptop. The best you can do is behavioral analytics at the application layer. This is the scenario where ZTA blurs into traditional application security — WAF, bot detection, rate limiting — which NIST doesn't dwell on. The chapter's honesty about this limitation is as important as its prescriptions for the other four scenarios.

---

## Chapter 4 Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| Five scenarios are compounding, not siloed | HIGH | Vendor products that address one scenario as "ZT" |
| Satellite facilities = cloud-hosted PE/PA (4.1) | VERY HIGH | Legacy VPN vendors claiming VPN is still necessary |
| Multi-cloud = SDP server-to-server (4.2) | VERY HIGH | Cloud-provider-native IAM replacing cross-cloud ZT |
| Contractors = SDP dark network (4.3) | HIGH | NAC solutions masking as ZT without resource-level PEPs |
| Cross-enterprise = federated ID + PEP (4.4) | HIGH | Bilateral network integration inertia in government |
| Public-facing: ZT has limits (4.5) | VERY HIGH | Overreach claims that ZT secures everything |
| PE/PA hosting location varies by scenario | VERY HIGH | One-size-fits-all deployment architectures |

**Strongest section:** Scenario 4.2 (multi-cloud). NIST correctly identifies that the multi-cloud case makes perimeter-based security not just obsolete but actively harmful — forcing cloud-to-cloud traffic through the enterprise network creates latency, cost, and a single point of failure. The CSA SDP reference is the right citation. This scenario is the theoretical death blow to perimeter-centric architectures.

**Weakest section:** Scenario 4.5 (public-facing). NIST acknowledges ZT's limits here but doesn't provide an alternative framework. The behavioral monitoring suggestion is underdeveloped — it's more of a WAF/SIEM discussion than a ZT discussion. This section exposes a genuine gap: ZT assumes the enterprise can assess device posture, but public-facing services can't.

**Most important structural insight:** Across all five scenarios, the PE/PA hosting decision is the key architectural variable. NIST presents three options: cloud-hosted (best for scenarios 4.1, 4.2, 4.4), LAN-hosted (possible for 4.3 if on-prem dominant), or a mix. The scenarios aren't about *different architectures* — they're about *different PE/PA placement patterns* within the same PDP/PEP model. This is the chapter's implicit argument: ZTA is one architecture that scales across all deployment topologies.

**Cross-source synthesis:**

| NIST Scenario | BeyondCorp Mapping | DoD ZT RA Pillar | Green-Ortiz Chapter |
|--------------|-------------------|-----------------|-------------------|
| 4.1 Satellite | Access Proxy + Device Trust | User + Device Pillars | Ch 3–4 (Branch/Campus ZT) |
| 4.2 Multi-cloud | BeyondProd (service mesh) | Network/Environment Pillar | Ch 4 (Cloud Enclave) |
| 4.3 Contractors | Unprivileged Network | Device Pillar (Comply-to-Connect) | Appendix A (SBC Inc. contractors) |
| 4.4 Cross-enterprise | Federated Access Proxy | User Pillar (ABAC/Federation) | Ch 5 (Enclave Exploration) |
| 4.5 Public-facing | Gmail/G Suite public proxy | Data Pillar (DRM/DLP) | Ch 9 (Graduated Enforcement) |

**Missing from NIST:** The chapter doesn't address *operational sequencing* — which scenario to deploy first, or how to prioritize. Ch 7 (migration) partially addresses this at the capability level, but the scenario-level sequencing question is left to the implementer. This is where Green-Ortiz (Ch 8: "Developing a Successful Segmentation Plan") and the DoD ZT Strategy & Roadmap (phased capability deployment) fill the gap.
