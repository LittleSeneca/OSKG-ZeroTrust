---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-architecture
  - topic/zt-network
  - topic/zt-policy
claim_id: "gc-ch1-3.10"
statement: "There are three distinct types of PEPs, and understanding their differences is essential for architecture design."
confidence: "high"
confidence_rationale: 'HIGH. The three-type model cleanly maps real-world security infrastructure to ZT functions. It survives the "fuzzy line" test — the authors'
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Ch1-3 — Introduction and Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-ch1-3.10: There are three distinct types of PEPs, and understanding their differences is essential for architecture design.

**Source:** [[Garbis and Chapman — Ch1-3 — Introduction and Architecture]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"We believe that there are actually three types of PEPs: user agent PEPs, network PEPs, and application PEPs."

| PEP Type | Function | Examples |
|----------|----------|----------|
| **User Agent** | Runs on user device; establishes encrypted connections, introspects device posture, interacts with end user (MFA prompts, notifications) | ZTNA client, browser extension |
| **Network** | Inline network enforcement; controls traffic based on identity and context; inspects metadata or content | NGFW (with automation layer), ZT gateway, SDP gateway |
| **Application** | Enforces policies at application layer; may be external (PAM, DLP) or internal (host agent, app-integrated) | PAM, DLP, host-based firewall agent, SAML-based JIT provisioning |

## Evidence

The distinction emerges from analyzing where enforcement can and must happen. Network PEPs are "the most common starting point" and align with NIST's orientation. Application PEPs enable just-in-time provisioning and role enforcement. User agent PEPs handle device posture and secure tunnel establishment.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The three-type model cleanly maps real-world security infrastructure to ZT functions. It survives the "fuzzy line" test — the authors acknowledge that DLP can be network-based or host-based, and that the important thing is inclusion in the policy model, not rigid categorization.

## Stakes

If all PEPs are treated as equivalent, architecture design loses precision. A network PEP can't enforce application roles; an application PEP can't control network access. Knowing which type you need for which function prevents architecture mistakes.

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

The user agent PEP is the most interesting category. The authors note it's "optional" but most commercial systems provide one and most enterprises need one. The tension between agent-based and agentless (clientless) access is a recurring theme in ZT deployment — agent-based gives richer context but creates deployment friction. The authors handle this balance well.
