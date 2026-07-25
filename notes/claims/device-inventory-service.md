---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/beyondcorp
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-governance
  - topic/zt-device
claim_id: "beyondcorp.4"
statement: "The Device Inventory Service — ingesting 3M deltas/day from 15+ sources, correlating disparate identifiers, and precomputing trust evaluations — is the single most important operational component of BeyondCorp, and its data quality directly determines access availability."
confidence: "high"
confidence_rationale: "HIGH — Specific operational metrics (3M deltas/day, 15+ sources, 80+ TB, <1 second latency) from the implementing team. The precomputation design"
claim_type: "implementation"
source_note: "[[BeyondCorp — Research Papers]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondcorp.4: The Device Inventory Service — ingesting 3M deltas/day from 15+ sources, correlating disparate identifiers, and precomputing trust evaluations — is the single most important operational component of BeyondCorp, and its data quality directly determines access availability.

**Source:** [[BeyondCorp — Research Papers]] — Google, *BeyondCorp Research Papers*, 2014-2020

## The Claim

The Device Inventory Service is "arguably the single most important operational component" — a continuously updated pipeline that ingests from 15+ data sources at 30-100 changes/second, transforms data into common format, correlates disparate sources into unique device-specific records, notifies Trust Inferer to trigger reevaluation, and publishes trust tier assignments and VLAN annotations to enforcement gateways.

## Evidence

Data types: Observed (programmatically generated — security scan results, AD sync timestamps, OS version/patch level, installed software) and Prescribed (manually maintained by IT — assigned owner, allowed users/groups, DNS/DHCP assignments, explicit VLAN access). Correlation challenge: different data sources use different identifiers (asset ID, serial number, hard drive serial, certificate fingerprint, MAC address) — records combined when inventory agent reports several identifiers together, system handles component replacement during device lifecycle. Trust evaluation: Trust Inferer references dozens of fields (millions available); high trust requirements example: encrypted, all management agents executing successfully, most recent OS security patches installed, consistent data across all input sources. Precomputation strategy: trust evaluation is precomputed (not at request time) to reduce data pushed to gateways, reduce computation at access time, and enable pre-commit tests and canary deployments for policy changes — update latency typically <1 second.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — Specific operational metrics (3M deltas/day, 15+ sources, 80+ TB, <1 second latency) from the implementing team. The precomputation design decision (evaluate at pipeline time, not request time) is a specific architectural choice with clear rationale.

## Stakes

_Not addressed separately in the source note._

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**
- [[endpoint-new-perimeter|Treating the endpoint as the new perimeter requires fleet health and device trustworthiness data that only the Device In]]
- [[tiered-access|Tiered access levels depend on device trust evaluations computed by the Device Inventory Service from its 15+ data sourc]]

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
