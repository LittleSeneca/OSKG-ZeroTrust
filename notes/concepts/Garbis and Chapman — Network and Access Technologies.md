---
tags:
  - source/books
  - garbis-chapman
  - zt-network
  - zt-nac
  - zt-vpn
  - zt-ngfw
  - zt-pam
  - oskg-zerotrust
created: 2026-07-24
source:
  title: "Zero Trust Security: An Enterprise Guide"
  authors: "Jason Garbis and Jerry W. Chapman"
  year: 2021
  publisher: "Apress"
  local_file: "sources/books/_txt/Zero_Trust_Security_An_Enterprise_Guide.txt"
  chapters: "6–10, 12"
  lines: "3427–3805 (Ch6), 3807–4251 (Ch7), 4252–4616 (Ch8), 4617–4872 (Ch9), 4873–5133 (Ch10), 5515–5752 (Ch12)"
related:
  - "[[Concepts Index]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[CISA ZTMM — Device Network App Data Pillars]]"
---
# Garbis & Chapman — Ch6–10, 12: Network and Access Technologies in Zero Trust

**Combined note.** Six chapters covering existing network security technologies — Network Infrastructure (Ch6), NAC (Ch7), IDS/IPS (Ch8), VPNs (Ch9), NGFW (Ch10), and PAM (Ch12) — each evaluated against Zero Trust principles. Combining them makes the comparative evaluation explicit: every chapter asks the same question ("does this technology advance or impede Zero Trust?") and reaches a distinct but interrelated verdict. The pattern reveals a spectrum: some technologies are outright replaced (VPNs), some are diminished and reframed (NAC, NGFW), some are repositioned as ZT data sources (IDPS, PAM), and some (core firewalls, DNS, WAFs) persist but with simplified roles.

---

## Chapter 6: Network Infrastructure

### Core claim
**Existing network infrastructure will be reshaped by Zero Trust — not eliminated, but transformed.** Firewalls simplify, DNS becomes policy-driven, WANs diminish, and secondary infrastructure (load balancers, WAFs) must be consciously positioned relative to PEPs.

### Firewalls

**Firewalls persist but their role bifurcates.** The authors present three scenarios (Figure 6-1):

- **Scenario A (Traditional):** IP-centric 5-tuple rules (`src IP, src port, dest IP, dest port, protocol`). This "impoverished vocabulary" cannot express identity or context, and leads to overprivileged access because IP addresses are not identities and get remapped across subnets.
- **Scenario B (PEP behind firewall):** The firewall rules simplify dramatically as enforcement shifts to the Zero Trust PEP, which terminates encrypted tunnels and enforces identity-centric rules. The firewall effectively cedes control.
- **Scenario C (PEP merged with firewall):** The PEP is integrated into the firewall platform — common when the ZT vendor is also the NGFW vendor. Functionally equivalent to Scenario B; differences arise in vendor-specific policy models and manageability.

**Verdict:** Firewalls will continue to exist in Zero Trust networks, but with simplified configurations, fewer rules, and reduced management burden. The access controls historically attempted with firewalls are achieved more effectively through Zero Trust PEPs. Organizations can reduce firewall size, complexity, and cost.

### DNS

**DNS is both a critical infrastructure component and a security monitoring tool.** The chapter distinguishes:

- **Public DNS:** Hierarchical, unencrypted by default (UDP), publicly accessible. Limited security issues beyond availability.
- **Private DNS:** The source of complexity — private DNS servers are only accessible from local networks, return non-routable IPs, and create headaches for remote users and cloud resources. ZT solutions must solve DNS resolution for private hosts across distributed environments.

**ZT approaches to DNS:** Two models — (1) publish internal server records to public DNS, directing external users to cloud-facing proxies (static, cloud-routed model); (2) transmit client DNS requests to private DNS servers via a PEP based on search domains (dynamic, eliminates need for public DNS entries, suits virtual/cloud environments).

**DNS monitoring:** Monitoring DNS for known-bad domains is "high-value and low-risk" and must be part of any ZT architecture. ZT platforms should include DNS filtering/blocking and react to malicious DNS requests by adjusting user access.

