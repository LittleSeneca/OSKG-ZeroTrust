---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-governance
  - topic/zt-monitoring
claim_id: "nist207-ch6.7"
statement: "EINSTEIN/NCPS must evolve its perimeter-situational-awareness model to ingest cloud-based telemetry and ZTA-generated data — ZTA improves detection data quality but requires NCPS to adapt its sensor model from perimeter-based to resource-proximate."
confidence: "medium"
confidence_rationale: "MEDIUM. The evolution path is logically sound but NIST is describing a desired future state — NCPS adaptation to ZTA was not operationally realized"
claim_type: "governance"
source_note: "[[NIST 800-207 — Ch6 — Federal Guidance]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch6.7: EINSTEIN/NCPS must evolve its perimeter-situational-awareness model to ingest cloud-based telemetry and ZTA-generated data — ZTA improves detection data quality but requires NCPS to adapt its sensor model from perimeter-based to resource-proximate.

**Source:** [[NIST 800-207 — Ch6 — Federal Guidance]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

NCPS (EINSTEIN) delivers intrusion detection, advanced analytics, information sharing, and intrusion prevention for federal networks. Current NCPS sensor placement assumes perimeter defense; ZTA moves protections to the resource level. (§6.5)

## Evidence

- NCPS must evolve to (a) ingest cloud-based traffic telemetry, (b) receive expanded situational awareness data from ZTA systems, and (c) inform policy enforcement at both legacy NCPS locations and new ZTA PEPs.
- **Upside for incident response:** ZTA generates richer authentication, inspection, and logging data that can improve event impact quantification, feed ML-based detection, and support after-the-fact forensic analysis.

**Implication for OSKG-ZeroTrust:**

NCPS is the legacy detection backbone. ZTA improves detection data quality but requires NCPS to adapt its sensor model. The chapter frames this as evolution, not replacement.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. The evolution path is logically sound but NIST is describing a desired future state — NCPS adaptation to ZTA was not operationally realized at time of publication.

## Stakes

_Not addressed separately in the source note._

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**
  - [[tic-3-converging-with-zta]]

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
