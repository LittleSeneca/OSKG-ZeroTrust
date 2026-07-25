---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-architecture
  - topic/zt-implementation
  - topic/zt-definition
  - topic/zt-governance
claim_id: "dod-ra-ov.6"
statement: "DoD's seven RA principles are the architectural bridge between tenets and implementation"
confidence: "high"
confidence_rationale: "HIGH. The principles provide specific, auditable guidance that the tenets alone don't. \"Assume a Hostile Environment\" is a mindset; \"No implicit or"
claim_type: "architectural"
source_note: "[[DoD ZT Reference Architecture — Overview and Strategy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-ov.6: DoD's seven RA principles are the architectural bridge between tenets and implementation

**Source:** [[DoD ZT Reference Architecture — Overview and Strategy]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

Seven Reference Architecture Principles (OV-6a) guide "the creation of the RA and other future documents":

1. **No implicit or explicit trusted zone in networks.** Goes beyond NIST (which says "no *implicit* trust" based on location) to also reject *explicit* trust zones. Every trust relationship must be continuously verified.

2. **Identity-based authentication and authorization strictly enforced for all connections.** Covers user-to-resource and user-to-infrastructure access. This operationalizes tenet 3 ("Never Trust, Always Verify").

3. **Machine-to-machine authentication and authorization strictly enforced.** This is a DoD-specific addition. NIST 800-207's tenets don't explicitly address M2M communication. In DoD environments, server-to-server and application-to-database flows are as critical as user-to-server flows.

4. **Risk profiles from near-real-time monitoring used in authorization.** Operationalizes tenet 4 ("Scrutinize Explicitly") and tenet 5 ("Apply Unified Analytics"). Risk is dynamic, not static — access decisions change as risk profiles change.

5. **All sensitive data encrypted in transit and at rest.** NIST's tenet 2 ("all communication is secured") is broader; DoD's principle is more specific and actionable.

6. **All events continuously monitored, collected, stored, and analyzed.** Operationalizes tenet 5 ("Apply Unified Analytics") and the Visibility & Analytics pillar. Compliance with security policies is demonstrated through telemetry, not assertions.

7. **Policy management and distribution is centralized.** This is the most architecturally significant principle. Decentralized policy management creates gaps and seams (Goal 1). Centralized policy enables consistent enforcement (Goal 3).

## Evidence

These seven principles are distinct from both the five tenets and the seven pillars. The tenets are *operational philosophy*; the pillars are *functional domains*; the principles are *architectural constraints*. This three-layer structure (tenets → pillars → principles) is more sophisticated than NIST's single-layer tenet model.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The principles provide specific, auditable guidance that the tenets alone don't. "Assume a Hostile Environment" is a mindset; "No implicit or explicit trusted zone in networks" is a design rule.

## Stakes

Without principles, tenets are too abstract to guide implementation. With principles, every architectural decision can be tested: "Does this design create an implicit or explicit trust zone? Does it enforce identity-based authentication? Does it encrypt sensitive data?" This is how architecture becomes auditable.

## Disagreement

**Who disagrees:**

NIST 800-207 doesn't have a separate principles layer — the seven tenets serve both as philosophy and as architectural guidance. The DoD's three-layer model is more complex but provides clearer separation of concerns. CISA's maturity model effectively adds a fourth layer (maturity levels) on top.

**Alternative reading:**

The seven principles could be seen as redundant with the five tenets and seven pillars. But the repetition is intentional — each layer serves a different audience. Tenets are for leadership (why we're doing this). Pillars are for program managers (where we're investing). Principles are for architects (how we design). This is good communication design.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[the-nist-pdppep-model-is-the-correct-foundation|The DoD RA principles as architectural bridge add a layer above the PDP/PEP model, connecting high-level tenets to PDP/P]]

## Assessment

M2M authentication (Principle 3) is the most important DoD-specific contribution. NIST 800-207 barely addresses service-to-service communication. In DoD environments, a compromised application server can move laterally through databases and APIs just as easily as a compromised user can. M2M ZT is the next frontier, and the DoD is ahead of civilian guidance on this point.
