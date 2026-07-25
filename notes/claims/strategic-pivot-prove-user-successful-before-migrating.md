---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/beyondcorp
  - topic/zt-implementation
  - topic/zt-architecture
claim_id: "beyondcorp.7"
statement: 'The strategic pivot from "prove the user will be successful before migrating" (opt-in) to "assume the user will be successful and migrate" (opt-out) was essential for reaching full coverage — without it, the long tail of noncompliant applications would have blocked migration indefinitely.'
confidence: "high"
confidence_rationale: 'HIGH — This is a documented strategic pivot with specific operational mechanics. The "temporary exceptions only with concrete remediation plan"'
claim_type: "implementation"
source_note: "[[BeyondCorp — Research Papers]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondcorp.7: The strategic pivot from "prove the user will be successful before migrating" (opt-in) to "assume the user will be successful and migrate" (opt-out) was essential for reaching full coverage — without it, the long tail of noncompliant applications would have blocked migration indefinitely.

**Source:** [[BeyondCorp — Research Papers]] — Google, *BeyondCorp Research Papers*, 2014-2020

## The Claim

Phase 1 — newly provisioned, unanalyzed devices defaulted to privileged network; users of noncompliant apps couldn't be migrated; risk that unmigrated users could create NEW noncompliant applications. Phase 2 — after reducing exceptions by remediating high-volume use cases, all devices defaulted to MNP site-by-site, with exceptions granted only to users in job functions with unremediated applications. This policy shift from opt-in to opt-out was essential.

## Evidence

Difficult use cases (the long tail): NFS/CIFS file servers required major project to move home directories to local disk with secure cloud backup, replace NFS with Google Drive; CAD editors deeply dependent on NFS required special solutions; thick client applications with proprietary protocols; Java RMI and direct socket connections; license servers using non-HTTP sockets; some HTTP applications not designed to present client certificates; load balancer logic incompatible with Access Proxy. Temporary exceptions policy: for critical framework services without compliant solutions, temporarily opened access — but only when a concrete plan for compliant solution existed, preventing exceptions from becoming permanent. Scaling support: empowered tech support (BeyondCorp champions), self-service infrastructure (automated emails, web portal for delay requests, dedicated error-messaging application, internal discussion list), internal publicity campaign (laptop stickers, visible articles). Phased rollout: small-scale pilot geographically close to project team → progressive expansion to locations with local experts → eventual expansion to risky workflows and distant sites. "Tech support load decreased as rollout size and affected workflows increased" — counterintuitive but the system matured faster than the user base grew.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — This is a documented strategic pivot with specific operational mechanics. The "temporary exceptions only with concrete remediation plan" policy is a specific implementation of the broader ZT principle of avoiding permanent exceptions.

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