**Encrypted DNS:** The IETF is standardizing DNS over TLS (DoT, RFC 8310) and DNS over HTTPS (DoH, RFC 8484). The authors recommend DoT (works within enterprise DNS setups) and strongly discourage DoH (bypasses enterprise DNS controls). Some ZT systems improve DNS security by tunneling DNS requests through encrypted ZT tunnels, providing encryption *and* enterprise monitoring simultaneously.

### Wide Area Networks (WANs)

**WANs diminish under Zero Trust.** Two factors contribute: (1) Zero Trust systems "don't care" about the underlying network — they presume it's insecure and encrypt all traffic; (2) Internet connectivity is ubiquitous, inexpensive, and reliable enough for business-critical communications.

**SD-WAN complication:** SD-WANs rely on network traffic metadata (port, protocol) for QoS traffic shaping. ZT encrypted overlay tunnels are opaque to these intermediaries, so SD-WAN routing decisions may be impaired. Coordination between ZT and networking teams is required.

**Verdict:** Zero Trust adoption will reduce WAN reliance. WANs can often be reduced or eliminated, replaced by simple Internet connectivity. This is a cost-saving conversation that network, IT, and security teams should have.

### Load Balancers, ADCs, API Gateways

**These will persist largely unchanged** — they provide performance and availability functions, not security. The key consideration is topology: if they sit *behind* a PEP (within the implicit trust zone), they work well with enclave-based and cloud-routed models. Resource-based and microsegmentation models could interfere because they may require an active network intermediary.

### Web Application Firewalls (WAFs)

**WAFs retain a role even in Zero Trust environments.** ZT reduces the attack surface (limiting access to only authorized users) but doesn't eliminate attacks from authorized users whose devices may be compromised. "If 10% of the user population uses an application, ZT eliminates the ability of the remaining 90% to even attempt to attack it." The 10% may still host malicious software — WAFs protect against this. The authors applaud WAF deployment for internal applications as reflecting a "presumption of compromise" mindset.

---

## Chapter 7: Network Access Control (NAC)

### Core claim
**NAC represents an early attempt at identity-centric network access, but its 802.1x architecture is fundamentally incompatible with Zero Trust's universal scope.** NAC's value is diminished, not eliminated — it can serve as a complementary component for guest networking and device discovery but cannot be the core of a ZT environment.

### How NAC works (and why it fails ZT)

NAC uses the 802.1x protocol (IEEE/IETF), operating at Layer 2 (EAPOL). The device (supplicant) communicates credentials to an Authenticator (network switch), which validates via RADIUS against an Authentication Service. On success, the device is assigned to a VLAN. **The architecture has five fatal limitations from a ZT perspective:**

1. **Local-only scope:** The supplicant and authenticator must be on the same broadcast domain — same physical network media, enterprise-owned and operated. NAC is useless for remote users or cloud resources.
2. **Coarse-grained access:** 802.1x assigns devices to VLANs — commonly with dozens or hundreds of services visible. A device can only be assigned to one VLAN at a time. This is "not compatible with the principle-of-least-privilege tenet of Zero Trust."
3. **No encryption or remote access:** NAC does not provide network traffic encryption or remote access (though some vendors have added these in separate products).
4. **Static posture:** Once assigned to a VLAN, many NAC solutions have no further involvement beyond periodic reauthentication. Access control within the VLAN falls to firewalls with their own (IP-centric) policy model.
5. **Hardware-dependent:** Requires ubiquitously deployed enterprise-owned network hardware — incompatible with cloud, home, and third-party networks.

### NAC's legitimate residual roles

**Guest network access:** This is the strongest remaining use case. The authors distinguish unmanaged (password-protected Wi-Fi, no user identification) from managed (registration portal, time-limited access, employee sponsorship workflow). Their recommendation: a password-protected guest Wi-Fi (WPA3 preferred) separated from the corporate network is sufficient for most enterprises. ZT doesn't change guest networking requirements.

**BYOD comparison:** The authors provide a thorough comparison table (Table 7-2): NAC can only serve on-premises users and only provides coarse-grained VLAN access; ZT provides granular, identity-specific access for both on-premises and remote users equally, with optional clientless access for pure BYOD.

**Device discovery:** NAC detects devices at the infrastructure layer when they connect — a byproduct of how it works. This discovery data can feed into a ZT policy model, as in Google BeyondCorp, which used 802.1x for coarse-grained network assignment *alongside* an access proxy for fine-grained access control.

