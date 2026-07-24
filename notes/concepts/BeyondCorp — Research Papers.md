---
tags:
  - source/papers
  - beyondcorp
  - google
  - zt-implementation
  - zt-migration
  - oskg-zerotrust
  - tier/3
  - security/zero-trust
  - security/implementation
created: 2026-07-24
confidence: high
related:
  - "[[NIST 800-207 — Ch7 — Migration]]"
  - "[[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]]"
  - "[[BeyondProd — Cloud-Native Security]]"
  - "[[Concepts Index]]"
sources:
  - "BeyondCorp_1_A_New_Approach.txt (Ward & Beyer, Dec 2014)"
  - "BeyondCorp_2_Design_to_Deployment.txt (Osborn, McWilliams, Beyer, Saltonstall, Spring 2016)"
  - "BeyondCorp_4_Migrating.txt (Peck, Beyer, Beske, Saltonstall, Summer 2017)"
  - "BeyondCorp_6_Building_a_Healthy_Fleet.txt (King, Janosko, Beyer, Saltonstall, Fall 2018)"
---

# BeyondCorp — Research Papers

**The canonical implementation story of Zero Trust at Google.** This note consolidates Papers 1, 2, 4, and 6 of Google's six-paper series (excluding Papers 3 and 5 on the Access Proxy and Login Challenges). Together they trace the full arc from architectural vision through multi-year operational deployment — the most thoroughly documented large-scale ZT migration in the industry.

---

## Executive Summary

Between 2009 and 2018, Google undertook one of the most ambitious enterprise security transformations ever attempted: **removing the privileged corporate network entirely**. The BeyondCorp initiative replaced the castle-and-moat perimeter model with a system where **access depends solely on device and user credentials, regardless of network location**. Every access request is authenticated, authorized, and encrypted on a per-request basis.

The program spanned nearly a decade, involved coordination across virtually every layer of the corporate technology stack, and was executed through a meticulously phased migration that **caused 30% fewer support issues** than comparable large-scale IT changes. The key innovation was simple in concept but radical in practice: **the internal network is as fraught with danger as the public Internet — treat them identically.**

---

## Paper 1: A New Approach to Enterprise Security (Ward & Beyer, Dec 2014)

### Claim 1: The perimeter security model's core assumptions no longer hold — the internal network is as dangerous as the public Internet, and trust in network location is fundamentally misplaced.

**Author's claim:** The founding paper articulates the core critique of perimeter security: "Key assumptions of this model no longer hold: The perimeter is no longer just the physical location of the enterprise, and what lies inside the perimeter is no longer a blessed and safe place to host personal computing devices and enterprise applications."

**Evidence presented:** Google's operational experience demonstrated that trust in the internal network is misplaced. The alternative: assume the internal network is as dangerous as the public Internet and build applications accordingly. The paper lays out six foundational components that remain the backbone of BeyondCorp: (1) Device Inventory Database — tracks every managed device through procurement/changes/decommissioning, amalgamating data from multiple source databases; (2) Device Identity via X.509 Certificates — stored in hardware/software TPM, qualification validates certificate store, periodic renewal enforces continued compliance, identifies device but does NOT single-handedly grant access; (3) User and Group Database — tightly integrated with HR processes, updated on join/role-change/leave; (4) SSO — centralized authentication with primary + second-factor credentials, generates short-lived tokens; (5) Unprivileged Network — resembles external network but within private address space, only connects to Internet, limited infrastructure (DNS, DHCP, NTP), and configuration management (Puppet); (6) Internet-Facing Access Proxy — all enterprise applications exposed externally, enforces encryption, global reachability, load balancing, access control checks, health checks, DoS protection.

**Confidence:** HIGH — This is the foundational critique from the canonical ZT implementation at Google, published in USENIX ;login:. The six-component architecture is the reference design that NIST 800-207's logical components (PDP, PEP, PIP) later abstracted.

### Claim 2: The BeyondCorp access flow enforces per-request authorization through a continuously running trust inference pipeline that dynamically computes trust levels for both devices and users based on OS patch level, device model, security scan results, location, and behavioral heuristics.

**Author's claim:** The Access Control Engine performs per-request authorization checking: user in correct group, sufficient trust level, device managed and in good standing, sufficient device trust level. All checks pass → forward to backend; any check fails → denied. This is fed by a "continuously running pipeline" that dynamically infers trust levels.

