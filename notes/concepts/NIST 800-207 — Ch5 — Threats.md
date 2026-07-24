---
tags:
  - source/standards
  - nist
  - zt-threats
  - denial-of-service
  - insider-threat
  - oskg-zerotrust
created: 2026-07-24
source: "[[NIST SP 800-207 Zero Trust Architecture]]"
related:
  - "[[NSA Embracing Zero Trust]]"
  - "[[Zero Trust Networks (Gilman & Barth)]]"
  - "[[Concepts Index]]"
---

# NIST 800-207 — Chapter 5 — Threats Associated with Zero Trust Architecture

## Overview

Chapter 5 of NIST SP 800-207 catalogs the threats that **persist or take unique forms** under a Zero Trust Architecture. The chapter's framing is realistic: "No enterprise can eliminate cybersecurity risk." ZTA reduces overall risk, but certain threats have distinctive features when the policy engine (PE) and policy administrator (PA) become the critical control points for all resource access. This note covers all seven threat categories (Sections 5.1–5.7) and cross-references the threat models presented in NSA's *Embracing a Zero Trust Security Model* (2021) and Gilman & Barth's *Zero Trust Networks* (Chapter 10, "The Adversarial View").

---

## 5.1 Subversion of ZTA Decision Process

**Core risk:** The PE and PA are the linchpins of a ZTA — no inter-resource communication occurs without their approval. If an attacker subverts these components, the entire access control fabric collapses.

- **Configuration abuse:** An administrator with PE configuration access can make unapproved changes or errors that disrupt operations.
- **Compromised PA:** A subverted PA could grant access to otherwise-denied resources (e.g., a personally-owned rogue device).
- **Mitigations:** Proper configuration, continuous monitoring, logging of all configuration changes, and audit.

### Cross-reference — Gilman & Barth: Control Plane Security

Gilman & Barth devote a full section of Chapter 10 to this exact threat. They warn that compromising the policy engine leads to "a complete compromise of zero trust authorization, allowing the attacker to authorize anything they please." Their mitigations align with NIST's but go further:
- Group authentication/authorization for changes to sensitive control plane systems
- Changes should be infrequent and generate broadly visible alerts
- Administrative isolation (dedicated cloud account, rigorous access control) while keeping systems logically integrated into the network
- Eventually apply zero trust enforcement to the control plane itself ("rewriting the C compiler in C")

---

## 5.2 Denial-of-Service or Network Disruption

**Core risk:** The PA is the gatekeeper for all resource access. If attackers disrupt the PEP, PE, or PA, enterprise operations grind to a halt.

**Attack vectors:**
- DoS/DDoS or route hijacking against the PEP or PE/PA
- Botnet attacks (Mirai-scale) against key infrastructure
- Interception/blocking of traffic to a PEP or PA for a subset of users (branch office, remote employee) — not unique to ZTA; also possible with legacy VPNs
- Accidental cloud provider outages (IaaS or SaaS) taking PE/PA offline

**Pathology unique to ZTA:** Even if access is granted, the PA may be unable to configure the communication path due to DDoS or unexpected heavy usage — the resource becomes unreachable despite authorization.

**Mitigations:**
- Host PE/PA in a properly secured cloud environment or replicate across locations per cyber resiliency guidance (NIST SP 800-160v2)

### Cross-reference — NSA Embracing ZT

NSA's document is fundamentally threat-model-driven: it opens by "acknowledging that threats exist both inside and outside traditional network boundaries." While NSA does not treat DoS as a standalone category, its "assume breach" principle subsumes availability concerns — a mature ZT implementation is designed to "perform rapid damage assessment, control, and recovery operations" when disruption occurs.

### Cross-reference — Gilman & Barth: Distributed Denial of Service

Gilman & Barth are blunt: "DDoS is still a problem in the zero trust world." Key points:
- Volumetric DDoS affects any system that can receive packets, even ZTA ones
- "Darkening" internet-facing endpoints via pre-authentication helps obscure addresses but doesn't fundamentally mitigate DDoS
- **ZT-specific advantage:** Policy information about expected traffic patterns can be used to calculate coarse enforcement rules for upstream filtering devices that remain **stateless** — obviating expensive hardware and state replication
- Cloud-native deployments should leverage online DDoS-prevention services

