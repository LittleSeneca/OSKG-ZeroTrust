---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-migration
  - topic/zt-implementation
  - topic/zt-governance
claim_id: "nist207-ch7.9"
statement: "Candidate solution selection must evaluate client footprint, traffic patterns, logging/analysis capabilities, protocol support, and subject behavior changes — with a recommended pilot approach that serves as a proving ground before full transition."
confidence: "high"
confidence_rationale: "HIGH. The evaluation factors are concrete and operational — they reflect genuine deployment tradeoffs."
claim_type: "migration"
source_note: "[[NIST 800-207 — Ch7 — Migration]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch7.9: Candidate solution selection must evaluate client footprint, traffic patterns, logging/analysis capabilities, protocol support, and subject behavior changes — with a recommended pilot approach that serves as a proving ground before full transition.

**Source:** [[NIST 800-207 — Ch7 — Migration]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

Enterprise architects compose a list of candidate solutions, evaluating them against five factors. (§7.3.5)

## Evidence

| Factor | Question |
|--------|----------|
| **Client footprint** | Does the solution require components installed on the client asset? This may limit BYOD or cross-agency collaboration. |
| **Traffic pattern** | Does the solution work where resources exist on enterprise premises (east-west traffic), or does it assume cloud-resident resources (north-south traffic)? |
| **Logging and analysis** | Does the solution provide a means to log interactions for analysis that feeds back into the Policy Engine? |
| **Protocol support** | Does the solution support a broad range of protocols (web, SSH, etc.) and transports (IPv4, IPv6), or is it narrowly focused? |
| **Subject behavior** | Does the solution require changes to how enterprise subjects perform their workflow? |

- **Recommended approach:** Model the existing business process as a **pilot program** rather than just a replacement. The pilot serves as a "proving ground" for ZTA before transitioning subjects away from legacy process infrastructure.

**Cross-reference:**

This solution-selection phase corresponds to the architecture decisions that Gilman & Barth's [[Zero Trust Networks]] addresses through detailed protocol-level analysis. Green-Ortiz et al.'s [[Zero Trust Architecture]] provides vendor-neutral evaluation criteria and decision matrices. The [[DoD ZT Reference Architecture v2.0]] specifies approved deployment patterns for federal environments.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The evaluation factors are concrete and operational — they reflect genuine deployment tradeoffs.

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
  - [[policy-formulation-step4-migration]]

## Assessment

_Not addressed separately in the source note._
