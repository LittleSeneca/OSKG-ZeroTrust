---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-app
  - topic/zt-authentication
claim_id: "gb-ch7-8.5"
statement: "Per-instance time-bound secrets are the mechanism for authorizing running applications"
confidence: "high"
confidence_rationale: "HIGH. This is the foundation of modern service identity (SPIFFE/SPIRE, Istio workload identity, AWS IAM roles with session tokens). The pattern has"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch7-8 — Applications and Traffic]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch7-8.5: Per-instance time-bound secrets are the mechanism for authorizing running applications

**Source:** [[Gilman and Barth — Ch7-8 — Applications and Traffic]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

Knowing what's running in your infrastructure requires that every running instance be individually authorized. This authorization can be implemented through per-instance secrets with defined lifetimes. By generating a unique secret for each deployed instance and attaching a lifetime, you assert that you know precisely what's running because you know how many secrets you generated, who you gave them to, and when they expire.

## Evidence

HashiCorp Vault's response wrapping feature: the deployment system notifies Vault to expect a new instance, Vault provisions unique time-bound credentials, and the application retrieves them using a one-time token injected during deployment. If an instance goes rogue, its credentials expire and it can no longer operate.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is the foundation of modern service identity (SPIFFE/SPIRE, Istio workload identity, AWS IAM roles with session tokens). The pattern has become industry standard.

## Stakes

Without per-instance, time-bound credentials, you can't distinguish between authorized instances and rogue ones. A compromised host could continue operating indefinitely with stolen long-lived credentials.

## Disagreement

**Who disagrees:**

The debate has moved from "should we do this" to "how should we do this." SPIFFE/SPIRE uses X.509 SVIDs with short lifetimes (typically 1 hour). Cloud IAM uses session tokens. The authors' Vault example is one implementation among many now.

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

This claim connects the application pipeline to the traffic chapter: the secrets provisioned here (often X.509 certificates or API keys) are exactly what Chapter 8's mutually authenticated TLS and IPsec will use to authenticate network flows. The deployment system is the bridge between "this is an authorized application instance" and "this is an authorized network flow."
