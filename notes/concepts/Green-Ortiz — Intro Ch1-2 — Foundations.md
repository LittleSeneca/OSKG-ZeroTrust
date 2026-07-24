---
tags:
  - source/books
  - green-ortiz
  - zt-introduction
  - zt-components
  - zt-networking
  - zt-history
  - five-pillars
  - oskg-zerotrust
created: 2026-07-24
confidence: high
source:
  title: "Zero Trust Architecture (Networking Technology: Security)"
  authors: "Cindy Green-Ortiz, Brandon Fowler, David Houck, Hank Hensel, Patrick Lloyd, Andrew McDonald, Jason Frazier"
  year: 2024
  publisher: "Cisco Press"
  local_file: "sources/books/_txt/Zero_Trust_Architecture_Networking_Technology_Security.txt"
  sections: "Introduction, Chapter 1 — Overview of Zero Trust, Chapter 2 — Zero Trust Capabilities"
  lines: "1313–3743"
related:
  - "[[Gilman and Barth — Ch1 — Zero Trust Fundamentals]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[Concepts Index]]"
---

# Green-Ortiz et al. — Intro + Ch1–2: Foundations and Core Components

The most detailed single-source treatment of Zero Trust architecture from a networking and infrastructure perspective. Green-Ortiz and her six co-authors bring 85 combined years of security and architectural experience, organized around Cisco's five-pillar capability model. This combined note covers the book's introduction (audience, approach, executive sponsorship), Chapter 1 (historical origins, discovery workshop methodology, organizational dynamics, the five pillars), and Chapter 2 (the full "dictionary of capabilities" within each pillar). Where NIST 800-207 defines what ZT *is* and Gilman & Barth define how to *build* it, Green-Ortiz defines how to *plan, assess, and operationalize* it in enterprise environments.

---

## Claim 1: Zero Trust originated from the Morris Worm and Stephen Marsh's thesis, not from a vendor marketing campaign

**Green-Ortiz's claim:** The concept of Zero Trust traces to the 1988 Morris Worm, which exploited implicit trust in Unix remote services (rexec, rsh, sendmail, finger) to propagate to 10% of Internet-connected computers within 24 hours. Stephen Paul Marsh's 1994 doctoral thesis "Formalizing Trust as a Computational Concept" explicitly identified implicit trust as "unreasonable and misguided," providing the first formal treatment of trust in digital systems. The Jericho Forum (2003) advanced "de-perimeterization," and John Kindervag at Forrester (2009) popularized the modern basis. Google's BeyondCorp initiative (2009) provided the first large-scale implementation and lessons learned.

**Evidence presented:** The FBI's public reporting on the Morris Worm, Marsh's thesis (University of Stirling, 1994), Jericho Forum's merger into The Open Group Security Forum (2014), and Google's published BeyondCorp papers. The historical timeline (Figure 1-1) shows a clear progression from reactive incident → academic formalization → industry forum → analyst articulation → implementation.

**Confidence:** HIGH. This historical account is consistent across multiple sources and independently verifiable.

**What's at stake:** This lineage makes ZT a 30-year response to a well-understood problem (implicit trust is exploitable), not a vendor narrative. The invocation of Marsh's 1994 thesis as the intellectual root is distinctive to Green-Ortiz and adds academic credibility absent from most industry accounts.

**Cross-reference — Gilman & Barth Ch1:** Gilman & Barth trace perimeter security's failure to a different historical accident: RFC 1597 creating private address space, the DMZ emerging as a side effect, and NAT providing inadvertent firewall properties. Both histories converge on the same conclusion — security models based on location (inside/outside) were never designed; they accreted. Gilman & Barth's narrative is about *network architecture*, Green-Ortiz's is about *the trust concept itself*. Together they provide both the network-level and the conceptual-level origin stories.

**Cross-reference — NIST 800-207:** NIST 800-207 does not provide a historical origin narrative. Its ZT definition is presented as a response to enterprise architectural evolution (Chapter 1), not as a lineage. Green-Ortiz fills a gap the standards literature leaves open.

**My assessment:** The Marsh → Jericho → Kindervag → BeyondCorp lineage is the most complete origin story in the ZT literature. It's better than the common "Forrester invented ZT in 2010" simplification found in marketing collateral. The four-phase progression (incident → theory → industry consensus → implementation) makes ZT adoption feel like maturation rather than trend-chasing.

