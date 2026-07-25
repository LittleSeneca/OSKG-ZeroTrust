---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-network
  - topic/zt-architecture
  - topic/zt-segmentation
  - topic/zt-policy
claim_id: "gc-net-access.7"
statement: "NGFWs are neither sufficient as a ZT platform nor irrelevant to one — they are a component whose role depends on architecture, but NGFW-based single-entry-point architectures can impose constraints that limit the ZT journey."
confidence: "high"
confidence_rationale: "HIGH — The evaluation is balanced, crediting NGFW innovation while identifying specific architectural constraints. The single-entry-point vs"
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Network and Access Technologies]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-net-access.7: NGFWs are neither sufficient as a ZT platform nor irrelevant to one — they are a component whose role depends on architecture, but NGFW-based single-entry-point architectures can impose constraints that limit the ZT journey.

**Source:** [[Garbis and Chapman — Network and Access Technologies]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

The verdict: NGFWs are "neither sufficient as a Zero Trust platform nor irrelevant to one — they are a component whose role depends on architecture." The authors give credit: NGFW providers were "pioneers in enabling and enforcing some Zero Trust principles for on-premises enterprise networks." But NGFWs are not platforms that provide security for "all users for all resources regardless of location."

## Evidence

The encryption problem (Figure 10-1): three deployment scenarios — (A) core firewall only, operates on network headers, works unchanged; (B) logical PEP with re-encryption, high processing load and latency; (C) logical PEP with expanded implicit trust zone — a ZT anti-pattern. Critical warning: policy misalignment risk when NGFW (as logical PEP) and second PEP enforce different policies from different vendors. Network architecture constraint (Figure 10-2): some NGFW-based ZT platforms impose single-entry-point architecture — remote users backhaul through one PEP, distributed resources require WAN, perpetuates hard-perimeter/soft-interior model. Preferred alternative: distributed entry points — users connect directly to authorized PEPs, no backhaul, reduced latency and WAN costs.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The evaluation is balanced, crediting NGFW innovation while identifying specific architectural constraints. The single-entry-point vs. distributed entry-point distinction is an architecturally significant choice that maps to NIST 800-207 deployment scenarios.

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
