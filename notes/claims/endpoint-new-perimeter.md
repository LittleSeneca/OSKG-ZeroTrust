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
claim_id: "beyondcorp.9"
statement: 'The endpoint is the new perimeter — fleet health and device trustworthiness replace network location as the foundation of access decisions, and the "identified state" solves the chicken-and-egg problem of transitioning untrusted devices into a trustworthy state.'
confidence: "high"
confidence_rationale: "HIGH — Primary-source documentation of Google's endpoint security model. The Identified State is a specific architectural solution to a well-defined"
claim_type: "implementation"
source_note: "[[BeyondCorp — Research Papers]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondcorp.9: The endpoint is the new perimeter — fleet health and device trustworthiness replace network location as the foundation of access decisions, and the "identified state" solves the chicken-and-egg problem of transitioning untrusted devices into a trustworthy state.

**Source:** [[BeyondCorp — Research Papers]] — Google, *BeyondCorp Research Papers*, 2014-2020

## The Claim

"The platforms that make up the fleet are the new perimeter." The paper shifts focus from network architecture to endpoint security. A healthy device "can withstand most attacks" (preventative controls) and "provides sufficient telemetry to contain a compromise when one occurs" (detective controls).

## Evidence

Ten threat classes mapped to controls: unknown devices → fleet inventory; platform compromise via misconfigured OS → configuration management; security control bypass → policy management; privilege escalation → resilience against takeover; malware → software control + anti-malware; prolonged persistence → remotely verifiable platform state; authentication bypass → robust auth of platform and user; unauthorized data access → encryption at rest + in transit; attack concealment → logging and log collection; attack repudiation → detection and response. The Identified State: a critical operational insight — transitioning a device into a trustworthy state requires access to a client software repository, but a client software repository is a sensitive system (chicken-and-egg). Solution: an intermediate "Identified" state between untrusted and trusted — device is in inventory and believed to be in good standing but not yet trusted, can access a subset of the client software repository, can download remediation software, report device state, apply patches, fulfill trusted platform requirements.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — Primary-source documentation of Google's endpoint security model. The Identified State is a specific architectural solution to a well-defined operational problem (bootstrapping trust).

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
