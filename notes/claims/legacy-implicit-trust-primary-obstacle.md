---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-migration
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-network
claim_id: "cisa-ztmm-ov.5"
statement: "Legacy implicit-trust systems are the primary obstacle to ZTA adoption"
confidence: "high"
confidence_rationale: "HIGH. This is consistent with every major ZTA implementation report. Google's BeyondCorp migration took years specifically because legacy"
claim_type: "implementation"
source_note: "[[CISA ZTMM — Overview and Framework]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-ov.5: Legacy implicit-trust systems are the primary obstacle to ZTA adoption

**Source:** [[CISA ZTMM — Overview and Framework]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

"Legacy systems often rely on 'implicit trust,' in which access and authorization are infrequently assessed based on fixed attributes; this conflicts with the core principle of adaptive evaluation of trust within a ZTA. Existing infrastructures built on implicit trust will require investment to change systems to better align with zero trust principles."

## Evidence

The document identifies several concrete challenges: (1) legacy systems with implicit trust, (2) stove-piped and siloed IT services and staff, (3) need for "agency-wide buy in for a common architecture and governance policies," (4) different starting points across agencies. The acknowledgment that "agencies are beginning their journeys to zero trust from different starting points" is strategically important — it normalizes partial progress.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is consistent with every major ZTA implementation report. Google's BeyondCorp migration took years specifically because legacy applications assumed network location = trust. DoD's ZT Strategy (2022) identifies legacy systems as a primary risk.

## Stakes

If legacy systems are unchangeable (common in classified environments), ZTA may be practically impossible for certain high-security systems. The ZTMM doesn't fully address this — it assumes legacy systems CAN be migrated. NSA's guidance is more explicit about the need for compensating controls where migration isn't feasible.

## Disagreement

**Who disagrees:**

The "rip and replace" school argues that legacy systems should be decommissioned, not migrated. The "incremental" school (which the ZTMM represents) argues that gradual migration is practical. Both agree legacy systems are the problem; they disagree on the solution.

**Alternative reading:**

The focus on legacy systems could be a convenient excuse — the real challenge is organizational resistance and funding, not technology. The ZTMM addresses this implicitly by requiring governance and culture change across pillars.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

Legacy implicit-trust systems are a real obstacle, but the framework's maturity model handles this well — Traditional level IS the legacy state, and Initial level is the first meaningful step. Agencies don't need to solve legacy systems to start; they need to start solving them.
