---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/beyondcorp
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-network
  - topic/zt-governance
claim_id: "beyondcorp.2"
statement: "The BeyondCorp access flow enforces per-request authorization through a continuously running trust inference pipeline that dynamically computes trust levels for both devices and users based on OS patch level, device model, security scan results, location, and behavioral heuristics."
confidence: "high"
confidence_rationale: "HIGH — Primary-source architecture documentation from the implementing team. The early migration strategy framework, while still conceptual in 2014"
claim_type: "implementation"
source_note: "[[BeyondCorp — Research Papers]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondcorp.2: The BeyondCorp access flow enforces per-request authorization through a continuously running trust inference pipeline that dynamically computes trust levels for both devices and users based on OS patch level, device model, security scan results, location, and behavioral heuristics.

**Source:** [[BeyondCorp — Research Papers]] — Google, *BeyondCorp Research Papers*, 2014-2020

## The Claim

The Access Control Engine performs per-request authorization checking: user in correct group, sufficient trust level, device managed and in good standing, sufficient device trust level. All checks pass → forward to backend; any check fails → denied. This is fed by a "continuously running pipeline" that dynamically infers trust levels.

## Evidence

Trust inference factors: device — OS patch level, specific device model/class, recent security scan results; user — access from new locations, role changes, behavioral heuristics. Both static rules and heuristics are used. A device missing recent OS patches might be relegated to reduced trust. A specific phone model might be assigned a particular trust level. The early migration strategy (2014, still conceptual): workflow qualification (VPN-only → split DNS → access proxy for ALL networks), job function analysis, VPN reduction, Traffic Analysis Pipeline (sampled netflow from every switch), Unprivileged Network Simulator (client-side traffic monitor with logging and enforcement modes), migration triggers (>99.9% eligible traffic for 30 days → simulator enforcement → >99.99% + 30 days enforcement → VLAN reassignment). Early warning: "We anticipate a long tail of workflows that will take some time to move to BeyondCorp. For example, fat-client applications that use proprietary protocols to talk to servers will be a challenge." This prediction was validated spectacularly.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — Primary-source architecture documentation from the implementing team. The early migration strategy framework, while still conceptual in 2014, already contains the key operational patterns (simulator, gradual migration triggers, long-tail anticipation) that Papers 2 and 4 later validate.

## Stakes

_Not addressed separately in the source note._

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

_Not addressed separately in the source note._
