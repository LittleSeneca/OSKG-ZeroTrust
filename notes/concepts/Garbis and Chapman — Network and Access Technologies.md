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

## Claim 1 (Ch6 — Firewalls): Firewalls persist under Zero Trust but their role bifurcates — rules simplify dramatically as enforcement shifts to ZT PEPs, and the access controls historically attempted with firewalls are achieved more effectively through identity-centric policy.

**Author's claim:** Garbis & Chapman present three scenarios: (A) Traditional IP-centric 5-tuple rules with "impoverished vocabulary" that cannot express identity or context, leading to overprivileged access; (B) PEP behind firewall — firewall rules simplify dramatically as enforcement shifts to the ZT PEP; (C) PEP merged with firewall — functionally equivalent to B. Their verdict: "Firewalls will continue to exist in Zero Trust networks, but with simplified configurations, fewer rules, and reduced management burden. The access controls historically attempted with firewalls are achieved more effectively through Zero Trust PEPs. Organizations can reduce firewall size, complexity, and cost."

**Evidence presented:** The 5-tuple model (`src IP, src port, dest IP, dest port, protocol`) is explicitly critiqued: IP addresses are not identities and get remapped across subnets. The authors provide a figure (6-1) showing the three deployment scenarios and their policy complexity implications. The firewall's retained role is for advanced features that access switches cannot provide (IPS, malware detection, TCP normalization, VPN termination).

**Confidence:** HIGH — The firewall evaluation is systematic across three deployment scenarios. The verdict is measured (persist but simplify) rather than absolutist, consistent with Green-Ortiz and the BeyondCorp papers which also preserve firewalls as one enforcement layer among many.

## Claim 2 (Ch6 — DNS): DNS is both a critical infrastructure component and a security monitoring tool under ZT — private DNS resolution must adapt to distributed environments, and DNS monitoring for known-bad domains is "high-value and low-risk."

**Author's claim:** The authors distinguish public DNS (hierarchical, unencrypted by default) from private DNS (source of complexity — only accessible from local networks, returns non-routable IPs). Two ZT models for DNS: (1) publish internal records to public DNS directing external users to cloud-facing proxies; (2) transmit client DNS requests to private DNS servers via a PEP based on search domains. DNS monitoring is described as "high-value and low-risk" and "must be part of any ZT architecture."

**Evidence presented:** On encrypted DNS: the IETF is standardizing DNS over TLS (DoT, RFC 8310) and DNS over HTTPS (DoH, RFC 8484). The authors recommend DoT (works within enterprise DNS setups) and "strongly discourage" DoH (bypasses enterprise DNS controls). Some ZT systems tunnel DNS requests through encrypted ZT tunnels, providing encryption and enterprise monitoring simultaneously. The authors note that ZT platforms should include DNS filtering/blocking and react to malicious DNS requests by adjusting user access.

**Confidence:** HIGH — The DoT vs. DoH recommendation reflects a specific, well-reasoned position grounded in enterprise operational requirements. The DNS monitoring claim is widely supported across security frameworks.

## Claim 3 (Ch6 — WANs): WAN reliance will diminish under Zero Trust — ZT encrypted overlays combined with ubiquitous, inexpensive Internet connectivity can often replace dedicated WAN links, creating a cost-saving opportunity.

**Author's claim:** "Zero Trust systems don't care about the underlying network — they presume it's insecure and encrypt all traffic." Combined with ubiquitous, inexpensive, and reliable Internet connectivity, the authors argue that WANs can often be "reduced or eliminated, replaced by simple Internet connectivity." This is "a cost-saving conversation that network, IT, and security teams should have."

**Evidence presented:** SD-WAN complication: SD-WANs rely on network traffic metadata (port, protocol) for QoS traffic shaping — ZT encrypted overlay tunnels are opaque to these intermediaries, so SD-WAN routing decisions may be impaired. Coordination between ZT and networking teams is required. WAFs retain a role even in ZT environments: "If 10% of the user population uses an application, ZT eliminates the ability of the remaining 90% to even attempt to attack it. The 10% may still host malicious software — WAFs protect against this."

**Confidence:** MEDIUM — The WAN reduction claim is directionally consistent with ZT principles but depends heavily on Internet reliability and latency characteristics that vary by geography and use case. The SD-WAN complication is a specific, well-identified technical tension.