---

## Claim 2: The Zero Trust Discovery Workshop is the critical first step — skip it at your peril

**Green-Ortiz's claim:** Most organizations fail at Zero Trust because they skip the business-understanding phase and jump directly to technology implementation. A structured Discovery Workshop with four attendee categories (principal stakeholders, cross-functional SMEs, key strategists/decision makers, end-user experience representatives) is the mechanism to align business units, surface risks, and create an actionable roadmap before any enforcement is applied.

**Evidence presented:** The authors' collective experience across "tens of organizations, hundreds across their respective careers." The workshop framework (Figure 1-2: Planning → Collect Data → Analyze Data → Presentation) with artifacts including 90-day short-term and 360-day long-term improvement plans. The SBC Healthcare fictional use case provides a worked example showing how business requirements (prevent PHI data loss, minimize ransomware impact) translate into technical requirements (AAA to ISE, device profiling, east-west traffic control, endpoint lifecycle management).

**Key dynamics:**

- **Top-down + bottom-up discovery must be combined.** Business unit interviews establish context (what data is sensitive, what processes are critical); traffic discovery tools (NetFlow, taps, firewall logs, endpoint telemetry) validate the actual communication patterns. Either alone produces blind spots.
- **Traffic discovery must span the "busy season."** Capturing only off-hours traffic misses quarterly financial reporting, end-of-month batch processing, and other critical-but-infrequent communication patterns. Change freezes should be carefully planned around data collection windows.
- **Artifacts are concrete deliverables.** The workshop should produce: policy documentation for endpoint types, identification flows (how users/devices are authenticated), endpoint requirements for network access, access restrictions per use case, and locations for storing/analyzing monitoring data.
- **The "Problem? What problem?" syndrome is the most dangerous.** Organizations that don't recognize ZT as needed have the worst gaps. Marketing dilution of the term — where vendors claim a single product delivers ZT "with a click of a button" — fuels skepticism. The response: ZT is an *architectural strategy*, not a product strategy.
- **"Cloud is Zero Trust by default" is false.** Cloud providers' shared responsibility model means organizations must bring their own tools, solutions, and visibility. Moving to the cloud without ZT principles is just moving the problem.

**Cross-reference — NIST 800-207:** NIST 800-207 Ch7 (Migration) defines a 7-step deployment cycle (identify actors → assets → business processes → policies → candidate solutions → deploy/monitor → expand). Green-Ortiz's workshop maps to NIST's first four steps but adds the crucial organizational dynamics dimension (stakeholder buy-in, executive sponsorship, competing teams) that NIST's technical focus omits.

**Cross-reference — Gilman & Barth Ch1:** Gilman & Barth's five assertions (the network is hostile, locality doesn't determine trust, every flow is authenticated, etc.) are what the workshop participants need to *internalize* before planning. The workshop is the process; the assertions are the principles that guide the process.

**My assessment:** This is the most operationally valuable section of the book. The workshop methodology addresses the #1 ZT failure mode — treating it as a technology project rather than an organizational transformation. The four attendee categories are particularly well-chosen: they ensure authority, technical knowledge, and frontline impact awareness are all represented.

---

## Claim 3: Cisco's five-pillar model (Policy & Governance, Identity, Vulnerability Management, Enforcement, Analytics) provides a comprehensive capability taxonomy for ZT assessment

**Green-Ortiz's claim:** Every capability needed for a Zero Trust strategy falls into one of five pillars. Organizations that have these capabilities can move to a Zero Trust strategy; those that don't will struggle. The pillars are not sequential — they're interdependent, with Identity serving as the "second most critical pillar" (after Policy & Governance) because it infuses all other capabilities with a subject to which they can be applied.

**Evidence presented:** The five-pillar model is "aligned to many different frameworks and methodologies" and represents Cisco's accumulated assessment experience. Each pillar is operationalized in Chapter 2 as a detailed "dictionary of capabilities" with 45+ discrete components.

