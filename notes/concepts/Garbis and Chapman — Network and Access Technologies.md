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
claims_status: extracted
claims_extracted: 2026-07-24
---
# Garbis & Chapman — Ch6–10, 12: Network and Access Technologies in Zero Trust

**Combined note.** Six chapters covering existing network security technologies — Network Infrastructure (Ch6), NAC (Ch7), IDS/IPS (Ch8), VPNs (Ch9), NGFW (Ch10), and PAM (Ch12) — each evaluated against Zero Trust principles. Combining them makes the comparative evaluation explicit: every chapter asks the same question ("does this technology advance or impede Zero Trust?") and reaches a distinct but interrelated verdict. The pattern reveals a spectrum: some technologies are outright replaced (VPNs), some are diminished and reframed (NAC, NGFW), some are repositioned as ZT data sources (IDPS, PAM), and some (core firewalls, DNS, WAFs) persist but with simplified roles.

---

**Claim 1 —** Firewalls persist under Zero Trust but their role bifurcates — rules simplify dramatically as enforcement shifts to ZT PEPs, and the access controls historically attempted with firewalls are achieved more effectively through identity-centric policy. → [[firewalls-persist-under-zero-trust-but-their-role]]

**Claim 2 —** DNS is both a critical infrastructure component and a security monitoring tool under ZT — private DNS resolution must adapt to distributed environments, and DNS monitoring for known-bad domains is "high-value and low-risk." → [[dns-is-both-a-critical-infrastructure-component-and]]

**Claim 3 —** WAN reliance will diminish under Zero Trust — ZT encrypted overlays combined with ubiquitous, inexpensive Internet connectivity can often replace dedicated WAN links, creating a cost-saving opportunity. → [[wan-reliance-will-diminish-under-zero-trust-zt]]

**Claim 4 —** 802.1x-based NAC is fundamentally incompatible with Zero Trust's universal scope — it is local-only, coarse-grained (VLAN assignment), provides no encryption, has static posture, and is hardware-dependent. → [[8021x-based-nac-is-fundamentally-incompatible-with-zero-trusts]]

**Claim 5 —** IDPS capabilities remain essential but the *how* changes — network-based IDPS is challenged by encrypted ZT tunnels, host-based IDPS gains relative advantage, and IDPS will increasingly be "baked in" to the ZT platform. → [[idps-capabilities-remain-essential-but-the-how-changes]]

**Claim 6 —** VPNs must be replaced — not augmented, not integrated, but retired. This is the authors' strongest and most unequivocal verdict, grounded in five architectural flaws that Zero Trust inherently solves. → [[vpns-must-be-replaced-not-augmented-not-integrated]]

**Claim 7 —** NGFWs are neither sufficient as a ZT platform nor irrelevant to one — they are a component whose role depends on architecture, but NGFW-based single-entry-point architectures can impose constraints that limit the ZT journey. → [[ngfws-are-neither-sufficient-as-a-zt-platform]]

**Claim 8 —** PAM provides valuable functions (secrets management, session recording) that persist under ZT, but password vaulting is premised on the non-ZT model of a too-open network — and PAM is identity-aware rather than identity-centric. → [[pam-provides-valuable-functions-secrets-management-session-recording]]

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
