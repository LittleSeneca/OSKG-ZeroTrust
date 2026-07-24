---
tags:
  - source/standards
  - nist
  - zt-definition
  - zt-tenets
  - zt-principles
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
confidence: very-high
source:
  title: "NIST SP 800-207 — Zero Trust Architecture"
  authors: "Scott Rose, Oliver Borchert, Stu Mitchell, Sean Connelly"
  year: 2020
  publisher: "National Institute of Standards and Technology"
  local_file: "sources/standards/_txt/NIST_SP_800-207_Zero_Trust_Architecture.txt"
related:
  - "[[NIST 800-207 Index]]"
  - "[[Concepts Index]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[CISA Zero Trust Maturity Model]]"
  - "[[NSA Embracing Zero Trust]]"
---

# NIST SP 800-207 — Ch2: Zero Trust Basics

The chapter that canonically defines Zero Trust for the U.S. federal government. Contains the operative definition, the seven tenets, and the foundational assumptions about networks. This is the most-cited chapter in Zero Trust literature.

## Claim 1: Zero Trust is defined by its positive tenets, not by what it excludes

**NIST's claim:** "Many definitions and discussions of ZT stress the concept of removing wide-area perimeter defenses... However, most of these definitions continue to define themselves in relation to perimeters in some way... The following is an attempt to define ZT and ZTA in terms of basic tenets that should be involved rather than what is excluded."

**Evidence presented:** The seven tenets are technology-agnostic and stated positively — what ZTA DOES, not what it eliminates. The authors explicitly note that perimeter-based defenses (like micro-segmentation) are still part of ZTA, just not the organizing principle.

**Confidence:** VERY HIGH. This is the canonical government definition, adopted by CISA, DoD, NSA, and referenced by every subsequent standard.

**What's at stake:** If ZT is defined by what it excludes (firewalls, VPNs, perimeter), vendors can claim "we're ZT because we don't use firewalls." If defined by positive tenets, the burden shifts to implementation evidence. The entire regulatory framework depends on this distinction.

**Who disagrees:** Chase Cunningham's ZTX framework (2018) defines ZT more expansively across seven pillars. Google BeyondCorp doesn't use the term "tenets" at all — it defines ZT through implementation. Kindervag's original formulation emphasized "no more chewy centers" — eliminating the trusted interior. NIST's positive-tenet framing is less dramatic but more enforceable.

**Alternative reading:** The positive-tenet approach could be seen as political compromise — making ZTA compatible with existing perimeter investments to increase adoption. A stricter reading would demand elimination of all implicit trust zones, including those created by micro-segmentation.

**My assessment:** The positive-tenet framing is the right call for a government standard. "Thou shalt not" definitions invite loopholes. "Thou shalt" definitions are auditable. CISA's maturity model operationalizes this perfectly: each tenet maps to capabilities at each maturity level.

---

## Claim 2: The operative definition establishes ZT as uncertainty minimization, not absolute security

**NIST's claim:** "Zero trust (ZT) provides a collection of concepts and ideas designed to minimize uncertainty in enforcing accurate, least privilege per-request access decisions in information systems and services in the face of a network viewed as compromised."

**Evidence presented:** The definition is carefully worded: "minimize uncertainty" (not eliminate), "least privilege per-request" (granularity), "network viewed as compromised" (assume breach). ZTA is defined as the *plan* — the architecture document — not the deployed system. The zero trust *enterprise* is the deployed result.

**Confidence:** VERY HIGH. This definition has held for 5+ years without revision. It survives because it's modest — it doesn't promise perfect security, just better risk management.

**What's at stake:** If the goal is "eliminate all uncertainty" ZTA is impossible (and unfundable). If the goal is "minimize uncertainty," ZTA is a continuous improvement program. This framing makes ZTA compatible with NIST's Risk Management Framework (see Ch 6).