**Evidence presented:** Trust inference factors: device — OS patch level, specific device model/class, recent security scan results; user — access from new locations, role changes, behavioral heuristics. Both static rules and heuristics are used. A device missing recent OS patches might be relegated to reduced trust. A specific phone model might be assigned a particular trust level. The early migration strategy (2014, still conceptual): workflow qualification (VPN-only → split DNS → access proxy for ALL networks), job function analysis, VPN reduction, Traffic Analysis Pipeline (sampled netflow from every switch), Unprivileged Network Simulator (client-side traffic monitor with logging and enforcement modes), migration triggers (>99.9% eligible traffic for 30 days → simulator enforcement → >99.99% + 30 days enforcement → VLAN reassignment). Early warning: "We anticipate a long tail of workflows that will take some time to move to BeyondCorp. For example, fat-client applications that use proprietary protocols to talk to servers will be a challenge." This prediction was validated spectacularly.

**Confidence:** HIGH — Primary-source architecture documentation from the implementing team. The early migration strategy framework, while still conceptual in 2014, already contains the key operational patterns (simulator, gradual migration triggers, long-tail anticipation) that Papers 2 and 4 later validate.

---

## Paper 2: Design to Deployment at Google (Osborn et al., Spring 2016)

### Claim 3: Tiered access — organizing trust levels into tiers of increasing sensitivity with each resource requiring a minimum trust tier — was the critical architectural innovation between Papers 1 and 2, enabling minimally interrupted users by limiting devices to the minimum tier needed.

**Author's claim:** The architecture matured from Paper 1's binary trust model (managed vs. unmanaged) to tiered access: trust levels organized into tiers of increasing sensitivity, each resource associated with a minimum trust tier, device trust tier assignment must be ≥ resource's minimum. Higher tiers require more frequent user-presence tests and shorter-lived credentials. "Limiting a device to the minimum tier needed → minimally interrupted users."

**Evidence presented:** Example: centrally managed laptop missing noncritical OS patches → downgraded to intermediate tier → access to business apps but not sensitive ones. Missing critical security patch or AV reports infection → only remediation services. Known lost/stolen → denied all access. The evolved architecture components (Paper 1 → Paper 2): Trust Model — Binary → Tiered Access; Device Identity — Single certificate → Certificate as persistent GUID with collision detection via auxiliary identifiers; Inventory — Meta-inventory database → Device Inventory Service continuously updated pipeline ingesting 3M deltas/day from 15+ sources, 80+ TB retained; Access Control — Per-request authorization → Centralized Access Control Engine referencing access policy, Trust Inferer output, resource requested, and real-time credentials; Network — Unprivileged VLAN → Dynamic VLAN assignment via RADIUS + 802.1x where Trust Inferer annotates VLAN eligibility per device.

**Confidence:** HIGH — The tiered access model is a well-documented architectural evolution supported by specific operational examples. The comparison table showing Paper 1 → Paper 2 evolution is extracted directly from the papers.

### Claim 4: The Device Inventory Service — ingesting 3M deltas/day from 15+ sources, correlating disparate identifiers, and precomputing trust evaluations — is the single most important operational component of BeyondCorp, and its data quality directly determines access availability.

**Author's claim:** The Device Inventory Service is "arguably the single most important operational component" — a continuously updated pipeline that ingests from 15+ data sources at 30-100 changes/second, transforms data into common format, correlates disparate sources into unique device-specific records, notifies Trust Inferer to trigger reevaluation, and publishes trust tier assignments and VLAN annotations to enforcement gateways.

**Evidence presented:** Data types: Observed (programmatically generated — security scan results, AD sync timestamps, OS version/patch level, installed software) and Prescribed (manually maintained by IT — assigned owner, allowed users/groups, DNS/DHCP assignments, explicit VLAN access). Correlation challenge: different data sources use different identifiers (asset ID, serial number, hard drive serial, certificate fingerprint, MAC address) — records combined when inventory agent reports several identifiers together, system handles component replacement during device lifecycle. Trust evaluation: Trust Inferer references dozens of fields (millions available); high trust requirements example: encrypted, all management agents executing successfully, most recent OS security patches installed, consistent data across all input sources. Precomputation strategy: trust evaluation is precomputed (not at request time) to reduce data pushed to gateways, reduce computation at access time, and enable pre-commit tests and canary deployments for policy changes — update latency typically <1 second.

**Confidence:** HIGH — Specific operational metrics (3M deltas/day, 15+ sources, 80+ TB, <1 second latency) from the implementing team. The precomputation design decision (evaluate at pipeline time, not request time) is a specific architectural choice with clear rationale.

