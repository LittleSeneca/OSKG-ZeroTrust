---
title: "Green-Ortiz — Ch9-11 — Advanced Enforcement, Operations, and the Future of Zero Trust"
date: 2026-07-24
tags: [source/books, green-ortiz, zt-advanced, zt-cloud, zt-future, oskg-zerotrust]
source: "Green-Ortiz, *Zero Trust Architecture*, Chapters 9-11"
---

# Green-Ortiz Chapters 9-11: Enforcement, Operations & Conclusion

## Overview

The final three chapters of Green-Ortiz move from design and principles into the practical realities of enforcing Zero Trust, operating it day-to-day, and sustaining the journey. Chapter 9 covers the hands-on mechanics of enforcement — monitor mode, phased rollout, greenfield vs brownfield, and the NAC backbone. Chapter 10 addresses the human and organizational dimension: breaking down silos, adoption lifecycles, and policy life cycle management. Chapter 11 synthesises the five-capability model and validates it through the Smart Building Central (SBC) applied use case in Appendix A.

---

## Chapter 9: Zero Trust Enforcement

### Claim 1: The biggest mistake in ZT implementation is rushing past monitor mode — organizations must inventory and understand endpoints in production before enforcing any restrictions, and monitor mode never truly ends.

**Author's claim:** Green-Ortiz et al. argue that monitor mode (also called visibility mode or unenforced discovery) is the critical data-gathering phase where endpoints are detected, profiled, and classified via DHCP, DNS, AD logins, CDP/LLDP, and NMAP scans — but no restrictions are enforced. An authorization result is allocated to the session for later use in traffic analysis and policy building, but not enforced.

**Evidence presented:** The SBC Manufacturing case study: 1,600 devices took 4 months with a 3-person team to map. For larger organizations, 12–18 months is not unreasonable. Key tasks during monitor mode: (1) identify suspected device type (the "what" of contextual identity), (2) determine business functionality/owner/support team, (3) traffic analysis to create baseline, (4) document into asset management database. The authors explicitly state: "Monitor mode never truly ends" — it should continue for new devices even after enforcement is live. A remediation/quarantine policy as default on the NAC system helps manage "hard denials."

**Confidence:** HIGH — Consistently reinforced across the BeyondCorp papers (log-before-enforce), Garbis & Chapman (PAM integration patterns), and NIST 800-207 migration guidance. This is one of the most convergent claims across the entire ZT literature.

### Claim 2: Distributed enforcement — applying policies as close to the endpoint as possible across four layers (intra-VLAN, inter-VLAN, inter-VRF, host-level) — yields substantial firewall rule reduction and enables firewall consolidation.

**Author's claim:** The cardinal rule is: "apply policies as close to the endpoint as possible." The authors prescribe four enforcement layers: intra-VLAN (TrustSec tags on switch ports), inter-VLAN (downloadable ACLs on switches), inter-VRF (firewalls), and host-level (agents modifying local firewall).

**Evidence presented:** SBC Corporate's implementation yielded a 50% reduction in edge firewall rules (from 350,000+) and allowed firewall consolidation, reducing both CapEx and OpEx. The authors warn that enforcement is not a finite accomplishment — policies evolve continuously as new endpoints and use cases emerge. Never fall back to firewall-only segmentation; maintain layered identity-based enforcement.

**Confidence:** HIGH — The 50% rule reduction is a specific, quantified outcome from a documented case study. The multi-layer model is Cisco's core enforcement architecture and is consistent with Green-Ortiz Ch6's layered segmentation framework.

### Claim 3: Brownfield environments require 3–4× the timeline of greenfield deployments because every newly profiled device forces recursive re-analysis of previously identified devices.

**Author's claim:** The authors contrast greenfield (new building, no existing endpoints, systematic and deterministic, 1× baseline) with brownfield (existing network, all devices expected to keep working, requires recursive analysis as each unique device is identified, 3–4× baseline).

**Evidence presented:** SBC Emerging Tech (brownfield): 3 months of recursive identification where every newly profiled device required re-running the analysis against all observed devices. SBC Financial's site selection matrix prioritized both business criticality and variety of endpoints — heterogeneous sites yield more profiling lessons that transfer. The authors recommend starting where both conditions exist: large device variety AND on-site presence ("sneaker net") for physical identity validation.

**Confidence:** HIGH — The 3–4× multiplier is a specific empirical finding from documented Cisco services engagements. This claim is directly actionable for project planning.

### Claim 4: NAC (e.g., Cisco ISE) functions as the single source of truth for access decisions across all connection mediums, but each medium (wired, wireless, VPN) has distinct rollout characteristics.

**Author's claim:** The NAC system is positioned as the identity engine for ZT enforcement, serving as the authoritative source for access decisions across wired, wireless, and VPN connections.

**Evidence presented:** Wired is the easiest starting point — passive profiling via DHCP/DNS/HTTP/CDP without changing user experience, with switch port configurations ranging from `authentication open` (monitor) to no `authentication open` (full enforcement). Wireless is harder because WLCs enforce authorization results immediately upon RADIUS completion; workaround is standing up a new SSID for managed devices. VPN is mid-difficulty — tunnel group auth source migration is trivial (3 lines), and a "permit any" authorization result provides a soft start. The authors explicitly warn against "workaround" policies that grant partial access to failed-authentication users: instead, force MAC Authentication Bypass → captive portal → verified registration → Internet-only ACL.

