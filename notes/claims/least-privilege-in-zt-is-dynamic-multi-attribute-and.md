---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-access-mgmt
  - topic/zt-device
claim_id: "gb-ch2.4"
statement: "Least privilege in ZT is dynamic, multi-attribute, and device-bound"
confidence: "high"
confidence_rationale: "HIGH. This multi-attribute, contextual approach to least privilege is the operational heart of ZT authorization. It's directly implemented in"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch2 — Managing Trust]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch2.4: Least privilege in ZT is dynamic, multi-attribute, and device-bound

**Source:** [[Gilman and Barth — Ch2 — Managing Trust]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

Least privilege in ZT goes beyond traditional user/application privilege to include the device, the temporal context, the geographic context, and the behavioral baseline. "It is the combination of user or application and the device being used that determines the privilege level granted." Privilege is temporary and contextual — "users should similarly operate in a reduced privilege mode on the network most of the time, only elevating their permissions when needed." The authors also make the subtle point that encryption itself is an application of least privilege: "Who really needs access to the packet payload?"

## Evidence

Three dimensions of dynamic privilege are described: (1) temporal — access outside normal working hours is more suspicious; (2) geographical — access from an unusual location triggers additional authentication; (3) behavioral — access to resources the user doesn't normally access raises the risk score. The chapter distinguishes between low-risk elevation (re-prompt for password, second factor) and high-risk elevation (active confirmation from a peer via out-of-band request).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This multi-attribute, contextual approach to least privilege is the operational heart of ZT authorization. It's directly implemented in BeyondCorp's access tiers, in Okta's contextual access policies, and in every ZTNA product's device posture checks.

## Stakes

If device context binding is weak, credential theft still grants access — the device becomes just another attribute that can be spoofed. The strength of device binding (TPM, secure enclave, hardware-backed keys) is the practical limit on how much ZT least privilege actually improves security over traditional models.

## Disagreement

**Who disagrees:**

Traditional RBAC proponents would argue that multi-attribute privilege is just ABAC (Attribute-Based Access Control) and that ZT hasn't invented anything new — it's applying existing access control models in a network context. This is technically correct; the novelty is in making ABAC the default operating mode for network access decisions, not just application-level authorization.

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

The marriage of user identity and device identity into a single authorization decision is the most underappreciated insight in this chapter. Traditional networks treat "user logged into a device" and "device on the network" as two separate problems. ZT recognizes that a compromised credential on a trusted device and a valid credential on a compromised device are different threats requiring different responses — and that you can't distinguish them without binding user and device identity together. This is the argument that Chapter 3 (Network Agents) will develop in detail.