**Confidence:** HIGH as a practical assessment framework. The taxonomy is comprehensive and actionable. It is, however, Cisco-specific in its decomposition — other frameworks (NIST's logical components, CISA's five pillars, DoD's seven pillars) slice differently.

**Cross-reference — NIST 800-207 Ch3:** NIST's logical component model (PE, PA, PEP, trust algorithm, data sources) is an *architectural* decomposition — it answers "what components make access decisions?" Green-Ortiz's five pillars are an *organizational capability* decomposition — they answer "what does the organization need to have in place?" The mapping is not one-to-one. The Policy Engine (PE) from NIST requires capabilities from all five Green-Ortiz pillars: Policy & Governance (rules), Identity (subject attributes), Vulnerability Management (posture inputs), Enforcement (PEP deployment), and Analytics (trust algorithm inputs).

**Cross-reference — Gilman & Barth Ch1:** Gilman & Barth's control plane / data plane split is a *functional* decomposition. The control plane (authentication, authorization, coordination) maps most directly to Identity + Policy & Governance. The data plane (enforcement) maps to Enforcement. Vulnerability Management and Analytics are control-plane-adjacent concerns that Gilman & Barth address in later chapters (Ch4 device trust, Ch9 realization).

**My assessment:** The five-pillar model is the book's organizing principle and its primary contribution to the ZT literature. It's more granular than NIST's architectural model, more enterprise-operations-focused than Gilman & Barth's engineering model, and provides a structured assessment framework that maps naturally to compliance and audit requirements. The limitation is that pillars overlap in practice (anti-malware software serves both Vulnerability Management and Enforcement), which the authors acknowledge explicitly.

---

## Claim 4: Policy & Governance is the "badge and shield" — it authorizes enforcement and defines the rules

**Green-Ortiz's claim:** Policy & Governance is the foundational pillar because it establishes what can and cannot be done within the organization. It encompasses change control (ITIL-based), data governance (classification: PII, ePHI, PCI, restricted IP), data retention (legal/compliance-driven), QoS (prioritization of control plane traffic during congestion), redundancy (control plane + data plane), replication (encrypted, automated backups), business continuity (BCP with tabletop exercises), disaster recovery (RPO/RTO definitions), and risk classification. Finding the right balance between security and business enablement is the central tension.

**Evidence presented:** Detailed treatment of each sub-capability with operational guidance. The key insight is that Policy & Governance must be "strict enough to act as the badge and shield allowing for enforcement actions to be taken" while "striking the right balance between allowing devices to perform their business purpose... while maintaining least privileged access."

**What's at stake:** Without Policy & Governance, enforcement has no authority. Without DR/BCP, a ZT environment can't recover from a successful attack. The authors argue that "without a business continuity plan and a disaster recovery plan, there cannot be a valid and implemented Zero Trust strategy" — a stronger claim than any other ZT source makes.

**Cross-reference:** NIST 800-207's "Data Access Policies" and "Industry Compliance" data sources (Ch3, Claim 2) are the closest equivalents. Gilman & Barth treat policy as an output of the trust engine, not as a standalone governance function. Green-Ortiz's treatment of governance as a separate, foundational pillar reflects the enterprise reality that policy precedes architecture.

---

## Claim 5: Identity must be contextual — WHO, WHAT device, WHERE, HOW, and WHEN all matter

**Green-Ortiz's claim:** Identity is the most critical pillar because it provides the subject to which all other capabilities apply. But identity alone is not enough — full *contextual* identity is required. Contextual identity answers five questions: WHO (user/owner/manager), WHAT (device type, posture, certificate), WHERE (location, network medium), HOW (connection method: 802.1X, VPN, MAB), and WHEN (time of access, baseline behavior deviations).

**Evidence presented:** Detailed treatment of AAA (Authentication, Authorization, Accounting), certificate authorities (EAP-TLS, chain of trust), NAC (integration with all pillars), provisioning (Device, User, People, Infrastructure, Services), privileged access (least privilege, audit requirements), MFA (knowledge + possession + biometric + challenge factors), asset identity (MAC OUI, passive profiling, CMDB), and IP schemas (IPv4/IPv6 dual-stack, PI vs. PA space). The SBC Healthcare use case demonstrates how contextual identity drives policy: a surgeon in the OR gets different access than the same surgeon connecting from home over VPN.

**Key dynamics:**

- **MAC Authentication Bypass is a fallback, not a primary method.** MAC addresses are easily spoofed. MAB should always be combined with profiling to add confidence. Devices with lower identity confidence get more restrictive authorization.
- **802.1X with RADIUS is the preferred network authentication method.** Combined with centralized authentication databases (LDAP, Active Directory, certificate authorities), it enables dynamic policy response to identity context changes.
- **Certificate-based identity is stronger than credential-based.** EAP-TLS with user + machine certificates creates a unique contextual identity that prevents credential export and sharing. The combination of "who" and "what" enables differentiated access.
- **IoT and headless devices require special handling.** MUD (Manufacturer Usage Description) and passive profiling compensate for the inability to run supplicants. The lower confidence in IoT identity means authorization must be more restrictive.

**Cross-reference — NIST 800-207 Ch3:** NIST's "ID Management" data source provides user identity and attributes to the PE. Green-Ortiz's contextual identity model is a superset: it adds device identity (what), location (where), connection method (how), and temporal (when) dimensions that NIST treats as separate data sources (CDM, activity logs, threat intelligence).

**Cross-reference — Gilman & Barth Ch1:** Gilman & Barth's assertion 4 — "Every device, user, and network flow is authenticated and authorized" — is the principle. Green-Ortiz's contextual identity model is the enterprise operationalization of that principle. Gilman & Barth focus on the authentication/authorization protocols; Green-Ortiz focuses on the operational processes (provisioning, onboarding, CMDB integration) that make identity reliable at scale.

**My assessment:** The contextual identity model — WHO, WHAT, WHERE, HOW, WHEN — is the most memorable framework in the book. It's immediately actionable for workshops and assessments. The treatment of IoT identity challenges is particularly valuable because it addresses the hardest ZT problem (devices that can't authenticate themselves) without hand-waving.

