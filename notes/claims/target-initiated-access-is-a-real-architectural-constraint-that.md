---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-architecture
  - topic/zt-implementation
claim_id: "gc-iam-policy.13"
statement: "Target-initiated access is a real architectural constraint that eliminates some ZT deployment models"
confidence: "medium"
confidence_rationale: "MODERATE-HIGH on the architectural constraint; MODERATE on the claim about cloud-routed models specifically — some cloud-routed ZTNA products have"
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Practice IAM Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-iam-policy.13: Target-initiated access is a real architectural constraint that eliminates some ZT deployment models

**Source:** [[Garbis and Chapman — Practice IAM Policy]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"Some applications and networks utilize a reverse type of communications, which means that our Zero Trust system must also support it." The authors call this "target-initiated" access — the policy target initiates network traffic toward the subject.

## Evidence

Two concrete examples: (1) VOIP softphones where calls are initiated from the VOIP server to the user's device, and (2) a patching server that must periodically connect to a remote BI server. The authors note that "solutions based on the cloud-routed deployment model typically struggle to support this" while enclave-based and resource-based models handle it naturally.

## Confidence

**Rating:** MEDIUM
**Rationale:** MODERATE-HIGH on the architectural constraint; MODERATE on the claim about cloud-routed models specifically — some cloud-routed ZTNA products have added reverse proxy capabilities since the book's 2021 publication.

## Stakes

If an organization has significant target-initiated traffic patterns (VOIP, remote desktop support, CI/CD deployments, monitoring systems), cloud-routed ZTNA is a non-starter. The deployment model choice is constrained by traffic patterns, not just security requirements.

## Disagreement

**Who disagrees:**

Cloud-routed ZTNA vendors (Zscaler, Netskope) have evolved since 2021 and now offer some target-initiated capabilities. The book's claim may be time-bound.

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

The target-initiated scenario is an important architectural litmus test. Few ZT evaluation frameworks ask "does your traffic ever flow in the reverse direction?" — but they should. Combined with the SPA discussion, the authors are clearly signaling a preference for direct-connection models (enclave-based, resource-based) over cloud-routed ones, even if they don't state it explicitly.
