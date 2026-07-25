---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cisa-ztmm
  - topic/zt-definition
  - topic/zt-threats
  - topic/zt-network
  - topic/zt-implementation
claim_id: "cisa-ztmm-ov.2"
statement: "Recent nation-state cyber incidents made legacy perimeter-based security indefensible"
confidence: "high"
confidence_rationale: "VERY HIGH. These are publicly documented incidents. The SolarWinds attack compromised at least nine federal agencies including Treasury, State, and"
claim_type: "definitional"
source_note: "[[CISA ZTMM — Overview and Framework]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cisa-ztmm-ov.2: Recent nation-state cyber incidents made legacy perimeter-based security indefensible

**Source:** [[CISA ZTMM — Overview and Framework]] — CISA, *Zero Trust Maturity Model v2.0*, 2023

## The Claim

"Recent cyber incidents have highlighted the broad challenges of ensuring effective cybersecurity across the federal government... 'business as usual' approaches are no longer sufficient to defend the nation from cyber threats."

## Evidence

The document cites Emergency Directive 21-01 (SolarWinds Orion compromise) and Emergency Directive 21-02 (Microsoft Exchange vulnerabilities) in footnotes — both major nation-state supply chain attacks that exploited implicit trust between systems. The SolarWinds attack (2020) specifically compromised federal agency networks through a trusted software update mechanism.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. These are publicly documented incidents. The SolarWinds attack compromised at least nine federal agencies including Treasury, State, and Commerce. The operational failure of perimeter-based defenses is not theoretical — it's demonstrated.

## Stakes

If the threat assessment is wrong (i.e., if perimeter defenses + patching were sufficient), then the entire ZTA transition is unnecessary overhead. If it's right, federal agencies are currently exposed to nation-state threat actors. The billions in ZTA investment across the federal government depend on this assessment being correct.

## Disagreement

**Who disagrees:**

No one seriously disputes the incident severity. Some security practitioners argue that better patching habits and network segmentation would have prevented SolarWinds without a full ZTA — i.e., the problem was execution, not architecture. CISA's counter-argument is that implicit trust is the root cause that made the attacks so damaging.

**Alternative reading:**

The SolarWinds reference could be seen as rhetorical — invoking a high-profile incident to justify a pre-existing policy preference. But the operational details of SolarWinds (trusted software update → lateral movement → data exfiltration) map directly to ZTA principles of per-session access and continuous verification.

## Edges

**Depends on:**

**Supports:**
- [[traditional-enterprise-security-is-structurally-broken-not-merely|Nation-state incidents (SolarWinds, Exchange) are the empirical evidence that perimeter-based security is structurally b]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The threat narrative is well-supported. SolarWinds is the canonical "assume breach" case study — the attackers were inside trusted networks for months. ZTA wouldn't have prevented the initial compromise, but it would have dramatically limited lateral movement. The incident strengthens rather than weakens the ZTA case.
