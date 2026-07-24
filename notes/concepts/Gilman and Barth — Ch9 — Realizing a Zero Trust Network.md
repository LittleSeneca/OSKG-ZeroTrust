---
tags:
  - source/books
  - gilman-barth
  - zt-implementation
  - zt-deployment
  - zt-migration
  - beyondcorp
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
confidence: high
source:
  title: "Zero Trust Networks: Building Secure Systems in Untrusted Networks"
  authors: "Evan Gilman, Doug Barth"
  year: 2017
  publisher: "O'Reilly Media"
  chapter: 9
  lines: "6167–7479"
  local_file: "sources/books/_txt/Zero_trust_networks_building_secure_systems_in_untrusted_networks.txt"
related:
  - "[[NIST 800-207 — Ch7 — Migration]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
  - "[[Gilman and Barth — Ch1 — Zero Trust Fundamentals]]"
  - "[[Books Index]]"
  - "[[Concepts Index]]"
---

# Gilman & Barth — Ch9: Realizing a Zero Trust Network

The implementation chapter. Gilman & Barth pivot from architectural principles (Ch1–8) to deployment strategy: how to scope, assess, migrate, and operate a ZT network. The chapter is anchored by the two richest case studies in Zero Trust literature — Google's BeyondCorp (client-to-server) and PagerDuty's Cloud Agnostic Network (server-to-server) — each a complete migration narrative with real tradeoffs.

**Cross-references:** NIST 800-207 Ch7 provides the formal 7-step deployment cycle; this chapter is the field manual for that framework. The BeyondCorp case study is the direct source for every subsequent ZTNA product and every NIST deployment model that uses an Access Proxy / PEP gateway.

---

## Claim 1: The SHOULD/MUST list is ZT implementation's operational checklist

**Authors' claim:** The RFC 2119–style prioritized list defines what must exist for a system to be "considered compatible with the zero trust design" vs. what can be deprioritized under cost constraints.

The list:

| Priority | Requirement | Rationale |
|----------|------------|-----------|
| **MUST** | All network flows MUST be authenticated before being processed | Authentication is "the single most important component" — without it, we're forced to trust the network |
| **SHOULD** | All network flows SHOULD be encrypted before being transmitted | Reduces the attack surface of communication to the device itself; hostile-network assumption |
| **MUST** | Authentication and encryption MUST be performed by the application-layer endpoints | VPN concentrators and TLS-terminating load balancers leave upstream traffic exposed — cannot claim ZT if middleware handles these responsibilities |
| **MUST** | All network flows MUST be enumerated so access can be enforced | Without an expected-flow database, the system can't highlight unexpected communications. Distributing flow-definition responsibility into the organization is the only way to make this feasible. |
| **SHOULD** | Strongest authentication and encryption suites SHOULD be used | Device/application capabilities may limit choices, but administrators should be aware that weakening suites compromises security |
| **SHOULD** | Authentication SHOULD NOT rely on public PKI — private PKI instead | Multiple risks: growing number of trusted CAs each capable of fraudulent signing, state-actor judicial compulsion with gag orders, certificate pinning overhead |
| **SHOULD** | Devices SHOULD be regularly scanned, patched, and rotated | Reimaging servers quarterly and personal devices every two years is preferred over long-term scanning — device trustworthiness degrades over time |

**Evidence presented:** These are practitioner judgments from the authors' experience at Netflix and PagerDuty, not derived from formal threat models. The RFC 2119 framing is deliberate — it echoes the IETF convention of MUST/SHOULD/MAY to signal implementation weight.

**Confidence:** HIGH. Every subsequent ZT standard preserves this same hierarchy. NIST 800-207 requires authentication and authorization of all sessions (Tenet 4), encryption of all traffic (implicit in Tenet 1/2), and continuous device posture assessment (Tenet 5). CISA ZTMM maps MUST items to Traditional→Initial maturity and SHOULD items to Advanced→Optimal.

**What's at stake:** If every SHOULD gets deferred indefinitely, you have a perimeter system with extra logging — not ZT. The MUST list is the minimum viable ZT footprint. Organizations that claim "ZT" without flow enumeration are doing identity-aware perimeter, not ZT.

