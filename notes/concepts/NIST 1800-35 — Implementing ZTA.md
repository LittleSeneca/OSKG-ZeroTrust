---
tags:
  - source/standards
  - nist
  - zt-implementation
  - zt-vendors
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
confidence: high
source:
  title: "NIST SP 1800-35 — Implementing a Zero Trust Architecture (Final v2)"
  authors: "Oliver Borchert, Gema Howell, Alper Kerman, Scott Rose, Murugiah Souppaya (NIST); Jason Ajmo, Yemi Fashina, Parisa Grayeli et al. (MITRE); Karen Scarfone (Scarfone Cybersecurity); William Barker (Dakota Consulting); plus 24 vendor collaborators"
  year: 2025
  publisher: "NIST National Cybersecurity Center of Excellence (NCCoE)"
  local_file: "sources/papers/_txt/NIST_SP_1800-35_FINAL_v2.txt"
related:
  - "[[NIST 800-207 — Ch1 — Introduction]]"
  - "[[NIST 800-207 — Ch7 — Migration]]"
  - "[[NIST 800-207A — Cloud-Native Access Control]]"
  - "[[CISA ZTMM — Overview and Framework]]"
  - "[[Concepts Index]]"
  - "[[Standards Index]]"
  - "[[Notes Index]]"
---

# NIST SP 1800-35 — Implementing a Zero Trust Architecture

NIST SP 1800-35 is the most comprehensive vendor-neutral ZTA implementation guide ever published. Produced by the NCCoE with 24 commercial technology collaborators under CRADAs, it documents 19 end-to-end ZTA example implementations ("builds") deployed across four simulated enterprise environments in a physical laboratory. Published June 2025, it is the practical companion to SP 800-207 — where 800-207 defines *what* ZTA is, 1800-35 demonstrates *how* to build it with commercially available technology. The guide spans four ZTA deployment approaches (EIG, SDP, Microsegmentation, SASE) across three maturity phases, exhaustively documents integration patterns and pitfalls, and provides a seven-step ZTA journey framework. It is the definitive reference for organizations that need to *build* ZTA, not just understand it.

---

## §1: Project Structure — Four Enterprises, Three Phases, Four Architectural Approaches (§2–§3)

### Claim 1: ZTA implementation is not a single architecture but a spectrum of deployment approaches — EIG, SDP, Microsegmentation, and SASE — each appropriate for different organizational contexts and maturity levels. The most complete ZTAs combine multiple approaches.

**Author's structure:**
The project organized 19 builds across four simulated enterprises, each representing a different organizational starting point. Each enterprise could host multiple builds with different vendor combinations:

**Four ZTA deployment approaches:**
1. **Enhanced Identity Governance (EIG)** — Leverages ICAM solutions as Policy Decision Points. The identity-centric approach — authenticate users and devices, make access decisions based on identity attributes and endpoint health. Foundation of ZTA. Two phases: Crawl (on-premises only) and Run (adds cloud capabilities).
2. **Software-Defined Perimeter (SDP)** — Reconfigures network connectivity based on access decisions. Establishes secure tunnels between requesting endpoints and resources. Application-layer SDP uses agents on endpoints; network-layer SDP uses gateway appliances. "Darkens" resources — they're not discoverable until access is granted.
3. **Microsegmentation** — Places resources on unique network segments protected by gateway components and/or host-based agents. Fine-grained east-west traffic control within the perimeter. Can be network-based (VLANs, firewall rules) or host-based (software agents on endpoints).
4. **Secure Access Service Edge (SASE)** — Converged network + security delivered as a cloud service. Includes SD-WAN, SWG, CASB, NGFW, and ZTNA. Primarily cloud-delivered; enables identity-based zero trust access with real-time context.

**Three implementation phases:**
- **EIG Crawl** (3 builds) — Minimum viable ZTA: ICAM + endpoint security + SIEM. On-premises only. No cloud, no SDP, no microsegmentation. Demonstrates what organizations can achieve with legacy ICAM without adding ZTA-specific capabilities.
- **EIG Run** (3 builds) — Adds cloud-hosted resources, device discovery with enforcement, secure tunnels to private resources, proxy connectors for resource invisibility. Cloud capabilities without full SDP/SASE investment.
- **SDP, Microsegmentation, and SASE** (13 builds) — Unconstrained ZTA reference architecture. All four deployment approaches, singly and in combination. Full supporting component integration (data security, security analytics, advanced endpoint protection).

