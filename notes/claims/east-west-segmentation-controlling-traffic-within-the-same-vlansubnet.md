---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-network
  - topic/zt-segmentation
  - topic/zt-implementation
  - topic/zt-architecture
claim_id: "go-ch6-8.2"
statement: "East-west segmentation — controlling traffic within the same VLAN/subnet — is the harder problem that most distinguishes ZT from traditional perimeter security, requiring Layer 2 identity-based enforcement that doesn't depend on routing."
confidence: "high"
confidence_rationale: "HIGH — The east-west problem is a well-defined technical challenge acknowledged across the ZT literature. The 4094-VLAN limit and operational chaos"
claim_type: "implementation"
source_note: "[[Green-Ortiz — Ch6-8 — Implementation]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch6-8.2: East-west segmentation — controlling traffic within the same VLAN/subnet — is the harder problem that most distinguishes ZT from traditional perimeter security, requiring Layer 2 identity-based enforcement that doesn't depend on routing.

**Source:** [[Green-Ortiz — Ch6-8 — Implementation]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

The most important architectural distinction in Ch6: north-south segmentation (between security zones, with natural enforcement points at routers/firewalls) vs. east-west segmentation (within the same VLAN, where no intermediary performs path selection). East-west is where malware spreads laterally, and solving it requires either breaking every device into its own VLAN (hitting the 4094-VLAN limit) or using Layer 2 identity-based enforcement.

## Evidence

TrustSec / Security Group Tags (SGT) is presented as the Cisco solution: a 16-bit SGT embedded in the Ethernet frame header (Cisco Meta Data field), assigned dynamically by ISE at authentication time, independent of VLAN/IP/MAC, traveling with every frame. Enforcement at egress by the network access device. Key capability: two adjacent devices in the same VLAN can be prevented from communicating; policy granularity ranges from specific ports/protocols per SGT pair to simple permit/deny. Two critical considerations: (1) applying Layer 2 segmentation could block a device from reaching its IP gateway — requiring complete understanding of all required traffic before enforcement; (2) the SGT taxonomy must not become too granular — the authors warn against overcomplicating, which "hinders operations teams by overcomplicating troubleshooting."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The east-west problem is a well-defined technical challenge acknowledged across the ZT literature. The 4094-VLAN limit and operational chaos from per-device VLANs are concrete constraints. The TrustSec solution is Cisco-specific but the architectural problem is universal.

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
- [[lateral-movement-prevention-raison-detre|East-west segmentation is the hardest lateral movement problem — controlling traffic within the same VLAN/subnet is what]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[micro-segmentation-blast-radius|East-west segmentation extends micro segmentation to its most granular level — controlling traffic between adjacent devi]]

## Assessment

_Not addressed separately in the source note._