**Who disagrees:** Forrester's ZTX framework extends the scope well beyond network — data, workloads, people, devices, networks, automation, visibility. This list is narrower, deliberately. CISA's five-pillar model adds Governance and Visibility as explicit pillars, which Gilman & Barth treat as implicit in the MUST items.

**My assessment:** The MUST list is the most actionable single page in Zero Trust literature. NIST's seven tenets are more abstract; CISA's five pillars are broader. This list is what you tape to the wall during implementation planning. The private PKI requirement is the most controversial item — realistic for Google/PagerDuty scale, aspirational for smaller organizations — but the reasoning (public CA trust is trust in unknown third parties) is sound.

---

## Claim 2: Flow enumeration is the hardest requirement and the highest-value one

**Authors' claim:** "Without the list of expected network flows, zero trust systems are unable to highlight unexpected communications which need attention from administrators or should be denied." And critically: "deferring the effort to enumerate flows will ultimately result in a task list that is considered infeasible."

**Evidence presented:** 
- Flow data should be the **source of truth** for access decisions — generate enforcement configuration from the flow database, not independently
- Capture the **intended use** of a flow along with policy details (e.g., "LB access — from LB hosts to web application")
- Prefer **narrowly defined flows** over broad access
- For flow discovery: physical networks use SPAN/mirror ports or TAP devices; virtualized networks use cloud-native flow logs (AWS VPC Flow Logs); endpoint-based discovery via software firewalls in log-only mode gives richer application context
- **Zone-by-zone migration**: leverage existing perimeter boundaries to build ZT on either side, then spread zone to zone — incremental, not big-bang

**Confidence:** VERY HIGH. This is validated by every real migration: Google's netflow analysis pipeline, PagerDuty's iptables role-to-IP mapping, NIST 800-207's Step 3 (identify key processes and evaluate risks). Flow enumeration is the gating function — you can't do ZT without it, and it's the hardest inventory problem.

**What's at stake:** If flow enumeration is impossible (too many flows, too much churn, insufficient tooling), ZT is impossible. Organizations that skip this step are doing ZT theater — they have identity-aware proxies but no ability to detect or deny unexpected lateral movement.

**Cross-reference — NIST 800-207 Ch7:** NIST's Step 2 (Identify Assets) and Step 3 (Identify Key Processes) are the same exercise at higher abstraction. NIST categorizes assets as hardware, digital artifacts, and shadow IT; Gilman & Barth's flow enumeration is the network-level instantiation. Both agree: without the inventory, the Policy Engine will deny requests due to insufficient information.

---

## Claim 3: Configuration management is a legitimate stepping stone to the control plane

**Authors' claim:** The mature ZT control plane systems (policy engine, trust engine, controller) are ideal but unnecessary at the start. Configuration management tools (Chef, Puppet, Ansible) can serve as a "temporary stepping stone" — driving host-based firewalls, cryptographic configuration, and policy distribution — while the network matures.

**Evidence presented (PagerDuty):**
- Chef was already deployed on every VM; extending it to generate iptables rules required no new infrastructure
- Role-based iptables chains enumerated expected IPs for each server role, providing per-host microsegmentation
- Benefits: network compute power scales with instance count; failures are isolated (many small firewalls instead of "the firewall")
- Downsides: eventual consistency means policy changes aren't instantaneous; constant validation of expected state is required
- **Maturation path:** as the system grew, IPsec configuration graduated out of Chef into a dedicated service that could converge faster

**Confidence:** HIGH. This pattern is validated by PagerDuty's production ZT network (2013–2014, still running) and mirrors the NIST 800-207 hybrid approach. CM-driven policy distribution is how most organizations will start their ZT journey — it doesn't require buying new infrastructure.

**What's at stake:** CM as a stepping stone is pragmatic but insufficient for mature ZT. Host-based enforcement is vulnerable if the host is compromised. Mature systems push enforcement across an isolation boundary (hypervisor, host OS in containerized systems, network security groups).