**Confidence:** HIGH. The four-approach taxonomy is consistent with SP 800-207's deployment models and reflects real market segmentation. The phased crawl→run→advanced approach is the document's most important architectural contribution — it gives organizations a clear maturity ladder.

**What's at stake:** If organizations treat the approaches as mutually exclusive, they'll miss the integration value. The builds that combine approaches (SDP + Microsegmentation, SDP + SASE) demonstrated richer ZTA functionality than single-approach builds. The phased approach counters vendor claims that ZTA requires wholesale replacement.

**My assessment:** The four-approach taxonomy is the document's conceptual backbone and will age well. The market is evolving toward convergence (SASE incorporating SDP; microsegmentation incorporating identity), but the taxonomy captures distinct architectural patterns that remain useful for planning. The crawl→run→advanced phasing is the most important takeaway for organizations — it directly refutes "ZTA is too hard/complex/expensive" objections.

---

## §2: The 19 Builds — Implementation Patterns and Vendor Landscape (§3.6, §4)

### Claim 2: The 19 builds demonstrate that ZTA can be implemented with diverse vendor combinations, but integration gaps between PDPs, PEPs, and supporting components remain the primary practical challenge — not the ZTA concept itself.

**The 19 builds organized by deployment approach:**

| Build | PE/PDP | Approach | Key Pattern |
|-------|--------|----------|-------------|
| **EIG Crawl Phase** | | | |
| E1B1 | Okta + Ivanti | EIG Crawl | Multi-vendor ICAM: Okta for identity federation, Ivanti for ZSO, SailPoint for IGA, Radiant Logic for identity data platform |
| E2B1 | Ping Identity | EIG Crawl | Single-vendor ICAM: PingFederate as PE, Cisco Duo as PEP |
| E3B1 | Microsoft (Azure AD) | EIG Crawl | Microsoft-centric: Azure AD Conditional Access, Defender for Endpoint, Intune |
| **EIG Run Phase** | | | |
| E1B2 | Zscaler | EIG Run | Cloud-delivered PE: Zscaler ZPA Central Authority as PE/PA/PEP, ZCC client connector |
| E3B2 | Microsoft + Forescout | EIG Run | Hybrid PE: Azure AD + Intune + Forescout eyeControl/eyeExtend |
| E4B3 | IBM Security Verify | EIG Run | IBM-centric: IBM Verify as PE, MaaS360 for UEM, QRadar for SIEM |
| **SDP/Microsegmentation/SASE Phase** | | | |
| E1B3 | Zscaler | SDP | ZPA as SDP controller — secure tunnels, resource darkening |
| E2B3 | Cisco + Ping | Microsegmentation | Cisco ISE + Secure Workload for network microsegmentation, PingFederate for identity |
| E3B3 | Microsoft + Forescout | SDP + Microseg | Combined approach: Microsoft Conditional Access + Forescout eyeSegment |
| E1B4 | Appgate | SDP | Pure-play SDP: Appgate SDP Controller, Gateway, Client |
| E2B4 | Broadcom (Symantec) | SDP + SASE | Symantec Cloud SWG + ZTNA + CASB — SASE with SDP overlay |
| E3B4 | F5 | SDP | Application-delivery-centric SDP: F5 BIG-IP + NGINX Plus |
| E4B4 | Broadcom (VMware) | SDP + Microseg + EIG | VMware Workspace ONE + NSX-T — comprehensive on-prem ZTA |
| E1B5 | Palo Alto Networks | Microseg + SASE | PAN NGFW + Prisma Access + Prisma SASE — network-centric approach |
| E2B5 | Lookout + Okta | SDP + SASE | Cloud-native SASE: Lookout SSE (SPA/SCA/SIA) + Okta Identity Cloud |
| E3B5 | Microsoft Entra + SSE | SDP + SASE | Microsoft-native SASE: Entra Conditional Access + Security Service Edge (Private Access, Internet Access) |
| E4B5 | AWS Verified Access + VPC Lattice | SDP + Microseg | Cloud-provider-native: AWS Verified Access for user-to-app, VPC Lattice for service-to-service |
| E1B6 | Ivanti nZTA | SDP + Microseg | Ivanti Neurons for Zero Trust Access as PE |
| E2B6 | Google CEP | SASE | Google Chrome Enterprise Premium — Access Context Manager as PE |

