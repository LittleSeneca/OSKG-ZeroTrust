---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-migration
  - topic/zt-monitoring
  - topic/zt-implementation
  - topic/zt-network
claim_id: "gb-ch9.6"
statement: "Log-then-enforce is THE migration procedure — validated by two independent case studies"
confidence: "high"
confidence_rationale: "VERY HIGH. This is the most validated procedure in ZT literature — two independent $1B+ organizations converged on the same approach. NIST 800-207"
claim_type: "migration"
source_note: "[[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch9.6: Log-then-enforce is THE migration procedure — validated by two independent case studies

**Source:** [[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

1. Deploy proposed policy in logging-only fashion
2. Collect production traffic over a sufficient period
3. Investigate traffic that would be rejected by the proposed policy
4. Enforce the proposed policy
5. Repeat until all desired policy is deployed
6. Enable a default-deny policy when all expected flows are captured

## Evidence

Both Google and PagerDuty independently converged on this pattern:

| Organization | Domain | Log-Then-Enforce Implementation |
|-------------|--------|-------------------------------|
| **Google BeyondCorp** | Client-to-server | Traffic analysis pipeline: sampled netflow from every switch → compare against canonical ACL between unprivileged and privileged networks → iteratively make non-passing traffic work in BeyondCorp. Unprivileged network simulator on all devices: logging mode → enforcement mode → 30-day successful enforcement → device assigned to unprivileged network |
| **PagerDuty** | Server-to-server | Firewall: deploy rules as LOG-only → classify flows → reduce logged traffic → reconfigure to DROP non-whitelisted traffic. IPsec: deploy policies in *none* state → transition small portions to *use* state → reconfigure to *required* state. Phased approach minimized time in risky intermediate state |

**Google's specific metrics:**

>99.9% eligible traffic for 30 days in logging mode → enforcement mode; >99.99% eligible traffic → enforcement; 30 days successful enforcement → unprivileged network assignment. Phased migration by job function/workflow/location.

**Cross-reference — NIST 800-207 Ch7:**

NIST's Step 6 (Initial Deployment and Monitoring) is the formalization: "few policy sets are complete on the first iteration," grant access for most requests initially, log and trace all connections, compare actual patterns against developed policy. Same procedure, different vocabulary.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This is the most validated procedure in ZT literature — two independent $1B+ organizations converged on the same approach. NIST 800-207 Ch7 §7.3.6 explicitly recommends "reporting-only mode" with the same logic.

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
- [[the-biggest-mistake-in-zt-implementation-is-rushing|The log-then-enforce pattern, validated by two independent case studies, provides the empirical evidence for why rushing]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