**Cross-reference — NIST 800-207 Ch7:** NIST's Step 5 (Identify Candidate Solutions) explicitly considers client footprint, protocol support, and deployment model. The CM-driven approach maps to the agent-based gateway model in NIST's taxonomy — it requires components on the client asset but doesn't require new central infrastructure.

---

## Claim 4: Zero Trust proxies are the bridge between ZT and legacy systems

**Authors' claim:** Zero trust proxies "can be used to build a zero trust network" but must be deployed **on the same device as the workload** — not on dedicated appliances. External proxies that handle authentication and then forward to backend services over untrusted links violate the ZT model.

**Two proxy modes:**

| Mode | Use Case | How It Works |
|------|----------|-------------|
| **Reverse proxy** | ZT-enabled clients accessing services | Proxy receives connection, validates authorization, passes request to application |
| **Forward proxy** | Non-ZT-aware legacy components accessing ZT services | Legacy component communicates through co-located proxy that handles authentication |

**The isolation requirement:** Non-ZT-aware components behind a forward proxy must be **completely isolated** — all network communication to/from that component must go through its authentication proxy. Direct mechanical connection is preferred.

**Confidence:** HIGH. This is exactly the BeyondCorp Access Proxy model and the architecture behind every ZTNA product (Zscaler, Cloudflare Access, AppGate). The co-location requirement is what distinguishes ZT proxies from traditional reverse proxies.

**Cross-reference — NIST 800-207 Ch3:** The Access Proxy maps to NIST's Policy Enforcement Point (PEP) — the component that "enables, monitors, and eventually terminates connections between a subject and an enterprise resource." Gilman & Barth's insistence on co-located proxies is stricter than NIST's model, which allows the PEP to be a separate component (e.g., the resource gateway deployment variation).

---

## Claim 5: Client-to-server and server-to-server migrations are different problems with different starting points

**Authors' claim:** The decision of where to start "should focus on which target is the weakest link in the system's network defenses."

| Starting Point | Advantages | Challenges |
|---------------|-----------|-----------|
| **Client-to-server** (BeyondCorp) | Clients are physically mobile on uncontrolled networks — high value; user experience parity between office/remote is compelling | No existing automation on client machines; diverse device types; harder to retrofit |
| **Server-to-server** (PagerDuty) | Existing automation tools already installed; less diverse providers; servers house sensitive data | Internal actors may resist change; requires deep infrastructure knowledge |

**Confidence:** HIGH. Both case studies validate their respective starting points and both succeeded. The field has largely standardized on client-to-server first (ZTNA products), but server-to-server (service mesh, workload identity) is the harder long-term problem.

**Cross-reference — NIST 800-207 Ch7:** NIST's Step 3 recommends starting with a "low-risk business process" — cloud-based resources and remote worker workflows are flagged as good candidates. This favors the client-to-server approach for most organizations. Green-Ortiz et al.'s maturity model adds the dimension of organizational readiness: do you have the DevOps maturity for server-to-server first?

---

## Claim 6: Log-then-enforce is THE migration procedure — validated by two independent case studies

**Authors' claim (policy rollout procedure):**
1. Deploy proposed policy in logging-only fashion
2. Collect production traffic over a sufficient period
3. Investigate traffic that would be rejected by the proposed policy
4. Enforce the proposed policy
5. Repeat until all desired policy is deployed
6. Enable a default-deny policy when all expected flows are captured

**Evidence presented:** Both Google and PagerDuty independently converged on this pattern:

| Organization | Domain | Log-Then-Enforce Implementation |
|-------------|--------|-------------------------------|
| **Google BeyondCorp** | Client-to-server | Traffic analysis pipeline: sampled netflow from every switch → compare against canonical ACL between unprivileged and privileged networks → iteratively make non-passing traffic work in BeyondCorp. Unprivileged network simulator on all devices: logging mode → enforcement mode → 30-day successful enforcement → device assigned to unprivileged network |
| **PagerDuty** | Server-to-server | Firewall: deploy rules as LOG-only → classify flows → reduce logged traffic → reconfigure to DROP non-whitelisted traffic. IPsec: deploy policies in *none* state → transition small portions to *use* state → reconfigure to *required* state. Phased approach minimized time in risky intermediate state |

