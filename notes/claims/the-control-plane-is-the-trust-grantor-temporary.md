---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-architecture
  - topic/zt-authentication
  - topic/zt-implementation
  - topic/zt-definition
  - topic/zt-sdn
claim_id: "gb-ch2.5"
statement: "The control plane is the trust grantor — temporary trust and leased tokens are its operational expression"
confidence: "high"
confidence_rationale: 'HIGH. This is a direct extension of the Ch1 architecture with operational specifics. The "lease" model — credentials that expire and require renewal'
claim_type: "architectural"
source_note: "[[Gilman and Barth — Ch2 — Managing Trust]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch2.5: The control plane is the trust grantor — temporary trust and leased tokens are its operational expression

**Source:** [[Gilman and Barth — Ch2 — Managing Trust]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

The control plane "is the trust grantor for the entire network. Due to its far-reaching control of the network's behavior, the control plane's trustworthiness is critical." Trust granted by the control plane "should have limited real-time value. Trust should be temporary, requiring regular check-ins between the truster and trustee to ensure that the continued trust is reasonable." The interface between control plane and data plane "should resemble the user/kernel space interface, where interactions between those two systems are heavily isolated to prevent privilege escalation."

## Evidence

The chapter specifies leased access tokens and short-lifetime certificates as the implementation mechanism for temporary trust. These credentials must be validated both within the data plane (agent-to-resource) and between the data plane and control plane (agent-to-controller). The isolation requirement is structural — the data plane cannot be used to gain privilege in the control plane, preventing lateral movement.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is a direct extension of the Ch1 architecture with operational specifics. The "lease" model — credentials that expire and require renewal — is now standard in service mesh (mTLS with short-lived certificates), Kubernetes (service account tokens with expiry), and cloud IAM (temporary security credentials via STS).

## Stakes

If credential lifetimes are too long, the system reverts to static trust and loses its ZT properties. If they're too short, the control plane becomes a bottleneck and availability suffers. The rotation frequency trade-off — "inversely proportional to the cost of rotation" — is the key operational tension. The chapter's examples of expensive-to-rotate secrets (certificates requiring external coordination, hand-configured service accounts, database passwords requiring downtime) are still painfully relevant.

## Disagreement

**Who disagrees:**

Some architectures (e.g., SPIFFE) push toward very short-lived credentials (minutes) with automated rotation, arguing that the operational cost of rotation has been solved by modern infrastructure. Others (especially in OT/IoT contexts) argue that frequent rotation is impractical and push for hardware-backed long-lived credentials with attestation instead. Both are valid in their domains.

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

The "trust is temporary" principle is the practical expression of "never trust, always verify" — verification isn't a one-time gate, it's a continuous process requiring regular re-authentication. The chapter's framing of the control plane as trust grantor also makes clear why the control plane is the highest-value target in the entire architecture. If you compromise the control plane, you don't need to attack individual resources — you can grant yourself access to everything.
