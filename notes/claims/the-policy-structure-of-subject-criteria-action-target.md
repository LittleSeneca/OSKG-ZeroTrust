---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-policy
  - topic/zt-identity
claim_id: "gc-ch1-3.14"
statement: "The policy structure of Subject Criteria + Action + Target + Condition provides a universal template for ZT policy definition."
confidence: "high"
confidence_rationale: "HIGH. This structure is compatible with ABAC (NIST SP 800-162), with XACML, and with every commercial ZT policy engine. It's the formal expression of"
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Ch1-3 — Introduction and Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-ch1-3.14: The policy structure of Subject Criteria + Action + Target + Condition provides a universal template for ZT policy definition.

**Source:** [[Garbis and Chapman — Ch1-3 — Introduction and Architecture]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"We define a policy as a declarative statement specifying that a subject is permitted to perform an action on a target, if and only if certain conditions are met."

| Component | Description |
|-----------|-------------|
| **Subject Criteria** | Authenticated identities (people or NPEs) with attributes from IAM, device profile, network/geolocation |
| **Action** | The activity — must contain network or application component, may contain both |
| **Target** | The resource — statically (hostname/IP) or dynamically (IaaS tags, hypervisor labels) defined |
| **Condition** | Circumstances under which access is permitted — draws on subject, environment, and target attributes |

## Evidence

A sample policy makes it concrete: Billing department users accessing billing.internal.company.com on port 443/HTTPS, with conditions for MFA (remote users) and device posture (company-managed with endpoint security).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This structure is compatible with ABAC (NIST SP 800-162), with XACML, and with every commercial ZT policy engine. It's the formal expression of "identity-centric, context-sensitive access control."

## Stakes

Without a structured policy model, ZT policies become ad hoc rules that don't scale. The template ensures every policy answers: who, what, to what, under what conditions.

## Disagreement

**Who disagrees:**

_None identified._

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

The policy template is simple enough to fit on a whiteboard but complete enough to drive implementation. The dynamic target concept (resolving targets via IaaS tags at runtime) is the bridge to cloud-native environments. The chapter wisely defers detailed policy discussion to Ch17 but establishes enough foundation to make the architecture comprehensible.