**Vendor landscape patterns observed:**
- **24 collaborators:** Appgate, AWS, Broadcom, Cisco, DigiCert, F5, Forescout, Google Cloud, IBM, Ivanti, Lookout, Mandiant, Microsoft, Okta, Omnissa, Palo Alto Networks, PC Matic, Ping Identity, Radiant Logic, SailPoint, Tenable, Trellix, Zimperium, Zscaler.
- **Vendor concentration:** Microsoft appears in 6 builds (most widely integrated). Okta appears in 7 builds as the identity federation layer. Tenable appears in nearly every build for vulnerability/asset context. Mandiant (MSV) is in every build for security validation. DigiCert provides certificates across all builds.
- **Architecture archetypes:**
  1. **Single-vendor stacks** (E3B1, E4B3, E1B5, E3B5, E4B5) — Microsoft, IBM, Palo Alto Networks, or AWS providing most ZTA components. Tighter integration, fewer gaps, but vendor lock-in risk.
  2. **Best-of-breed integrations** (E1B1, E2B3, E2B5) — Identity from one vendor (Okta/Ping), network from another (Cisco/Zscaler), endpoint from a third. Richer capability but integration gaps.
  3. **Cloud-provider-native** (E4B5, E2B6) — AWS Verified Access or Google CEP as the ZTA backbone. Leverages cloud provider's identity and network infrastructure.
- **Identity federation is universal.** Every build, regardless of approach, has an ICAM/PDP component. No ZTA exists without strong identity.
- **SIEM is universal.** IBM QRadar or Microsoft Sentinel in every build — monitoring is non-negotiable.
- **Certificate infrastructure is universal.** DigiCert in every build — PKI is the silent foundation of ZTA.

**Confidence:** HIGH on the build descriptions — these are documented implementations, not theoretical architectures. MEDIUM on generalization — the lab environment was clean and controlled; real enterprise environments have legacy constraints the lab doesn't capture.

**What's at stake:** The 19 builds demonstrate that ZTA is *buildable* with commercially available technology. This is the document's primary value — it refutes the claim that ZTA is theoretical or requires custom development. But the integration gaps documented in §5 show that *building* and *operating* are different challenges.

**My assessment:** The build matrix is the document's center of gravity. It provides a menu of approaches that organizations can map to their existing vendor relationships and technical constraints. The patterns are more valuable than the individual builds — single-vendor vs. best-of-breed vs. cloud-native are genuine architectural choices with different tradeoffs. The document doesn't recommend one over another, which is appropriate but leaves organizations without clear decision criteria.

---

## §3: Key Findings — What Actually Works and What's Still Broken (§5)

### Claim 3: The EIG crawl phase proved that legacy ICAM solutions can serve as PDPs for basic ZTA, but resource management (authenticating and verifying the health of the endpoint hosting the resource) is beyond current out-of-the-box integration capabilities.

**EIG Crawl findings (lines 1381–1418):**
- **What worked:** All three EIG crawl builds (E1B1, E2B1, E3B1) could authenticate/reauthenticate users and endpoints, verify endpoint health, and make access decisions based on those factors. Periodic reauthentication and session termination on failure was demonstrated.
- **What didn't work:** None could authenticate the *resource-hosting* endpoint or verify its health. Resource management (steps R(1) and R(A)–R(D) in the ZTA reference architecture) was entirely absent. Devices were joined to the network manually — no network-level enforcement prevented non-authenticated devices from connecting.
- **Integration reality:** "Many of the vendor solutions used in the EIG crawl phase do not integrate with each other out-of-the-box in ways that are needed to enable the ICAM solutions to function as PDPs." Network-level PEPs (routers, switches, firewalls) generally don't integrate with ICAM unless they're identity-aware. Endpoint protection solutions don't typically integrate directly with ICAM — they integrate through MDM/UEM intermediaries.