---

## 5.3 Stolen Credentials / Insider Threat

**Core risk:** ZT's "no implicit trust based on network location" means attackers must compromise an existing account or device to gain a foothold. A properly implemented ZTA prevents that compromised account from accessing resources outside its normal purview — but within its authorized scope, damage is still possible.

**Key dynamics:**
- Attackers target accounts with access policies aligned to their objectives (admin accounts for control, financial accounts for monetary gain)
- Phishing, social engineering, or combined attacks to obtain credentials
- MFA reduces risk of information loss but does not eliminate it — a valid-credentialed attacker still accesses resources the account is authorized for
- **ZTA advantage:** No lateral movement. If credentials aren't authorized for a resource, access is denied regardless of network position
- **Contextual trust algorithm (Section 3.3.1):** Detects out-of-normal access patterns faster than perimeter-based networks, can deny the compromised account access to sensitive resources

### Cross-reference — NSA Embracing ZT

NSA provides two worked examples that directly parallel Section 5.3:

1. **Compromised user credentials:** A malicious actor uses stolen credentials on an unauthorized device. In a traditional network, credentials alone suffice. In ZT, the unknown device fails authentication/authorization, access is denied, and the activity is logged. MFA makes credential theft harder in the first place.

2. **Remote exploitation / insider threat:** A compromised device or malicious insider uses valid credentials to enumerate the network and move laterally. In ZT, network segmentation limits enumeration and lateral movement. Even authenticated, access is capped by policy, user role, and device attributes. Analytics continuously monitor for anomalous activity — damage is limited and detection time is reduced.

### Cross-reference — Gilman & Barth: Identity Theft

Gilman & Barth identify identity theft as the **first threat** in their adversarial view: "Practically all of the decisions and operations performed within a zero trust network are made on the basis of authenticated identity." Key insights:
- ZT requires theft of **at least two identities** (device + user/application) to gain access — raising the bar compared to traditional approaches
- Trust engine behavioral analysis provides additional mitigation
- Identity theft is an industry-wide concern, not ZT-specific, but its importance is "large enough to justify calling it out"
- They also address **social engineering** (phishing, face-to-face coercion) and **physical coercion** as vectors for identity compromise, recommending group authentication for critical assets to prevent single-individual compromise

---

## 5.4 Visibility on the Network

**Core risk:** All traffic is inspected and logged in ZTA, but much of it may be opaque to Layer 3 network analysis tools — particularly encrypted traffic from non-enterprise-owned assets or applications resistant to passive monitoring.

**Key dynamics:**
- Enterprises that cannot perform deep packet inspection on encrypted traffic must use alternative assessment methods
- **Metadata analysis is still viable:** Source/destination addresses and other metadata from encrypted traffic can detect active attackers or malware
- **Machine learning techniques** (citing Anderson) can categorize encrypted traffic as valid or possibly malicious without decryption

### Cross-reference — Gilman & Barth: Endpoint Enumeration

Gilman & Barth raise a related but distinct concern: the perimeterless nature of ZT means an adversary can **build a system diagram by observing which systems talk to which endpoints**. They distinguish between:
- **Confidentiality** (ZT guarantees this — conversation contents are protected)
- **Privacy** (ZT does not guarantee this — the existence of conversations can be observed)

This is a tradeoff: VPNs obscure endpoint-level conversations but introduce scaling and availability problems that ZT eliminates.

---

## 5.5 Storage of System and Network Information

**Core risk:** The monitoring data that enables ZTA's contextual policies becomes a high-value target for attackers.

**Attack surfaces:**
- Network traffic scans, metadata, and logs stored for forensics or analysis
- Network diagrams, configuration files, and architecture documents
- The **management tool used to encode access policies** — this reveals which accounts have access to which resources, effectively telling an attacker which accounts are most valuable to compromise

**Mitigations:**
- Most restrictive access policies for security data
- Accessible only from designated/dedicated administrator accounts
- Same protections as any valuable enterprise data, but heightened because of the reconnaissance value

