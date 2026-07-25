---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-identity
  - topic/zt-encryption
  - topic/zt-implementation
  - topic/zt-definition
claim_id: "gb-ch2.2"
statement: "Private PKI is the non-negotiable bedrock of ZT identity"
confidence: "high"
confidence_rationale: "HIGH. This has been validated by every major ZT deployment. Google's BeyondCorp runs its own CA. Service mesh implementations (Istio, Linkerd) all"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch2 — Managing Trust]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch2.2: Private PKI is the non-negotiable bedrock of ZT identity

**Source:** [[Gilman and Barth — Ch2 — Managing Trust]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"All zero trust networks rely on PKI to prove identity throughout the network. As such, it acts as the bedrock of identity authentication for the majority of operations." Private PKI is strongly preferred over public PKI for three reasons: (1) cost at scale — a ZT network has many certificates and public CAs charge per signing; (2) trust — "any one of these [public] CAs can cut certificates that your network trusts," creating a multi-jurisdictional trust problem; (3) flexibility — public CAs restrict certificate metadata, but ZT often needs site-specific metadata like roles or user IDs embedded in certificates.

## Evidence

The authors enumerate the entities authenticated by PKI (devices, users, applications) and argue that the sheer number of certificates demands automation — "if humans are required in order to process certificate signing requests, the procedure will be applied sparingly, weakening the overall system." The private-vs-public analysis is practical: public PKI is "strictly better than none" but a stepping stone, not the destination.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This has been validated by every major ZT deployment. Google's BeyondCorp runs its own CA. Service mesh implementations (Istio, Linkerd) all use private PKI. The "automation or death" insight — that manual certificate processing leads to sparse issuance and weak identity — is a hard-won operational truth.

## Stakes

If PKI is the bedrock, PKI failures are catastrophic. The CA's private key is the skeleton key to the entire network. The authors acknowledge this — "the CA must be protected at all costs, since its subversion would be catastrophic." This makes PKI security the single most important operational concern in a ZT deployment.

## Disagreement

**Who disagrees:**

Some cloud-native approaches argue that workload identity (SPIFFE/SPIRE) can replace traditional PKI in some contexts. Managed PKI services (AWS Private CA, Azure Key Vault) argue they solve the automation problem without requiring in-house PKI expertise. But these are implementation details — the underlying principle (private, automated, cryptographically-verified identity) is universal.

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

This chapter correctly identifies PKI as the ZT identity substrate but understates the operational complexity of running a private CA at scale. Certificate rotation, revocation, and cross-datacenter CA trust are hard problems that the book defers to Chapter 5. The "private PKI is better than public PKI" argument is correct but incomplete — the real question is whether your team has the expertise to operate a private CA securely, and the honest answer for many organizations is "no." Cloud-managed PKI may be the pragmatic middle path.
