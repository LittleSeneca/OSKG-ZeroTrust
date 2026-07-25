---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nsa-embracing-zt
  - topic/zt-definition
  - topic/zt-threats
  - topic/zt-network
  - topic/zt-implementation
claim_id: "nsa-embrace.1"
statement: 'Zero Trust is defined by "assume breach," not architecture'
confidence: "high"
confidence_rationale: "HIGH. This framing is consistent across all NSA Zero Trust publications."
claim_type: "threat"
source_note: "[[NSA — Embracing a Zero Trust Security Model]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---

# nsa-embrace.1: Zero Trust is defined by "assume breach," not architecture

**Source:** [[NSA — Embracing a Zero Trust Security Model]] — National Security Agency, *Embracing a Zero Trust Security Model*, 2021

## The Claim

The Zero Trust security model assumes that a breach is inevitable or has likely already occurred, so it constantly limits access to only what is needed and looks for anomalous or malicious activity.

## Evidence

The document opens with the threat landscape — sophisticated adversaries, perimeter defense failure, insider threats — before defining what Zero Trust IS. This is a rhetorical choice: define the problem first, then present Zero Trust as the solution. NIST 800-207 does the opposite: defines the architecture, then discusses threats in Ch 5.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This framing is consistent across all NSA Zero Trust publications.

## Stakes

If "assume breach" is the core principle, ZT is fundamentally a threat-response strategy. If architecture is the core (NIST's framing), ZT is a design methodology. Both are true but the emphasis matters for implementation priorities: NSA starts with monitoring and detection; NIST starts with policy engine design.

## Disagreement

**Who disagrees:**

NIST 800-207 defines ZT as "minimizing uncertainty" — a gentler, more risk-management-oriented framing. DoD ZT Strategy splits the difference: assume breach AND architect accordingly.

**Alternative reading:**

The "assume breach" framing could be read as NSA's institutional bias — as a signals intelligence agency, they think in terms of adversaries. NIST's "minimize uncertainty" is more appropriate for civilian agencies that face compliance risk as much as adversarial risk.

## Edges

**Depends on:**
<!-- Claims this one requires to be true -->

**Supports:**
- [[zt-network-assumptions]]

**Contradicts:**
<!-- Claims that cannot be true if this one is -->

**Challenged by:**
<!-- Evidence or arguments that weaken this claim -->

**Operationalizes:**
<!-- Standards/implementations that put this claim into practice -->

**Extends:**
- [[zt-positive-tenets]]

## Assessment

Both framings are correct and complementary. NSA's threat-centric view makes ZT feel urgent and operational. NIST's architecture-centric view makes ZT implementable and auditable. The CISA maturity model synthesizes both: it measures maturity by capability (architecture) against a threat-informed baseline.

## Zero Trust Taxonomy

### Topic tags
`topic/zt-definition` `topic/zt-threats`

### Evidence tags
`evidence/primary-standard`