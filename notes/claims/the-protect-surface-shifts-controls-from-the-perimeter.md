---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-definition
  - topic/zt-architecture
  - topic/zt-implementation
  - topic/zt-network
claim_id: "finney-ch1-3.10"
statement: "The protect surface shifts controls from the perimeter to the asset"
confidence: "high"
confidence_rationale: "HIGH. This is the core ZT architectural principle — microsegmentation with policy enforcement at each protect surface boundary. The physical security"
claim_type: "definitional"
source_note: "[[Finney — Ch1-3 — The Zero Trust Story]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch1-3.10: The protect surface shifts controls from the perimeter to the asset

**Source:** [[Finney — Ch1-3 — The Zero Trust Story]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"We put cameras and fire suppression and card access around the data center, but maybe we don't need all of those things at the perimeter of the facility in the parking lots. But that's exactly what we're doing in cybersecurity when we put a firewall by the Internet and call it a day."

## Evidence

The team discovers that card readers, cameras, and HVAC systems are all on the same network as user workstations. Aaron points out that while the physical building has layered security zones (lobby → office areas → data center), the network treats everything as equally trusted once inside the perimeter. The ZT solution: microsegmentation, moving card readers and cameras to separate non-routed networks, and only allowing specific, authenticated access.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is the core ZT architectural principle — microsegmentation with policy enforcement at each protect surface boundary. The physical security analogy makes it intuitive.

## Stakes

If organizations implement microsegmentation without the other ZT principles (identity-based policy, continuous monitoring), they've just created smaller perimeters with the same trust assumptions. The protect surface concept only works as part of the full methodology.

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

Finney correctly uses physical security to teach *both* the protect surface concept and its limitations. The physical building has zones of different trust (lobby, office, data center) — exactly what network microsegmentation creates. But the physical analogy also shows why you need monitoring: Dylan was caught in the data center because a human noticed him, not because the card reader system detected an anomaly. In ZT, the monitoring step (#5) is the equivalent of having guards who notice things.
