---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-implementation
  - topic/zt-network
  - topic/zt-cloud
  - topic/zt-segmentation
claim_id: "gb-ch9.2"
statement: "Flow enumeration is the hardest requirement and the highest-value one"
confidence: "high"
confidence_rationale: "VERY HIGH. This is validated by every real migration: Google's netflow analysis pipeline, PagerDuty's iptables role-to-IP mapping, NIST 800-207's"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch9.2: Flow enumeration is the hardest requirement and the highest-value one

**Source:** [[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"Without the list of expected network flows, zero trust systems are unable to highlight unexpected communications which need attention from administrators or should be denied." And critically: "deferring the effort to enumerate flows will ultimately result in a task list that is considered infeasible."

## Evidence

- Flow data should be the **source of truth** for access decisions — generate enforcement configuration from the flow database, not independently
- Capture the **intended use** of a flow along with policy details (e.g., "LB access — from LB hosts to web application")
- Prefer **narrowly defined flows** over broad access
- For flow discovery: physical networks use SPAN/mirror ports or TAP devices; virtualized networks use cloud-native flow logs (AWS VPC Flow Logs); endpoint-based discovery via software firewalls in log-only mode gives richer application context
- **Zone-by-zone migration**: leverage existing perimeter boundaries to build ZT on either side, then spread zone to zone — incremental, not big-bang

**Cross-reference — NIST 800-207 Ch7:**

NIST's Step 2 (Identify Assets) and Step 3 (Identify Key Processes) are the same exercise at higher abstraction. NIST categorizes assets as hardware, digital artifacts, and shadow IT; Gilman & Barth's flow enumeration is the network-level instantiation. Both agree: without the inventory, the Policy Engine will deny requests due to insufficient information.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This is validated by every real migration: Google's netflow analysis pipeline, PagerDuty's iptables role-to-IP mapping, NIST 800-207's Step 3 (identify key processes and evaluate risks). Flow enumeration is the gating function — you can't do ZT without it, and it's the hardest inventory problem.

## Stakes

If flow enumeration is impossible (too many flows, too much churn, insufficient tooling), ZT is impossible. Organizations that skip this step are doing ZT theater — they have identity-aware proxies but no ability to detect or deny unexpected lateral movement.

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
- [[the-zero-trust-discovery-workshop-is-the-critical|Flow enumeration is a core activity within the Zero Trust Discovery Workshop's data collection and analysis phase, makin]]
- [[the-shouldmust-list-is-zt-implementations-operational-checklist|Flow enumeration is a specific, critical item on the SHOULD/MUST operational checklist, identified as both the hardest a]]

## Assessment

_Not addressed separately in the source note._
