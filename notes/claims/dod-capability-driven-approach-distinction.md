---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-governance
  - topic/zt-definition
  - topic/zt-identity
  - topic/zt-implementation
claim_id: "dod-ra-cap.11"
statement: "The DoD's capability-driven approach distinguishes itself from other ZT frameworks — where NIST 800-207 provides the abstract logical model and CISA provides the maturity ladder, the DoD provides an exhaustive capability inventory, a concrete five-decision-point enforcement architecture, and 17 use cases that operationalize every major ZT concept with defined resource flows."
confidence: "medium"
confidence_rationale: "MEDIUM. The comparison is this note's analytical framing — the framework distinctions are visible in the documents but neither NIST nor CISA"
claim_type: "governance"
source_note: "[[DoD ZT Reference Architecture — Capabilities and Use Cases]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-cap.11: The DoD's capability-driven approach distinguishes itself from other ZT frameworks — where NIST 800-207 provides the abstract logical model and CISA provides the maturity ladder, the DoD provides an exhaustive capability inventory, a concrete five-decision-point enforcement architecture, and 17 use cases that operationalize every major ZT concept with defined resource flows.

**Source:** [[DoD ZT Reference Architecture — Capabilities and Use Cases]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

This is a synthesis claim by this note's author comparing the three major frameworks.

## Evidence

1. **An exhaustive capability inventory** — 7 aggregated capabilities with dozens of sub-capabilities, each mapped to specific pillars and decision points
2. **A concrete enforcement architecture** — not one PDP but a chain of five decision points, each with independent confidence evaluation
3. **17 use cases that operationalize every major ZT concept** — each with defined resource flows

**The confidence scoring feedback loop (through-line across all use cases):**

```
Identity + Device + Behavior → Confidence Score → Policy Decision → Enforcement → Logging → Analytics → Refined Score
```

**Gaps and tensions identified by this analysis:**

- The DoD taxonomy assumes significant enterprise infrastructure (FEIS, SDE, SIEM, SOAR) already in place — the "brownfield" assumption. Organizations without these face a steeper path.
- The 17 use cases are documented at OV-1/OV-2 level (operational concepts and resource flows). They stop at defining *what* must happen, not *how* to build it. Reference Designs (RDs) and Reference Implementations (RIs) are the missing next layer.
- NPE identity management is called out as critical but acknowledged as immature even in industry. The DoD flags this as an area requiring further development.
- The feedback loop's AI evolution (out-of-band → in-band) is aspirational. The architecture correctly identifies the path but does not prescribe a timeline or decision criteria for when to trust automated policy changes.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. The comparison is this note's analytical framing — the framework distinctions are visible in the documents but neither NIST nor CISA explicitly positions itself as complementary to the DoD RA.

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