---

## Claim 6: Vulnerability Management must extend beyond CVEs to include communication baselines and device behavior

**Green-Ortiz's claim:** Traditional vulnerability management (CVEs, CVSS scores, authenticated scanning) is necessary but insufficient for ZT. Zero Trust vulnerability management must also establish baselines of which resources a device connects to (internal and external), detect deviations from those baselines, and factor in the contextual identity of the device. The CVSS base score must be adapted with temporal and environmental metrics to reflect the organization's actual risk.

**Evidence presented:** Detailed treatment of endpoint protection (malware detection, file reputation, behavioral analysis, ML-based zero-day prevention), malware prevention and inspection (layered, network-level, integration with endpoint agents), vulnerability management systems (automation, AI, prioritization, residual risk tracking), authenticated vulnerability scanning (vs. unauthenticated; the case for bypassing authentication controls to gain deeper visibility), and database change monitoring ("crown jewels" protection, FIM for databases, correlated monitoring across database types).

**Key dynamics:**

- **Layered malware prevention is required because IoT/OT can't run endpoint agents.** Network-level inspection placed before OT segments compensates for agentless endpoints.
- **Authenticated scanning reveals the true risk posture.** Unauthenticated scans show only what an external attacker sees. Authenticated scans show what an attacker with any credential (even low-privilege) could exploit, including privilege escalation vectors.
- **Residual risk must be tracked.** It's not possible to eliminate all risk. A residual risk database tracks mitigated vulnerabilities, ensuring that accepted risks are documented and periodically reviewed rather than forgotten.
- **Database change monitoring correlates across database types.** The crown jewels need monitoring that understands usage patterns across the organization, not per-database. Integration with privileged identity systems enables end-to-end access control.

**Cross-reference — NIST 800-207 Ch3:** NIST's CDM (Continuous Diagnostics and Mitigation) system is the closest equivalent — it provides asset posture information to the PE. Green-Ortiz's Vulnerability Management pillar expands CDM into a full program with scanning, endpoint protection, malware inspection, and database monitoring.

**Cross-reference — Gilman & Barth:** Gilman & Barth address vulnerability management implicitly through device trust (Ch4) and the trust engine's posture-based decision-making. Green-Ortiz makes it an explicit, standalone pillar — reflecting the enterprise reality that vulnerability management programs predate ZT initiatives and must be integrated, not replaced.

**My assessment:** The vulnerability management pillar is where Green-Ortiz's enterprise-operations perspective most clearly differs from the architecture-centric sources. NIST and Gilman & Barth treat vulnerability data as an input to the policy engine; Green-Ortiz treats it as an ongoing program that must be mature before the policy engine can function reliably.

---

## Claim 7: Enforcement must be layered and applied as close to the source as possible

