---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-architecture
  - topic/zt-policy
claim_id: "nist207-ch2.4"
statement: "The PDP/PEP model is the abstract architecture underlying all ZTA deployments"
confidence: "high"
confidence_rationale: "VERY HIGH. The PDP/PEP model appears in every ZTA implementation: Google's Access Proxy, ZTNA products, SDP controllers/gateways. It is the architectu"
claim_type: "architectural"
source_note: "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---

# nist207-ch2.4: The PDP/PEP model is the abstract architecture underlying all ZTA deployments

**Source:** [[NIST 800-207 — Ch2 — Zero Trust Basics]] — Scott Rose, Oliver Borchert, Stu Mitchell, Sean Connelly, *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

Access is granted through a Policy Decision Point (PDP) and Policy Enforcement Point (PEP). All subjects must pass through this gateway, and the implicit trust zone must be as small as possible.

## Evidence

The airport security analogy — all passengers pass through the checkpoint (PDP/PEP), and the boarding area is the implicit trust zone. The PDP/PEP cannot apply additional policies beyond its location in the traffic flow. Moving PDP/PEPs closer to resources shrinks the implicit trust zone.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. The PDP/PEP model appears in every ZTA implementation: Google's Access Proxy, ZTNA products, SDP controllers/gateways. It is the architectu

## Stakes

If PDP/PEP is the only model, ZTA requires an inline enforcement point for every resource — a scalability challenge. Alternative models (e.g., distributed policy enforcement via service mesh) exist but NIST doesn't explore them here.

## Disagreement

**Who disagrees:**

Gilman & Barth (Zero Trust Networks) describe this as the "control plane / data plane" split rather than PDP/PEP. The concepts are equivalent but the terminology differs. Google BeyondCorp uses "Access Proxy" rather than PDP/PEP. Sounil Yu's Cyber Defense Matrix situates ZT enforcement differently depending on the asset class.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**
<!-- Claims this one requires to be true -->

**Supports:**
- [[zt-control-data-plane-split]]

**Contradicts:**
<!-- Claims that cannot be true if this one is -->

**Challenged by:**
<!-- Evidence or arguments that weaken this claim -->

**Operationalizes:**
- [[zt-control-data-plane-split]]

**Extends:**
<!-- Claims this one builds upon or elaborates -->

## Assessment

The PDP/PEP model is the most important architectural concept in NIST 800-207. Everything in Ch 3 (logical components) elaborates this model. Understanding PDP/PEP is the prerequisite for understanding ZTA deployment.

## Zero Trust Taxonomy

### Topic tags
`topic/zt-architecture` `topic/zt-policy`

### Evidence tags
`evidence/primary-standard`
