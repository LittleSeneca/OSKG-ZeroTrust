---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-implementation
  - topic/zt-governance
  - topic/zt-trust
claim_id: "finney-ch1-3.11"
statement: "Incident management without problem management creates a firefighting culture"
confidence: "high"
confidence_rationale: "HIGH. The incident/problem management distinction comes from ITIL and is well-established in IT service management. Finney's contribution is applying"
claim_type: "implementation"
source_note: "[[Finney — Ch1-3 — The Zero Trust Story]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch1-3.11: Incident management without problem management creates a firefighting culture

**Source:** [[Finney — Ch1-3 — The Zero Trust Story]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"There's a big difference between incident management and problem management. Incident management is all about the processes you use to respond to incidents in real time. Cybersecurity teams are often built around having mature incident response processes and plans to be prepared when bad things happen. Problem management is focused on finding the root cause of why whole categories of incidents occur and preventing them from happening. If an organization focuses exclusively on incident management without addressing the underlying source of the issues, the risk is that they'll be stuck in firefighting mode."

## Evidence

The security guards know how to reboot frozen cameras (incident management) but never investigate *why* cameras keep freezing (problem management). "A team can become desensitized to alarms and bad things can slip through. The reason that Zero Trust is successful is that it addresses the underlying source of incidents — trust."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The incident/problem management distinction comes from ITIL and is well-established in IT service management. Finney's contribution is applying it to security strategy: ZT is *problem management* for the category of incidents caused by implicit trust.

## Stakes

If organizations treat ZT as another incident response tool (another layer in defense in depth), they miss the point. ZT is a *structural* fix — it addresses the root cause (trust assumptions) rather than the symptoms (breaches).

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[prevention-is-possible-and-more-cost-effective-than-recovery|Problem management (investigating root causes) is the operational mechanism for prevention, making incident-without-prob]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

This is the most important claim for understanding Finney's overall argument. ZT is not "better incident response." It's not "more detection." It's fundamentally rearchitecting the system so the trust vulnerabilities that enable incidents don't exist. This is why Finney insists ZT is a *strategy* — strategies address root causes; tactics address symptoms. The incident/problem distinction makes this argument precise.
