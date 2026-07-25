---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-threats
  - topic/zt-network
  - topic/zt-implementation
  - topic/zt-architecture
claim_id: "nist207-ch5.2"
statement: "DoS and network disruption against the PA/PEP are a unique ZTA pathology — even if access is authorized, the PA may be unable to configure the communication path, making resources unreachable despite valid authorization."
confidence: "high"
confidence_rationale: "HIGH. The PA-as-gatekeeper architecture creates a structural availability dependency that perimeter-based networks don't have in the same way"
claim_type: "threat"
source_note: "[[NIST 800-207 — Ch5 — Threats]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch5.2: DoS and network disruption against the PA/PEP are a unique ZTA pathology — even if access is authorized, the PA may be unable to configure the communication path, making resources unreachable despite valid authorization.

**Source:** [[NIST 800-207 — Ch5 — Threats]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

The PA is the gatekeeper for all resource access. If attackers disrupt the PEP, PE, or PA, enterprise operations grind to a halt. (§5.2)

## Evidence

- DoS/DDoS or route hijacking against the PEP or PE/PA
- Botnet attacks (Mirai-scale) against key infrastructure
- Interception/blocking of traffic to a PEP or PA for a subset of users (branch office, remote employee) — not unique to ZTA; also possible with legacy VPNs
- Accidental cloud provider outages (IaaS or SaaS) taking PE/PA offline
- **Pathology unique to ZTA:** Even if access is granted, the PA may be unable to configure the communication path due to DDoS or unexpected heavy usage — the resource becomes unreachable despite authorization.

- Host PE/PA in a properly secured cloud environment or replicate across locations per cyber resiliency guidance (NIST SP 800-160v2)

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The PA-as-gatekeeper architecture creates a structural availability dependency that perimeter-based networks don't have in the same way.

**Cross-reference — NSA Embracing ZT**

NSA's document is fundamentally threat-model-driven: it opens by "acknowledging that threats exist both inside and outside traditional network boundaries." While NSA does not treat DoS as a standalone category, its "assume breach" principle subsumes availability concerns — a mature ZT implementation is designed to "perform rapid damage assessment, control, and recovery operations" when disruption occurs.

**Cross-reference — Gilman & Barth: Distributed Denial of Service**

Gilman & Barth are blunt: "DDoS is still a problem in the zero trust world." Key points:
- Volumetric DDoS affects any system that can receive packets, even ZTA ones
- "Darkening" internet-facing endpoints via pre-authentication helps obscure addresses but doesn't fundamentally mitigate DDoS
- **ZT-specific advantage:** Policy information about expected traffic patterns can be used to calculate coarse enforcement rules for upstream filtering devices that remain **stateless** — obviating expensive hardware and state replication
- Cloud-native deployments should leverage online DDoS-prevention services

## Stakes

_Not addressed separately in the source note._

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
