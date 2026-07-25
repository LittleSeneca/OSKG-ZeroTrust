---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-governance
  - topic/zt-identity
claim_id: "finney-ch4-7.6"
statement: "Identity governance needs a cross-functional stakeholder group, and GDPR/privacy assessments can jump-start the data flow mapping that ZT requires."
confidence: "high"
confidence_rationale: "HIGH for the governance model. The GDPR leverage insight is one of the most practical in the book — many organizations have done privacy assessments"
claim_type: "governance"
source_note: "[[Finney — Ch4-7 — Building the ZT Strategy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch4-7.6: Identity governance needs a cross-functional stakeholder group, and GDPR/privacy assessments can jump-start the data flow mapping that ZT requires.

**Source:** [[Finney — Ch4-7 — Building the ZT Strategy]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"The goal of identity is to ensure uniqueness of every human or non-human in our environment... The best way to ensure we're employing least privilege across all our systems is to start with the data, what services are connected to the data, and then decide who needs access to it."

## Evidence

The Identity Governance group includes Noor (CISO), Kofi (Legal), Kim Self (Compliance), Vic (Sales, soon-to-be CEO), Mia (HR), and April (Marketing/Communications). Dylan presents the ZT identity strategy to this group and gets specific policy commitments:
- MFA required for all applications by default before rollout
- Daily reauthentication, with more frequent triggers for high-value transactions (payments, code deployments)
- Role cleanup tied to HR job descriptions, not titles
- Quarterly user access reviews with increasing frequency over time
- Orphaned account detection and remediation

The chapter also shows that MarchFit's GDPR data mapping project (hundreds of rows of data flows and role-based access) had already done the heavy lifting for the "map transaction flows" step — "probably took about a year off that time frame."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH for the governance model. The GDPR leverage insight is one of the most practical in the book — many organizations have done privacy assessments without realizing they've already completed the hardest part of ZT data flow mapping.

## Stakes

Without a governance group, identity decisions are made in isolation by IT, leading to permission bloat, orphaned accounts, and resistance from business units. The cross-functional model creates shared ownership.

## Disagreement

**Who disagrees:**

The IDSA framework (Identity-Defined Security Alliance) pushes the "seven components" model (Identity, Device, Network, Compute, Application, Storage, Data) as a more comprehensive reference architecture. The chapter presents this as complementary.

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

The Identity Governance group is the most underappreciated element of ZT strategy. Technical ZT implementations fail not because the technology doesn't work but because no one owns the identity life cycle end-to-end. Finney embeds this governance lesson in the narrative rather than stating it as a principle — the group meeting where Brent brings a Bundt cake to celebrate completing the user access review workflow is both humanizing and instructive: ZT governance requires sustained, cross-functional commitment, and celebrating wins builds momentum.
