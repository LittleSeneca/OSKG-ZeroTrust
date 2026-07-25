---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/ncsc
  - topic/zt-cloud
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-network
claim_id: "ncsc.1"
statement: "The NCSC's 8 principles provide a practical, vendor-agnostic framework for ZT architecture that is complementary to NIST SP 800-207 but more operationally prescriptive."
confidence: "high"
confidence_rationale: "HIGH on the NCSC principles being a valid ZT framework. They are more operationally prescriptive than NIST's seven tenets — Principle 7 (\"don't trust"
claim_type: "implementation"
source_note: "[[NCSC — ZT Principles on Google Cloud]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# ncsc.1: The NCSC's 8 principles provide a practical, vendor-agnostic framework for ZT architecture that is complementary to NIST SP 800-207 but more operationally prescriptive.

**Source:** [[NCSC — ZT Principles on Google Cloud]] — NCSC, *Zero Trust Principles on Google Cloud*, 2023

## The Claim

The NCSC's 8 principles provide a practical, vendor-agnostic framework for ZT architecture that is complementary to NIST SP 800-207 but more operationally prescriptive.

## Evidence

**Context:**

The NCSC Zero Trust Architecture Design Principles are the UK government's equivalent of NIST SP 800-207. The 8 principles are:

1. **Know your architecture** — including users, devices, services, and data
2. **Know your User, Service and Device identities** — each uniquely identifiable
3. **Assess your user behaviour, devices and services health** — continuous health evaluation as signals for policy engines
4. **Use policies to authorize requests** — each request authorized against policy
5. **Authenticate & Authorise everywhere** — multiple signals; assume hostile network
6. **Focus your monitoring on users, devices and services** — not just network boundaries
7. **Don't trust any network, including your own** — secure transport; traditional network-based protections must shift
8. **Choose services designed for zero trust** — prefer standards-based, ZT-native services; legacy services require additional integration

**Google's mapping:**

The whitepaper maps each principle to specific Google Cloud services. For example: Principle 1 maps to Cloud Asset Inventory, Data Catalog, and Professional Services migration planning; Principle 2 maps to Cloud Identity, IAM, service accounts, and Verified Access (device identity via TPM on ChromeOS); Principle 4 maps to Identity-Aware Proxy (IAP) as the PEP, Access Context Manager as the Rules Engine, and VPC Service Controls for network-layer enforcement.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the NCSC principles being a valid ZT framework. They are more operationally prescriptive than NIST's seven tenets — Principle 7 ("don't trust any network, including your own") is a stronger, more directive statement than NIST's "all communication is secured regardless of network location." The NCSC framework is designed for UK government adoption but is jurisdiction-agnostic in its technical content.

## Stakes

The NCSC principles represent an alternative ZT articulation to NIST. For organizations operating in both US and UK contexts (or multinationals), understanding the mapping between the two frameworks is essential. Google's whitepaper implicitly claims GCP satisfies both.

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[zt-operationalized-three-principles-apply-differently-per|Both provide practical operational frameworks for ZT: NCSC's 8 principles are vendor-agnostic guidance complementing the]]
- [[beyondcorp-google-implementation-zt-model-provides-architectural|NCSC's vendor-agnostic framework validates and complements Google's ZT implementation, showing it satisfies an independe]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The NCSC principles are a valuable complement to NIST. They are more concrete — Principle 1 ("know your architecture") is an action, not an abstraction. Principle 3 ("assess user behaviour, devices and services health") operationalizes continuous monitoring more explicitly than NIST's tenet 5. The 8-principle structure maps cleanly to an implementation sequence (know → identify → assess → authorize → authenticate → monitor → secure transport → choose services), making it a more natural project plan than NIST's seven tenets.
