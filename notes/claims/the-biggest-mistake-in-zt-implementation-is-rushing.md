---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-implementation
  - topic/zt-migration
  - topic/zt-architecture
  - topic/zt-network
claim_id: "go-ch9-11.1"
statement: "The biggest mistake in ZT implementation is rushing past monitor mode — organizations must inventory and understand endpoints in production before enforcing any restrictions, and monitor mode never truly ends."
confidence: "high"
confidence_rationale: "HIGH — Consistently reinforced across the BeyondCorp papers (log-before-enforce), Garbis & Chapman (PAM integration patterns), and NIST 800-207"
claim_type: "migration"
source_note: "[[Green-Ortiz — Ch9-11 — Advanced and Future]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch9-11.1: The biggest mistake in ZT implementation is rushing past monitor mode — organizations must inventory and understand endpoints in production before enforcing any restrictions, and monitor mode never truly ends.

**Source:** [[Green-Ortiz — Ch9-11 — Advanced and Future]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

Green-Ortiz et al. argue that monitor mode (also called visibility mode or unenforced discovery) is the critical data-gathering phase where endpoints are detected, profiled, and classified via DHCP, DNS, AD logins, CDP/LLDP, and NMAP scans — but no restrictions are enforced. An authorization result is allocated to the session for later use in traffic analysis and policy building, but not enforced.

## Evidence

The SBC Manufacturing case study: 1,600 devices took 4 months with a 3-person team to map. For larger organizations, 12–18 months is not unreasonable. Key tasks during monitor mode: (1) identify suspected device type (the "what" of contextual identity), (2) determine business functionality/owner/support team, (3) traffic analysis to create baseline, (4) document into asset management database. The authors explicitly state: "Monitor mode never truly ends" — it should continue for new devices even after enforcement is live. A remediation/quarantine policy as default on the NAC system helps manage "hard denials."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — Consistently reinforced across the BeyondCorp papers (log-before-enforce), Garbis & Chapman (PAM integration patterns), and NIST 800-207 migration guidance. This is one of the most convergent claims across the entire ZT literature.

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
