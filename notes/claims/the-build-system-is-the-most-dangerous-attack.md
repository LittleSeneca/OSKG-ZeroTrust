---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-app
  - topic/zt-threats
claim_id: "gb-ch7-8.3"
statement: "The build system is the most dangerous attack vector — it sits between two cryptographically protected states with no protection of its own"
confidence: "high"
confidence_rationale: "HIGH. The SolarWinds attack (2020) proved this empirically — attackers compromised the build environment itself, and the signed Orion updates were"
claim_type: "threat"
source_note: "[[Gilman and Barth — Ch7-8 — Applications and Traffic]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch7-8.3: The build system is the most dangerous attack vector — it sits between two cryptographically protected states with no protection of its own

**Source:** [[Gilman and Barth — Ch7-8 — Applications and Traffic]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

Source code can be signed. Build artifacts can be signed. But the build process itself — the function applied between input and output — is generally not protected cryptographically. A compromised build system can inject malicious code during compilation, producing a signed binary that downstream systems validate as trusted while containing attacker-controlled logic.

## Evidence

The visual representation (Figure 7-3) shows the break in the chain: signed source → [unprotected build] → signed artifact. Without the right processes, subversion of this kind can be "difficult or impossible to detect." Reproducible builds are presented as the best available defense: if multiple parties can produce bit-for-bit identical binaries from the same source, build system compromise becomes detectable.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The SolarWinds attack (2020) proved this empirically — attackers compromised the build environment itself, and the signed Orion updates were trusted by customers. Reproducible builds remain aspirational for most organizations but are the gold standard (Debian, Bitcoin Core, Tor Browser all support them).

## Stakes

This is the architectural vulnerability that makes supply chain attacks so devastating. When a build system is compromised, the attack inherits all the trust of the organization's code signing infrastructure. Detection is nearly impossible at the consumer end because the artifact appears valid.

## Disagreement

**Who disagrees:**

NSA's device pillar argues that securing the build _host_ (TPM attestation, measured boot, firmware integrity) can prevent this class of attack before it reaches the reproducible build stage. Google's SLSA framework takes a complementary approach — multiple levels of build provenance requirements rather than relying solely on reproducibility.

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

The authors correctly identify this as the weakest link, but their proposed solution (reproducible builds) is difficult to adopt at scale. The ecosystem has since evolved: SLSA, in-toto, and Sigstore provide build provenance attestations that are lighter-weight than full reproducibility while still providing meaningful guarantees. The core insight — that the build process needs its own integrity protection — remains correct and under-addressed in most organizations.
