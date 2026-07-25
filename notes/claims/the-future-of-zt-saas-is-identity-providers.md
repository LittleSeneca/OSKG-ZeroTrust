---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-identity
  - topic/zt-authentication
  - topic/zt-cloud
claim_id: "gc-cloud.6"
statement: "The future of ZT + SaaS is identity providers as authorization centers, not just authentication points"
confidence: "medium"
confidence_rationale: "MODERATE. This is a prediction, not an evidence-based claim. Some elements have materialized: Microsoft's Continuous Access Evaluation (CAE) and"
claim_type: "implementation"
source_note: "[[Garbis and Chapman — Cloud IaaS SaaS]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-cloud.6: The future of ZT + SaaS is identity providers as authorization centers, not just authentication points

**Source:** [[Garbis and Chapman — Cloud IaaS SaaS]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"We believe that identity providers will not just serve as authoritative directories and authentication points but as 'centers of gravity' for user access to web apps, and for access control models." The future includes: JIT access provisioning via SCIM, a standard for communicating authenticated identity context to SaaS applications, and SaaS apps that are "Zero Trust-aware" — consuming external authorization signals.

## Evidence

The authors acknowledge this is forward-looking. Current IdP access portals provide only authentication + launchpad, not authorization. SCIM is the first step toward JIT provisioning. XACML failed to achieve adoption because "applications will never fully externalize their authorization." The opportunity is narrower: a commonly accepted way to communicate *trusted identity context* (authentication strength, device posture, session risk) to SaaS apps for consumption in their internal authorization models.

## Confidence

**Rating:** MEDIUM
**Rationale:** MODERATE. This is a prediction, not an evidence-based claim. Some elements have materialized: Microsoft's Continuous Access Evaluation (CAE) and Entra ID Conditional Access, Okta's Risk-Based Authentication, and the emerging CAEP standard. But full authorization context propagation remains aspirational. SCIM adoption for JIT is growing but not ubiquitous.

## Stakes

If IdPs remain authentication-only, ZT for SaaS is limited to access control at the network layer (IP allowlisting) and the gap between authentication and authorization stays unfilled. If IdPs become authorization hubs, the identity provider becomes the single most critical security component in the enterprise — a concentration of risk that demands extraordinary protection.

## Disagreement

**Who disagrees:**

The "authorization belongs in the application" school argues that only the application knows its data model and business logic well enough to make authorization decisions. The "authorization as code" school (OPA, Cedar, Google Zanzibar) argues that authorization logic should be externalized but owned by application teams, not centralized in the IdP. Both are partly correct — the likely future is a distribution of authorization logic across IdP (coarse access), policy engine (context evaluation), and application (fine-grained, data-level decisions).

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

This is a thoughtful prediction that has aged well. The trend toward identity-centered security architecture has accelerated, with Okta, Microsoft, and Ping all positioning themselves as more than authentication providers. The specific mechanism (SCIM + some authorization standard) is less important than the architectural direction: IdPs are becoming the control plane for access decisions, even if enforcement remains distributed.
