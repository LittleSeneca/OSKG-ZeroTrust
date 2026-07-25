---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-network
  - topic/zt-architecture
  - topic/zt-implementation
  - topic/zt-definition
claim_id: "nist207-ch2.5"
statement: "The network assumptions invert traditional perimeter thinking"
confidence: "high"
confidence_rationale: "HIGH. These assumptions accurately describe the modern enterprise: remote workers, cloud services, BYOD, contractor access. They're not theoretical — "
claim_type: "architectural"
source_note: "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---

# nist207-ch2.5: The network assumptions invert traditional perimeter thinking

**Source:** [[NIST 800-207 — Ch2 — Zero Trust Basics]] — Scott Rose, Oliver Borchert, Stu Mitchell, Sean Connelly, *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

Six assumptions in Section 2.2 redefine the relationship between networks and security: (1) the private network is not an implicit trust zone, (2) devices may not be enterprise-owned, (3) no resource is inherently trusted, (4) resources exist outside enterprise infrastructure, (5) remote subjects cannot trust their local network, (6) assets maintain consistent security posture across environments.

## Evidence

These assumptions are derived directly from the seven tenets. They're operational consequences: if Tenet 2 says "communication is secured regardless of location," the network assumption is "the enterprise network is not a trust zone."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These assumptions accurately describe the modern enterprise: remote workers, cloud services, BYOD, contractor access. They're not theoretical — 

## Stakes

These assumptions make perimeter-based security indefensible. If the network is hostile, the firewall is a speed bump, not a security boundary. This is the architectural death certificate for VPN-based security.

## Disagreement

**Who disagrees:**

Organizations with air-gapped networks (classified systems, OT/ICS environments) can maintain that their network IS a trust zone because physical access controls eliminate the threat model ZT assumes. NIST acknowledges this implicitly by limiting the document's scope to "civilian unclassified systems."

**Alternative reading:**

_None identified._

## Edges

**Depends on:**
<!-- Claims this one requires to be true -->

**Supports:**
- [[zt-phone-home-fatal-flaw]]
- [[zt-perimeter-historical-accident]]

**Contradicts:**
<!-- Claims that cannot be true if this one is -->

**Challenged by:**
<!-- Evidence or arguments that weaken this claim -->

**Operationalizes:**
<!-- Standards/implementations that put this claim into practice -->

**Extends:**
- [[zt-five-fundamental-assertions]]

## Assessment

The network assumptions are the operational bridge between the abstract tenets and concrete deployment. Ch 4 (deployment scenarios) operationalizes these assumptions for specific use cases. Ch 7 (migration) shows how to transition from a perimeter-trusting network to a ZT-assuming one.

## Zero Trust Taxonomy

### Topic tags
`topic/zt-network` `topic/zt-architecture`

### Evidence tags
`evidence/primary-standard`