**Green-Ortiz's claim:** Enforcement is the goal of ZT, but it must be layered throughout the network — from the application layer down through TrustSec tags, downloadable ACLs, firewall rules, and VRF segmentation. No single enforcement point should carry the full burden. Enforcement mechanisms should be applied "as close to the source of the communication as possible" to minimize lateral movement opportunities.

**Evidence presented:** Detailed treatment of CASB (shadow IT visibility, cloud access governance), DDoS protection, DLP (data creation, movement, storage, backup, destruction), DNSSEC, email security, firewalls (packet filtering, NGFW with DPI, NAT, SMLI inspecting all seven OSI layers), IPS (signature/anomaly/policy-based; NIPS/HIPS/NBA/WIPS platforms), proxy (forward for outbound control, reverse for inbound services), VPN (MPLS, RA VPN, VRF for traffic isolation), SOAR (automated policy orchestration across tools), FIM (file change detection triggering trust status changes), and segmentation (identifying and isolating sets of systems into enclaves).

**Key dynamics:**

- **The four firewall types serve different ZT roles.** Packet filtering for basic boundary control, NGFW for deep packet inspection and threat prevention, NAT for IP obfuscation, SMLI for full-stack inspection.
- **SOAR enables automated policy response.** Tie vulnerability management to NAC: if a device is found vulnerable, SOAR can automatically restrict its network access until remediation. This is the automation that makes ZT scalable.
- **FIM + SOAR enables real-time trust status changes.** Unexpected file changes on a server can trigger automatic isolation via orchestrated enforcement actions.
- **Segmentation is the art of defining enclaves.** "The foundational process for identification and classification of corporate assets is essential to creating a Zero Trust Architecture, where defining segments or enclaves is used to establish trusts to other enclaves."

**Cross-reference — NIST 800-207 Ch3:** NIST's PEP (Policy Enforcement Point) is the logical abstraction. Green-Ortiz's Enforcement pillar enumerates the concrete technologies that can serve as PEPs — firewalls, proxies, VPN concentrators, NAC systems, SOAR platforms. NIST defines the function; Green-Ortiz catalogs the implementations.

**Cross-reference — Gilman & Barth Ch1:** Gilman & Barth's control plane / data plane split maps Enforcement to the data plane — "the data plane accepts configuration from the control plane and enforces it." Green-Ortiz adds the operational layer: which enforcement technologies to deploy where, and how to layer them for defense-in-depth.

**My assessment:** The Enforcement pillar is the most Cisco-specific section of the book — many of the technologies described (TrustSec tags, ISE-based NAC, Cisco firewalls) reflect Cisco's product portfolio. However, the *principles* (layered enforcement, source-close application, SOAR-driven automation) are vendor-neutral and well-articulated. The segmentation discussion in particular foreshadows Chapter 6 which provides the book's most detailed technical content.

---

## Claim 8: Analytics closes the loop — the ZT journey is cyclical, not linear

**Green-Ortiz's claim:** Analytics is not a "set it and forget it" function. The Zero Trust journey is cyclical: analytics feeds back into all other pillars, validating their function and driving continuous improvement. Without analytics, an organization has no way to know whether enforcement is working, whether identity classification is accurate, or whether newly introduced devices/users are creating unmanaged risk.

**Evidence presented:** APM (synthetic tests, SLA tracking, user experience monitoring), auditing/logging/monitoring (AAA accounting data, syslog, behavioral baselines), change detection (what/how/who/where/when for all changes, integrated with file integrity monitoring and SIEM), network threat behavior analytics (east-west lateral movement detection, north-south exfiltration detection, baseline deviation alerting), SIEM (log ingestion, event classification, metadata tagging, integration with CMDB, ticketing, and APIs), threat intelligence (IOCs, CVEs, IPS rulesets, fusion center partnerships, InfraGard), traffic visibility (no blind spots, regulatory retention, segmentation policy input), and asset monitoring & discovery (full lifecycle from acquisition to decommissioning, configuration hardening).

**Key dynamics:**

