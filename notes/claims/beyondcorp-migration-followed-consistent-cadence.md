---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/beyondcorp
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-network
  - topic/zt-migration
claim_id: "beyondcorp.11"
statement: "The BeyondCorp migration followed a consistent cadence — Analyze → Log → Warn → Enforce → Default — where the Log phase (simulation, audit mode, monitor mode) was never skipped across any major change, and this pattern is the single most important operational lesson for ZT migration."
confidence: "high"
confidence_rationale: "HIGH — The Analyze → Log → Warn → Enforce → Default cadence is directly observable across all four papers and all major BeyondCorp changes. This is"
claim_type: "implementation"
source_note: "[[BeyondCorp — Research Papers]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondcorp.11: The BeyondCorp migration followed a consistent cadence — Analyze → Log → Warn → Enforce → Default — where the Log phase (simulation, audit mode, monitor mode) was never skipped across any major change, and this pattern is the single most important operational lesson for ZT migration.

**Source:** [[BeyondCorp — Research Papers]] — Google, *BeyondCorp Research Papers*, 2014-2020

## The Claim

Every major change (VLAN migration, trust tier enforcement, fleet health controls) went through the sequence: Analyze → Log → Warn → Enforce → Default. The Log phase was the critical data-gathering step that built confidence for enforcement.

## Evidence

The cadence appears across all four papers: Paper 1's Unprivileged Network Simulator (logging mode → enforcement mode → VLAN migration triggers); Paper 2's deployment strategy (Phase 1: apply access policy that mirrored IP-based perimeter model to allow safe deployment of incomplete components; Phase 2: gradual policy replacement as meta-inventory matured); Paper 4's 802.1x foundation (auditing mode comparing new vs. legacy assignments → enable when differences sufficiently few), MNP Simulator (logging → enforcement), and phased rollout (small pilot → progressive expansion → eventual expansion); Paper 6's control rollout (monitor mode first → iterate → graduate to enforcement) and audit-only mode for BAB. Additional cross-cutting themes: Partitioning for independence — decouple layers so they progress independently (network layer reached stability without waiting for application remediation); data quality as a security dependency — "accurate inventory = access" drove unprecedented data quality improvements with secondary security benefits (better patch compliance); user experience as a security requirement — productivity maintained through simulator preventing broken workflows, self-service tools, grace periods, VPN elimination as productivity win paying for implementation.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The Analyze → Log → Warn → Enforce → Default cadence is directly observable across all four papers and all major BeyondCorp changes. This is the single most convergent operational pattern across the entire ZT literature — NIST 800-207 Ch7, CISA ZTMM, Green-Ortiz Ch8, and Garbis & Chapman all converge on monitor-mode-first migration. BeyondCorp is the canonical validation of this pattern at the largest documented scale.

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
- [[zta-implementation-continuous-improvement-journey-one|BeyondCorp's documented Analyze→Log→Warn→Enforce→Default cadence serves as a canonical example of continuous improvement]]
- [[strategic-pivot-prove-user-successful-before-migrating|The Analyze→Log→Warn→Enforce→Default cadence provided the operational framework that made the strategic opt-out pivot sa]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
