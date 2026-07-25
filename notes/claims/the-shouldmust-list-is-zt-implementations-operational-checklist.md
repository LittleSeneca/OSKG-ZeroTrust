---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-implementation
  - topic/zt-governance
  - topic/zt-architecture
  - topic/zt-network
claim_id: "gb-ch9.1"
statement: "The SHOULD/MUST list is ZT implementation's operational checklist"
confidence: "high"
confidence_rationale: "HIGH. Every subsequent ZT standard preserves this same hierarchy. NIST 800-207 requires authentication and authorization of all sessions (Tenet 4)"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch9.1: The SHOULD/MUST list is ZT implementation's operational checklist

**Source:** [[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

The RFC 2119–style prioritized list defines what must exist for a system to be "considered compatible with the zero trust design" vs. what can be deprioritized under cost constraints.

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

## Evidence

These are practitioner judgments from the authors' experience at Netflix and PagerDuty, not derived from formal threat models. The RFC 2119 framing is deliberate — it echoes the IETF convention of MUST/SHOULD/MAY to signal implementation weight.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Every subsequent ZT standard preserves this same hierarchy. NIST 800-207 requires authentication and authorization of all sessions (Tenet 4), encryption of all traffic (implicit in Tenet 1/2), and continuous device posture assessment (Tenet 5). CISA ZTMM maps MUST items to Traditional→Initial maturity and SHOULD items to Advanced→Optimal.

## Stakes

If every SHOULD gets deferred indefinitely, you have a perimeter system with extra logging — not ZT. The MUST list is the minimum viable ZT footprint. Organizations that claim "ZT" without flow enumeration are doing identity-aware perimeter, not ZT.

## Disagreement

**Who disagrees:**

Forrester's ZTX framework extends the scope well beyond network — data, workloads, people, devices, networks, automation, visibility. This list is narrower, deliberately. CISA's five-pillar model adds Governance and Visibility as explicit pillars, which Gilman & Barth treat as implicit in the MUST items.

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

The MUST list is the most actionable single page in Zero Trust literature. NIST's seven tenets are more abstract; CISA's five pillars are broader. This list is what you tape to the wall during implementation planning. The private PKI requirement is the most controversial item — realistic for Google/PagerDuty scale, aspirational for smaller organizations — but the reasoning (public CA trust is trust in unknown third parties) is sound.
