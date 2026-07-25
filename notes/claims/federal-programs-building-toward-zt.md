---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-governance
  - topic/zt-migration
  - topic/zt-identity
  - topic/zt-implementation
claim_id: "nist207-ch1.7"
statement: "Federal agencies have been building toward ZT for over a decade through foundational programs (FISMA, RMF, FICAM, TIC, CDM) that were initially limited by technology but are now maturing toward dynamic, granular access control."
confidence: "high"
confidence_rationale: "HIGH on the existence of these programs and their access-restriction goals. MEDIUM-LOW on the claim that these programs were *designed* as building"
claim_type: "governance"
source_note: "[[NIST 800-207 — Ch1 — Introduction]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch1.7: Federal agencies have been building toward ZT for over a decade through foundational programs (FISMA, RMF, FICAM, TIC, CDM) that were initially limited by technology but are now maturing toward dynamic, granular access control.

**Source:** [[NIST 800-207 — Ch1 — Introduction]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

"Federal agencies have been urged to move to security based on zero trust principles for more than a decade, building capabilities and policies such as the Federal Information Security Modernization Act (FISMA) followed by the Risk Management Framework (RMF); Federal Identity, Credential, and Access Management (FICAM); Trusted Internet Connections (TIC); and Continuous Diagnostics and Mitigation (CDM) programs. All of these programs aim to restrict data and resource access to authorized parties. When these programs were started, they were limited by the technical capabilities of information systems. Security policies were largely static and were enforced at large 'choke points' that an enterprise could control to get the largest effect for the effort. As technology matures, it is becoming possible to continually analyze and evaluate access requests in a dynamic and granular fashion to a 'need to access' basis to mitigate data exposure due to compromised accounts, attackers monitoring a network, and other threats." (lines 403–413)

## Evidence

- Enumeration of existing federal security programs (FISMA, RMF, FICAM, TIC, CDM) — their existence is publicly verifiable.
- Characterization of these programs as "building capabilities and policies" toward ZT — this is NIST's interpretive framing.
- The technology-limitation argument: earlier programs were "static" and enforced at "choke points" — this is asserted without historical evidence.
- The maturation claim: technology now enables "dynamic and granular" access decisions.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the existence of these programs and their access-restriction goals. MEDIUM-LOW on the claim that these programs were *designed* as building blocks toward ZT — this reads as retroactive reframing. FISMA (2002) and TIC (2007) predate the ZT term by years; characterizing them as ZT precursors is historically convenient but may not reflect original intent.

## Stakes

If federal agencies have already invested in ZT-enabling capabilities for a decade, then ZT adoption is not a radical break but a natural continuation — lowering the perceived cost and risk of adoption. Conversely, if these programs are fundamentally incompatible with ZT principles (e.g., TIC's choke-point model is the antithesis of distributed ZT enforcement), then the legacy investment may be an obstacle rather than a foundation.

## Disagreement

**Who disagrees:**

The TIC program in particular has been criticized as enforcing exactly the kind of perimeter-based choke-point architecture that ZT seeks to eliminate. TIC 3.0 (released after SP 800-207) attempted to reconcile this by introducing "use cases" for cloud and remote access, but the tension remains. CDM's focus on continuous monitoring aligns well with ZT; FICAM's identity federation is foundational. The claim works better for some programs than others.

**Alternative reading:**

These programs weren't "building toward ZT" — they were separate, sometimes contradictory efforts that ZT now provides a unifying framework to rationalize. NIST is engaged in the standard bureaucratic practice of presenting new policy as the logical culmination of existing efforts rather than a departure.

## Edges

**Depends on:**

**Supports:**
- [[zta-complementary-not-replacement|The decade-long federal investment in FISMA, RMF, FICAM, TIC, and CDM validates that ZTA complements rather than replace]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[einstein-ncps-evolve-perimeter-model|EINSTEIN/NCPS evolving its sensor model refines the broader claim that federal programs were limited by technology but a]]
- [[tic-3-converging-with-zta|TIC 3.0's convergence with ZTA refines the broader claim that federal programs were maturing from static perimeter enfor]]
- [[cdm-visibility-prerequisite-zta|CDM being the visibility prerequisite for ZTA refines the broader claim that foundational federal programs were building]]

## Assessment

This is the most rhetorically interesting claim in the chapter because it reveals NIST's institutional strategy: make ZT adoption feel like continuation rather than disruption. The characterization is partially true (identity programs like FICAM are genuinely ZT-enabling) and partially revisionist (TIC's perimeter model was the problem ZT solves). The "technology maturation" argument is the strongest element — it's objectively true that dynamic, attribute-based access control (ABAC) is more feasible now than when these programs launched. The weakest element is the implication that these programs were conceived with ZT in mind.