**EIG Run findings (lines 1420–1472):**
- **What was gained over crawl:** Secure tunnels from endpoints to private resources (on-premises and cloud), proxy connectors for resource invisibility, direct cloud resource access without hairpinning through enterprise network, device discovery with policy-based blocking, cloud traffic monitoring/enforcement.
- **Gaps identified:** E1B2 (Zscaler) had no EPP — Zscaler's client connector does compliance checks but isn't a full endpoint protection platform. No automatic endpoint remediation. No confidence level/trust score calculation due to missing collaborator integration. E2B1 had no EPP at all — Cisco Duo provides limited device health info. E3B2 had one-way Forescout → Intune integration but couldn't pass Forescout-discovered endpoint issues back to Intune for Azure AD enforcement.
- **Core lesson:** "When planning a ZTA implementation, organizations should ensure that all of the ZTA core and supporting components that can integrate with each other are selected. This enables having end-to-end ZTA with full functionality." (lines 1460–1462)

**SDP/Microsegmentation/SASE findings (lines 1478–1512):**
- **Multi-PDP fragmentation:** "It is not unusual for a ZTA to have multiple PDPs... the policies that the ZTA enforces are not centrally located. Rather, they are configured and managed in association with each of the various PDPs. This makes it challenging to understand, articulate, and manage the ZTA's policies as a comprehensive whole." (lines 1482–1486)
- **PDP information silos:** Multiple PDPs don't share information — one PDP may know an endpoint is non-compliant, another may know the user exhibited suspicious behavior, but neither has the full picture. "Ideally, when a ZTA has multiple PDPs, it is desirable to have an integrated approach that enables the PDPs to share information so that they can each be more fully informed." (lines 1492–1494)
- **SIEM → PDP integration gap:** SIEM/SOAR components contain rich information useful for access decisions but "ideally... should send this information to the PDP in real-time, if possible" — implying this isn't standard today.
- **Resource management maturity gap:** SDP endpoint management solutions *can* manage resources by installing clients on them, but "solutions that are specifically designed to manage resources should be leveraged rather than the zero trust solutions that have the primary purpose of managing endpoints." PDP integration with resource management tools remains weak.
- **Endpoint compliance is non-negotiable:** "It is important to have tools that are capable of detecting when an endpoint is not compliant and ensuring that the endpoint is not permitted to access resources as a result." Automatic remediation should be integrated with configuration/patch management.

**Confidence:** HIGH on the findings themselves — these are documented observations from real lab implementations. HIGH on the generalizability of the integration gap findings — multi-vendor integration challenges are a universal enterprise problem, not specific to the NCCoE lab.

**What's at stake:** The integration gaps are the real barrier to ZTA adoption, not the conceptual framework. If PDPs can't share information, if resource management remains manual, if endpoint protection doesn't integrate with ICAM, the ZTA is incomplete regardless of how well-designed the architecture is. These findings should shape procurement requirements — organizations should prioritize integration capability over individual product features.

**My assessment:** These findings are the most honest and valuable part of the document. NIST doesn't pretend everything worked perfectly — they document the gaps, the workarounds, and the ideal state. The multi-PDP fragmentation finding is particularly important: it identifies a genuine architectural tension in ZTA (distributed decision-making vs. centralized policy management) that no vendor has fully resolved. The SIEM→PDP real-time integration gap is the most actionable finding — security analytics information needs to flow into access decisions, not just sit in dashboards.

---

## §4: The Seven-Step ZTA Journey (§8)

### Claim 4: ZTA implementation is a continuous improvement journey, not a one-time project — seven sequential steps, with discovery and identity as the non-negotiable foundations.

**The seven steps** (lines 2320–2528):

1. **Discover and Inventory the Existing Environment** (§8.1)
   - Identify all assets: hardware, software, applications, data, services — on-premises and cloud.
   - Deploy tools to monitor traffic and discover active resources, transaction flows, and communication patterns.
   - "If resources are overlooked, it's likely that they won't be appropriately protected by the ZTA."
   - Discovery is not a one-time activity — continue using tools to audit and validate the ZTA on an ongoing basis.

