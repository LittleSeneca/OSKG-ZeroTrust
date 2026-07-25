---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-network
  - topic/zt-architecture
  - topic/zt-implementation
  - topic/zt-segmentation
claim_id: "go-ch6-8.5"
statement: "The firewall-is-enough belief is mathematically disproven — a network with 2,046 VLANs passing through a firewall requires a minimum of 12,000 initial rules just for shared services, not counting business-specific rules."
confidence: "high"
confidence_rationale: "HIGH — The 12,000-rule calculation is a concrete, verifiable mathematical argument. The university network model provides an alternative operational"
claim_type: "architectural"
source_note: "[[Green-Ortiz — Ch6-8 — Implementation]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch6-8.5: The firewall-is-enough belief is mathematically disproven — a network with 2,046 VLANs passing through a firewall requires a minimum of 12,000 initial rules just for shared services, not counting business-specific rules.

**Source:** [[Green-Ortiz — Ch6-8 — Implementation]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

Organizations with large firewall estates believe firewalls alone constitute sufficient segmentation. The math disproves this: each VLAN requires DNS, DHCP, authentication, remote access protocols, and domain controller traffic rules — a set of 6 × N VLANs = ~12,000 rules minimum for 2,046 VLANs.

## Evidence

The authors propose a university/research network model where every endpoint is treated as a threat by default: (1) treat every endpoint as a threat to the network; (2) segment endpoints from everything except critical services; (3) require users to agree to policy stating explicit access requirements; (4) require the level of contextual identity the organization can facilitate; (5) apply enforcement and vulnerability management at network ingress. The firewall's retained role: advanced features that access switches cannot provide (IPS, malware detection, TCP normalization, DLP, VPN termination) — but it becomes one layer among many rather than the sole enforcement point. The firewall for external access can typically be a smaller, lower-throughput model.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The 12,000-rule calculation is a concrete, verifiable mathematical argument. The university network model provides an alternative operational paradigm with specific, enumerated principles.

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
