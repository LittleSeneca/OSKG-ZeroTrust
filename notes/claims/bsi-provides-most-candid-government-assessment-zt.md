---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/bsi
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-identity
  - topic/zt-architecture
claim_id: "bsi-zt.6"
statement: "BSI provides the most candid government assessment of ZT's limitations"
confidence: "high"
confidence_rationale: "HIGH. This is the most honest government assessment of ZT limitations I have found in any national framework."
claim_type: "definitional"
source_note: "[[BSI — Zero Trust Position Paper]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# bsi-zt.6: BSI provides the most candid government assessment of ZT's limitations

**Source:** [[BSI — Zero Trust Position Paper]] — BSI, *Zero Trust Position Paper*, 2023

## The Claim

- **ZT does not fully prevent attacks** — it primarily reduces damage scope (*"ihre Umsetzung verhindert Angriffe nicht vollständig, sie kann aber dazu beitragen, das Schadensausmaß verschiedenartiger Angriffe deutlich zu reduzieren"*)
- **ZT's focus is confidentiality and integrity, not availability** — DoS attacks on devices, applications, or PEPs are not prevented by ZT. Making applications more broadly reachable (as ZT enables) actually *increases* the risk surface for DoS attacks
- **Central components are critical single points of failure** — identity management, PDP, certificate management, inventories, and central detection require special protection across all three CIA objectives. The centralization inherent in ZT architectures may *increase* risk in these components compared to distributed architectures
- **Insider threats cannot be fully prevented** — insiders already possess required authorizations for their role. ZT can limit damage scope and detect unusual access patterns, but cannot eliminate insider risk
- **More complex access rules make attacks harder but not impossible** — attackers must now understand and manipulate additional criteria (device state, user behavior, access timing, authentication strength), but detection mechanisms must continuously evolve to match

## Evidence

_No evidence separable from the claim statement in the source note._

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is the most honest government assessment of ZT limitations I have found in any national framework.

## Stakes

This candor is strategically important. By explicitly acknowledging ZT's limitations, the BSI prevents the over-promising that has damaged ZT credibility in some implementations. The document is effectively saying: "ZT is worth doing, but here's exactly what it won't do for you."

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

The admission that ZT centralization creates new single points of failure is particularly significant. Most ZT frameworks either ignore this or treat it as a temporary condition. The BSI's recommendation is not to avoid centralization but to apply *all three CIA protections* to centralized components — essentially, the centralized components get perimeter-level protection while the Data Plane gets ZT protection. This hybrid approach is practical but philosophically inconsistent with pure ZT — the BSI is pragmatic enough to acknowledge this tension rather than resolve it.
