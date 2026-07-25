---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-network
  - topic/zt-implementation
claim_id: "nist207-ch3.8"
statement: "Ten network requirements support ZTA"
confidence: "high"
confidence_rationale: "HIGH — These requirements are concrete and testable. Requirement 8 (remote access without VPN backhaul) is particularly significant: it formalizes"
claim_type: "architectural"
source_note: "[[NIST 800-207 — Ch3 — Logical Components]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch3.8: Ten network requirements support ZTA

**Source:** [[NIST 800-207 — Ch3 — Logical Components]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

ZTA-capable networks must satisfy ten requirements: (1) basic network connectivity for enterprise assets, (2) ability to distinguish enterprise-owned/managed assets by credentials (not spoofable attributes like MAC addresses), (3) observation of all network traffic with metadata extraction for policy updates, (4) enterprise resources not reachable without accessing a PEP, (5) logically separate data and control planes, (6) enterprise assets can reach PEP components, (7) PEP is the only component accessing the PA in business flows, (8) remote assets can access enterprise resources without VPN backhaul, (9) scalable ZT infrastructure for process load changes, (10) policy-based restrictions on which PEPs certain assets can reach.

## Evidence

**Assessment of critical requirements:**

| # | Requirement | Operational Significance | Implementation Difficulty |
|---|---|---|---|
| 4 | Resources unreachable without PEP | Defines the architectural "cloaking" of resources | HIGH — requires rearchitecting network access |
| 5 | Separate control/data planes | Foundational to ZTA | MEDIUM — well-understood from SDN |
| 8 | Remote access without VPN backhaul | Key operational benefit of ZT | LOW-MEDIUM — SDP/ZTNA products deliver this |
| 9 | Scalable infrastructure | Prevents the PE/PA/PEP from becoming bottleneck | HIGH — often underestimated in initial deployments |
| 10 | Policy-based PEP restriction | Enables geolocation/device-type access controls | MEDIUM — depends on PE policy granularity |

**Cross-reference to CISA:**

CISA's Network pillar maps Requirements 4, 5, and 8 to specific maturity progression steps. CISA's Optimal level for the Network pillar assumes all ten requirements are met.

**Cross-reference to DoD:**

DoD ZT RA v2 operationalizes Requirement 8 through the "Universal Control Plane" concept, where remote users connect to enterprise resources through cloud-hosted PEPs without traversing the enterprise perimeter. DoD's Capability 2.3 (Remote Access) explicitly requires VPN replacement with ZTNA/SDP.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — These requirements are concrete and testable. Requirement 8 (remote access without VPN backhaul) is particularly significant: it formalizes one of ZT's most important operational benefits over traditional perimeter models.

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
