---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-threats
  - topic/zt-definition
  - topic/zt-network
  - topic/zt-implementation
claim_id: "dod-ra-ov.2"
statement: "The DoD threat model is fundamentally different from civilian ZT"
confidence: "high"
confidence_rationale: "HIGH. The threat model difference is visible in every section: \"Assume a Hostile Environment\" and \"Presume Breach\" are the DoD's first two tenets"
claim_type: "definitional"
source_note: "[[DoD ZT Reference Architecture — Overview and Strategy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-ov.2: The DoD threat model is fundamentally different from civilian ZT

**Source:** [[DoD ZT Reference Architecture — Overview and Strategy]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

"State-funded hackers are well trained, well-resourced, and persistent. The use of new tactics, techniques, and procedures combined with more invasive malware can enable motivated malicious personas to move with previously unseen speed and accuracy."

## Evidence

The threat discussion in §1.4.1 is specific and adversarial — not generic "cyber threats" but named adversaries with known capabilities. The problem statement (§1.5) emphasizes *insider threats* and *lateral movement* as primary concerns, reflecting the DoD's experience with APT-level adversaries. Compare NIST 800-207 Ch 1, which discusses threats in terms of "network complexity" and "cloud adoption" — civilian concerns.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The threat model difference is visible in every section: "Assume a Hostile Environment" and "Presume Breach" are the DoD's first two tenets (§2.2) — neither appears in NIST's seven tenets.

## Stakes

If the threat model is APT-level adversaries with persistent access, ZT must assume breach *operationally*, not just architecturally. This means continuous monitoring isn't optional — it's the primary control. For civilian agencies facing compliance risk more than APT risk, monitoring can be less urgent.

## Disagreement

**Who disagrees:**

NSA's "Embracing a Zero Trust Security Model" (2021) uses the same threat-centric framing — unsurprising since NSA co-authored the ZT RA. CISA's maturity model is threat-agnostic; it measures capability regardless of threat model.

**Alternative reading:**

The threat emphasis could be read as institutional bias — DISA and NSA are defense/intelligence agencies that think in adversary-centric terms. NIST's "minimize uncertainty" framing may be equally valid for organizations that face different threat profiles.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The threat model difference is the single most important distinction between DoD and civilian ZT. Every subsequent design decision — from micro-segmentation requirements to continuous authentication cadence — flows from the assumption that the adversary is already inside the network. This is not paranoia; it's the operational reality of defending the DoDIN against APT actors.
