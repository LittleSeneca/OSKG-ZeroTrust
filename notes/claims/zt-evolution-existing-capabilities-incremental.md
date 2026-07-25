---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-migration
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-network
claim_id: "dod-ra-ov.3"
statement: "ZT is an evolution of existing capabilities, not a greenfield deployment"
confidence: "high"
confidence_rationale: "HIGH. The incremental approach is consistent with the DoD ZT Strategy (also July 2022) and the CISA maturity model. No one advocates greenfield ZT"
claim_type: "migration"
source_note: "[[DoD ZT Reference Architecture — Overview and Strategy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-ov.3: ZT is an evolution of existing capabilities, not a greenfield deployment

**Source:** [[DoD ZT Reference Architecture — Overview and Strategy]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

"By reconfiguring, reprioritizing, and augmenting existing DoD capabilities, the DoD will be able to evolve towards a next-generation security architecture." The strategy is explicitly incremental — "ZT supports an incremental migration approach to cybersecurity with an end state of an interoperable, fully functioned, optimized cybersecurity architecture."

## Evidence

The document identifies existing DoD capabilities that serve as ZT baselines: JRSS (Joint Regional Security Stack), PKI/CAC for ICAM, Comply-to-Connect for device posture, SDN/SDE for network virtualization. The transition architecture (Ch 8) maps a maturity model with baseline → transition → target phases. This is not "rip and replace" — it's "reconfigure what you have."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The incremental approach is consistent with the DoD ZT Strategy (also July 2022) and the CISA maturity model. No one advocates greenfield ZT for organizations of this scale.

## Stakes

If ZT requires greenfield, it's unfundable (the DoD can't replace 4,000+ systems). If ZT is incremental, every dollar spent on existing capabilities (JRSS, ICAM, C2C) is a step toward the target. The framing matters for budget justification.

## Disagreement

**Who disagrees:**

Purists argue that incremental ZT is an oxymoron — if you still have implicit trust zones, you don't have ZT. The DoD implicitly acknowledges this by describing a "journey" (a word used throughout the ZT Strategy) rather than a destination.

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

The incremental framing is pragmatically necessary but analytically dangerous. The risk is that organizations claim "ZT progress" while preserving the implicit trust zones that ZT is supposed to eliminate. The CISA maturity model mitigates this by requiring specific capability demonstrations at each level. The DoD ZT RA's maturity model (Ch 8) serves the same function.
