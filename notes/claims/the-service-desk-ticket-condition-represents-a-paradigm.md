---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-governance
  - topic/zt-access-mgmt
claim_id: "gc-iam-policy.11"
statement: "The service desk ticket condition represents a paradigm shift — ZT can make business process compliance a runtime network enforcement, not an audit afterthought"
confidence: "high"
confidence_rationale: "HIGH on the concept. MODERATE on current adoption — integrating ticketing systems with ZT policy engines requires API maturity on both sides. PAM"
claim_type: "governance"
source_note: "[[Garbis and Chapman — Practice IAM Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-iam-policy.11: The service desk ticket condition represents a paradigm shift — ZT can make business process compliance a runtime network enforcement, not an audit afterthought

**Source:** [[Garbis and Chapman — Practice IAM Policy]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"By making access — enforced by the network or application — a byproduct of a properly executed business process, it guarantees that users will follow the process." The service desk ticket condition "eliminates the need for admins and their devices to have broad and continuous network access, while keeping them fully productive."

## Evidence

The sysadmin access policy (Table 17-3) uses a condition that requires "a service desk ticket in an 'open' state, and which specifies the hostname or IP address being accessed." Once the ticket is closed, admin access is revoked. This is a Just-In-Time (JIT) access model enforced at the network layer.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the concept. MODERATE on current adoption — integrating ticketing systems with ZT policy engines requires API maturity on both sides. PAM vendors (CyberArk, BeyondTrust) have pioneered similar patterns.

## Stakes

If ZT can bind to business processes this way, it transforms from a security tool into a compliance automation platform. Admin access becomes auditable-by-design because the network physically prevents access without a ticket. This is a stronger guarantee than any log-based audit.

## Disagreement

**Who disagrees:**

The zero-standing-privilege model in PAM literature achieves the same goal through credential vaulting and JIT provisioning rather than network-level enforcement. Both approaches are valid; network-level enforcement has the advantage of being application-agnostic.

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

This condition type is the most compelling example of ZT's potential beyond network security. It shows ZT as a business process enforcement mechanism. The challenge is the integration surface — every condition type (ticketing, SIEM risk level, maintenance window) requires a distinct API integration. The ZT platform's extensibility determines how many of these conditions are actually achievable.