2. **Formulate Access Policy to Support Mission and Business Use Cases** (§8.2)
   - Define who can access what under what conditions — least privilege, separation of duties, deny-by-default.
   - Use discovery tool output to understand observed access patterns rather than guessing — "By basing access policy on observed access patterns, an organization reduces the chances that it will create overly restrictive policies that interfere with normal operations."
   - Acknowledge that policy will be distributed across multiple PDPs — "organizations should explicitly keep track of not only what their access rules are but also where each of the rules is configured."

3. **Identify Existing Security Capabilities and Technology** (§8.3)
   - Inventory existing security technology: firewalls, IDS, ICAM, endpoint protection, vulnerability management, SIEM, SOC.
   - Determine what should continue, what should be repurposed, what's missing.
   - "Continuing to use existing technology will require the organization to understand what potential zero trust components and products its existing security technology will integrate with."

4. **Eliminate Gaps in Zero Trust Policy and Processes by Applying a Risk-Based Approach** (§8.4)
   - Design access protection topology: segment infrastructure into smaller parts, isolate critical resources in their own trust zones protected by PEPs.
   - Apply access control enforcement at multiple levels: application, host, and network.
   - "In designing its access protection topology, the organization will identify which PEP is responsible for protecting each resource as well as what supporting technologies will be involved in providing input to resource access decisions."

5. **Implement ZTA Components (People, Process, and Technology) Incrementally** (§8.5)
   - Start with discovery tools and baseline security tools (SIEM, vulnerability scanning, security validation).
   - "Identity, authentication, and authorization are critical... the organization will want to use its existing or a new ICAM solution as a foundational building block of its initial ZTA implementation."
   - MFA "in a risk-based manner" is strongly recommended.
   - Add endpoint protection that integrates with ICAM as the second foundational component — these two enable identity + device health-based access decisions.
   - Add supporting components incrementally based on mission priorities: data security, behavior analytics, network segmentation.

6. **Verify the Implementation to Support Zero Trust Outcomes** (§8.6)
   - Continuous real-time monitoring for suspicious activity and anomalies.
   - "The organization should perform ongoing verification that the policies that are being enforced, as revealed by the observed network flows, are in fact the policies that the organization has defined."
   - Periodic testing across use case scenarios: on-premises and cloud resources, managed and unmanaged endpoints, authorized and unauthorized access attempts, service-to-service requests.
   - Create a test suite for validation before each incremental deployment and on a periodic basis after rollout.

7. **Continuously Improve and Evolve** (§8.7)
   - Adapt to changing threat landscape, mission, technology, and regulations.
   - Replace obsoleted technology, integrate innovative new capabilities, evolve policies as security goals shift.
   - "Creating a ZTA is not a one-time project but an ongoing process."
   - CISO/security team should perform ongoing validation of access policies against mission and least privilege principles.

**Confidence:** HIGH on the framework's validity — the seven steps are logically sequenced and reflect real implementation experience. MEDIUM on the achievability for resource-constrained organizations — the framework assumes a level of tooling, staffing, and organizational maturity that smaller organizations may lack.

**What's at stake:** If organizations treat ZTA as a procurement exercise (buy the products, configure them, done), they'll fail. The journey framework emphasizes that ZTA is a process transformation with technology enablement, not the reverse. Step 3 (identify existing capabilities) is politically crucial — it gives organizations permission to build on what they have rather than starting over.

**My assessment:** The seven-step framework is well-structured and likely to be widely cited. The emphasis on discovery (Step 1) as the *first* step — before policy, before technology — is correct and often overlooked. Organizations that skip discovery end up protecting assets they don't know about. The framework's weakness is that it doesn't provide estimated timelines or resource requirements for each step — a small organization and a federal agency both follow the same seven steps, but the implementation looks radically different. The "incremental" emphasis throughout is the framework's most important characteristic — it directly counters the paralyzing perception that ZTA requires a big-bang deployment.

---