**Device posture checks:** NAC products often include posture assessment (OS patch level, AV status). The ability to create and enforce *dynamic* policy based on these attributes is more important than the attribute collection itself — and ZT platforms are better at this.

### Verdict

> "802.1x-based NAC functions are not suitable to use as the core part of any Zero Trust environment."

NAC can be part of a ZT environment (guest networking, device discovery) but 802.1x is architecturally limited. Some NAC vendors have innovated beyond 802.1x with cloud-based services and remote access, but enterprises must evaluate these carefully against ZT requirements.

---

## Chapter 8: Intrusion Detection and Prevention Systems (IDPS)

### Core claim
**IDPS capabilities remain essential, but the *how* changes under Zero Trust.** Network-based IDPS is challenged by encrypted ZT tunnels; host-based IDPS gains relative advantage. IDPS will increasingly be "baked in" to the ZT platform rather than deployed as standalone tools — in some sense, the ZT system *becomes* the IDPS.

### Host-based vs. network-based IDPS

| Dimension | Host-Based | Network-Based |
|-----------|-----------|---------------|
| Deployment | Software agent on user devices or servers | Network tap/span port (passive) or in-line (active) |
| Advantage in ZT | Has access to traffic "behind" the PEP — encryption doesn't blind it | Can cover devices that don't support agents (IoT, unmanaged) |
| Disadvantage in ZT | Agent proliferation and management burden | Encrypted ZT tunnels make traffic opaque; only works where nodes are deployed |
| Detection functions | File integrity, process behavior, privilege escalation, rootkit detection | DNS monitoring, deep packet inspection, network metadata analysis |
| Prevention functions | Process termination, block software installation, terminate connections | DNS filtering, content blocking, connection termination, sandbox detonation |

### The encryption problem

This is the chapter's central technical argument. Zero Trust typically uses mutual TLS (mTLS) with short-lived certificates between PEPs. A standard network IDPS between PEPs cannot decrypt this traffic — even if it has the application-level certificates, it lacks the ZT tunnel certificates. TLS 1.3 makes this worse by encrypting additional handshake portions.

**The only solutions:**
- Make the NIDPS "Zero Trust-aware" — part of the ZT system, with access to decryption keys (Figure 8-1, Scenarios B and C)
- Deploy NIDPS within the implicit trust zone, behind the PEP, where traffic is in native protocol
- Shift toward host-based IDPS, which operates below the encryption layer

### IDPS deployment across ZT models (Figure 8-1)

- **Resource-based model:** ZT-aware NIDPS required between PEPs; HIDPS on resources works unchanged.
- **Enclave-based model:** Standard NIDPS can operate within the implicit trust zone behind the PEP. ZT-aware NIDPS needed between PEPs.
- **Cloud-routed model:** Same pattern — standard NIDPS behind the PEP in the implicit trust zone.
- **Microsegmentation model:** HIDPS is the primary option; NIDPS may not have clear chokepoints.

### IDPS as ZT data source and enforcement catalyst

The authors advocate for a vision where IDPS is not a separate function but part of the "security fabric":

- IDPS provides input data (threat detection events) to the PDP
- PDP adjusts risk scores and triggers broader actions (step-up authentication, device quarantine across all networks)
- ZT context (user risk level, device posture, resource sensitivity) informs IDPS scrutiny level — reducing false positives and infrastructure load
- Standards like STIX/TAXII enable structured threat intelligence sharing between IDPS and ZT platforms

### Verdict

IDPS capabilities are "more likely going to be 'baked in' to an enterprise's Zero Trust platform, as opposed to being a standalone tool." Organizations should expect to increase host-based IDPS usage and invest in network-based IDPS that are integrated into the ZT system. The goal is not more detection points but smarter, context-aware enforcement.

---

## Chapter 9: Virtual Private Networks (VPNs)

### Core claim
**VPNs must be replaced — not augmented, not integrated, but retired.** This is the authors' strongest and most unequivocal verdict across all six chapters. Even a well-configured VPN suffers from architectural flaws that Zero Trust inherently solves. The chapter is effectively a prosecution brief against enterprise VPNs.

### Five fatal VPN flaws

