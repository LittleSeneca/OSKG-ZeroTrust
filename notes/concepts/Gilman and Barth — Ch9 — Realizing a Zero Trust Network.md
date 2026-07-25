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
claims_status: extracted
claims_extracted: 2026-07-24
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
  - topic/zt-implementation
  - topic/zt-migration
  - topic/zt-architecture
---

# Gilman & Barth — Ch9: Realizing a Zero Trust Network

The implementation chapter. Gilman & Barth pivot from architectural principles (Ch1–8) to deployment strategy: how to scope, assess, migrate, and operate a ZT network. The chapter is anchored by the two richest case studies in Zero Trust literature — Google's BeyondCorp (client-to-server) and PagerDuty's Cloud Agnostic Network (server-to-server) — each a complete migration narrative with real tradeoffs.

**Cross-references:** NIST 800-207 Ch7 provides the formal 7-step deployment cycle; this chapter is the field manual for that framework. The BeyondCorp case study is the direct source for every subsequent ZTNA product and every NIST deployment model that uses an Access Proxy / PEP gateway.

---

**Claim 1 —** The SHOULD/MUST list is ZT implementation's operational checklist → [[the-shouldmust-list-is-zt-implementations-operational-checklist]]

---

**Claim 2 —** Flow enumeration is the hardest requirement and the highest-value one → [[flow-enumeration-is-the-hardest-requirement-and-the]]

---

**Claim 3 —** Configuration management is a legitimate stepping stone to the control plane → [[configuration-management-is-a-legitimate-stepping-stone-to]]

---

**Claim 4 —** Zero Trust proxies are the bridge between ZT and legacy systems → [[zero-trust-proxies-are-the-bridge-between-zt]]

---

**Claim 5 —** Client-to-server and server-to-server migrations are different problems with different starting points → [[client-to-server-and-server-to-server-migrations-are-different-problems-with]]

---

**Claim 6 —** Log-then-enforce is THE migration procedure — validated by two independent case studies → [[log-then-enforce-is-the-migration-procedure-validated-by-two]]

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

**Claim 7 —** The two case studies demonstrate ZT is cross-domain applicable → [[the-two-case-studies-demonstrate-zt-is-cross-domain]]

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
