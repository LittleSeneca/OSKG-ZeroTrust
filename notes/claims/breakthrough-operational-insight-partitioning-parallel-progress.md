---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/beyondcorp
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-network
  - topic/zt-migration
claim_id: "beyondcorp.5"
statement: "The breakthrough operational insight was partitioning for parallel progress — deploying a new VLAN in its final BeyondCorp configuration and incrementally moving devices to it, rather than incrementally restricting the privileged VLAN."
confidence: "high"
confidence_rationale: "HIGH — This is an explicit, named architectural decision (partitioning for parallel progress) from the operational migration playbook, validated by"
claim_type: "implementation"
source_note: "[[BeyondCorp — Research Papers]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondcorp.5: The breakthrough operational insight was partitioning for parallel progress — deploying a new VLAN in its final BeyondCorp configuration and incrementally moving devices to it, rather than incrementally restricting the privileged VLAN.

**Source:** [[BeyondCorp — Research Papers]] — Google, *BeyondCorp Research Papers*, 2014-2020

## The Claim

Rather than incrementally restricting the privileged VLAN (removing one application/server at a time from the legacy network), Google deployed a new VLAN in its final BeyondCorp configuration and incrementally moved devices to it. This allowed the network layer to achieve stability independently, isolated the network layer from migration policy details via RADIUS-provided VLAN assignments, and enabled parallel progress at every layer of the stack.

## Evidence

Parallel workstreams: Network — new VLANs, 802.1x, RADIUS policy server; Client platforms — certificate generation/installation, user authentication tools; Applications — service and workflow remediation; Processes — continuous refinement of procedures. 802.1x foundation: install certificates on every user device (required new CA with APIs, per-OS distribution tools, telemetry for monitoring), transition to 802.1x for all network access (re-provision switches, integrate with policy-driven RADIUS), initial RADIUS policy matched existing assignments (avoiding failures from new server), deploy in auditing mode comparing new vs. legacy assignments, enable new policy when differences sufficiently few. Result: VLAN assignments controlled by high-level software and data-driven policies in near-real time, decoupled from network hardware configuration.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — This is an explicit, named architectural decision (partitioning for parallel progress) from the operational migration playbook, validated by the documented outcome of >50% fleet migration within one year.

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
