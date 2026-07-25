---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-identity
  - topic/zt-access-mgmt
  - topic/zt-network
claim_id: "gc-iam-policy.6"
statement: "The three-layer authorization model reveals why ZT is fundamentally about adding network-level enforcement to identity-driven access control"
confidence: "high"
confidence_rationale: "HIGH. This three-layer model provides the clearest explanation in ZT literature of _why_ identity matters for network security — it's not just about"
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Practice IAM Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-iam-policy.6: The three-layer authorization model reveals why ZT is fundamentally about adding network-level enforcement to identity-driven access control

**Source:** [[Garbis and Chapman — Practice IAM Policy]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"Without Zero Trust, security or networking teams typically have only been able to enforce access control in a static, coarse-grained fashion... With Zero Trust, the network layer can enforce fine-grained access controls, based on roles and attributes, which, in traditional security systems, are only available and effective at the application layer."

## Evidence

Figure 5-3 depicts three access control layers: (1) **Application-level authorization** — what actions can the user perform within the app, enforced by the application itself, governed by identity governance processes. (2) **Application account-level access** — does the user have an account, enforced via authentication (SSO, PAM). (3) **Network-level access control** — without ZT: coarse-grained VLANs, VPN full network access; with ZT: fine-grained policy based on roles and attributes. The authors argue that "network infrastructure has a very impoverished authorization model compared to applications, and Zero Trust is a way to replace that with a much richer policy model."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This three-layer model provides the clearest explanation in ZT literature of _why_ identity matters for network security — it's not just about authentication, it's about bringing application-grade authorization logic to the network.

## Stakes

If network-level enforcement can match application-level sophistication, the entire perimeter model (firewall rules based on IP/port) becomes obsolete. ZT is essentially the externalization of network authorization.

## Disagreement

**Who disagrees:**

NIST 800-207's logical component model implies this layering but doesn't articulate it as clearly. The NSA pillars treat identity and network as separate pillars rather than showing how identity attributes drive network enforcement.

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

This is the book's single most elegant conceptual contribution. The three-layer model makes ZT's value proposition concrete: we're not just adding another security layer, we're fixing the fact that network access control has been stuck at the IP/port level for 30 years while application authorization has become richly attribute-based. ZT bridges this gap.
