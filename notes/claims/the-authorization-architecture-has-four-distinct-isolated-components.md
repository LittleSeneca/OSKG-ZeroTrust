---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-architecture
  - topic/zt-access-mgmt
claim_id: "gb-ch4-6.1"
statement: "The authorization architecture has four distinct, isolated components"
confidence: "high"
confidence_rationale: "HIGH. This four-component decomposition has become the standard reference model. NIST 800-207 formalized the same components as PEP (enforcement), PA"
claim_type: "architectural"
source_note: "[[Gilman and Barth — Ch4-6 — Authorization Devices Users]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch4-6.1: The authorization architecture has four distinct, isolated components

**Source:** [[Gilman and Barth — Ch4-6 — Authorization Devices Users]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"The zero trust authorization architecture comprises four main components: Enforcement, Policy Engine, Trust Engine, and Data Stores. These four components are distinct in their responsibilities... these systems represent the practical crown jewels of the zero trust security model, so special care should be taken in their maintenance and security posture."

## Evidence

The authors argue from engineering principles — isolation prevents cascading compromise. The enforcement component is "in the user's data path, more exposed," so it must be process-level isolated from the policy engine. They reference Google's BeyondCorp as having "pioneered" the trust engine concept.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This four-component decomposition has become the standard reference model. NIST 800-207 formalized the same components as PEP (enforcement), PA (policy engine), and PE (with supporting data). The names differ but the functions align precisely.

## Stakes

If these four responsibilities are collapsed into a single system (which the authors explicitly warn against), a compromise of any one yields full authorization control. The isolation requirement is the structural security property that makes ZT authorization defendable.

## Disagreement

**Who disagrees:**

NIST 800-207 permits the PA and PE to be co-located or combined "for simple deployments" but maintains the same logical separation. Simplified vendor implementations (e.g., SDP controllers) often merge enforcement + policy engine for latency reasons, which the authors acknowledge but argue against without process-level isolation.

**Alternative reading:**

The four-component model could be read as describing an ideal rather than a minimum — in practice, many "zero trust" products ship only enforcement + basic policy engine, deferring trust scoring to SIEM/SOAR. The model works better as a maturity target than a compliance gate.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

This is the most architecturally significant claim in Ch4. The component isolation principle is what distinguishes ZT authorization from traditional firewall rules or RBAC. Without it, ZT degenerates to perimeter-by-policy.