**Google's specific metrics:** >99.9% eligible traffic for 30 days in logging mode → enforcement mode; >99.99% eligible traffic → enforcement; 30 days successful enforcement → unprivileged network assignment. Phased migration by job function/workflow/location.

**Confidence:** VERY HIGH. This is the most validated procedure in ZT literature — two independent $1B+ organizations converged on the same approach. NIST 800-207 Ch7 §7.3.6 explicitly recommends "reporting-only mode" with the same logic.

**Cross-reference — NIST 800-207 Ch7:** NIST's Step 6 (Initial Deployment and Monitoring) is the formalization: "few policy sets are complete on the first iteration," grant access for most requests initially, log and trace all connections, compare actual patterns against developed policy. Same procedure, different vocabulary.

---

## Case Study: Google BeyondCorp (in detail)

### Motivation
By the early 2010s, Google was "increasingly uncomfortable with the perimeter model." Tens of thousands of employees worked physically outside offices; thousands of visitors were invited inside daily. The castle-wall metaphor was "unsustainable." The goal: a system that "mediates access according to who you are, not which network you use." Four years of design and iteration.

### Core Design Principle
> "This new model dispenses with a privileged corporate network entirely. Instead, access depends solely on device and user credentials, regardless of a user's network location."

All access: fully authenticated, fully authorized, fully encrypted based on device state and user credentials. No VPN required. User experience identical between local and remote apart from latency differences.

### Major Components