---

## Paper 4: Migrating to BeyondCorp — Maintaining Productivity While Improving Security (Peck et al., Summer 2017)

### Claim 5: The breakthrough operational insight was partitioning for parallel progress — deploying a new VLAN in its final BeyondCorp configuration and incrementally moving devices to it, rather than incrementally restricting the privileged VLAN.

**Author's claim:** Rather than incrementally restricting the privileged VLAN (removing one application/server at a time from the legacy network), Google deployed a new VLAN in its final BeyondCorp configuration and incrementally moved devices to it. This allowed the network layer to achieve stability independently, isolated the network layer from migration policy details via RADIUS-provided VLAN assignments, and enabled parallel progress at every layer of the stack.

**Evidence presented:** Parallel workstreams: Network — new VLANs, 802.1x, RADIUS policy server; Client platforms — certificate generation/installation, user authentication tools; Applications — service and workflow remediation; Processes — continuous refinement of procedures. 802.1x foundation: install certificates on every user device (required new CA with APIs, per-OS distribution tools, telemetry for monitoring), transition to 802.1x for all network access (re-provision switches, integrate with policy-driven RADIUS), initial RADIUS policy matched existing assignments (avoiding failures from new server), deploy in auditing mode comparing new vs. legacy assignments, enable new policy when differences sufficiently few. Result: VLAN assignments controlled by high-level software and data-driven policies in near-real time, decoupled from network hardware configuration.

**Confidence:** HIGH — This is an explicit, named architectural decision (partitioning for parallel progress) from the operational migration playbook, validated by the documented outcome of >50% fleet migration within one year.

### Claim 6: The MNP Simulator — translating the network ACL into local iptables rules with logging and enforcement modes — was the operational linchpin that enabled high-velocity migration by testing enforcement at the client level before committing to network-level VLAN changes.

**Author's claim:** "Without this feature, we wouldn't have gained the confidence we needed to move devices to MNP at nearly the speed (or with the high level of success) that we did." The Managed Non-Privileged (MNP) Simulator translates the actual MNP network ACL into local iptables/Packet Filter rules (using Capirca). Logging mode monitors traffic, logs source/destination of non-MNP-compatible traffic to central repository, identifies failing users and failing services. Enforcement mode actually blocks/drops non-MNP traffic at the client level before network-level VLAN migration.

**Evidence presented:** The simulator enabled: identifying devices with MNP-compliant traffic → automatic VLAN assignment; identifying devices/users/services relying on noncompliant traffic → initiate remediation projects; testing enforcement at client level (easy/fast to toggle) before committing to network-level VLAN migration. The Access Proxy handled most high-usage applications because Google's core philosophy favors browser-based applications — apps behind the Access Proxy have CNAMEs in public DNS, accessible from corporate and public networks with equivalent security, causing VPN usage to "immediately and dramatically decrease." Within one year of activating the automated analysis/verification/migration process, over 50% of the fleet was moved to non-privileged network access. The authors claim: "According to our rough estimates, the resultant productivity gains easily outweigh the implementation costs of BeyondCorp."

**Confidence:** HIGH — Primary-source description of a specific operational tool with documented outcomes (50% fleet migration in one year). The Capirca-based implementation and two-mode operation (logging/enforcement) are specific technical details.

### Claim 7: The strategic pivot from "prove the user will be successful before migrating" (opt-in) to "assume the user will be successful and migrate" (opt-out) was essential for reaching full coverage — without it, the long tail of noncompliant applications would have blocked migration indefinitely.

**Author's claim:** Phase 1 — newly provisioned, unanalyzed devices defaulted to privileged network; users of noncompliant apps couldn't be migrated; risk that unmigrated users could create NEW noncompliant applications. Phase 2 — after reducing exceptions by remediating high-volume use cases, all devices defaulted to MNP site-by-site, with exceptions granted only to users in job functions with unremediated applications. This policy shift from opt-in to opt-out was essential.

