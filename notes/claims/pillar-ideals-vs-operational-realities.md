---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-implementation
  - topic/zt-governance
  - topic/zt-cloud
  - topic/zt-network
claim_id: "cisa-ztmm-dnad.25"
statement: "Key tensions exist between pillar ideals and operational realities — Device pillar vs. BYOD constraints, network vs. application-level controls (defense-in-depth tradeoff), encryption vs. visibility (monitoring tradeoff), and immutable workloads vs. legacy systems (modernization gap) — and CISA acknowledges these tensions without fully resolving them."
confidence: "medium"
confidence_rationale: "MEDIUM. These tensions are visible in the source document but are this note's analytical framing — CISA acknowledges the tensions implicitly through"
claim_type: "implementation"
source_note: "[[CISA ZTMM — Device Network App Data Pillars]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-dnad.25: Key tensions exist between pillar ideals and operational realities — Device pillar vs. BYOD constraints, network vs. application-level controls (defense-in-depth tradeoff), encryption vs. visibility (monitoring tradeoff), and immutable workloads vs. legacy systems (modernization gap) — and CISA acknowledges these tensions without fully resolving them.

**Source:** [[CISA ZTMM — Device Network App Data Pillars]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

This is a synthesis observation by this note's author identifying tensions across pillars.

## Evidence

- **Device vs. BYOD:** CISA acknowledges that BYOD policies reduce visibility and control options, creating a tension between the Device pillar's ideal state and practical workforce realities.
- **Network vs. Application-level controls:** Optimal ZTA pushes security controls *closer to applications and data*, reducing reliance on network-layer protections — but network segmentation remains critical for defense-in-depth.
- **Encryption vs. Visibility:** Encrypting all traffic (Network pillar Optimal) can conflict with traffic inspection needs for threat detection. Agencies must balance cryptographic protections with monitoring requirements.
- **Immutable workloads vs. legacy systems:** The Application pillar's Optimal state (immutable workloads, automated CI/CD) assumes modern cloud-native architectures, which many federal legacy systems cannot support.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. These tensions are visible in the source document but are this note's analytical framing — CISA acknowledges the tensions implicitly through stage descriptions rather than naming them explicitly.

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
  - "[[legacy-implicit-trust-primary-obstacle]]"

## Assessment

_Not addressed separately in the source note._
