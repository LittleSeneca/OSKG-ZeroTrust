---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-architecture
  - topic/zt-network
  - topic/zt-policy
claim_id: "gc-ch1-3.9"
statement: "The NIST PDP/PEP model is the correct foundation, but needs enterprise-specific refinement and extension."
confidence: "high"
confidence_rationale: "HIGH. These extensions are all value-adding without contradicting NIST. The three-PEP-type model is particularly useful for mapping existing"
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Ch1-3 — Introduction and Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-ch1-3.9: The NIST PDP/PEP model is the correct foundation, but needs enterprise-specific refinement and extension.

**Source:** [[Garbis and Chapman — Ch1-3 — Introduction and Architecture]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"We're extending and refining that architecture to make it more relevant for enterprises, and to better align with our approach... we'll be using these architectural concepts throughout the course of this book to make Zero Trust concepts concrete and relatable to your enterprise."

## Evidence

The authors adopt NIST's PDP/PEP model but make three extensions: (1) CDM, PKI, and other systems are treated as logically part of the ZT system — "producers and consumers of data and events, meshed together," (2) they introduce three distinct PEP types (user agent, network, application), (3) they define a formal policy structure (Subject Criteria + Action + Target + Condition).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These extensions are all value-adding without contradicting NIST. The three-PEP-type model is particularly useful for mapping existing infrastructure to ZT functions.

## Stakes

If the PDP/PEP model is too abstract, enterprises can't operationalize it. The extensions make it concrete: "your NGFW can be a network PEP, your PAM can be an application PEP, your endpoint agent can be a user agent PEP." This mapping is the book's most practical architectural contribution.

## Disagreement

**Who disagrees:**

NIST purists might argue that collapsing the Policy Engine/Policy Administrator distinction into "PDP" loses important nuance. The authors acknowledge this but consider it irrelevant for enterprise purposes. Service mesh architectures distribute PDP functions in ways that don't cleanly map to a logically centralized PDP.

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

The PDP/PEP model with three PEP types is the right level of abstraction for enterprise architects. It's concrete enough to drive design decisions and vendor evaluation without being so detailed that it prescribes specific products. The formal policy structure (Subject/Action/Target/Condition) is a significant contribution — it gives architects a template for defining ZT policies.