**Evidence presented:** Difficult use cases (the long tail): NFS/CIFS file servers required major project to move home directories to local disk with secure cloud backup, replace NFS with Google Drive; CAD editors deeply dependent on NFS required special solutions; thick client applications with proprietary protocols; Java RMI and direct socket connections; license servers using non-HTTP sockets; some HTTP applications not designed to present client certificates; load balancer logic incompatible with Access Proxy. Temporary exceptions policy: for critical framework services without compliant solutions, temporarily opened access — but only when a concrete plan for compliant solution existed, preventing exceptions from becoming permanent. Scaling support: empowered tech support (BeyondCorp champions), self-service infrastructure (automated emails, web portal for delay requests, dedicated error-messaging application, internal discussion list), internal publicity campaign (laptop stickers, visible articles). Phased rollout: small-scale pilot geographically close to project team → progressive expansion to locations with local experts → eventual expansion to risky workflows and distant sites. "Tech support load decreased as rollout size and affected workflows increased" — counterintuitive but the system matured faster than the user base grew.

**Confidence:** HIGH — This is a documented strategic pivot with specific operational mechanics. The "temporary exceptions only with concrete remediation plan" policy is a specific implementation of the broader ZT principle of avoiding permanent exceptions.

### Claim 8: BeyondCorp caused 30% fewer support issues than comparable wide-scale IT changes, and was responsible for only 0.3% of tech support issues — the user experience emphasis (self-service, grace periods, VPN elimination as productivity win) made the migration a net positive for users.

**Author's claim:** The end result metrics: BeyondCorp responsible for only 0.3% of issues handled by tech support (from initial 0.8%), 30% fewer support issues than comparable wide-scale internal IT changes, VPN usage dramatically decreased, remote access significantly easier and faster, network management simplified.

**Evidence presented:** Self-service infrastructure: automated emails with timeline, impact summary, links to FAQs/documentation/escalation; self-service web portal for users to delay migration (business-critical time constraints); internal discussion list for crowdsourced answers; dedicated web application for error messaging — clearly identified common problems, provided resolution steps, linked to knowledge base; users could fix group membership and certificate issues themselves. Internal publicity campaign: laptop stickers, common logos, visible articles in offices — focus on informing, educating, and helping built trust and goodwill directly.

**Confidence:** HIGH — These are specific, quantified operational metrics from the implementing team. The 30%-fewer-support-issues figure and 0.3% support load are specific measurable outcomes.

---

## Paper 6: Building a Healthy Fleet (King et al., Fall 2018)

### Claim 9: The endpoint is the new perimeter — fleet health and device trustworthiness replace network location as the foundation of access decisions, and the "identified state" solves the chicken-and-egg problem of transitioning untrusted devices into a trustworthy state.

**Author's claim:** "The platforms that make up the fleet are the new perimeter." The paper shifts focus from network architecture to endpoint security. A healthy device "can withstand most attacks" (preventative controls) and "provides sufficient telemetry to contain a compromise when one occurs" (detective controls).

**Evidence presented:** Ten threat classes mapped to controls: unknown devices → fleet inventory; platform compromise via misconfigured OS → configuration management; security control bypass → policy management; privilege escalation → resilience against takeover; malware → software control + anti-malware; prolonged persistence → remotely verifiable platform state; authentication bypass → robust auth of platform and user; unauthorized data access → encryption at rest + in transit; attack concealment → logging and log collection; attack repudiation → detection and response. The Identified State: a critical operational insight — transitioning a device into a trustworthy state requires access to a client software repository, but a client software repository is a sensitive system (chicken-and-egg). Solution: an intermediate "Identified" state between untrusted and trusted — device is in inventory and believed to be in good standing but not yet trusted, can access a subset of the client software repository, can download remediation software, report device state, apply patches, fulfill trusted platform requirements.

**Confidence:** HIGH — Primary-source documentation of Google's endpoint security model. The Identified State is a specific architectural solution to a well-defined operational problem (bootstrapping trust).

### Claim 10: Flexible policies using thresholds rather than absolutes, combined with platform-normalized security evaluations, prevent draconian enforcement that causes users to seek workarounds — "100% uniform control deployment is a mythical state where unicorns frolic unconcerned about malware."

**Author's claim: "We always attempt to introduce thresholds of policy compliance rather than institute absolute requirements. This strategy allows users greater flexibility to operate within a good state and avoids draconian rule sets that break many of our users (causing them to seek out workarounds or overrides)." Non-critical patches get a grace period before downgrading access.

