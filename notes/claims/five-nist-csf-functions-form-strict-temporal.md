---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/yu-cdm
  - topic/zt-architecture
  - topic/zt-definition
claim_id: "yu-cdm.2"
statement: "The five NIST CSF functions form a strict temporal sequence with clear semantics"
confidence: "high"
confidence_rationale: "VERY HIGH. This function taxonomy is the backbone of the NIST CSF and is adopted by CISA's ZT Maturity Model, which organizes capabilities by"
claim_type: "architectural"
source_note: "[[Yu — Cyber Defense Matrix]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# yu-cdm.2: The five NIST CSF functions form a strict temporal sequence with clear semantics

**Source:** [[Yu — Cyber Defense Matrix]] — Sounil Yu, *Cyber Defense Matrix*, 2022

## The Claim

The five functions are not interchangeable — each implies the existence of the prior function. IDENTIFY → PROTECT (left of boom); DETECT → RESPOND → RECOVER (right of boom). Actions must be classified consistently across all asset classes. If discovering DATA vulnerabilities is IDENTIFY, then discovering DEVICE vulnerabilities must also be IDENTIFY, not DETECT.

## Evidence

Yu distinguishes between structural awareness (left-of-boom: knowing what assets exist, their configurations, their weaknesses) and situational awareness (right-of-boom: analyzing events, investigating state changes, gathering evidence of exploitation). A vulnerability is a structural weakness — discovering it is IDENTIFY regardless of whether it's been exploited yet. Patching a vulnerability is always PROTECT, even if done in response to an incident. Confusing these distinctions leads to remediation being classified as both PROTECT and RESPOND depending on context.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This function taxonomy is the backbone of the NIST CSF and is adopted by CISA's ZT Maturity Model, which organizes capabilities by function within each pillar.

## Stakes

If organizations conflate IDENTIFY with DETECT (as NIST CSF itself sometimes does — ID.RA-1 and DE.CM-8 both reference vulnerability scanning), they lose the ability to measure coverage and maturity. Each cell in the matrix needs distinct metrics.

## Disagreement

**Who disagrees:**

The NIST CSF itself contains definitional ambiguities (using "identify" to describe DETECT activities). Yu's matrix imposes stricter internal consistency than NIST does, which is both a strength (clarity) and a limitation (some real-world activities legitimately span functions).

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

This function-level rigor is what makes the matrix useful as a ZT mapping tool. ZTNA (NETWORK-PROTECT), ZTAA (APPLICATION-PROTECT), and ZTDA (DEVICE-PROTECT) are all PROTECT functions — they control access to resources. They are not DETECT or RESPOND. This clarifies that ZT is primarily a PROTECT strategy, not a complete security program.