**Confidence:** HIGH — Detailed, medium-specific rollout guidance with concrete configuration examples. The caution against workaround policies is consistent with the broader ZT literature's emphasis on not creating exceptions.

---

## Chapter 10: Zero Trust Operations

### Claim 5: Siloed teams — where network, security, applications, and operations report to different executives with conflicting success metrics — are the #1 operational failure mode for ZT.

**Author's claim:** The authors identify organizational silos as the primary barrier to ZT success. The telltale signs: team members don't know counterparts' names, groups copy and compete instead of collaborating, funding goes to one team's projects but not another's.

**Evidence presented:** The SBC case study's first blocker was organizational: Network (CTO org) and Network Security (CIO org) had conflicting success metrics (uptime vs. threat response). The solution was moving Network Security under CTO alongside Network Admin and Network Ops, with a separate Corporate Security team (audit, pentest, IR, policy) reporting to CIO as an independent advisory body. The authors recommend gaining sponsorship at a level above both network and security leadership — a single executive with authority over both functions removes resource competition and establishes shared mission.

**Confidence:** HIGH — This is the most consistently reported non-technical barrier across the entire ZT literature. Dotse et al. (2025) found executive sponsorship was the #1 critical success factor (r = 0.78, β = 0.342, p < 0.001). The SBC reorg being the prerequisite for technical success provides a concrete case study.

### Claim 6: The Zero Trust journey is cyclical, not linear — five capabilities (Policy & Governance, Identity, Vulnerability Management, Enforcement, Analytics) form a continuous feedback loop with no final destination.

**Author's claim:** The book's capstone model presents five ongoing capabilities where analytics feeds identity, which feeds vulnerability management, which refines enforcement, which triggers policy updates, which loops back. "Zero Trust has no final destination — removing trust from a network is an ongoing, never-ending process."

**Evidence presented:** The five capabilities: (1) Policy & Governance — executive buy-in codified into policy, the foundation; (2) Identity — authentication + authorization based on contextual identity, "the long pole in the tent"; (3) Vulnerability Management — behavioral baseline vs. expected behavior; (4) Enforcement — layered, distributed, applied at correct network location; (5) Analytics — feeds all other capabilities, aggregates logs/switch counters/syslog/identity accounting. The SBC case study validates this: firewall rule cleanup went from 350,000 → ~125,000 active → further reduced via identity-based policies; TrustSec tag strategy capped at 10 tags; the question isn't "When will the building be secured?" but "Which phase is the building at, and how far along?"

**Confidence:** HIGH — The cyclical model is a synthesis that aligns with NIST 800-207's emphasis on continuous monitoring and iterative improvement. The SBC case study provides empirical grounding for the framework's practical application.

---

## Appendix A: Smart Building Central — Full Applied Use Case

### Claim 7: The SBC case study demonstrates that practical ZT implementation must constrain scope aggressively — 10 TrustSec tags maximum, 5–7 endpoint groups, and a dedicated IoT tiger team — to avoid analysis paralysis and operational chaos.

**Author's claim:** The authors' empirical finding from Cisco services: "Customers who use dynamic application of enforcement policy have the best likelihood of success when they start with no more than five to seven groups or enclaves." The SBC implementation validated this with a 10-tag TrustSec strategy.

**Evidence presented:** The SBC case study details: (1) TrustSec tag strategy capped at 10 tags (Corporate, Collaboration, IP Cameras, Printers, Print Servers, IoT, Guests, BMS, IT) with planned sub-tags deferred; (2) IP cameras received their own tag because of unique multicast discovery behavior — "carving them out was a conscious risk decision balancing security vs. operational continuity"; (3) "The Key Masters" — a dedicated tiger team for IoT device onboarding that documented ~10× more connections than manufacturers provided; (4) DNS enforcement via Cisco Umbrella with content filtering applied to corporate devices but not guests; (5) Analytics Triad: Secure Network Analytics + Secure Workload + Thousand Eyes; (6) Cultural resistance from staff bringing unauthorized devices — IT initially accommodated with dynamic quarantining but discontinued after Q1 to force proper onboarding.

**Confidence:** HIGH — This is a detailed, named, walkthrough-length case study with specific metrics and configuration details. The 10-tag cap and 5–7 enclave starting point are the most specific, empirically grounded implementation constraints in the ZT literature.

---

## Cross-Chapter Themes

1. **Identity is everything.** Without knowing what every device is, enforcement is guesswork. Monitor mode is where the real work happens.

2. **Distribution beats centralization.** Enforce at the access layer (TrustSec), across subnets (dACLs), across zones (firewalls), and on hosts (agents). No single chokepoint.

3. **Organization before technology.** The SBC reorg was the prerequisite for every technical success that followed. Siloed teams with conflicting metrics will defeat any ZT implementation.

4. **Start small, iterate.** Seven endpoint groups. One site with high variety + on-site presence. Gradual enforcement from permit/deny to port/protocol. The journey is infinite — measure progress in phases, not completion.

5. **Exceptions are the enemy.** Every exception process tends to become the rule. The authors urge critical scrutiny of every exception: "as soon as an exception process can be filed and granted, the exception process is almost guaranteed to become the rule."