## §5: Demonstration Methodology and Use Cases (§6)

### Claim 5: The project's eight use case categories (A–H) provide a comprehensive ZTA testing framework — from discovery through data-level security — that organizations can adapt for their own validation.

**The eight use case families** (lines 1584–1852):

| Use Case | Focus | Key Scenarios |
|----------|-------|---------------|
| **A: Discovery and Identification** | Asset discovery, authentication, reauthentication, transaction flow discovery | A-1: Endpoint discovery; A-2: Reauthentication; A-3: Transaction flow discovery |
| **B: Enterprise-ID Access** | Managed users accessing resources from managed/BYOD endpoints | B-1: Full/limited access; B-3: Stolen credential; B-7: Just-in-time access; B-8: Step-up authentication |
| **C: Federated-ID Access** | Cross-enterprise collaboration with federated identities | C-1/C-2: Full/limited access; C-7/C-8: Stolen credential from enterprise/BYOD endpoints |
| **D: Other-ID Access** | Registered external identities (contractors, partners) | D-3: Stolen credential; D-7: Just-in-time access; D-8: Step-up authentication |
| **E: Guest / No-ID Access** | Unidentified users on the network | E-1: Public internet access only |
| **F: Confidence Level** | Dynamic session reevaluation based on changing conditions | F-1: Reauth failure → termination; F-4: Compliance failure → termination; F-5: Compliance improvement → access granted; F-14: Suspicious endpoint → denial |
| **G: Service-Service Interaction** | Non-person entity (API) access across locations | G-1: On-prem to on-prem; G-2: On-prem to cloud; G-3: Cloud to cloud; G-4: Container to container |
| **H: Data-Level Security** | Classification-based access control at the data layer | H-1: Access by identity attributes; H-2: Access by endpoint type; H-4: MFA challenge for high-classification data; H-5: JIT for high-level data |

**Demonstration methodology** (lines 1522–1579):
- Dual-mode: manual (for human-interaction scenarios like MFA) and automated (for non-interactive scenarios).
- Mandiant Security Validation (MSV) deployed throughout the lab as both enterprise self-auditing tool and NCCoE testing tool, with a separate management backchannel to avoid ZTA policy interference.
- MSV protective theater for destructive testing without impacting production-like environments.

**Confidence:** HIGH on the comprehensiveness of the use case framework — covers the full identity spectrum (enterprise, federated, external, guest), both human and non-person entities, session lifecycle management, and data sensitivity. The framework can serve as a ZTA testing template.

**My assessment:** The use case framework may be the document's most exportable artifact. Organizations can take these eight categories and map them to their own environments, creating a ZTA testing/validation suite. The stolen credential scenarios (B-3, C-7, D-3) are particularly valuable — they test whether ZTA controls actually work against the attack they're designed to prevent. Use Case G (service-to-service) is a strong complement to SP 800-207A's identity-tier policy framework — it operationalizes the concept with specific test scenarios.

---

## §6: Risk and Compliance Mappings (§7)

### Claim 6: The project mapped ZTA security capabilities to NIST CSF 1.1/2.0, NIST SP 800-53r5, and NIST critical software security measures — demonstrating that ZTA implementations support, rather than replace, existing compliance frameworks.

**Mapping approach** (lines 2288–2316):
- Used NIST IR 8477 mapping relationship style: Supports, Is Supported By, Equivalent — each with properties: Example of, Integral to, Precedes.
- These mappings "were developed to support why and how organizations can implement ZTA" and "can help organizations articulate how current or planned implementations of CSF Subcategories, SP 800-53 controls, and NIST critical software security measures can help support a ZTA implementation."
- Organizations can "leverage their existing security investments and prioritize future security technology deployment to address the gaps."

**Confidence:** MEDIUM. The mapping concept is valuable but the details are in the online supplement (not the PDF). The mapping approach is methodologically sound (IR 8477) but the claim that ZTA "supports" existing frameworks needs validation — some SP 800-53 controls may conflict with ZTA principles, and the mappings should identify tensions, not just alignment.

