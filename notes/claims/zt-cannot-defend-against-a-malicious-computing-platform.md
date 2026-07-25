---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-threats
  - topic/zt-device
  - topic/zt-identity
  - topic/zt-architecture
claim_id: "gb-ch10.4"
statement: "ZT cannot defend against a malicious computing platform — only against simpler platform attacks"
confidence: "high"
confidence_rationale: "HIGH. This is the honest answer — no security model survives a compromised foundation. It echoes Ken Thompson's \"Reflections on Trusting Trust\""
claim_type: "threat"
source_note: "[[Gilman and Barth — Ch10 — The Adversarial View]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch10.4: ZT cannot defend against a malicious computing platform — only against simpler platform attacks

**Source:** [[Gilman and Barth — Ch10 — The Adversarial View]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"Totally defending against untrustworthy computing platforms is practically impossible." If hardware purposefully generates weak random numbers, even detecting the attack may be impossible if the attacker hides the capability most of the time. However, ZT can guard against "simpler attacks against the platform" through encryption of persistent data and swapped-out memory pages.

## Evidence

The distinction between the "computing platform" (cloud hardware, hypervisor) and the "device" is carefully maintained — attacks against each differ because of privilege levels. The authors recommend encrypting data at rest and swapped memory as a mitigation against malicious peers on the platform, acknowledging it removes "some small amount of trust in the platform's operators."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is the honest answer — no security model survives a compromised foundation. It echoes Ken Thompson's "Reflections on Trusting Trust" (1984): you can't trust code you didn't totally create yourself.

## Stakes

This is the argument for hardware roots of trust (TPM, secure enclaves) and supply chain security. If you can't trust the platform, the entire ZT architecture — which depends on device identity and attestation — is built on sand. This is why NSA's device pillar emphasizes firmware integrity and supply chain provenance so heavily.

## Disagreement

**Who disagrees:**

No one disputes the impossibility claim. The disagreement is about what "simpler attacks" means. Modern confidential computing (AMD SEV, Intel SGX) pushes the trusted boundary further down the stack but doesn't eliminate the problem. The authors' 2017 framing predates widespread confidential computing availability.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[zts-threat-model-is-the-internet-threat-model|zts-threat-model-is-the-internet-threat-model]]

## Assessment

Short section, correct conclusion. The more interesting question — which the authors don't explore — is whether ZT increases or decreases the attack surface of the platform. By requiring device attestation and identity, ZT gives the platform more responsibilities, making platform compromise more consequential. This is the double-edged sword again.