**Evidence presented:** Platform measurement and control parity: different platforms have fundamentally different capabilities — Chrome OS has robust software control via Secure Access; Linux has no out-of-the-box malware prevention. Google's approach: normalized security evaluations — analyze each platform against ideal control state, evaluate gaps, produce fleet health report (not a report card, a shared understanding of capabilities). For each platform evaluate: can the platform support the control? Is it on by default? Can we measure its state? Is the fleet in compliance? Where preventative controls are lacking: compensate with higher monitoring/detection signal confidence or more effective controls on a different platform. Exception management: exceptions must be measurable and time-based; classify root causes consistently; if exception perpetually renewed → control is not working → redesign; focus on new machines in compliance from first use → grandfather existing fleet → cluster failure reasons → tackle largest/riskiest clusters → repeat. Control rollout process: design/prototype → dogfood on targeted populations → monitor mode first → iterate → graduate to enforcement. Communications: map each control to threats addressed, high transparency and explicit criteria build consensus.

**Confidence:** HIGH — The "thresholds not absolutes" principle and "100% uniform control is mythical" are specific, documented operational philosophies. The platform-normalized evaluation methodology is a concrete approach to heterogeneous environments.

---

## Cross-Cutting Themes

### Claim 11: The BeyondCorp migration followed a consistent cadence — Analyze → Log → Warn → Enforce → Default — where the Log phase (simulation, audit mode, monitor mode) was never skipped across any major change, and this pattern is the single most important operational lesson for ZT migration.

**Author's claim:** Every major change (VLAN migration, trust tier enforcement, fleet health controls) went through the sequence: Analyze → Log → Warn → Enforce → Default. The Log phase was the critical data-gathering step that built confidence for enforcement.

**Evidence presented:** The cadence appears across all four papers: Paper 1's Unprivileged Network Simulator (logging mode → enforcement mode → VLAN migration triggers); Paper 2's deployment strategy (Phase 1: apply access policy that mirrored IP-based perimeter model to allow safe deployment of incomplete components; Phase 2: gradual policy replacement as meta-inventory matured); Paper 4's 802.1x foundation (auditing mode comparing new vs. legacy assignments → enable when differences sufficiently few), MNP Simulator (logging → enforcement), and phased rollout (small pilot → progressive expansion → eventual expansion); Paper 6's control rollout (monitor mode first → iterate → graduate to enforcement) and audit-only mode for BAB. Additional cross-cutting themes: Partitioning for independence — decouple layers so they progress independently (network layer reached stability without waiting for application remediation); data quality as a security dependency — "accurate inventory = access" drove unprecedented data quality improvements with secondary security benefits (better patch compliance); user experience as a security requirement — productivity maintained through simulator preventing broken workflows, self-service tools, grace periods, VPN elimination as productivity win paying for implementation.

**Confidence:** HIGH — The Analyze → Log → Warn → Enforce → Default cadence is directly observable across all four papers and all major BeyondCorp changes. This is the single most convergent operational pattern across the entire ZT literature — NIST 800-207 Ch7, CISA ZTMM, Green-Ortiz Ch8, and Garbis & Chapman all converge on monitor-mode-first migration. BeyondCorp is the canonical validation of this pattern at the largest documented scale.

---

## Comparison to NIST 800-207

| Dimension | NIST 800-207 | BeyondCorp |
|---|---|---|
| **Policy Engine** | Policy Decision Point (PDP) | Access Control Engine |
| **Policy Enforcement** | Policy Enforcement Point (PEP) | Access Proxy, RADIUS, gateways |
| **Policy Information** | Policy Information Point | Device Inventory Service, User/Group DB, Trust Inferer |
| **Trust Algorithm** | Abstract | Trust Inferer — precomputed tiers with continuous reevaluation |
| **Network Model** | Untrusted networks | Unprivileged network (VLAN) + external networks treated identically |
| **Device Identity** | Implied | X.509 certificates with hardware-backed TPM |
| **Migration Guidance** | High-level (Ch7) | Detailed operational playbook with specific metrics |

BeyondCorp **predates** NIST 800-207 and represents the most fully realized implementation of the abstract model NIST later codified.

---

## Gaps and Unanswered Questions

1. **Papers 3 and 5 not covered**: The Access Proxy (Paper 3) and Login Challenges (Paper 5) contain important technical detail not captured here.
2. **Cost**: No cost data published. The paper claims productivity gains outweigh implementation costs, but this is a rough estimate.
3. **Google-specific privilege**: Google's unusual degree of control over its fleet (all managed devices, browser-first culture, homogeneous infrastructure) may not transfer to organizations with heterogeneous environments.
4. **Fat-client future**: The papers acknowledge fat-client applications as the hardest case but don't present a general solution — only tactical workarounds.
5. **Post-2018 evolution**: What happened after Building a Healthy Fleet? Did the long tail ever fully resolve?
