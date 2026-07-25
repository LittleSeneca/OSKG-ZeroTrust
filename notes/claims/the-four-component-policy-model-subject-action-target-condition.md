---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-policy
  - topic/zt-architecture
  - topic/zt-implementation
  - topic/zt-network
claim_id: "gc-iam-policy.9"
statement: "The four-component policy model (Subject → Action → Target + Condition) is the universal grammar of Zero Trust access control"
confidence: "high"
confidence_rationale: "HIGH. This four-component model maps cleanly to NIST 800-207's trust algorithm inputs, to the PEP/PDP enforcement split, and to ABAC (Attribute-Based"
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Practice IAM Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-iam-policy.9: The four-component policy model (Subject → Action → Target + Condition) is the universal grammar of Zero Trust access control

**Source:** [[Garbis and Chapman — Practice IAM Policy]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"Policies are the structures created by organizations to define which identities are permitted to get access to which resources, under which circumstances." The model has four components: Subject Criteria (who the policy applies to), Action (what they can do), Target (what they can act upon), and Condition (the circumstances under which access is permitted).

## Evidence

The model is presented as a logical structure that "actual Zero Trust implementations may well structure their policy model differently, but should contain these elements." Multiple concrete examples are provided: Subject Criteria ranging from broad ("All employees") to narrow ("Users in group Marketing, assigned to project Bruin, using Windows devices"), Actions spanning network (TCP 443, RDP, DNS) and application (URL access, SSH commands, data classification), Targets from static (IP, hostname, subnet) to dynamic (tags: "department=Marketing", "stage=test"), Conditions including time-of-day, MFA recency, device posture, endpoint scan status, and service desk ticket state.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This four-component model maps cleanly to NIST 800-207's trust algorithm inputs, to the PEP/PDP enforcement split, and to ABAC (Attribute-Based Access Control) theory. It's abstract enough to be universal and concrete enough to be actionable.

## Stakes

If the policy model is the right decomposition, ZT platform evaluation becomes straightforward: can this platform express Subject, Action, Target, and Condition independently? If not, it's incomplete. The model also reveals that many ZTNA products only support a subset — e.g., hostname targets and group-based subjects, but no dynamic tag-based targets.

## Disagreement

**Who disagrees:**

NIST 800-207's trust algorithm uses a criteria-based vs. score-based distinction that the authors acknowledge but don't fully adopt. Istio's authorization model uses source principals, operations, and conditions but collapses subject+together differently.

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

The four-component model is rigorous enough to serve as a vendor evaluation framework. The distinction between Subject Criteria (evaluated by PDP at session establishment) and Conditions (evaluated by PEP at access time) is particularly useful — it turns a vague "dynamic policy" into two concrete enforcement points with different attribute refresh rates.
