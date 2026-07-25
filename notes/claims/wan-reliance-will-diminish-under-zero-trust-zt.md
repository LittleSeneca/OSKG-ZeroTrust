---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-network
  - topic/zt-implementation
  - topic/zt-identity
  - topic/zt-access-mgmt
claim_id: "gc-net-access.3"
statement: "WAN reliance will diminish under Zero Trust — ZT encrypted overlays combined with ubiquitous, inexpensive Internet connectivity can often replace dedicated WAN links, creating a cost-saving opportunity."
confidence: "medium"
confidence_rationale: "MEDIUM — The WAN reduction claim is directionally consistent with ZT principles but depends heavily on Internet reliability and latency"
claim_type: "implementation"
source_note: "[[Garbis and Chapman — Network and Access Technologies]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-net-access.3: WAN reliance will diminish under Zero Trust — ZT encrypted overlays combined with ubiquitous, inexpensive Internet connectivity can often replace dedicated WAN links, creating a cost-saving opportunity.

**Source:** [[Garbis and Chapman — Network and Access Technologies]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"Zero Trust systems don't care about the underlying network — they presume it's insecure and encrypt all traffic." Combined with ubiquitous, inexpensive, and reliable Internet connectivity, the authors argue that WANs can often be "reduced or eliminated, replaced by simple Internet connectivity." This is "a cost-saving conversation that network, IT, and security teams should have."

## Evidence

SD-WAN complication: SD-WANs rely on network traffic metadata (port, protocol) for QoS traffic shaping — ZT encrypted overlay tunnels are opaque to these intermediaries, so SD-WAN routing decisions may be impaired. Coordination between ZT and networking teams is required. WAFs retain a role even in ZT environments: "If 10% of the user population uses an application, ZT eliminates the ability of the remaining 90% to even attempt to attack it. The 10% may still host malicious software — WAFs protect against this."

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM — The WAN reduction claim is directionally consistent with ZT principles but depends heavily on Internet reliability and latency characteristics that vary by geography and use case. The SD-WAN complication is a specific, well-identified technical tension.

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
- [[vpns-must-be-replaced-not-augmented-not-integrated|ZT encrypted overlays replacing dedicated WAN links supports the broader argument that VPN-based connectivity is obsolet]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
