---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-governance
  - topic/zt-network
claim_id: "gb-ch7-8.13"
statement: "Forwarding and routing authorization extends policy enforcement into the network fabric itself"
confidence: "medium"
confidence_rationale: "MODERATE. The concept is sound and aligns with software-defined perimeter (SDP) architectures. However, practical deployment at scale remains"
claim_type: "governance"
source_note: "[[Gilman and Barth — Ch7-8 — Applications and Traffic]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch7-8.13: Forwarding and routing authorization extends policy enforcement into the network fabric itself

**Source:** [[Gilman and Barth — Ch7-8 — Applications and Traffic]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

Zero trust networks leverage slowly changing details of the network to distribute enforcement. This opens the possibility of propagating enforcement into the network infrastructure: an SDN controller that only installs flow instructions based on strong authentication and authorization. A client signals the control plane with credentials, the request is authorized, and the network fabric is configured to allow only that specific flow.

## Evidence

The observation that "filtering at every point" implies network devices themselves can be policy enforcement points, not just passive packet forwarders. The SDN controller model is presented as an ideal.

## Confidence

**Rating:** MEDIUM
**Rationale:** MODERATE. The concept is sound and aligns with software-defined perimeter (SDP) architectures. However, practical deployment at scale remains limited. SDN-based security is deployed in some environments (VMware NSX, Cisco ACI with security groups) but is far from universal.

## Stakes

If the network fabric enforces policy, the attack surface shrinks dramatically. Malicious traffic never reaches the host — it's dropped by the first switch that knows the flow isn't authorized. This is the ultimate realization of "the network is hostile" — even the network infrastructure doesn't trust the traffic it carries.

## Disagreement

**Who disagrees:**

The debate is about where authorization logic should live. Application-layer proponents argue that authorization belongs at the application/service mesh layer because it has richer context. Network-layer proponents argue that pushing enforcement down reduces attack surface. The authors' SDN vision sits between these positions but hasn't seen widespread adoption.

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

This is the chapter's most speculative claim. It's the logical endpoint of the filtering argument, but the operational complexity of tying SDN flow rules to application-level authorization has limited adoption. Service meshes achieve a similar goal at a different layer — the sidecar proxy is effectively a per-host SDN enforcement point. The vision is correct; the implementation layer has shifted.
