---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-migration
  - topic/zt-governance
  - topic/zt-maturity
claim_id: "nist207-ch7.7"
statement: "Business process selection for ZTA migration should start with low-risk processes and cloud-based/remote-worker workflows, using the NIST RMF to evaluate tradeoffs in performance, user experience, and workflow fragility."
confidence: "high"
confidence_rationale: 'HIGH. The "start low-risk, scale up" pattern is standard migration guidance and well-supported.'
claim_type: "migration"
source_note: "[[NIST 800-207 — Ch7 — Migration]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch7.7: Business process selection for ZTA migration should start with low-risk processes and cloud-based/remote-worker workflows, using the NIST RMF to evaluate tradeoffs in performance, user experience, and workflow fragility.

**Source:** [[NIST 800-207 — Ch7 — Migration]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

The enterprise must **identify and rank business processes, data flows, and their relation to agency missions**. (§7.3.3)

## Evidence

- **Start with a low-risk business process** for the first ZTA transition — disruptions will likely not negatively impact the entire organization.
- Once enough experience is gained, **more critical business processes** become candidates.
- **Cloud-based resources** and **remote worker workflows** are often good candidates — rather than projecting the enterprise perimeter into the cloud or using VPNs, clients can request cloud services directly through PEPs.
- **Tradeoffs to consider:** performance degradation, user experience changes, possible increased workflow fragility.
- Risk evaluation should use the NIST Risk Management Framework ([[NIST SP 800-37]]).

**Cross-reference:**

This is where the organizational narrative from Finney's [[Project Zero Trust]] is most relevant — selecting the first pilot process is as much a political and organizational decision as a technical one. Green-Ortiz et al.'s [[Zero Trust Architecture]] provides a maturity model that maps candidate processes to organizational readiness levels.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The "start low-risk, scale up" pattern is standard migration guidance and well-supported.

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
