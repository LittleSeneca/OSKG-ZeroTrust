---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-migration
  - topic/zt-maturity
  - topic/zt-device
claim_id: "gb-ch9.5"
statement: "Client-to-server and server-to-server migrations are different problems with different starting points"
confidence: "high"
confidence_rationale: "HIGH. Both case studies validate their respective starting points and both succeeded. The field has largely standardized on client-to-server first"
claim_type: "migration"
source_note: "[[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch9.5: Client-to-server and server-to-server migrations are different problems with different starting points

**Source:** [[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

The decision of where to start "should focus on which target is the weakest link in the system's network defenses."

| Starting Point | Advantages | Challenges |
|---------------|-----------|-----------|
| **Client-to-server** (BeyondCorp) | Clients are physically mobile on uncontrolled networks — high value; user experience parity between office/remote is compelling | No existing automation on client machines; diverse device types; harder to retrofit |
| **Server-to-server** (PagerDuty) | Existing automation tools already installed; less diverse providers; servers house sensitive data | Internal actors may resist change; requires deep infrastructure knowledge |

## Evidence

**Cross-reference — NIST 800-207 Ch7:**

NIST's Step 3 recommends starting with a "low-risk business process" — cloud-based resources and remote worker workflows are flagged as good candidates. This favors the client-to-server approach for most organizations. Green-Ortiz et al.'s maturity model adds the dimension of organizational readiness: do you have the DevOps maturity for server-to-server first?

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Both case studies validate their respective starting points and both succeeded. The field has largely standardized on client-to-server first (ZTNA products), but server-to-server (service mesh, workload identity) is the harder long-term problem.

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
