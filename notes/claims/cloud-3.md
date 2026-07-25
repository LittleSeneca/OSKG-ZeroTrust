---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/halley-resilient-cloud
  - topic/zt-cloud
  - topic/zt-implementation
claim_id: "halley.3"
statement: "Cloud-native architectures are inherently ZT-aligned — but introduce new security surfaces"
confidence: "high"
confidence_rationale: "HIGH for the structural alignment claim; cloud-native architectures genuinely embody ZT principles better than traditional data centers. MODERATE for"
claim_type: "implementation"
source_note: "[[Halley — Zero Trust in Resilient Cloud]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# halley.3: Cloud-native architectures are inherently ZT-aligned — but introduce new security surfaces

**Source:** [[Halley — Zero Trust in Resilient Cloud]] — Andrew Halley et al., *Zero Trust in Resilient Cloud*, 2023

## The Claim

Cloud-native architectures (microservices, containers, Kubernetes, serverless) share deep structural alignment with ZT principles: immutable infrastructure (no persistent trust), declarative APIs (policy as code), service-to-service communication (no implicit trust between services), and dynamic orchestration (continuous adaptation). However, they also introduce new attack surfaces: container escape, supply chain compromise, API vulnerabilities, and misconfigured IAM roles.

## Evidence

The book's Part 4 (Ch15-18) provides a comprehensive security stack from infrastructure through application to end-user. Key ZT-aligned patterns include:
- **Immutable infrastructure:** Containers are replaced, not patched — eliminating configuration drift and persistent compromise.
- **Service mesh (Istio):** mTLS between services + fine-grained authorization policies — ZT for east-west traffic.
- **Policy-as-code (OPA, Sentinel):** Security policies are version-controlled, tested, and deployed through CI/CD — making policy enforcement auditable and repeatable.
- **CNAPP (Cloud-Native Application Protection Platform):** Unified security from code to cloud — shift-left scanning + runtime protection.
- **Shared responsibility model:** Cloud provider secures the infrastructure; customer secures everything in the cloud. ZT is the customer's responsibility.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH for the structural alignment claim; cloud-native architectures genuinely embody ZT principles better than traditional data centers. MODERATE for specific product recommendations (Cisco SFCN, Cisco Secure Workload).

## Stakes

Organizations migrating to cloud often carry over perimeter-based security thinking — assuming the cloud provider's firewall is sufficient. Cloud-native ZT requires rethinking security at every layer: network (VPC, security groups), container (network policies, runtime security), application (API auth, service mesh), and data (encryption, classification).

## Disagreement

**Who disagrees:**

"Lift-and-shift" advocates argue that moving VMs to the cloud with existing security controls is sufficient. Halley argues this loses the security benefits of cloud-native patterns — you're running a data center security model on cloud infrastructure, inheriting the cloud's attack surface without its defensive capabilities.

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

The cloud-native ZT alignment is the most forward-looking contribution of this book. As organizations increasingly adopt Kubernetes and serverless, understanding how ZT maps to these environments becomes critical. This is where Halley adds value beyond NIST 800-207, which predates widespread cloud-native adoption.
