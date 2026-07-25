---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-policy
  - topic/zt-app
  - topic/zt-implementation
  - topic/zt-cloud
claim_id: "gc-iam-policy.10"
statement: "Dynamic, tag-based targets are the policy model's most powerful feature — they bind security enforcement to business/DevOps processes"
confidence: "high"
confidence_rationale: "HIGH. Tag-based dynamic targets are already operational in service mesh systems (Istio's authorization policies use label-based selectors), cloud"
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Practice IAM Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-iam-policy.10: Dynamic, tag-based targets are the policy model's most powerful feature — they bind security enforcement to business/DevOps processes

**Source:** [[Garbis and Chapman — Practice IAM Policy]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

Dynamic targets "provide the ability to define and enforce access based on attributes which are unknown and unknowable until runtime." Tag-based targets like "department=Marketing" or "stage=test" enable access controls that automatically follow workloads through their lifecycle.

## Evidence

Two compelling examples: (1) "Systems tagged as department=Marketing" — the PEP resolves hosts by interrogating environment metadata, so new marketing servers automatically get the right access policies without manual intervention. (2) "Systems tagged as stage=test" coupled with DevOps CI/CD — "as a workload or service's stage is changed, its access controls will automatically follow." The authors explicitly note this can tie into containerized/microservices environments where multiple services share a host or IP — the policy model must distinguish services, not just hosts.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Tag-based dynamic targets are already operational in service mesh systems (Istio's authorization policies use label-based selectors), cloud IaaS (AWS security groups with tags), and CMDB-driven network segmentation. The authors are describing a proven pattern.

## Stakes

If tag-based targets work, ZT security becomes a byproduct of existing operational processes — DevOps teams get security without doing security work. If they don't work (because tag hygiene is poor, or the PEP can't resolve tags), ZT collapses back to static rules.

## Disagreement

**Who disagrees:**

No one disputes the value. The implementation challenge is that tag-based targets require the PEP to have real-time access to tag/label metadata — which imposes architectural requirements (PEP must be able to interrogate its environment, or the PDP must have complete visibility). Cloud-routed ZTNA models may struggle with on-premises tag resolution.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**
- [[policy-should-be-defined-in-terms-of-logical|Tags (department=Marketing, stage=test) are a concrete form of logical components — they replace network addressing with]]
- [[the-four-component-policy-model-subject-action-target-condition|Tag-based targets are a dynamic, business-aligned implementation of the Target component in the four-component model, bi]]

## Assessment

This is the most forward-looking claim in Ch17. The "stage=test" DevOps scenario shows ZT reaching its full potential: security policy that self-adjusts as code moves through the pipeline. The authors are describing an integration that most enterprises haven't achieved yet — but the path is clear.
