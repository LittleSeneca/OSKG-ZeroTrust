---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-network
  - topic/zt-definition
claim_id: "nist207-ch1.1"
statement: "Perimeter-based network security has been rendered obsolete by enterprise complexity."
confidence: "high"
confidence_rationale: "HIGH. The factual premise — enterprise infrastructure has become multi-perimeter — is publicly verifiable. Nearly every enterprise operates hybrid"
claim_type: "definitional"
source_note: "[[NIST 800-207 — Ch1 — Introduction]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch1.1: Perimeter-based network security has been rendered obsolete by enterprise complexity.

**Source:** [[NIST 800-207 — Ch1 — Introduction]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

"A typical enterprise's infrastructure has grown increasingly complex... This complexity has outstripped legacy methods of perimeter-based network security as there is no single, easily identified perimeter for the enterprise. Perimeter-based network security has also been shown to be insufficient since once attackers breach the perimeter, further lateral movement is unhindered." (lines 337–342)

## Evidence

- Multiple internal networks, remote offices, mobile individuals, and cloud services all coexist in a single enterprise — no single boundary encloses them.
- Attackers who breach the perimeter face no further barriers to lateral movement.
- The evidence is observational/descriptive rather than empirical — NIST cites no breach statistics or studies.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The factual premise — enterprise infrastructure has become multi-perimeter — is publicly verifiable. Nearly every enterprise operates hybrid on-premises/cloud environments. The lateral-movement observation is also well-attested in breach forensics (Mandiant M-Trends, Verizon DBIR). However, NIST offers no quantitative evidence here; the confidence rests on widely accepted operational reality, not NIST's specific argumentation.

## Stakes

If this claim is false — if perimeter-based security remains adequate for some enterprise architectures — then the entire Zero Trust project is unnecessary for those enterprises. The urgency of ZT adoption depends on accepting that the perimeter model is fundamentally broken, not merely inconvenient. This claim is the *casus belli* for everything that follows in NIST 800-207.

## Disagreement

**Who disagrees:**

Perimeter-defense vendors (traditional firewall/VPN companies) have an economic interest in disputing this. The "defense in depth" school argues perimeter security remains a valid layer within a broader strategy, not an obsolete paradigm. Gartner's Secure Access Service Edge (SASE) framework preserves some perimeter concepts within a cloud-delivered model. See also [[History Index#Key Debates]] — Greenfield vs. Brownfield debate.

**Alternative reading:**

The perimeter hasn't disappeared — it has multiplied and become dynamic. Rather than "no perimeter," modern enterprise has many micro-perimeters (cloud VPCs, SaaS boundaries, endpoint perimeters). The failure is not of perimeter *concept* but of *static, single-perimeter enforcement*.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The claim is fundamentally correct as stated but imprecise. The problem isn't that perimeters are obsolete — it's that *static, implicit-trust-inside* perimeters are obsolete. NIST later acknowledges this nuance by describing hybrid ZT/perimeter-based operations (line 371–373). The stronger version of this claim (perimeter security is broken) holds up; the weaker version (perimeters don't exist) overstates the case.
