---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-identity
  - topic/zt-device
claim_id: "go-ch6-8.4"
statement: "True contextual identity is never just a device type — a displayless hardware phone used after hours by Facilities has a fundamentally different identity than a director's hardware phone at home during business hours, and this multi-dimensional profiling is the foundation of all ZT enforcement."
confidence: "high"
confidence_rationale: "HIGH — The profiling methodology is the most detailed practical guide to device identification in the ZT literature. The multi-attribute identity"
claim_type: "definitional"
source_note: "[[Green-Ortiz — Ch6-8 — Implementation]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch6-8.4: True contextual identity is never just a device type — a displayless hardware phone used after hours by Facilities has a fundamentally different identity than a director's hardware phone at home during business hours, and this multi-dimensional profiling is the foundation of all ZT enforcement.

**Source:** [[Green-Ortiz — Ch6-8 — Implementation]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

The authors expand the familiar "who, what, where, when, how" framework with specific profiling techniques and make the provocative point: "True contextual identity is never just 'phone,' 'printer,' 'laptop,' or 'camera.'" The contextual identity decision tree (Figure 7-1) demonstrates that identity is the product of multiple intersecting attributes.

## Evidence

Specific profiling techniques: Who — directory services for domain-joined devices, asset management databases for headless devices; What (Active) — NMAP scanning with caution for legacy devices, OS fingerprinting, SNMP, vulnerability scanner integration; What (Passive) — RADIUS probe data, DHCP options and hostname, HTTP User-Agent headers, CDP/LLDP, MUD URLs for IoT, with DHCP weighted higher than MAC address because harder to spoof; Where — geographic location narrows identity; When — time-of-day patterns, 3 AM connections may indicate compromise; How — connection medium, an iPad via wired Ethernet triggers additional scrutiny. The "minimum viable products" approach: break network into functional elements, use agile methodologies for incremental value.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The profiling methodology is the most detailed practical guide to device identification in the ZT literature. The multi-attribute identity claim is a conceptual insight with direct operational implications.

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
