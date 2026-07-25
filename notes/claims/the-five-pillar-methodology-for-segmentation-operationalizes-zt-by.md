---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-governance
  - topic/zt-network
claim_id: "go-ch6-8.3"
statement: 'The five-pillar methodology for segmentation operationalizes ZT by making contextual identity the engine of policy — but organizations must start with 5–7 broad enclaves and refine iteratively, treating segmentation as "eating an elephant — one small step at a time."'
confidence: "high"
confidence_rationale: "HIGH — The five-pillar methodology is the book's core framework. The \"start with 5-7 enclaves\" recommendation is an empirically grounded Cisco"
claim_type: "implementation"
source_note: "[[Green-Ortiz — Ch6-8 — Implementation]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch6-8.3: The five-pillar methodology for segmentation operationalizes ZT by making contextual identity the engine of policy — but organizations must start with 5–7 broad enclaves and refine iteratively, treating segmentation as "eating an elephant — one small step at a time."

**Source:** [[Green-Ortiz — Ch6-8 — Implementation]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

The chapter operationalizes segmentation through the book's five ZT pillars: (1) Understand Contextual Identity (who/what/where/when/how + vulnerability posture via RADIUS + ISE profiling); (2) Understand External Resource Consumption (PXGrid + NetFlow for identity-injected flow data); (3) Validate Vulnerabilities to External Sites (Layer 7 firewall for application discovery + IPS); (4) Understand Internal Communication (NetFlow + identity integration for internal flows); (5) Understand Communication Within the Broadcast Domain/VLAN (hardest step, requires contextual identity first). The authors warn: "Far too many organizations start with too many segments based on contextual identity, attempting to replace primarily authentication-based mechanisms, such as Active Directory, with TrustSec tags."

## Evidence

The endpoint segmentation plan (Figure 6-6) maps device types → business units → required restrictions → enforcement mechanisms. The prescribed stacking order: VLAN (dynamic assignment) → Firewall (inter-VLAN traversal + advanced features) → Downloadable ACLs (distributed to access switches) → TrustSec SGTs (intra-VLAN peer-to-peer control). For data centers where virtual switches don't support TrustSec: host-based agents (Cisco Secure Workload or Secure Endpoint) that write IP tables based on centrally managed policy.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The five-pillar methodology is the book's core framework. The "start with 5-7 enclaves" recommendation is an empirically grounded Cisco services finding that provides a concrete starting point other ZT frameworks leave abstract.

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
