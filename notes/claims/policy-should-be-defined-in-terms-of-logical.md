---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-policy
  - topic/zt-architecture
claim_id: "gb-ch4-6.3"
statement: "Policy should be defined in terms of logical components, not network addressing"
confidence: "high"
confidence_rationale: "HIGH. This is widely adopted — Kubernetes NetworkPolicy, service mesh authorization policies, and cloud IAM all define policy on logical labels. NIST"
claim_type: "architectural"
source_note: "[[Gilman and Barth — Ch4-6 — Authorization Devices Users]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch4-6.3: Policy should be defined in terms of logical components, not network addressing

**Source:** [[Gilman and Barth — Ch4-6 — Authorization Devices Users]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"Instead of defining policy in terms of network implementation details (IP addresses and ranges), policy is best defined in terms of logical components in the network. These components will generally consist of: Network services, Device endpoint classes, User roles."

## Evidence

They cite Kubernetes network policies (workload labels computing IP rules at enforcement time) as an example. Policy stored in version control enables code review, change tracking, validation. They add: "Most policy should include a trust score component." On who defines policy: distributed across teams with security review, layered with infrastructure policy that no user can override.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is widely adopted — Kubernetes NetworkPolicy, service mesh authorization policies, and cloud IAM all define policy on logical labels. NIST 800-207's PA operates on "subject attributes" (identity-based) not network attributes. The version-control recommendation is standard practice.

## Stakes

If policy is defined on IP addresses, ZT loses its ability to adapt to dynamic infrastructure. Workload scheduling, auto-scaling, and failover all break static IP-based policy. The "logical component" principle is what makes ZT feasible in cloud-native environments.

## Disagreement

**Who disagrees:**

No major source disagrees. The gap is in standardization — Gilman & Barth note: "Currently, mature zero trust networks implement their own policy language/format on a case-by-case basis... such work remains an open research question." This remains true in 2024 (OPA/Rego, Cedar, various vendor-specific DSLs).

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
