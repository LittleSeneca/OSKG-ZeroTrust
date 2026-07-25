---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-definition
  - topic/zt-trust
  - topic/zt-governance
  - topic/zt-architecture
claim_id: "nist207-ch1.2"
statement: "Zero Trust assumes breach and eliminates implicit trust — every access request must be continuously authenticated, authorized, and risk-evaluated."
confidence: "high"
confidence_rationale: "HIGH as a *definition* (NIST is the authoritative definer for federal purposes), MEDIUM as an *empirical claim* about effectiveness. The definition"
claim_type: "definitional"
source_note: "[[NIST 800-207 — Ch1 — Introduction]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch1.2: Zero Trust assumes breach and eliminates implicit trust — every access request must be continuously authenticated, authorized, and risk-evaluated.

**Source:** [[NIST 800-207 — Ch1 — Introduction]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

"Zero trust security models assume that an attacker is present in the environment and that an enterprise-owned environment is no different—or no more trustworthy—than any nonenterprise-owned environment. In this new paradigm, an enterprise must assume no implicit trust and continually analyze and evaluate the risks to its assets and business functions and then enact protections to mitigate these risks." (lines 349–357)

## Evidence

- Definitional — NIST is establishing the concept, not proving it with evidence.
- The definition is operationalized: "minimizing access to resources... to only those subjects and assets identified as needing access as well as continually authenticating and authorizing the identity and security posture of each access request." (lines 354–357)
- References FIPS 199 for classification/sensitivity levels to which ZT applies (line 366).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH as a *definition* (NIST is the authoritative definer for federal purposes), MEDIUM as an *empirical claim* about effectiveness. The definition is NIST's to make — there's no factual dispute about what NIST *says* ZT means. Whether ZT *works* as defined is a separate question requiring empirical evidence from Sections 4–5.

## Stakes

This is the core definitional claim of the entire document. If "assume breach" is too extreme a posture, ZT becomes infeasibly expensive. If "no implicit trust" is impossible to operationalize (every access decision requires context that can't always be evaluated), ZTA designs may be unrealizable. Conversely, if this definition is too weak, ZTA becomes indistinguishable from existing defense-in-depth.

## Disagreement

**Who disagrees:**

Practitioners who argue that "assume breach" is a useful thought experiment but not an operational stance — you can't effectively run an enterprise while acting as if every component is already compromised. The "trust but verify" school retains a role for baseline trust. See Garbis & Chapman's critique in "Zero Trust Security: An Enterprise Guide" — they argue for pragmatic trust levels rather than absolute zero. Finney ("Project Zero Trust") frames ZT as a *strategy* that tolerates progressive implementation, not an absolute state.

**Alternative reading:**

"Assume breach" is aspirational framing, not literal operational guidance. NIST itself walks this back by describing hybrid ZT/perimeter operations (line 371–373). The practical reading is "don't assume safety behind the perimeter" rather than "assume everything is already compromised."

## Edges

**Depends on:**

**Supports:**
- [[zta-prevent-breach-limit-lateral-movement|The operational mechanism (assume breach, continuous auth) is what enables the design goal (prevent breaches, limit late]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The definition is crisp and has proven durable — subsequent NIST publications (800-207A, 2024) retain essentially the same formulation. The tension between the absolute language ("no implicit trust") and the pragmatic implementation guidance ("hybrid mode," "incremental") is a feature, not a bug: NIST sets the aspirational target while acknowledging real-world constraints. The definition's strength is that it closes the door on "trusted internal network" thinking.
