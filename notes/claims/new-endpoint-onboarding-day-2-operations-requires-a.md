---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-implementation
  - topic/zt-device
claim_id: "go-ch6-8.7"
statement: 'New endpoint onboarding ("Day 2 Operations") requires a centralized receiving process — a secured, isolated network segment with lenient NAC policy, separate Internet access, and full NetFlow collection, followed by a structured onboarding checklist.'
confidence: "high"
confidence_rationale: "HIGH — The Day 2 operations gap is a well-recognized operational failure mode. The centralized receiving segment and structured checklist provide a"
claim_type: "implementation"
source_note: "[[Green-Ortiz — Ch6-8 — Implementation]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch6-8.7: New endpoint onboarding ("Day 2 Operations") requires a centralized receiving process — a secured, isolated network segment with lenient NAC policy, separate Internet access, and full NetFlow collection, followed by a structured onboarding checklist.

**Source:** [[Green-Ortiz — Ch6-8 — Implementation]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

Organizations focus on segmenting what's already on the network but neglect the process for new devices. The old model — firewall admins receive tickets requesting "allow our IP range to access these DNS names" without explanation — is incompatible with ZT.

## Evidence

The onboarding process: centralized receiving segment with secured/isolated network, lenient NAC policy, separate Internet access, full NetFlow collection. Onboarding checklist: (1) create contextual identity (active + passive profiling); (2) collect traffic patterns (local switch NetFlow, upstream firewall logs); (3) document architecture and device capabilities; (4) evaluate authentication capability (802.1X, posture, management enrollment); (5) assign to static group in NAC server → authorization result → distributed enforcement policy. For remote users, the authors endorse MDM-based provisioning (Meraki Systems Manager) for pushing VPN/client configurations with minimal user steps.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The Day 2 operations gap is a well-recognized operational failure mode. The centralized receiving segment and structured checklist provide a concrete, actionable process that addresses a gap in most ZT planning.

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