## Claim 4 (Ch7 — NAC): 802.1x-based NAC is fundamentally incompatible with Zero Trust's universal scope — it is local-only, coarse-grained (VLAN assignment), provides no encryption, has static posture, and is hardware-dependent.

**Author's claim:** The authors deliver their strongest rejection of NAC: "802.1x-based NAC functions are not suitable to use as the core part of any Zero Trust environment." Five fatal limitations are enumerated: (1) local-only scope — supplicant and authenticator must be on same broadcast domain, useless for remote users or cloud; (2) coarse-grained access — VLAN assignment with dozens/hundreds of services visible, "not compatible with the principle-of-least-privilege tenet of Zero Trust"; (3) no encryption or remote access; (4) static posture — once assigned to VLAN, no further involvement beyond periodic reauthentication; (5) hardware-dependent — requires ubiquitously deployed enterprise-owned network hardware.

**Evidence presented:** NAC's legitimate residual roles: guest network access (managed or unmanaged Wi-Fi), device discovery (a byproduct of how NAC works — data can feed ZT policy model as in Google BeyondCorp), and device posture checks (though ZT platforms are better at dynamic policy enforcement based on these attributes). The authors provide a comparison table (Table 7-2): NAC can only serve on-premises users with coarse-grained VLAN access; ZT provides granular, identity-specific access for both on-premises and remote users equally.

**Confidence:** HIGH — The five limitations are architectural rather than implementation-specific, meaning they apply to any 802.1x-based NAC regardless of vendor. The residual roles are clearly scoped. Google BeyondCorp's use of 802.1x alongside an access proxy validates the "complementary component, not core" verdict.

## Claim 5 (Ch8 — IDPS): IDPS capabilities remain essential but the *how* changes — network-based IDPS is challenged by encrypted ZT tunnels, host-based IDPS gains relative advantage, and IDPS will increasingly be "baked in" to the ZT platform.

**Author's claim:** The authors' central technical argument: Zero Trust typically uses mTLS with short-lived certificates between PEPs. A standard network IDPS between PEPs cannot decrypt this traffic — even if it has application-level certificates, it lacks the ZT tunnel certificates. TLS 1.3 makes this worse by encrypting additional handshake portions. Their verdict: IDPS capabilities are "more likely going to be 'baked in' to an enterprise's Zero Trust platform, as opposed to being a standalone tool."

**Evidence presented:** Three solution paths: (1) make the NIDPS "Zero Trust-aware" — part of the ZT system with access to decryption keys; (2) deploy NIDPS within the implicit trust zone behind the PEP; (3) shift toward host-based IDPS operating below the encryption layer. Deployment across ZT models (Figure 8-1): resource-based requires ZT-aware NIDPS between PEPs; enclave-based allows standard NIDPS within the implicit trust zone; microsegmentation makes HIDPS the primary option. The vision: IDPS → PDP integration where IDPS provides threat detection events, PDP adjusts risk scores and triggers broader actions (step-up auth, device quarantine), and ZT context informs IDPS scrutiny level to reduce false positives.

**Confidence:** HIGH — The encryption problem is a well-defined technical constraint (mTLS between PEPs blinds intermediate inspection). The three solution paths are architecturally sound and map to specific ZT deployment models.

## Claim 6 (Ch9 — VPNs): VPNs must be replaced — not augmented, not integrated, but retired. This is the authors' strongest and most unequivocal verdict, grounded in five architectural flaws that Zero Trust inherently solves.

**Author's claim:** "VPNs provide an outdated and frankly insecure approach to remote access, and must be retired or replaced as organizations move to Zero Trust." The authors argue: "Your enterprise shouldn't contain a remote access solution (enterprise VPN). It should just be an access solution, which is deployed so that it enforces access control for both remote and on-premises users, based on a unified platform and policy model."

**Evidence presented:** Five fatal VPN flaws: (1) static identity model — access identical regardless of device, location, or risk context; (2) static resource model — access granted to fixed subnets/IPs, cannot dynamically resolve targets in DevOps environments, leading to "too-broad network access, in order to keep users productive"; (3) single entry point — forces perimeter-based model, one ingress, all resources connected via internal LAN/WAN, technically impossible in distributed cloud; (4) exposed attack surface — open ports on Internet, "an inviting target for attackers worldwide," citing "many, many recent and widely publicized VPN vulnerabilities"; (5) remote-access silo — cannot enforce for on-premises users, creating duplicated expenses and inconsistent policies. The ZT replacement is contrasted point-by-point: dynamic contextual access, distributed PEPs, cloaked entry points (SPA), unified access control for all users.