- **"Signal within the noise" is the central challenge.** After identity, vulnerability, and enforcement are in place, the ongoing labor-intensive work is monitoring behavior and validating it against policy.
- **Behavior analytics must cover both east-west and north-south.** Lateral movement (east-west) is the primary ZT concern — communications between servers that shouldn't talk, database data being exfiltrated into files, compromised endpoints probing the network. North-south monitoring catches C2 communication to external threat actors and geographic anomalies.
- **SIEM must integrate to be actionable.** Direct integration with CMDBs, ticketing systems, and security event monitoring tools is required to make SIEM output drive responses rather than sit in dashboards.
- **Threat intelligence must be ingested in real time.** Firewalls, segmentation solutions, endpoint protection, and monitoring solutions all need active threat feeds. Diversity of feeds and methods of intake is critical.
- **Asset management extends to decommissioning.** Assets must be properly purged of sensitive data at end-of-life. A gap in decommissioning process is a gap in Zero Trust.

**Cross-reference — NIST 800-207 Ch3:** NIST's eight data sources (CDM, Industry Compliance, Threat Intelligence, Activity Logs, Data Access Policies, PKI, ID Management, SIEM) map directly to Green-Ortiz's Analytics pillar inputs. The difference is that Green-Ortiz treats Analytics as an active, ongoing function that modifies the other pillars, whereas NIST treats data sources as inputs to a decision point. Green-Ortiz's model is more dynamic and better reflects operational reality.

**Cross-reference — Gilman & Barth:** Gilman & Barth's trust engine (Ch4) makes decisions based on trust scores derived from device posture, user authentication strength, and historical behavior. Green-Ortiz's Analytics pillar provides the continuous stream of data that would feed such a trust engine. The relationship is: Analytics produces the data → trust engine computes the score → Enforcement acts on the result.

**My assessment:** The cyclical framing — Analytics feeds back into Identity, Vulnerability Management, Policy, and Enforcement — is the most sophisticated element of the five-pillar model. It transforms ZT from a one-time architectural migration into an ongoing operational practice. This is where Green-Ortiz most clearly advances beyond NIST 800-207's relatively static component model.

---

## Synthesis: Three Frameworks, Three Perspectives

| Dimension | Green-Ortiz (2024) | NIST 800-207 (2020) | Gilman & Barth (2017) |
|---|---|---|---|
| **Organizing model** | Five operational pillars | Logical components (PE/PA/PEP) | Control plane / data plane |
| **Primary audience** | Enterprise architects, operations teams | Federal agencies, standards bodies | Engineers, implementers |
| **Identity treatment** | Contextual identity: WHO/WHAT/WHERE/HOW/WHEN | ID Management data source + ICAM integration | Authentication of every device, user, and flow |
| **Governance treatment** | Standalone foundational pillar (Policy & Governance) | Industry Compliance data source | Implicit in trust engine policy |
| **Vulnerability treatment** | Full program: scanning, endpoint protection, malware, database | CDM system (posture input to PE) | Device trust (Ch4, posture signals) |
| **Enforcement treatment** | Catalog of technologies (firewalls, IPS, proxy, VPN, SOAR, FIM) | PEP — logical abstraction, no technology enumeration | Data plane — accepts configuration from control plane |
| **Analytics treatment** | Cyclical feedback loop modifying all pillars | Inputs to PE (SIEM, activity logs, threat intel) | Trust engine computation (Ch4) |
| **Key contribution** | Operational framework for assessing and planning ZT maturity | Canonical architectural definitions (PE/PA/PEP) | Implementation blueprint (assertions, architecture, protocols) |
| **Weakness** | Cisco-specific in technology enumeration; light on protocol-level detail | Static component model; no operational guidance | Pre-dates enterprise ZT maturity; no governance treatment |

**Key insight:** The three sources form a progression from *principle* (Gilman & Barth: how to build ZT) to *definition* (NIST: what ZT is) to *operation* (Green-Ortiz: how to plan, assess, and run ZT in an enterprise). Gilman & Barth's 2017 book established the control-plane/data-plane architecture that all subsequent frameworks assume. NIST 800-207 in 2020 canonized the PE/PA/PEP component model and provided the standards vocabulary. Green-Ortiz in 2024 completes the picture by addressing the organizational, governance, and operational dimensions that neither of the earlier sources covers adequately. Read together, they answer: *why* ZT (history and threat landscape), *what* ZT (architecture and definitions), *how* to build it (implementation), and *how* to run it (operations and continuous improvement).

The most important practical insight from Green-Ortiz that neither NIST nor Gilman & Barth provide: **the Discovery Workshop methodology.** The technical architecture (NIST, Gilman & Barth) is necessary but insufficient; the organizational alignment (Green-Ortiz) determines whether the architecture ever gets deployed successfully.