**Who disagrees:** Vendor marketing routinely overpromises ("achieve Zero Trust"). NSA's guidance (Embracing a Zero Trust Security Model, 2021) takes a stronger "assume breach" position, emphasizing threat response over uncertainty minimization. The difference is emphasis, not contradiction.

**Alternative reading:** "Minimize uncertainty" is a weasel phrase — it lets organizations claim progress without measurable outcomes. The CISA maturity model fixes this by defining specific capability levels.

**My assessment:** This definition is the single most important sentence in Zero Trust literature. Everything else — CISA's pillars, DoD's reference architecture, NSA's threat model — builds on this foundation. If this definition changes, the entire regulatory stack changes.

---

## Claim 3: The seven tenets are aspirational, not mandatory

**NIST's claim:** "These tenets are the ideal goal, though it must be acknowledged that not all tenets may be fully implemented in their purest form for a given strategy."

**Evidence presented:** The authors explicitly hedge before listing the tenets. This is unusual for a NIST standard — most SP 800-series documents state requirements, not aspirations. The hedging signals that ZTA is a journey (a word used repeatedly in Ch 7) rather than a destination.

**Confidence:** HIGH. The hedging reflects political reality — federal agencies can't rip out their networks overnight. The DoD ZT Strategy (2022) also uses "target" and "advanced" levels rather than requirements.

**What's at stake:** If the tenets are requirements, every federal system must comply by EO 14028 deadlines, which is practically impossible. If aspirational, they provide direction without creating an unfunded mandate. The CISA maturity model resolves this tension by defining maturity levels that normalize partial implementation.

**Who disagrees:** NSA's guidance treats the tenets as operational requirements for National Security Systems — not aspirational. The difference reflects the threat model: NSS can't afford "aspirational" security.

**Alternative reading:** The hedging could be read as NIST acknowledging that ZTA is theoretically sound but practically incomplete — the technology and standards don't exist yet to fully implement all tenets (see Appendix B on gaps).

**My assessment:** The honesty of the hedging is what makes NIST 800-207 credible. Compare to vendor white papers that claim their product "achieves Zero Trust." NIST admits the limitations. That admission is itself evidence of rigor.

---

## The Seven Tenets

### Tenet 1: All data sources and computing services are considered resources
Everything from SaaS platforms to IoT actuators to personally-owned devices counts. This tenet expands the scope of what must be protected beyond traditional "servers and data."

### Tenet 2: All communication is secured regardless of network location
The death of the trusted LAN. Network location grants zero implicit trust. All traffic must be encrypted and authenticated, whether on the corporate network or public Wi-Fi.

### Tenet 3: Access to individual enterprise resources is granted on a per-session basis
Authentication to one resource does not grant access to another. This is per-session least privilege — the opposite of VPN-based access where connecting to the network grants broad access.

### Tenet 4: Access is determined by dynamic policy including observable state
Policy decisions incorporate client identity, device state, behavioral attributes, and environmental factors. This is the "context-aware" dimension of ZT. Static role-based access is insufficient.

### Tenet 5: The enterprise monitors and measures integrity and security posture of all assets
Continuous diagnostics and mitigation (CDM). No asset is inherently trusted. Subverted devices are denied or restricted. This creates a feedback loop: monitoring → posture assessment → policy enforcement.

### Tenet 6: All authentication and authorization are dynamic and strictly enforced before access
Constant re-evaluation. MFA. Continuous monitoring during sessions. This is the "never trust, always verify" operationalization.

### Tenet 7: The enterprise collects as much information as possible about the current state of assets and uses it to improve security posture
Data-driven security improvement. Telemetry from assets, network traffic, and access requests feeds policy refinement. This is the learning system dimension.

---

## Claim 4: The PDP/PEP model is the abstract architecture underlying all ZTA deployments

**NIST's claim:** Access is granted through a Policy Decision Point (PDP) and Policy Enforcement Point (PEP). All subjects must pass through this gateway, and the implicit trust zone must be as small as possible.