1. **Static identity model:** VPNs authenticate users against IAM (LDAP/RADIUS) and can use group membership, but access is typically identical regardless of device, location, or risk context. "This makes it harder for security teams to restrict access from personal devices, or to prevent the abuse of stolen credentials."

2. **Static resource model:** Access is granted to fixed subnets or IP addresses. VPNs cannot dynamically resolve target resources in modern virtualized/DevOps environments. "This leads organizations to grant too-broad network access, in order to keep users productive."

3. **Single entry point:** VPNs impose a perimeter-based model: one ingress point, all resources must be connected via internal LAN/WAN. This is technically impossible in distributed cloud environments and forces users to disconnect/reconnect to different VPN servers for different resources.

4. **Exposed attack surface:** VPN servers expose open ports on the Internet — "an inviting target for attackers worldwide." The authors cite "many, many recent and widely publicized VPN vulnerabilities" and call it "unconscionable to expose the 'front door' of your enterprise network in this fashion."

5. **Remote-access silo:** VPNs are only a remote access tool — they cannot enforce access for on-premises users. This creates duplicated expenses, duplicated work, and inconsistent policies that default to too-broad access.

### What Zero Trust provides instead

The ZT model (Figure 9-2) is contrasted point-by-point:

| VPN Limitation | ZT Replacement |
|---------------|----------------|
| Static identity + group membership | Dynamic, contextual access based on user, device, network, and resource attributes |
| Fixed IP/subnet access | Dynamic resource resolution via PDP |
| Single entry point | Distributed PEPs — users connect directly to the PEP protecting the target resources |
| Open port on Internet | Entry points cloaked (SPA) or moved to cloud platform |
| Remote-only silo | Unified access control for on-premises AND remote users |

**Two architectural advantages unique to ZT:** (1) Hiding the network entry point from unauthorized users — "a huge step forward in terms of security"; (2) a single unified access control model across all environments, eliminating the VPN silo and its operational overhead.

### Deployment model differences

- **Enclave-based and cloud-routed models:** Inherently provide remote access — fully replace VPNs.
- **Resource-based and microsegmentation models:** May not provide built-in remote access — requires careful vendor evaluation.

### Verdict

> "VPNs provide an outdated and frankly insecure approach to remote access, and must be retired or replaced as organizations move to Zero Trust."

The authors are unambiguous: your enterprise "shouldn't contain a remote access solution (enterprise VPN). It should just be an access solution, which is deployed so that it enforces access control for both remote and on-premises users, based on a unified platform and policy model."

---

## Chapter 10: Next-Generation Firewalls (NGFW)

### Core claim
**NGFWs are neither sufficient as a Zero Trust platform nor irrelevant to one — they are a component whose role depends on architecture.** The NGFW market will blur into the ZT landscape as vendors add ZT capabilities, but NGFW-based solutions can impose architectural constraints that limit the ZT journey.

### What NGFWs are

NGFWs evolved from traditional 5-tuple firewalls by adding IDS/IPS, application awareness, URL filtering, and malware detection. Some NGFW vendors have added Zero Trust PEP capabilities. The authors give credit: NGFW providers were "pioneers in enabling and enforcing some Zero Trust principles for on-premises enterprise networks."

### What NGFWs are not

NGFWs are not platforms that provide security for "all users for all resources regardless of location." They typically lack fine-grained remote access, user authentication, encryption, device isolation (no user agent PEP), and are often hardware-based. Their scope of control is limited by design.

### The encryption implications (Figure 10-1)

NGFWs deployed between ZT PEPs face the same encryption problem as IDPS. Three deployment scenarios:

- **Scenario A — Core firewall only:** The NGFW operates on network headers only (no payload access needed for basic firewall functions). Works unchanged.
- **Scenario B — Logical PEP with re-encryption:** The NGFW decrypts, inspects, re-encrypts. High processing load, added latency, expensive appliance required. The NGFW must be considered part of the ZT platform.
- **Scenario C — Logical PEP with expanded implicit trust zone:** The NGFW decrypts but doesn't re-encrypt before forwarding. Less workload, but expands the implicit trust zone — a ZT anti-pattern.

**Critical warning:** Policy misalignment risk when the NGFW (as logical PEP) and the second PEP enforce different policies from different vendors with different policy models.

