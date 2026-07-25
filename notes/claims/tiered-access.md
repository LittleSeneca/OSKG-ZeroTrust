---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/beyondcorp
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-network
  - topic/zt-governance
claim_id: "beyondcorp.3"
statement: "Tiered access — organizing trust levels into tiers of increasing sensitivity with each resource requiring a minimum trust tier — was the critical architectural innovation between Papers 1 and 2, enabling minimally interrupted users by limiting devices to the minimum tier needed."
confidence: "high"
confidence_rationale: "HIGH — The tiered access model is a well-documented architectural evolution supported by specific operational examples. The comparison table showing"
claim_type: "implementation"
source_note: "[[BeyondCorp — Research Papers]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondcorp.3: Tiered access — organizing trust levels into tiers of increasing sensitivity with each resource requiring a minimum trust tier — was the critical architectural innovation between Papers 1 and 2, enabling minimally interrupted users by limiting devices to the minimum tier needed.

**Source:** [[BeyondCorp — Research Papers]] — Google, *BeyondCorp Research Papers*, 2014-2020

## The Claim

The architecture matured from Paper 1's binary trust model (managed vs. unmanaged) to tiered access: trust levels organized into tiers of increasing sensitivity, each resource associated with a minimum trust tier, device trust tier assignment must be ≥ resource's minimum. Higher tiers require more frequent user-presence tests and shorter-lived credentials. "Limiting a device to the minimum tier needed → minimally interrupted users."

## Evidence

Example: centrally managed laptop missing noncritical OS patches → downgraded to intermediate tier → access to business apps but not sensitive ones. Missing critical security patch or AV reports infection → only remediation services. Known lost/stolen → denied all access. The evolved architecture components (Paper 1 → Paper 2): Trust Model — Binary → Tiered Access; Device Identity — Single certificate → Certificate as persistent GUID with collision detection via auxiliary identifiers; Inventory — Meta-inventory database → Device Inventory Service continuously updated pipeline ingesting 3M deltas/day from 15+ sources, 80+ TB retained; Access Control — Per-request authorization → Centralized Access Control Engine referencing access policy, Trust Inferer output, resource requested, and real-time credentials; Network — Unprivileged VLAN → Dynamic VLAN assignment via RADIUS + 802.1x where Trust Inferer annotates VLAN eligibility per device.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The tiered access model is a well-documented architectural evolution supported by specific operational examples. The comparison table showing Paper 1 → Paper 2 evolution is extracted directly from the papers.

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
