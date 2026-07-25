---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-definition
  - topic/zt-access-mgmt
  - topic/zt-network
claim_id: "gc-ch1-3.5"
statement: "The three core principles — secure all resources regardless of location, enforce least privilege, inspect/log all traffic — are universally necessary for any ZT implementation."
confidence: "high"
confidence_rationale: "HIGH. These three principles are directly traceable to Kindervag's original formulation and are validated by every subsequent ZT standard (NIST"
claim_type: "definitional"
source_note: "[[Garbis and Chapman — Ch1-3 — Introduction and Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-ch1-3.5: The three core principles — secure all resources regardless of location, enforce least privilege, inspect/log all traffic — are universally necessary for any ZT implementation.

**Source:** [[Garbis and Chapman — Ch1-3 — Introduction and Architecture]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"Across the industry, there are three core Zero Trust principles that are generally accepted as being foundational and essential. These were initially defined in the 'No More Chewy Centers' paper published by Forrester, and we believe that they must hold true in any Zero Trust implementation."

## Evidence

1. **Ensure all resources are accessed securely, regardless of location.** Requires all resources (data, applications, servers) to be in scope, all identities (human and machine) covered, regardless of where either is located. "This principle effectively mandates the dissolution of the traditional corporate perimeter."

2. **Adopt a least privilege strategy and strictly enforce access control.** The novel element: "the ability to send network packets to a system is a privilege, and must be managed as such. If users are not authorized to access a given service... they must not have the ability to connect to that service at a network layer." This closes the gap between network and application security.

3. **Inspect and log all traffic.** Networks are where distributed components communicate — making them the natural monitoring point. Traffic metadata should be enriched with identity and device context and fed into NGFWs, SIEMs, and monitoring tools.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These three principles are directly traceable to Kindervag's original formulation and are validated by every subsequent ZT standard (NIST, CISA, DoD all embed variants of these).

## Stakes

These principles define the minimum bar. Any system that fails any of them is not ZT. They also create the engineering requirements: if network access is a privilege, you need network-layer PEPs that understand identity. If all resources must be in scope, you need a platform, not point products.

## Disagreement

**Who disagrees:**

NIST's seven tenets are more granular but map cleanly to these three. Gartner's CARTA adds continuous risk assessment as a separate dimension. The principles are widely accepted; debate is about relative priority and implementation, not the principles themselves.

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

Principle 2 contains the single most important operational insight in the book: "network access is a privilege." This reframes network security from "protect the perimeter" to "control every connection based on identity." It's the bridge between identity management (IAM) and network security that most enterprises are missing.
