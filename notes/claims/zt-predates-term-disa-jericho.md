---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-architecture
claim_id: "nist207-ch1.5"
statement: 'The concept of zero trust predates the term — DISA "black core" and the Jericho Forum were conceptual predecessors focused on per-transaction security and de-perimeterization.'
confidence: "high"
confidence_rationale: "HIGH. The existence of DISA black core and the Jericho Forum is publicly verifiable. The Jericho Forum's papers on de-perimeterization are archived"
claim_type: "definitional"
source_note: "[[NIST 800-207 — Ch1 — Introduction]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch1.5: The concept of zero trust predates the term — DISA "black core" and the Jericho Forum were conceptual predecessors focused on per-transaction security and de-perimeterization.

**Source:** [[NIST 800-207 — Ch1 — Introduction]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

"The concept of zero trust has been present in cybersecurity since before the term 'zero trust' was coined. The Defense Information Systems Agency (DISA) and the Department of Defense published their work on a more secure enterprise strategy dubbed 'black core' [BCORE]. Black core involved moving from a perimeter-based security model to one that focused on the security of individual transactions. The work of the Jericho Forum in 2004 publicized the idea of de-perimeterization—limiting implicit trust based on network location and the limitations of relying on single, static defenses over a large network segment [JERICHO]." (lines 390–396)

## Evidence

- DISA's "black core" [BCORE] — DoD strategy for per-transaction security (date not specified in this text; DISA black core work dates to early 2000s).
- Jericho Forum (2004) — industry consortium that coined "de-perimeterization" [JERICHO].
- NIST cites these as precursors, establishing intellectual lineage for the federal audience.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The existence of DISA black core and the Jericho Forum is publicly verifiable. The Jericho Forum's papers on de-perimeterization are archived and accessible. The claim that these concepts *preceded* the ZT term is factually correct — Kindervag's first ZT paper came in 2010, while Jericho Forum was active from 2004.

## Stakes

Establishing ZT as having *military and defense roots* rather than being a vendor invention gives it institutional legitimacy for federal adoption. It's harder for agencies to dismiss ZT as a Forrester marketing term when the DoD was exploring the same concepts independently. The intellectual lineage also protects ZT from being dismissed as a fad — it's presented as the culmination of 15+ years of thinking.

## Disagreement

**Who disagrees:**

No serious scholarly disagreement with the chronology. Some might argue that DISA black core and Jericho Forum were qualitatively different from ZT — they addressed network architecture, not the full identity/data/device scope that ZT encompasses. Kindervag added the explicit "zero trust" framing that transformed a network architecture concept into a comprehensive security paradigm.

**Alternative reading:**

The lineage is real but NIST may be retroactively claiming ancestors to build legitimacy. DISA black core was a specific DoD program, not a general cybersecurity movement. Jericho Forum failed to achieve widespread adoption — de-perimeterization remained a niche concept until Kindervag rebranded it. The true conceptual breakthrough was Kindervag's synthesis, not the isolated predecessor efforts.

## Edges

**Depends on:**

**Supports:**
- [[nist-document-structure-framework|Including the intellectual lineage of ZT predecessors is part of the comprehensive framework that nist207-ch1.8 claims t]]
- [[kindervag-coined-zero-trust|The DISA black core and Jericho Forum predecessors establish the intellectual lineage and conceptual need that Kindervag]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

NIST's history is accurate but compressed. The Jericho Forum's importance is probably overstated here for rhetorical purposes — de-perimeterization had limited industry impact compared to what ZT achieved. DISA black core is genuinely underappreciated and deserves the acknowledgment NIST gives it. The most significant omission: NIST doesn't mention Google's BeyondCorp (2014), which was arguably the most influential ZT predecessor, because that history is in §1.2's scope limitation (federal focus). The cross-reference to [[History Index]] is essential for the full timeline.