### Network architecture constraints (Figure 10-2)

Some NGFW-based ZT platforms impose a **single-entry-point architecture** (Scenario A):

- Remote users backhaul through one PEP into the enterprise network
- Distributed resources require WAN/backbone
- Perpetuates the hard-perimeter/soft-interior model
- Adds WAN latency and bandwidth costs
- PEP1 is "so far away" from remote resources that it loses policy fidelity

The preferred alternative is **distributed entry points** (Scenario B):

- Users connect directly to their authorized PEPs
- No backhaul — reduced latency, reduced WAN costs
- All PEPs enforce full fine-grained, identity-centric, dynamic policies
- PEPs can discover attributes about their local protected environments via API

### Verdict

The key ZT architecture decisions are "the sources of identity and context available to the PDP, and how broadly the policy model can be applied via PEPs distributed across enterprise assets." No single commercial platform today applies universally. NGFW vendor platforms may be sensible core components, but architects must understand their boundaries, integration capabilities, and architectural constraints. Rich APIs and integration support are essential — siloed security solutions are "antithetical to a Zero Trust approach."

---

## Chapter 12: Privileged Access Management (PAM)

### Core claim
**PAM provides valuable functions (vaulting, secrets management, session recording) that persist under Zero Trust, but PAM is identity-aware rather than identity-centric — it cannot substitute for a full ZT platform.** Integration between PAM and ZT enhances both.

### Three core PAM functions

1. **Password vaulting:** Secure storage and lifecycle management of privileged credentials. Evolved from "checking out" passwords to automated, ephemeral credential rotation. Supports API access for service accounts and application bootstrapping. Valuable because it enforces least privilege around credential access, enforces business processes for sensitive resource access, and ensures audit logging.

2. **Secrets management:** Expanded beyond passwords to certificates, API keys, cloud tenant info, hashes, SSH keys, database connection strings. Unified secure storage for any sensitive information needed to secure systems, accessible only to authenticated/authorized identities, with integrity guarantees.

3. **Privileged Session Management (PSM):** Intercepts/proxies admin access (RDP, SSH) to monitor, record, and constrain privileged sessions. Provides keylogging/session recording for audit/compliance and "supervised" admin access (real-time oversight by a second individual). Can enforce RBAC at the command level — e.g., allow IIS site restart but block IISRESET.

### The "800-pound gorilla": password vaulting and Zero Trust

The authors make a striking argument:

> "The entire premise of password vaulting is based on the non-Zero Trust approach of a too-open network, where every user has ongoing network access to every server, and therefore a vault with server password obfuscation and rotation is required. This premise is no longer true with Zero Trust!"

In theory, a ZT network could eliminate passwords for privileged server access entirely — PEPs enforce policies tied to context and business processes, so the vault becomes unnecessary. The authors don't recommend decommissioning existing PAM vaults but advise against deploying new ones for ZT-protected environments. Secrets management and session recording remain relevant regardless.

### Three ZT+PAM integration patterns

1. **PAM behind a PEP (Figure 12-2):** The simplest and most immediately valuable — protect the PAM server itself by placing it behind a PEP. Prevents unauthorized users/devices from even seeing the "keys to the kingdom."

2. **PDP consumes PAM policies (Figure 12-3):** The PDP integrates with PAM to consume information about high-value servers (which require stronger auth) or administrator access policies. PAM policies inform ZT enforcement decisions.

3. **PAM consumes PDP context (Figure 12-4):** PAM uses ZT-provided identity/device attributes (e.g., geolocation) to make better access decisions. Addresses the fact that most PAM solutions lack built-in remote access — they can leverage ZT's remote access capabilities.

The latter two patterns are forward-looking — not common in practice today but expected to grow as ZT platforms become more open.

### Verdict

PAM is "identity-aware, rather than identity-centric." It uses enterprise IAM for authentication and group membership for access, but this is typically the limit of its scope. PAM is not a ZT substitute but a complement. The growing adoption of serverless computing and immutable infrastructure is also reducing the relevance of traditional PSM and password vaulting, as admins shift to "as code" workflows where they never log into production systems.

---

## Synthesis: The Spectrum from Replacement to Persistence

