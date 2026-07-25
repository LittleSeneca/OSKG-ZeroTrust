---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-architecture
  - topic/zt-implementation
claim_id: "nist207-ch3.4"
statement: "Four deployment models operationalize the logical architecture"
confidence: "high"
confidence_rationale: "HIGH — These deployment models accurately characterize the real-world implementation patterns observed in enterprise ZT deployments. They are not"
claim_type: "architectural"
source_note: "[[NIST 800-207 — Ch3 — Logical Components]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch3.4: Four deployment models operationalize the logical architecture

**Source:** [[NIST 800-207 — Ch3 — Logical Components]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

The logical components can be deployed in four ways: (1) Device Agent/Gateway, where the PEP is split into a client-side agent and a resource-side gateway; (2) Enclave-Based, where a gateway protects a collection of resources behind a boundary; (3) Resource Portal, where a single portal serves as a gateway without requiring client-side agents; and (4) Device Application Sandboxing, where vetted applications run in isolated compartments on assets. Multiple models may coexist in one enterprise.

## Evidence

Descriptions with architectural diagrams (Figures 3–6). Each model is evaluated for use cases, strengths, and limitations.

#### 3.2.1 Device Agent/Gateway

**Model:** Client-side agent forwards requests to PA; PA configures secure channel between agent and resource-side gateway. This is the CSA SDP client-server implementation.

**Best for:** Enterprises with robust device management programs and discrete resources that can have individual gateways. Not suitable for BYOD (agent must be installed on enterprise-owned assets).

**Confidence:** HIGH — This is the dominant ZTNA deployment pattern.

#### 3.2.2 Enclave-Based

**Model:** Gateway at the boundary of a resource enclave (e.g., data center, private cloud) protecting a collection of resources that serve a single business function. Can be hybrid with agent/gateway model.

**Best for:** Legacy applications, on-premises data centers that cannot support individual resource gateways, cloud micro-services behind a single gateway.

**Key downside:** Gateway protects a collection, not individual resources. Subjects may see resources they don't have access to. Less granular than agent/gateway.

**Confidence:** HIGH — This is a pragmatic model for legacy environments and correctly identifies the trade-offs.

#### 3.2.3 Resource Portal

**Model:** Single PEP component acting as a gateway portal — no client-side agent required. Access is via a web portal or similar interface.

**Best for:** BYOD policies, inter-organizational collaboration, environments where agent installation is infeasible.

**Key limitation:** Cannot continuously monitor devices between sessions. Limited device visibility. Portal is exposed to discovery and DoS attacks.

**Confidence:** HIGH — This model is widely used (browser-based access, Citrix-style portals) and the limitations are accurately described.

#### 3.2.4 Device Application Sandboxing

**Model:** Vetted applications run in isolated compartments (VMs, containers) on assets. The PEP refuses access requests from non-sandboxed applications.

**Advantage:** Protects individual applications from potentially compromised hosts.

**Disadvantage:** Enterprise must maintain sandboxed applications for all assets. May not have full visibility into client assets. More operational overhead than monitoring devices.

**Confidence:** MEDIUM — This model is conceptually sound but less commonly deployed as a standalone ZTA pattern. It's better understood as a defense-in-depth complement rather than a primary deployment model.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — These deployment models accurately characterize the real-world implementation patterns observed in enterprise ZT deployments. They are not mutually exclusive and an enterprise may use different models for different workflows.

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