**Evidence presented:** The airport security analogy — all passengers pass through the checkpoint (PDP/PEP), and the boarding area is the implicit trust zone. The PDP/PEP cannot apply additional policies beyond its location in the traffic flow. Moving PDP/PEPs closer to resources shrinks the implicit trust zone.

**Confidence:** VERY HIGH. The PDP/PEP model appears in every ZTA implementation: Google's Access Proxy, ZTNA products, SDP controllers/gateways. It is the architectural invariant across all deployment models (see Ch 3).

**What's at stake:** If PDP/PEP is the only model, ZTA requires an inline enforcement point for every resource — a scalability challenge. Alternative models (e.g., distributed policy enforcement via service mesh) exist but NIST doesn't explore them here.

**Who disagrees:** Gilman & Barth (Zero Trust Networks) describe this as the "control plane / data plane" split rather than PDP/PEP. The concepts are equivalent but the terminology differs. Google BeyondCorp uses "Access Proxy" rather than PDP/PEP. Sounil Yu's Cyber Defense Matrix situates ZT enforcement differently depending on the asset class.

**My assessment:** The PDP/PEP model is the most important architectural concept in NIST 800-207. Everything in Ch 3 (logical components) elaborates this model. Understanding PDP/PEP is the prerequisite for understanding ZTA deployment.

---

## Claim 5: The network assumptions invert traditional perimeter thinking

**NIST's claim:** Six assumptions in Section 2.2 redefine the relationship between networks and security: (1) the private network is not an implicit trust zone, (2) devices may not be enterprise-owned, (3) no resource is inherently trusted, (4) resources exist outside enterprise infrastructure, (5) remote subjects cannot trust their local network, (6) assets maintain consistent security posture across environments.

**Evidence presented:** These assumptions are derived directly from the seven tenets. They're operational consequences: if Tenet 2 says "communication is secured regardless of location," the network assumption is "the enterprise network is not a trust zone."

**Confidence:** HIGH. These assumptions accurately describe the modern enterprise: remote workers, cloud services, BYOD, contractor access. They're not theoretical — they describe the world federal agencies already live in.

**What's at stake:** These assumptions make perimeter-based security indefensible. If the network is hostile, the firewall is a speed bump, not a security boundary. This is the architectural death certificate for VPN-based security.

**Who disagrees:** Organizations with air-gapped networks (classified systems, OT/ICS environments) can maintain that their network IS a trust zone because physical access controls eliminate the threat model ZT assumes. NIST acknowledges this implicitly by limiting the document's scope to "civilian unclassified systems."

**My assessment:** The network assumptions are the operational bridge between the abstract tenets and concrete deployment. Ch 4 (deployment scenarios) operationalizes these assumptions for specific use cases. Ch 7 (migration) shows how to transition from a perimeter-trusting network to a ZT-assuming one.

---

## Chapter 2 Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| ZT defined by positive tenets | VERY HIGH | Vendors redefining "tenets" to match their product |
| Operative definition as uncertainty minimization | VERY HIGH | Political pressure to define ZT as "eliminate all risk" |
| Tenets are aspirational | HIGH | NSA/DoD treating tenets as requirements for NSS |
| PDP/PEP model is the universal architecture | VERY HIGH | Emergence of distributed enforcement models (service mesh) |
| Network assumptions invert perimeter thinking | HIGH | Air-gapped classified systems as counter-example |

**Strongest section:** The operative definition and seven tenets (Sections 2.0 and 2.1). These 40 lines are the most-cited text in all of Zero Trust literature.

**Weakest section:** Section 2.2 (network assumptions). These are important but derivative — they restate the tenets as network-specific consequences rather than adding new insights. Useful for network architects, skippable for policy makers.

**Missing:** The chapter doesn't address *how* to operationalize the tenets. That's deferred to Ch 3 (logical components) and Ch 7 (migration). The tenets are principles; the architecture is the implementation. This separation is deliberate but means Ch 2 can't stand alone — it requires Ch 3 for the reader to understand what "PDP/PEP" actually means.
