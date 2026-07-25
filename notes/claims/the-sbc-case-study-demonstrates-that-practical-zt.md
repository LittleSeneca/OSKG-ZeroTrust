---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-implementation
  - topic/zt-device
  - topic/zt-cloud
  - topic/zt-architecture
claim_id: "go-ch9-11.7"
statement: "The SBC case study demonstrates that practical ZT implementation must constrain scope aggressively — 10 TrustSec tags maximum, 5–7 endpoint groups, and a dedicated IoT tiger team — to avoid analysis paralysis and operational chaos."
confidence: "high"
confidence_rationale: "HIGH — This is a detailed, named, walkthrough-length case study with specific metrics and configuration details. The 10-tag cap and 5–7 enclave"
claim_type: "implementation"
source_note: "[[Green-Ortiz — Ch9-11 — Advanced and Future]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch9-11.7: The SBC case study demonstrates that practical ZT implementation must constrain scope aggressively — 10 TrustSec tags maximum, 5–7 endpoint groups, and a dedicated IoT tiger team — to avoid analysis paralysis and operational chaos.

**Source:** [[Green-Ortiz — Ch9-11 — Advanced and Future]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

The authors' empirical finding from Cisco services: "Customers who use dynamic application of enforcement policy have the best likelihood of success when they start with no more than five to seven groups or enclaves." The SBC implementation validated this with a 10-tag TrustSec strategy.

## Evidence

The SBC case study details: (1) TrustSec tag strategy capped at 10 tags (Corporate, Collaboration, IP Cameras, Printers, Print Servers, IoT, Guests, BMS, IT) with planned sub-tags deferred; (2) IP cameras received their own tag because of unique multicast discovery behavior — "carving them out was a conscious risk decision balancing security vs. operational continuity"; (3) "The Key Masters" — a dedicated tiger team for IoT device onboarding that documented ~10× more connections than manufacturers provided; (4) DNS enforcement via Cisco Umbrella with content filtering applied to corporate devices but not guests; (5) Analytics Triad: Secure Network Analytics + Secure Workload + Thousand Eyes; (6) Cultural resistance from staff bringing unauthorized devices — IT initially accommodated with dynamic quarantining but discontinued after Q1 to force proper onboarding.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — This is a detailed, named, walkthrough-length case study with specific metrics and configuration details. The 10-tag cap and 5–7 enclave starting point are the most specific, empirically grounded implementation constraints in the ZT literature.

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
- [[zta-implementation-continuous-improvement-journey-one|The SBC case study's aggressive scope constraint (10 tags, 5-7 endpoint groups) demonstrates a practical strategy for su]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[the-zero-trust-implementation-curve-prevents-boiling-the|The SBC case study is a concrete, detailed example of the Implementation Curve in practice, showing how aggressive scope]]

## Assessment

_Not addressed separately in the source note._
