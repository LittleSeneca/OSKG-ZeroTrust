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
claims_status: "extracted"
claims_extracted_date: 2026-07-24
claims_count: 5
claims_files:
  - "[[zt-positive-tenets]]"
  - "[[zt-uncertainty-minimization]]"
  - "[[zt-tenets-aspirational]]"
  - "[[zt-pdp-pep-model]]"
  - "[[zt-network-assumptions]]"
---

# NIST SP 800-207 — Ch2: Zero Trust Basics

The chapter that canonically defines Zero Trust for the U.S. federal government. Contains the operative definition, the seven tenets, and the foundational assumptions about networks. This is the most-cited chapter in Zero Trust literature.

**Claim 1 —** Zero Trust is defined by its positive tenets, not by what it excludes → [[zt-positive-tenets]]

**Claim 2 —** The operative definition establishes ZT as uncertainty minimization, not absolute security → [[zt-uncertainty-minimization]]

**Claim 3 —** The seven tenets are aspirational, not mandatory → [[zt-tenets-aspirational]]

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

**Claim 4 —** The PDP/PEP model is the abstract architecture underlying all ZTA deployments → [[zt-pdp-pep-model]]

**Claim 5 —** The network assumptions invert traditional perimeter thinking → [[zt-network-assumptions]]

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