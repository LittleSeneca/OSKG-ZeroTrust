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

### The Monitor-Mode Imperative

The authors argue that **the biggest mistake in ZT implementation is rushing past monitor mode**. Organizations must inventory and understand endpoints *in production* — not just in a lab — because lab sampling misses the real traffic patterns and external interactions that define business-relevant behavior.

- **Monitor mode** (also called visibility mode or unenforced discovery): endpoints are detected, profiled, and classified via DHCP, DNS, AD logins, CDP/LLDP, NMAP scans, but no restrictions are enforced.
- An authorization result is still *allocated* to the session (for later use in traffic analysis and policy building), but it is not enforced.
- The SBC Manufacturing case study: 1,600 devices took **4 months with a 3-person team** to map. For larger organizations, 12–18 months is not unreasonable.
- Key tasks during monitor mode:
  1. Identify the suspected device type (the **"what"** of contextual identity)
  2. Determine business functionality, owner, support team
  3. Traffic analysis to create a baseline
  4. Document everything into an asset management database (AMDB)
- **Monitor mode never truly ends** — it should continue for new devices even after enforcement is live. A remediation/quarantine policy as the default on the NAC system helps manage "hard denials."

### Phased Rollout: Site Selection Criteria

SBC Financial used a matrix to order sites:
1. **Business criticality** — if 10% of devices at a site went offline, what's the impact?
2. **Variety of endpoints/business units** — heterogeneous sites yield more profiling lessons that transfer to other sites.

The authors recommend starting where both conditions exist: a large variety of devices *and* an on-site presence ("sneaker net") that can physically validate identities, building standard profiles reusable across the network.

### Enforcement: Layered and Distributed

When transitioning to enforcement, the cardinal rule is: **apply policies as close to the endpoint as possible**.

SBC Corporate's four enforcement layers:
| Layer | Mechanism | Scope |
|-------|-----------|-------|
| Intra-VLAN | TrustSec tags on switch ports | Same-subnet restrictions |
| Inter-VLAN | Downloadable ACLs on switches | Cross-subnet at L2/L3 boundary |
| Inter-VRF | Firewalls | Cross-security-zone |
| Host-level | Agents modifying local firewall (Secure Workload) | VM-to-VM on same chassis |

This **distributed enforcement** approach yielded a **50% reduction in edge firewall rules** (from 350,000+) and allowed firewall consolidation, reducing both CapEx and OpEx.

**Critical caution**: enforcement is not a finite accomplishment. Policies evolve continuously as new endpoints and use cases emerge. Never fall back to firewall-only segmentation; maintain layered identity-based enforcement.

### NAC as the Identity Engine

The NAC system (e.g., Cisco ISE) is the **single source of truth** for access decisions across all connection mediums:

- **Wired**: Easiest starting point. Passive profiling via DHCP/DNS/HTTP/CDP without changing the user experience. Switch port configurations range from `authentication open` (monitor) to no `authentication open` (full enforcement).
- **Wireless**: Harder — WLCs enforce authorization results immediately upon RADIUS completion. Workaround: stand up a new SSID for managed devices and use profiling on a per-SSID basis. Migration of unmanaged devices becomes a signal for contextual identity gaps.
- **VPN**: Mid-difficulty. Tunnel group auth source migration is trivial (3 lines). A "permit any" authorization result provides a soft start. Often used as a bellwether for NAC rollout readiness.

### Greenfield vs Brownfield

| Environment | Characteristics | Timeline Multiplier |
|-------------|-----------------|---------------------|
| **Greenfield** | New building, no existing endpoints. Devices added in controlled groups. Systematic, deterministic. | 1× baseline |
| **Brownfield** | Existing network, one-for-one swap or config overlay. All devices expected to keep working. Requires recursive analysis as each unique device is identified. | 3–4× baseline |

SBC Emerging Tech (brownfield): 3 months of recursive identification, where every newly profiled device required re-running the analysis against all observed devices.

### Practical Contextual Identity Considerations

