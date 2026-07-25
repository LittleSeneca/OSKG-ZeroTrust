---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-embracing-zt
  - topic/zt-threats
  - topic/zt-implementation
  - topic/zt-network
  - topic/zt-governance
claim_id: "nsa-embrace.3"
statement: "The threat examples demonstrate ZT's value, not ZT's completeness"
confidence: "high"
confidence_rationale: "MEDIUM-HIGH. The scenarios are well-constructed and plausible, but they're illustrative, not empirical. NSA doesn't provide data on how often ZT actua"
claim_type: "implementation"
source_note: "[[NSA — Embracing a Zero Trust Security Model]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---

# nsa-embrace.3: The threat examples demonstrate ZT's value, not ZT's completeness

**Source:** [[NSA — Embracing a Zero Trust Security Model]] — National Security Agency, *Embracing a Zero Trust Security Model*, 2021

## The Claim

Three scenarios — compromised credentials, insider threat/remote exploitation, and supply chain compromise — show where ZT detects and contains threats that perimeter-based security misses.

## Evidence

Each scenario walks through the attack chain in a traditional vs. ZT environment. In every case, ZT either prevents the attack (compromised credentials → device authentication fails), limits the blast radius (insider threat → microsegmentation), or provides detection that perimeter security lacks (supply chain → deny-by-default blocks C2).

## Confidence

**Rating:** HIGH
**Rationale:** MEDIUM-HIGH. The scenarios are well-constructed and plausible, but they're illustrative, not empirical. NSA doesn't provide data on how often ZT actua

## Stakes

These scenarios are the evidence base for ZT adoption in the DoD. If they're idealized, agencies may overestimate ZT's protective value. If they're realistic, they make a strong case.

## Disagreement

**Who disagrees:**

Academic research (see ZTA Enterprise Implementation paper, IJCA 2025) provides empirical evidence but at smaller scale. NIST 800-207 Ch 5 covers threats more systematically but less vividly.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**
<!-- Claims this one requires to be true -->

**Supports:**
- [[zt-phone-home-fatal-flaw]]

**Contradicts:**
<!-- Claims that cannot be true if this one is -->

**Challenged by:**
<!-- Evidence or arguments that weaken this claim -->

**Operationalizes:**
- [[zt-assume-breach]]

**Extends:**
<!-- Claims this one builds upon or elaborates -->

## Assessment

The scenarios are effective communication, not rigorous evidence. They're designed to persuade, not to prove. For claims about ZT effectiveness, the academic papers (Phase 1, Tier 4) will provide better evidence. But as a teaching tool, they're excellent — every CISO should be able to explain these three scenarios.

## Zero Trust Taxonomy

### Topic tags
`topic/zt-threats` `topic/zt-implementation`

### Evidence tags
`evidence/primary-standard`