**My assessment:** The compliance mappings address the most common organizational objection to ZTA: "Will this break our compliance?" By demonstrating that ZTA supports (rather than replaces) existing frameworks, NIST removes a major adoption barrier. However, the mappings should be treated as a starting point, not a complete compliance assessment — organizations still need to map ZTA to their specific control implementations.

---

## Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| 1: Four deployment approaches (EIG, SDP, Microseg, SASE) are a spectrum | HIGH | Market convergence blurring approach boundaries |
| 2: 19 builds demonstrate ZTA is buildable; integration gaps are the real barrier | HIGH (buildability) / HIGH (gaps) | Vendors closing integration gaps faster than anticipated |
| 3: EIG crawl proves legacy ICAM can do basic ZTA; resource management is the gap | HIGH | Resource management tools evolving faster than projected |
| 4: Seven-step ZTA journey framework | HIGH | Resource-constrained organizations finding steps infeasible |
| 5: Eight use case categories as comprehensive ZTA testing framework | HIGH | New attack patterns requiring additional use cases |
| 6: ZTA supports existing compliance frameworks (CSF, 800-53) | MEDIUM | Conflicts between ZTA principles and specific SP 800-53 controls |

**Strongest contributions:**
1. **The 19-build matrix** — proof that ZTA can be built with commercially available technology. The single most valuable artifact for organizations seeking to understand what's possible.
2. **The integration gap findings (§5)** — honest documentation of what didn't work. More valuable than the successes because they shape procurement requirements.
3. **The incremental journey framework (§8)** — seven steps that make ZTA feel achievable rather than overwhelming.
4. **The eight use case categories (§6)** — exportable testing framework for any ZTA implementation.

**Weakest areas:**
1. **No cost data.** The document doesn't address what any of these builds cost — hardware, software licenses, integration labor, ongoing operations. For organizations making investment decisions, this is the missing variable.
2. **No performance benchmarking.** The lab environment is controlled — no data on how ZTA enforcement affects application latency, user experience, or operational overhead at scale.
3. **Limited legacy integration testing.** The lab started clean — real enterprises have mainframes, legacy applications, OT systems. The document acknowledges OT/IoT is out of scope, but even legacy IT (not just OT) poses integration challenges not represented.
4. **The supplement dependency.** Critical details (build architecture, implementation instructions, detailed demonstration results, compliance mappings) are in the online supplement only. The PDF is an executive summary, not the complete guide. Organizations must use the web format for implementation.

**Cross-cutting observations:**
- **The document is a marketing counterweight.** By demonstrating 19 builds with 24 vendors, NIST shows that ZTA isn't a single-vendor play. This undercuts vendor claims that ZTA requires their specific platform while still giving each vendor a showcase.
- **Identity is the gravitational center.** Every build, regardless of approach, has ICAM at its core. SDP builds still need Okta/Ping/Azure AD. SASE builds still need identity federation. This validates SP 800-207's identity-centric framing.
- **The lab is both a strength and a limitation.** The controlled environment enables rigorous, reproducible testing. But it also means the builds haven't faced the chaos of real enterprise environments — shadow IT, legacy systems, political resistance, budget constraints.
- **The phased approach is a political tool.** By showing that EIG crawl (legacy ICAM) is a valid starting point, NIST gives CISOs cover to begin their ZTA journey without requesting massive new budgets. The crawl → run → advanced framing is as much about organizational change management as it is about technology.
- **Mandiant MSV integration is significant.** By embedding security validation into every build, NIST demonstrates that ZTA isn't just about preventing access — it's about continuously verifying that controls work. This is an operational pattern that most ZTA guidance omits.

**Open questions:**
- Will the online supplement remain available and maintained? Practice guides that depend on linked web content risk link rot.
- How do these builds perform at enterprise scale (10,000+ users, 1,000+ applications)?
- What is the migration path from an EIG crawl build to an SDP + SASE build? The document shows they can both exist but doesn't describe the transition.
- How do these approaches handle the non-standard enterprise: IoT/OT environments, air-gapped systems, classified networks?
- What happens when a key component in a multi-vendor build reaches EOL or the vendor is acquired? The Broadcom/VMware/Omnissa footnote (line 322–324) hints at this risk without exploring it.
