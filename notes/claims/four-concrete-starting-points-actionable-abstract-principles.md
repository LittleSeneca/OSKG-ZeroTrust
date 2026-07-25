---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/cccs
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-architecture
claim_id: "cccs-model.5"
statement: "Four concrete starting points are more actionable than abstract principles"
confidence: "high"
confidence_rationale: "HIGH. These four steps are specific, actionable, and achievable for most organizations. They don't require architectural transformation — they're"
claim_type: "definitional"
source_note: "[[CCCS — Zero Trust Security Model]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# cccs-model.5: Four concrete starting points are more actionable than abstract principles

**Source:** [[CCCS — Zero Trust Security Model]] — Canadian Centre for Cyber Security, *Zero Trust Security Model — ITSAP.10.008*, 2023

## The Claim

"To improve your organization's cyber security posture consider implementing the following steps as a starting point in your transition towards ZT":

1. **Use dedicated devices (PAW/SAW)** — separate sensitive tasks and accounts from non-administrative computer uses (email, web browsing)
2. **Employ JIT/JEA risk-based adaptive policies** — implement least privilege access through just-in-time and just-enough access
3. **Enforce strong MFA** — aim for Level of Assurance (LoA) 3, referencing ITSP.30.031 v3
4. **Grant access based on user/device information, not logical location** — use multiple data points (identity, location, device health, resource, data classification, anomalies)

## Evidence

_No evidence separable from the claim statement in the source note._

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These four steps are specific, actionable, and achievable for most organizations. They don't require architectural transformation — they're incremental improvements that any organization can start today. PAW/SAW (step 1) is the lowest-hanging fruit; MFA (step 3) is the highest-impact.

## Stakes

If organizations treat these four steps as sufficient for ZT, they'll stop here and never implement microsegmentation, continuous monitoring, or dynamic policy — the architectural elements that make ZT transformative rather than just better authentication.

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

The four steps are well-chosen for an awareness document. They're the "ZT on-ramp" — things every organization should do regardless of whether they pursue full ZT. Steps 1 and 3 (PAW + MFA) are security hygiene; steps 2 and 4 (JIT/JEA + identity-based access) are the mindset shift. The document wisely references specific CCCS technical guidance (ITSP.30.031 for authentication, ITSG-33 for risk management) — this creates a documented trail for auditors and demonstrates that ZT is supported by existing Canadian government security standards.