These six chapters reveal a consistent evaluative framework. Garbis & Chapman judge each technology against the same ZT criteria — identity-centrism, dynamic policy, universal scope, encrypted transport, least privilege, and unified control plane — and the answers distribute across a clear spectrum:

| Technology | Verdict | Role Under ZT | Key Limitation |
|-----------|---------|---------------|----------------|
| **VPNs (Ch9)** | **Replace** | Eliminated; ZT remote access replaces it entirely | Static, perimeter-based, remote-only silo, exposed attack surface |
| **NAC (Ch7)** | **Diminish** | Retained for guest networking and device discovery only; 802.1x is not ZT-compatible | Layer 2, local-only, coarse-grained VLAN assignment, hardware-dependent |
| **NGFW (Ch10)** | **Reframe** | Core firewall functions persist; IDS/IPS functions migrate into ZT platform; NGFW may become a ZT PEP | Encryption blinds intermediate NGFWs; single-entry-point architectures perpetuate perimeter model |
| **IDPS (Ch8)** | **Integrate** | Functions absorbed into ZT platform; shift from network-based to host-based + ZT-aware NIDPS; IDPS becomes data source and enforcement catalyst | Encrypted tunnels blind passive NIDPS; agent proliferation on endpoints |
| **PAM (Ch12)** | **Complement** | Secrets management and session recording persist; password vaulting diminishes under ZT; PAM+PDP integration enhances both | Identity-aware not identity-centric; vaulting premise assumes too-open network |
| **Core firewalls (Ch6)** | **Simplify** | Rules become simpler; enforcement shifts to PEPs; reduced size/cost | IP-centric rules cannot express identity |
| **DNS (Ch6)** | **Adapt** | ZT-driven private DNS resolution; DNS monitoring integrated into ZT policy; encrypted DNS with enterprise visibility | DoH bypasses enterprise controls |
| **WANs (Ch6)** | **Reduce** | Diminished reliance; can be eliminated; replaced by Internet + encrypted ZT tunnels | SD-WAN QoS depends on traffic metadata that ZT tunnels hide |
| **WAFs (Ch6)** | **Persist** | Internal WAFs remain valuable; ZT reduces attack surface but doesn't eliminate attacks from authorized users | Protects at application layer only |
| **Load Balancers/ADCs (Ch6)** | **Persist unchanged** | Continue behind PEPs within implicit trust zone | May conflict with resource-based/microsegmentation ZT models |

### Key insight: The unifying pattern is the shift from network-enforced to identity-enforced security

Every technology in this set faces the same fundamental displacement: **security decisions that were historically made at the network layer (by IP address, VLAN, subnet, or physical location) are migrating to the identity layer (by user, device, context, and dynamic policy).** Technologies that enable this shift (ZT PEPs, host-based agents, encrypted tunnels) gain relevance; technologies that resist it (VPNs, 802.1x NAC, passive NIDPS) lose relevance.

The secondary insight is that **encryption is the forcing function.** Zero Trust's requirement for encrypted transport between PEPs is what most directly breaks legacy network security appliances (NIDPS, intermediate NGFWs, SD-WAN traffic shaping). Technology that cannot see inside the tunnel cannot enforce policy — and the only legitimate way to see inside is to *be* part of the ZT platform.

### Cross-reference notes

- **NIST 800-207 Ch3 (Logical Components):** Garbis & Chapman's PEP-centric analysis maps directly to NIST's PDP/PE/PEP architecture. The firewall discussion (Scenario B vs. C) is essentially asking whether the PEP is *behind* or *merged with* the network gateway — a deployment choice NIST's model accommodates but doesn't prescribe.
- **CISA ZTMM Network/Environment Pillar:** CISA's maturity progression from Traditional (perimeter-based, VPN-dependent) through Initial, Advanced, to Optimal (fully distributed ZT enforcement) aligns exactly with the trajectory Garbis & Chapman describe — VPNs at Traditional, NAC at Initial/Advanced, distributed PEPs at Optimal.
- **NSA Network Environment Pillar:** The NSA's emphasis on eliminating implicit trust and encrypting all traffic in transit directly supports Garbis & Chapman's arguments about the encryption problem for NIDPS and NGFWs — the NSA guidance doesn't fully address the operational tension between encryption and inspection that Garbis & Chapman surface.