- **Authentication (AuthC)**: AD users/computers is the minimum. Certificates from an org CA (or cloud MDM) are preferred — they embed identity attributes (username, device type, email) into the credential itself. Different certificates on different device types allow differentiated access even without profiling.
- **Authorization (AuthZ)**: The authors explicitly warn against "workaround" policies that grant partial access to failed-authentication users. Instead: force MAC Authentication Bypass → captive portal → verified registration (email/SMS) → Internet-only ACL. Failing users should never get internal access.
- **Segmentation**: **Start with no more than 7 endpoint groups**. The authors provide a master list of ~20 candidate groups (Corporate, Contractor, Data Center, Medical, Security, Branch, Manufacturing, Media, Quarantined, Research, Demo, Remediation, Lab, Network Devices, Shared Services, Servers, Infrastructure, UC, IoT, Headless, Guest, Authenticated). Organizations that try to bypass the 7-group rule enter "analysis paralysis." The risk assessment question: "Do the access needs of two groups differ significantly enough to justify separate policies?"

### Data Exchange

PXGRID and STIX/TAXI protocols enable cross-tool identity and vulnerability data sharing. Even when not used in active policy decisions, they add massive context to a device's identity and should be part of the architecture.

---

## Chapter 10: Zero Trust Operations

### The Organizational Problem

The authors identify **siloed teams** as the #1 operational failure mode for ZT. The four essential teams — network, security, applications, and operations — must collaborate under unified sponsorship. The telltale signs of silos:
- Team members don't know the names of counterparts in "partner" organizations.
- One group copies another's idea and competes instead of collaborating.
- Funding goes to one team's projects but not the other's.

**Solution**: Gain sponsorship at a level above both network and security leadership. A single executive with authority over both functions removes the resource competition and establishes a shared mission.

### Adoption Lifecycle (Moore's *Crossing the Chasm*)

| Group | Characteristics | How to Engage |
|-------|----------------|---------------|
| **Innovators** | Sponsors, creators of the design. Internal "venture capitalists." | Must continually evangelize as leaders change. Build ZT into governance documents and policies. |
| **Early Adopters** | Pilot/test teams. | Address questions early in the implementation cycle. Minor plan updates may suffice. |
| **Early Majority** | Responsible for long-haul migration and ongoing maintenance. Program success lives or dies here. | Address deeper questions. They need to be part of the solution. |
| **Late Majority** | Experienced with change, find obstacles at every turn. Want others to fail first. | Leadership must "take on all the risk" and de-risk sufficiently. |
| **Laggards** | Analysis paralysis. Admire problems from every angle to avoid action. | Top-down mandates. May require leadership or core team changes to thaw. |

### Team-Specific Engagement

- **Application Owners**: Must be engaged *early*. Excluding them until the end almost guarantees resistance. They hold the intellectual property, data, and customer systems.
- **Operations / Help Desk**: Need clear ownership, runbooks, operational guides, and consistent 24×7 governance documentation.
- **Network and Security**: One or both may initiate the program, but long-term oversight often shifts to operations + governance. Identity and access management (IAM) teams are critical stakeholders.

### Policy Life Cycle

The NIST 800-207 Policy Decision Point (PDP = Policy Engine + Policy Administrator) is rarely a single product — it's a **conglomeration of components** (NAC on campus, PAM in the data center, remote access solution elsewhere), each managed by different teams.

Two trustworthiness criteria:
1. **Attribution**: Criteria presented to PEPs and measured against PDPs at connection time (who, what, where, when, how).
2. **State**: Criteria derived from external sources — threat intelligence, CVE reporting, vulnerability data.

The authors recommend a **common attribution schema** (who, what, where, when, why, how) that standardizes trustworthiness measurement across all use cases and feeds into CMDBs for CAB/CCB governance processes.

### Cisco Architecture Mapping

Three primary domains where attribution evaluation and enforcement occur:
- **LAN**: DNA Center + ISE → PA/PE; access layer interfaces → PEP; TrustSec tags for segmentation.
- **WAN Edge**: vManage infrastructure; enforcement based on tag value, VXLAN headers, or application parameters.
- **Data Center**: APIC + ACI → PA/PE; VRFs, tenants, EPGs, contracts; Secure Workload for host-based firewall.

### Moves, Adds, and Changes

Onboarding new device types must go through an **Architecture Review Board**. If the device aligns 95% to an existing template, minor tweaks are handled via a defined change process. Heavy processes breed shadow processes — keep onboarding lightweight enough that people actually use it.

---

## Chapter 11: Conclusion & The SBC Applied Use Case

### The Five Capabilities — Cyclical, Not Linear

The book's capstone model presents five ongoing capabilities:

1. **Policy & Governance**: Executive buy-in codified into policy, propagated to all contributors. The foundation.
2. **Identity**: Authentication + authorization based on contextual identity. Must include an explicit onboarding process for new devices. The "long pole in the tent."
3. **Vulnerability Management**: Behavioral baseline vs. expected behavior. Reliant on contextual identity. Risk analysis feeds enforcement policy.
4. **Enforcement**: Layered, distributed, applied at the correct network location. Prevents single points of failure.
5. **Analytics**: Feeds all other capabilities. Aggregates logs, switch counters, syslog, identity accounting. Validates functionality and improves application of controls. Must consider external threat feeds.

The journey is **cyclical** — analytics feeds identity, which feeds vulnerability management, which refines enforcement, which triggers policy updates, which loops back.

### Key Takeaways from the Conclusion

- Zero Trust starts with **singular steps**; a "big bang" is rarely correct.
- Small groupings of assets reveal larger themes.
- The question isn't "When will the building be secured?" but **"Which phase is the building at, and how far along?"**
- Zero Trust has no final destination — removing trust from a network is an **ongoing, never-ending process**.

### Appendix A: Smart Building Central — Full Applied Use Case

The SBC case study is a 30+ page walkthrough of a real ZT implementation at a smart-building headquarters. Key highlights:

- **The Reorg**: The first blocker was organizational. Network (CTO org) and Network Security (CIO org) had conflicting success metrics (uptime vs. threat response). Solution: moved Network Security under CTO alongside Network Admin and Network Ops, with a separate Corporate Security team (audit, pentest, IR, policy) reporting to CIO as an independent advisory body.
- **Business Discovery Workshop**: Department heads were asked the standard who/what/where/when/how questions. Revealed widespread shadow IT: employees used personal laptops on guest Wi-Fi and transferred data via USB because corporate laptops were locked down. The guest Wi-Fi PSK was printed on plastic placards in IT cubicles.
- **VRF Design**: Five VRFs — Corporate, Building Management Systems, Labs, Guests, IoT — each with 100 VLANs allocated predictably.
- **"The Key Masters"**: A dedicated tiger team for IoT device onboarding. Every IoT device was tested in a hardened lab with its full system dependencies. Manufacturers rarely documented internal system interactions (developers lacked networking backgrounds). The Key Masters documented **~10× more connections than manufacturers provided**.
- **Firewall Rule Cleanup**: 350,000 rules → ~125,000 active → further reduced to manageable numbers via identity-based policies on ISE. Rule identification used DHCP tracing, DNS lookups, SIEM log analysis (13-month retention), and incremental disabling on campus firewalls.
- **TrustSec Tag Strategy**: Capped at **10 tags** (Corporate, Collaboration, IP Cameras, Printers, Print Servers, IoT, Guests, BMS, IT) with planned sub-tags deferred. IP cameras were given their own tag because of their unique multicast discovery behavior — carving them out was a conscious risk decision balancing security vs. operational continuity.
- **DNS Enforcement**: Cisco Umbrella for external resolution, evaluating domain age, registration, certificate status, content, and business relevance. Content filtering applied to corporate devices but not guests/personal mobile.
- **Analytics Triad**: Secure Network Analytics (NetFlow-based flow visibility) + Secure Workload (host-level IP tables enforcement and alerting) + Thousand Eyes (application response time and connectivity monitoring).
- **Cultural Resistance**: Despite policies, staff continued bringing unauthorized devices. IT operations initially accommodated them with dynamic quarantining and analysis, but discontinued this after Q1 to force proper onboarding.
- **Outcome**: SBC Inc. adopted the ZT model for all net-new and renovated buildings, creating a roadmap with phase-based progress measurement.

---

## Cross-Chapter Themes

1. **Identity is everything.** Without knowing what every device is, enforcement is guesswork. Monitor mode is where the real work happens.
2. **Distribution beats centralization.** Enforce at the access layer (TrustSec), across subnets (dACLs), across zones (firewalls), and on hosts (agents). No single chokepoint.
3. **Organization before technology.** The SBC reorg was the prerequisite for every technical success that followed. Siloed teams with conflicting metrics will defeat any ZT implementation.
4. **Start small, iterate.** Seven endpoint groups. One site with high variety + on-site presence. Gradual enforcement from permit/deny to port/protocol. The journey is infinite — measure progress in phases, not completion.
5. **Exceptions are the enemy.** Every exception process tends to become the rule. The authors urge critical scrutiny of every exception: "as soon as an exception process can be filed and granted, the exception process is almost guaranteed to become the rule."
