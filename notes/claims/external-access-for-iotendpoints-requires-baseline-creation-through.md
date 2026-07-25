---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-access-mgmt
  - topic/zt-device
  - topic/zt-implementation
  - topic/zt-identity
claim_id: "go-ch6-8.6"
statement: "External access for IoT/endpoints requires baseline creation through multiple collection points — edge firewall logs, Internet proxy logs, NetFlow, endpoint agents, and DNS analytics — because vendor documentation of network interactions is unreliable."
confidence: "high"
confidence_rationale: "HIGH — The multi-collection-point methodology is specific and operational. The observation about legitimate resources having longer-lived connection"
claim_type: "implementation"
source_note: "[[Green-Ortiz — Ch6-8 — Implementation]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch6-8.6: External access for IoT/endpoints requires baseline creation through multiple collection points — edge firewall logs, Internet proxy logs, NetFlow, endpoint agents, and DNS analytics — because vendor documentation of network interactions is unreliable.

**Source:** [[Green-Ortiz — Ch6-8 — Implementation]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

IoT devices rely on elastic cloud infrastructure with dynamically updated DNS names, and vendor documentation of network interactions is unreliable. The binary choice appears to be "allow anything to *.vendor.com" or exhaustively track every destination — neither is acceptable.

## Evidence

The solution uses multiple collection points: edge firewall logs + identity injection, Internet proxy logs, NetFlow (Cisco Secure Network Analytics), endpoint agents (Network Traffic Analysis module), and DNS analytics (Cisco Umbrella). Key insight: "resources to run the business... will be longer lived and more commonly accessed than malware-infected resources, which will need to change servers, hosting providers, or cloud services on a regular basis to avoid detection." The firewall rule lifecycle problem: without audit processes, "it's common to have hundreds of thousands of rules, with large percentages representing overlaps in address and purpose." ZT's distributed policy approach forces cleanup of poorly managed centralized firewall rules as a side benefit.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The multi-collection-point methodology is specific and operational. The observation about legitimate resources having longer-lived connection patterns vs. malware is a useful heuristic for baseline differentiation.

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