**Confidence:** HIGH — The strongest claim in the book, supported by five specific architectural flaws that are inherent to VPN design rather than implementation-specific. This is one of the most convergent claims across the ZT literature — every major source (NIST, CISA, NSA, Gilman & Barth, BeyondCorp) advocates VPN replacement or retirement.

## Claim 7 (Ch10 — NGFW): NGFWs are neither sufficient as a ZT platform nor irrelevant to one — they are a component whose role depends on architecture, but NGFW-based single-entry-point architectures can impose constraints that limit the ZT journey.

**Author's claim:** The verdict: NGFWs are "neither sufficient as a Zero Trust platform nor irrelevant to one — they are a component whose role depends on architecture." The authors give credit: NGFW providers were "pioneers in enabling and enforcing some Zero Trust principles for on-premises enterprise networks." But NGFWs are not platforms that provide security for "all users for all resources regardless of location."

**Evidence presented:** The encryption problem (Figure 10-1): three deployment scenarios — (A) core firewall only, operates on network headers, works unchanged; (B) logical PEP with re-encryption, high processing load and latency; (C) logical PEP with expanded implicit trust zone — a ZT anti-pattern. Critical warning: policy misalignment risk when NGFW (as logical PEP) and second PEP enforce different policies from different vendors. Network architecture constraint (Figure 10-2): some NGFW-based ZT platforms impose single-entry-point architecture — remote users backhaul through one PEP, distributed resources require WAN, perpetuates hard-perimeter/soft-interior model. Preferred alternative: distributed entry points — users connect directly to authorized PEPs, no backhaul, reduced latency and WAN costs.

**Confidence:** HIGH — The evaluation is balanced, crediting NGFW innovation while identifying specific architectural constraints. The single-entry-point vs. distributed entry-point distinction is an architecturally significant choice that maps to NIST 800-207 deployment scenarios.

## Claim 8 (Ch12 — PAM): PAM provides valuable functions (secrets management, session recording) that persist under ZT, but password vaulting is premised on the non-ZT model of a too-open network — and PAM is identity-aware rather than identity-centric.

**Author's claim:** The authors make a striking argument: "The entire premise of password vaulting is based on the non-Zero Trust approach of a too-open network, where every user has ongoing network access to every server, and therefore a vault with server password obfuscation and rotation is required. This premise is no longer true with Zero Trust!" They don't recommend decommissioning existing PAM vaults but advise against deploying new ones for ZT-protected environments.

**Evidence presented:** Three core PAM functions: (1) password vaulting — secure storage and lifecycle management of privileged credentials, evolved from "checking out" passwords to automated ephemeral credential rotation; (2) secrets management — expanded beyond passwords to certificates, API keys, SSH keys, connection strings; (3) Privileged Session Management — intercepts/proxies admin access (RDP, SSH) for monitoring/recording/constraining, can enforce RBAC at the command level. Three ZT+PAM integration patterns: (1) PAM behind a PEP — simplest, most immediately valuable; (2) PDP consumes PAM policies — PAM informs ZT enforcement decisions; (3) PAM consumes PDP context — PAM uses ZT-provided identity/device attributes for better access decisions. The growing adoption of serverless/immutable infrastructure is also reducing relevance of traditional PSM and vaulting.

**Confidence:** HIGH — The PAM evaluation is nuanced, distinguishing between functions that persist (secrets management, session recording) and those premised on outdated network models (password vaulting). The three integration patterns provide actionable architecture guidance.

---

## Synthesis: The Spectrum from Replacement to Persistence

These six chapters reveal a consistent evaluative framework. Garbis & Chapman judge each technology against the same ZT criteria — identity-centrism, dynamic policy, universal scope, encrypted transport, least privilege, and unified control plane — and the answers distribute across a clear spectrum:

| Technology | Verdict | Role Under ZT | Key Limitation |
|---|---|---|---|
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