**Device Identity:**
- **Device Inventory Database** — tracks all managed devices through lifecycle changes; meta-inventory amalgamates multiple inventory sources
- **Device certificates** — X.509 machine certificates with private key in TPM or qualified certificate store; certificate uniquely identifies device but does not single-handedly grant access (it's a key to information, not a privilege)
- Device qualification process validates certificate store effectiveness; certificates renewed periodically
- Mobile: iOS uses identifierForVendor; Android uses EMM device ID (not certificates)

**User Identity:**
- User Database + Group Database integrated with HR processes (job categorization, usernames, group memberships)
- Externalized SSO system validates primary + second-factor credentials
- Generates short-lived tokens for authorization decisions

**Access Proxy (AP):**
- Internet-facing; enforces encryption between client and application
- Built on Google Front End (GFE) infrastructure — already provided load balancing, TLS management, global reachability, DDoS protection
- Extended GFE with authentication and authorization policies
- **User authentication:** integrates with Google's Identity Provider; supports OpenID Connect, OAuth, and custom protocols; strips credentials before forwarding to backend (prevents replay, keeps proxy transparent to backends)
- **Authorization:** centralized ACL engine queryable via RPC; domain-specific language for ACLs; combines coarse-grained authorization at the AP with fine-grained authorization at the backend
- **Mutual authentication between proxy and backend:** LOAS (Low Overhead Authentication System) bidirectionally authenticates and encrypts all proxy-to-backend traffic; ensures backend can trust metadata (user identity, device trust level) inserted by AP

**Inventory-Based Access Control:**
- Access Control Engine within the AP provides per-request service-level authorization
- Factors: user info, group membership, device certificate, device inventory data, inferred trust level, location
- Dynamic trust inference examples: unpatched OS → reduced trust; specific device class → assigned trust level; new location → different trust level
- Example policies: "Restrict bug tracker access to full-time engineers using engineering devices"; "Restrict finance app to FT/PT employees in finance ops using managed non-engineering devices"

### Migration Strategy

**Unprivileged network:** All client devices assigned to a network that closely resembles an external network — only connects to internet, limited infrastructure (DNS, DHCP, NTP), and Puppet. Strictly managed ACL between this network and rest of Google's network.

**Workflow qualification phases:**
1. Available from privileged network + VPN externally
2. Available from privileged network + via AP from external/unprivileged networks (split DNS)
3. Available via AP from all networks (external, privileged, unprivileged)

**VPN decommissioning:**
1. Restrict VPN to users with proven need
2. Monitor usage; remove access from non-users
3. Monitor active users; encourage VPN surrender when all workflows available via AP

**Traffic analysis pipeline:**
1. Capture sampled netflow from every switch
2. Analyze against canonical ACL between unprivileged and privileged networks
3. Attach non-passing traffic to specific workflows/users/devices
4. Progressively make non-passing traffic work in BeyondCorp

**Device-level unprivileged network simulator:** installed on all user devices; two modes — logging (captures ineligible traffic but permits it) and enforcement (captures and drops ineligible traffic)

**Phased migration:**
1. Identify candidate sets by job function/workflow/location
2. Simulator in logging mode → identify >99.9% eligible for 30 days
3. Simulator enforcement mode for >99.99% eligible → user can revert to logging
4. 30 days successful enforcement → recorded in device inventory
5. Successful enforcement + candidate set → unprivileged network assignment

**Exemption handling:** Known list of unqualified workflows; users could request exemptions with approval; notifications when workflows became qualified.

### Lessons Learned

| Lesson | Detail |
|--------|--------|
| **Communication** | Under-communication → surprised users, inefficient remediation, unsustainable IT load. Over-communication → change-resistant users seek unnecessary exemptions, users become inured, access issues conflated with other efforts. |
| **Developer support** | Make developers' lives easier: sane defaults, walkthrough guides, documentation, sandboxes (separate AP instances reachable via DNS override) |
| **Data quality** | Typos, transposed identifiers, repairs corrupting device records → unintentional access loss. Solutions: local workflow improvements, automated input validation, double-entry accounting. Secondary benefit: inventory accuracy forced patch compliance higher. |
| **Sparse data** | Upstream sources don't share device identifiers; heuristics handle most deltas but 100% accuracy requires extremely complex edge-case handling. Tiny fraction of mismatched devices can lock hundreds of employees out. |

### Outcome
As of 2017, the majority of Google employees work completely within BeyondCorp. Four-year journey from ambition to near-completion. Google acknowledges its unique scale and resources but notes that by 2017, commercial offerings had matured enough that smaller enterprises didn't need to build from scratch.

**Cross-reference — NIST 800-207 Ch7:** BeyondCorp's migration is the canonical implementation of NIST's hybrid brownfield model. Every element maps: workflow qualification = NIST Step 3 (identify key processes), traffic analysis pipeline = NIST Step 6 (monitoring mode), phased rollout = NIST's recurring cycle. The unprivileged network concept is the ZT equivalent of NIST's micro-perimeters.

---

## Case Study: PagerDuty's Cloud Agnostic Network (in detail)

### Motivation
Server-to-server interactions across multiple public cloud providers. Some cloud providers offer no stateful firewall, private addressing, or network ACLs — hosts are on the public internet and must secure themselves. Additionally, WAN communication is normal operation: business-critical systems deployed across three regions with the goal of surviving entire region loss.

### Architecture

**Configuration Management as Automation Platform (Chef):**
- Policy centrally managed in code; enforcement distributed into the fleet
- Benefits: network compute scales with instances; failures are isolated (many small firewalls instead of "the firewall")
- Downsides: constant validation of expected state required; changes eventually consistent
- Long-term: IPsec configuration graduated out of Chef into dedicated service

**Dynamically Calculated Local Firewalls:**
- Servers categorized by **role** (capturing services and expected communication patterns)
- iptables chains constructed per-host, enumerating IP addresses for servers of each role
- Rules define expected access by role; non-matching packets dropped
- Equivalent to relationship-oriented policy / microperimeterization

**Distributed Traffic Encryption (IPsec Mesh):**
- Host-to-host IPsec in transport mode, all traffic encapsulated in UDP (cloud providers don't always route ESP)
- Strongest cipher suites per RFC 6379
- Benefits: all packets encrypted and authenticated by every node; capacity scales with host count
- Rationale for kernel-level vs. application-level: application encryption has implementation errors, lacks configuration controls for vulnerability response, can introduce performance regressions
- Out-of-process encryption is increasingly the standard — separate process reduces attack surface for secret data

**Decentralized User Management:**
- Local users and groups programmatically constructed on each host (removes network dependency)
- Centralized definitions in Chef databags; servers only get users/groups that need access
- No centralized LDAP dependency

### Rollout (Log-Then-Enforce)
1. New policies defined
2. Policies deployed in no-op / metrics collection mode
3. Metrics inspected over long period
4. Policy enabled slowly from small percentage to 100%

**Firewall:** hosts configured to LOG → rules classify flows → logs reduced → reconfigure to DROP non-whitelisted

**IPsec:** policies in *none* state → small portions to *use* state (optimistic) → *required* state; phased approach minimized risky intermediate state where fallback to plaintext could be blocked by stateful firewalls

### Provider-Agnostic Value
When PagerDuty moved off one cloud provider: normally a multi-month effort with high-risk change windows. With provider-agnostic ZT network: ~6 weeks total (mostly research/testing/reworking Chef), production changes deployed in **one week during normal business hours with zero customer impact**.

---

## Claim 7: The two case studies demonstrate ZT is cross-domain applicable

**Authors' claim:** The case studies cover the spectrum — client-to-server (BeyondCorp) and server-to-server (PagerDuty), large enterprise and mid-size, custom-built and CM-driven. Together they show ZT principles adapt to different starting points, scales, and constraints.

**Cross-domain comparison:**

| Dimension | BeyondCorp (Google) | PagerDuty |
|-----------|-------------------|-----------|
| **Focus** | Client-to-server | Server-to-server |
| **Scale** | Tens of thousands of employees | Mid-size SaaS platform |
| **Resources** | Custom infrastructure from scratch | Leveraged existing Chef + open source |
| **Network** | Corporate LAN + remote | Multi-cloud public internet |
| **Enforcement** | Centralized Access Proxy | Distributed iptables per host |
| **Encryption** | LOAS (custom) + TLS | IPsec host-to-host mesh (kernel) |
| **Identity** | X.509 device certs + SSO + TPM | Role-based Chef automation |
| **Migration** | 4-year phased, netflow pipeline, simulator | Incremental log-then-enforce, per-role |
| **Key Lesson** | Data quality is the hidden bottleneck | Provider-agnostic pays off in agility |

**Confidence:** VERY HIGH. These two case studies are the most-cited ZT implementation narratives in the literature. NIST 800-207 references the BeyondCorp model implicitly throughout the PEP/PDP architecture. CISA's ZTMM and DoD's ZT RA use similar migration patterns.

---

## Chapter 9 Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| MUST/SHOULD prioritized list | HIGH | Being too network-centric; CISA's five pillars add identity and data dimensions |
| Flow enumeration as highest-value requirement | VERY HIGH | Organizations that can't enumerate flows (shadow IT, M&A) — but that just means they can't do ZT |
| CM as stepping stone to control plane | HIGH | Being mistaken for end state — CM-driven enforcement is insufficient when hosts are compromised |
| ZT proxies as bridge to legacy | HIGH | Co-location requirement being ignored; dedicated proxy appliances marketed as "ZT" |
| Client vs. server migration tradeoffs | HIGH | Field has overly converged on client-to-server (ZTNA products); server-to-server underinvested |
| Log-then-enforce as THE migration procedure | VERY HIGH | Organizational impatience — leadership demanding enforcement before sufficient observation |
| Cross-domain applicability via case studies | VERY HIGH | Scale — both case studies are tech-native companies with DevOps maturity most enterprises lack |

**Strongest section:** The two case studies. Together they provide the most complete, validated migration playbook in ZT literature. Every subsequent implementation guide (NIST, CISA, DoD, Green-Ortiz) is a formalization of patterns first demonstrated here.

**Weakest section:** The controller-less architecture section (CM as stepping stone) is undertheorized. It presents CM as temporary but doesn't address the migration path from CM-driven to controller-driven. The PagerDuty case study partially fills this gap (IPsec graduated to a dedicated service), but the general pattern isn't articulated.

**Unique contribution to OSKG-ZeroTrust:** This chapter bridges the gap between ZT theory (NIST 800-207, CISA ZTMM) and ZT practice (BeyondCorp papers, Green-Ortiz case studies). It's the only source that provides both the architectural framework *and* the operational playbook *with* validated case studies. The MUST/SHOULD list is the single most actionable prioritization in ZT literature; the log-then-enforce procedure is the most validated migration pattern; and the two case studies are primary source material for every subsequent implementation guide.
