---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-identity
  - topic/zt-architecture
claim_id: "gc-iam-policy.2"
statement: "Server-to-server ZT is a fundamentally different problem than user-to-server, requiring a CMDB as source of truth instead of IAM"
confidence: "high"
confidence_rationale: "HIGH. The claim that server-to-server ZT requires a solid CMDB or network discovery matches the DoD ZT Reference Architecture's emphasis on asset"
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Practice IAM Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-iam-policy.2: Server-to-server ZT is a fundamentally different problem than user-to-server, requiring a CMDB as source of truth instead of IAM

**Source:** [[Garbis and Chapman — Practice IAM Policy]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

PagerDuty's ZT network "is heavily reliant upon their configuration management system... it served as the 'source of truth' for all their resources and also as an automation platform. Effectively, this is a combination of the Policy Decision Point and the control channel."

## Evidence

PagerDuty's model (reported by Gilman & Barth) uses a central PDP based on their Chef configuration management system, distributed PEPs implemented as local iptables firewall rules, and IPsec mesh for network privacy. Each server is assigned a role; all servers in a given role have identical configurations. The system acts as a "normalization layer" across multiple public cloud environments with disparate security capabilities.

**Key contrast with BeyondCorp:**

PagerDuty focused on server-to-server (vs. user-to-server), securing resources across multiple public clouds (vs. a corporate network), using config management as the authoritative data source (vs. IAM + device inventory). Servers are "very different from user devices because they're generally deployed into fixed locations, and are 100% under the control of the enterprise."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The claim that server-to-server ZT requires a solid CMDB or network discovery matches the DoD ZT Reference Architecture's emphasis on asset management and the CISA maturity model's Device pillar. The PagerDuty approach is essentially the microsegmentation deployment model.

## Stakes

If server-to-server truly demands a different source-of-truth system than user-to-server, then a unified ZT platform must integrate with both CMDB and IAM — not just one. Platforms that only do user-to-server (many ZTNA products) are solving half the problem.

## Disagreement

**Who disagrees:**

Service mesh architectures (Istio, Linkerd) take a different approach: they embed PEPs as sidecars and use Kubernetes-native identity rather than a CMDB. The NIST logical component model is silent on the specific data source — it just says "external data sources" feed the PDP.

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

The CMDB vs. IAM distinction is a genuinely useful framework. It explains why BeyondCorp's emphasis on device posture doesn't map naturally to server environments — servers don't have users logging in from coffee shops. Every ZT deployment must explicitly decide which system is authoritative for which entity type.
