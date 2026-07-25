---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-trust
  - topic/zt-architecture
claim_id: "gb-ch2.6"
statement: "Trust delegation via trust chains is what makes ZT scalable"
confidence: "high"
confidence_rationale: "HIGH. Trust delegation via chains anchored in human operators is a well-established concept in computer security (it's how PKI itself works — the"
claim_type: "architectural"
source_note: "[[Gilman and Barth — Ch2 — Managing Trust]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch2.6: Trust delegation via trust chains is what makes ZT scalable

**Source:** [[Gilman and Barth — Ch2 — Managing Trust]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

Trust in a ZT network "always originates with the operator" but operators don't scale — so trust must be delegated. "Trust delegation is important because it allows us to build automated systems that can grow to large scale and to operate in a secure and trusted way with minimal human intervention." The mechanism is a trust chain: the operator trusts a provisioning system, the provisioning system creates and vouches for new hosts, and those hosts can be trusted because "the provisioning system can prove that the operator has granted it the ability to do so." The operator is the trust anchor at the root of the chain.

## Evidence

The auto-scaling example makes the case concretely: when a new server provisions itself, how do you know it's yours and not an attacker's? Because the provisioning system — which the operator explicitly trusted — created it and can cryptographically attest to that fact. This pattern of delegated, provable trust chains is the mechanism that allows ZT to operate at scale without human approval for every access decision.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Trust delegation via chains anchored in human operators is a well-established concept in computer security (it's how PKI itself works — the root CA is the trust anchor). The ZT application of this pattern extends it from identity (who are you) to authorization (what are you allowed to do and create).

## Stakes

The trust chain is only as strong as its weakest link. If the provisioning system is compromised, every host it creates is compromised, and the trust chain validates the attacker's hosts as legitimate. The chapter acknowledges this implicitly through the PKI discussion — the CA must be protected at all costs — but doesn't fully explore the blast radius of a broken trust chain. This is a gap that Chapter 4 (on control plane security) partially addresses.

## Disagreement

**Who disagrees:**

Some argue that trust delegation via chains is too brittle — a single compromise anywhere in the chain cascades. Alternatives like distributed trust (threshold signatures, multi-party authorization) reduce the blast radius but add complexity. The authors' position is pragmatic: chains are simple, well-understood, and the risks can be managed through operational security of the trust anchors.

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

Trust delegation is the least developed concept in this chapter — it gets a brief introduction at the start and then the chapter moves on. But it's foundational: without delegation, ZT doesn't scale, and without chains, delegation is unverifiable. The chapter could have made a stronger connection between trust delegation and PKI (they're the same concept at different layers — PKI is trust delegation for identity; variable trust scores are trust delegation for authorization). This connection is implicit but not explicit.
