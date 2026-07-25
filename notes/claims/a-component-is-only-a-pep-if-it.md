---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-architecture
  - topic/zt-identity
  - topic/zt-definition
  - topic/zt-policy
claim_id: "gc-ch1-3.11"
statement: "A component is only a PEP if it enforces identity-centric, dynamic policies via an automated control channel — traditional firewalls alone don't qualify."
confidence: "high"
confidence_rationale: 'VERY HIGH. This is the most important architectural claim in Ch3. It defines the boundary between "existing security infrastructure" and "ZT security'
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Ch1-3 — Introduction and Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-ch1-3.11: A component is only a PEP if it enforces identity-centric, dynamic policies via an automated control channel — traditional firewalls alone don't qualify.

**Source:** [[Garbis and Chapman — Ch1-3 — Introduction and Architecture]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"Our fundamental premise is that a Zero Trust system must be able to enforce identity and context-sensitive dynamic policies... every PEP must be able to receive ongoing updates from the PDP, and automatically adjust the policies it's enforcing in near-real time and without human intervention."

## Evidence

A thought experiment: a 5-year-old basic firewall with static IP-based rules is NOT a PEP because it fails three tests: (1) can't enforce identity-centric and context-sensitive policy, (2) can't automatically respond to PDP-driven policy changes, (3) lacks a control channel for PDP communication. BUT — the same firewall with a policy-driven automation layer on top *could* be considered a PEP, as long as the automation software is tied into the PDP.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This is the most important architectural claim in Ch3. It defines the boundary between "existing security infrastructure" and "ZT security infrastructure." It also creates a migration path: you don't need to rip out firewalls, you need to automate them.

## Stakes

Without this criterion, every firewall is a PEP and ZT is indistinguishable from existing security. With it, ZT requires either new infrastructure or an automation overlay. This is the architectural hard line.

## Disagreement

**Who disagrees:**

Vendors selling "ZT-ready" firewalls might claim their products already meet this bar. The test is whether the firewall can enforce policies based on user identity (not IP address) and whether those policies can change automatically in response to context shifts (not just scheduled rule updates).

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[the-nist-pdppep-model-is-the-correct-foundation|The refined PEP definition elaborates the PDP/PEP model by specifying that a traditional firewall alone does not satisfy]]
- [[there-are-three-distinct-types-of-peps-and|The definition of what qualifies as a PEP—identity-centric, dynamic, automated control channel—provides the criteria for]]

## Assessment

This claim is the book's sharpest analytical knife. It draws a clear, testable line between traditional security and ZT. The automation overlay insight is practically valuable — it means you can ZT-enable existing infrastructure rather than replace it. The "automated ≠ automatic" distinction (manual approval steps are fine in workflows; day-to-day changes must be automated) prevents overreach.
