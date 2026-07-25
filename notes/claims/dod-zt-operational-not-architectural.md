---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/dod-zt-ra
  - topic/zt-definition
  - topic/zt-governance
claim_id: "dod-ra-ov.1"
statement: "DoD's ZT strategy is operational, not architectural"
confidence: "high"
confidence_rationale: "HIGH. The operational framing is explicit throughout: the document's primary audience is Mission Owners, not architects. The ZT RA tells MOs *what"
claim_type: "definitional"
source_note: "[[DoD ZT Reference Architecture — Overview and Strategy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# dod-ra-ov.1: DoD's ZT strategy is operational, not architectural

**Source:** [[DoD ZT Reference Architecture — Overview and Strategy]] — DISA and NSA Zero Trust Engineering Team, *DoD Zero Trust Reference Architecture v2.0*, 2022

## The Claim

The ZT RA is "an authoritative source of information about a specific subject area that guides and constrains the instantiations of multiple architectures and solutions." It is a *capability-centric* description — not a blueprint, but a framework for capability planning, portfolio management, and IT investment decisions.

## Evidence

The RA uses DoDAF operational views (OV-1, OV-2, CV-1, CV-2) rather than technical specifications. Artifacts are intentionally informal — "informal drawings are easier to understand by a wide audience." The document's organization prioritizes Strategy and Vision → Pillars and Principles → Conceptual Capability Architecture → Use Cases. The architecture is the *last* concern, not the first. This is the opposite of NIST 800-207, which leads with the PDP/PEP logical architecture.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The operational framing is explicit throughout: the document's primary audience is Mission Owners, not architects. The ZT RA tells MOs *what capabilities to build*, not how to build them.

## Stakes

If ZT is framed architecturally (NIST), implementation starts with policy engine design. If framed operationally (DoD), implementation starts with capability inventory and gap analysis. The DoD approach is more realistic for an organization with 3M+ endpoints and 4,000+ systems that can't be rebuilt from scratch.

## Disagreement

**Who disagrees:**

NIST 800-207 is explicitly architectural — the PDP/PEP model is the centerpiece. CISA's maturity model synthesizes both: it measures operational maturity (DoD's concern) against architectural capabilities (NIST's concern).

**Alternative reading:**

The operational framing could be read as political necessity — the DoD can't mandate specific architectures across all services, so it provides operational guidance that each service interprets. A stricter reading would demand architectural conformity.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The operational framing is the right call for the DoD's federated command structure. DISA can't tell the Army how to architect its networks, but it can tell all services what ZT capabilities they must demonstrate. The CISA maturity model operationalizes this for civilian agencies; the DoD ZT RA does the same for defense.
