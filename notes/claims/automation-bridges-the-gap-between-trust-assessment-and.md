---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-implementation
  - topic/zt-maturity
claim_id: "go-ch3-5.6"
statement: "Automation bridges the gap between trust assessment and enforcement at scale — continuous, not occasional, evaluation"
confidence: "high"
confidence_rationale: 'HIGH in principle, MODERATE in specificity. The "automation is essential" claim is widely validated — no one disputes that manual ZT enforcement'
claim_type: "implementation"
source_note: "[[Green-Ortiz — Ch3-5 — Trust and Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch3-5.6: Automation bridges the gap between trust assessment and enforcement at scale — continuous, not occasional, evaluation

**Source:** [[Green-Ortiz — Ch3-5 — Trust and Policy]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

Automation is "a key focus area for organizations as they attempt to reduce complexity and increase productivity." The specific ZT value of automation is that it enables "constantly evaluating trust rather than the common implicit trust or single evaluation of trust at entry to the network." Automation turns trust assessment from a periodic check into a continuous process: "Automation assists an organization where detection within this network behavior platform can automatically cause the execution of changes to other security controls" — such as "firewall rule changes to prevent data exfiltration or a DNS security update to block identified suspect domains."

## Evidence

- Ch5 retail example: attacks that bypass NAC "often attempt to reside in a retail environment" and "have shown difficulty in both identifying the cause and scope of the attack. With a Zero Trust architecture focus on visibility, the time to identify and resolve these attacks is shortened."
- Ch5 policy orchestration: "It is recommended that an organization implement a solution that automates and orchestrates network security policy management on-premises and in the cloud."
- Ch5 PCI-DSS benefit: Automated documentation reduces the labor for Reports on Compliance (ROC) — "hundreds of employees and thousands of hours of labor" reduced through maintained, accurate policy data.
- Ch5 feedback loop: "Iterative feedback and consumption of outputs from other pillars within the Zero Trust architecture ensures that the policy continues to adapt to changes in the environment."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH in principle, MODERATE in specificity. The "automation is essential" claim is widely validated — no one disputes that manual ZT enforcement doesn't scale. But the specific automation mechanisms Green-Ortiz describes (ISE, Cisco Secure Network Analytics, policy orchestration tools) are vendor-specific, and the generic claim "use automation" is not particularly actionable.

## Stakes

Without automation, ZT reduces to a static set of policies that are checked at connection time — which is basically a more complex firewall. The continuous, adaptive nature of ZT — the property that makes it genuinely different — requires automation to be feasible at enterprise scale. The gap between "use automation" and a fully automated trust assessment-to-enforcement pipeline is enormous.

## Disagreement

**Who disagrees:**

Gilman & Barth's agent model embeds automation into the architecture itself — agents report trust signals, the trust engine computes scores, the control plane enforces. Green-Ortiz's approach layers automation on top of existing infrastructure. The former is architecturally cleaner; the latter is more realistic for brownfield deployments.

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

This connects back to the trust assessment pipeline in Claim 3. The pipeline (NAC → DNS → IPAM → endpoint database → classification → policy → enforcement) IS the automation specification for trust assessment. Green-Ortiz describes it as a sequence of data sources, but the real insight is that it must be automated — you can't do this manually for thousands of endpoints. The PCI-DSS ROC example is particularly valuable: it shows that automation pays for itself in compliance cost reduction, not just security improvement.