### Cross-reference — Gilman & Barth

Gilman & Barth's "Control Plane Security" section warns that compromising a data store housing historical access data lets an attacker "artificially raise their level of trust by falsifying access patterns" — a subtler attack than compromising the policy engine but still dangerous. This maps directly to NIST's concern about the management tool and stored traffic data being recon targets.

---

## 5.6 Reliance on Proprietary Data Formats or Solutions

**Core risk:** ZTA depends on diverse data sources (subject info, asset state, threat intelligence) that often lack common open standards for interaction and exchange. This creates vendor lock-in.

**Key dynamics:**
- Interoperability issues can lock an enterprise into a subset of providers
- If a provider has a security issue or disruption, migration costs may be extreme (replacing multiple assets, translating proprietary policy formats)
- Not unique to ZTA, but **amplified** because ZTA is "heavily dependent on the dynamic access of information" — disruption affects core business functions

**Mitigations:**
- Evaluate service providers holistically: vendor security controls, enterprise switching costs, supply chain risk management — not just performance and stability

---

## 5.7 Use of Non-Person Entities (NPE) in ZTA Administration

**Core risk:** AI and software-based agents are being deployed to manage ZTA security components (PE, PA), sometimes replacing human administrators. Their authentication and decision-making introduce new threat vectors.

**Key dynamics:**
- **Authentication gap:** NPEs typically authenticate via API keys rather than MFA — a lower bar than human users
- **Decision quality:** False positives (innocuous actions mistaken for attacks) and false negatives (attacks mistaken for normal activity) impact security posture — mitigated by regular retuning
- **Agent coercion:** An attacker could trick or coerce an NPE into performing privileged tasks on their behalf
- **Credential impersonation:** An attacker could steal a software agent's credentials and impersonate it

**Status:** NIST flags this as an "open issue" — how NPEs should authenticate in a ZTA is unresolved.

### Cross-reference — Gilman & Barth

Gilman & Barth do not address NPEs directly (their 2017 framing predates widespread AI-agent deployment in security operations), but their "Invalidation" section raises a related concern: the speed at which ongoing authorized actions can be revoked. If an NPE grants access that later proves malicious, can the system invalidate it fast enough? This is the "hard problem" of invalidation that Gilman & Barth explore — and it becomes harder when NPEs make authorization decisions at machine speed.

---

## Synthesis: Three Views of the Same Threat Landscape

| Threat Category | NIST 800-207 (2020) | NSA Embracing ZT (2021) | Gilman & Barth (2017) |
|---|---|---|---|
| **Decision process subversion** | §5.1 — PE/PA compromise | Implicit in "assume breach" | Control plane security (Ch10) |
| **DoS / disruption** | §5.2 — DoS against PEP/PA, cloud outages | Assume breach → recovery ops | DDoS still a problem; policy-driven upstream filtering |
| **Stolen credentials / insider** | §5.3 — MFA, contextual TA, no lateral movement | Worked examples: compromised creds, remote exploitation, supply chain | Identity theft (two identities required), social engineering, physical coercion |
| **Visibility / monitoring gaps** | §5.4 — Encrypted traffic, metadata, ML | Not addressed directly | Endpoint enumeration, confidentiality vs. privacy distinction |
| **Data storage as target** | §5.5 — Monitoring data, policy management tools | Not addressed directly | Control plane data store compromise, falsifying access patterns |
| **Proprietary lock-in** | §5.6 — Vendor interoperability, switching costs | Not addressed | Not addressed |
| **NPEs / automated agents** | §5.7 — API auth, false positives/negatives, agent coercion | Not addressed | Invalidation speed (adjacent concern) |

**Key insight:** The three documents form a progression. Gilman & Barth (2017) provide the **engineering-level adversarial analysis** — what specific attacks look like and how to mitigate them at the implementation level. NIST 800-207 (2020) provides the **architectural threat taxonomy** — what an enterprise must account for at the system-design level. NSA Embracing ZT (2021) provides the **operational threat model** — the "assume breach" mindset and worked examples that connect threats to ZT's defensive advantages. Together they cover threats from implementation detail through architecture to operational philosophy.
