---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-monitoring
  - topic/zt-governance
  - topic/zt-implementation
claim_id: "finney-ch4-7.10"
statement: "The SOC's value is measured by false positive reduction and dwell time containment, not by ticket counts or response SLAs."
confidence: "high"
confidence_rationale: "HIGH. The shift from activity-based metrics (tickets, response times) to outcome-based metrics (false positive reduction, dwell time, MITRE stage"
claim_type: "implementation"
source_note: "[[Finney — Ch4-7 — Building the ZT Strategy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch4-7.10: The SOC's value is measured by false positive reduction and dwell time containment, not by ticket counts or response SLAs.

**Source:** [[Finney — Ch4-7 — Building the ZT Strategy]] — George Finney, *Project Zero Trust*, 2022

## The Claim

Harmony: "We don't want reporting that says you responded to tickets within five minutes or how many cases you opened. That doesn't tell us that we're more secure or more effective. If we're going to have a Zero Trust SOC, we want to report on how many false positives we've reduced."

Chris elaborates: "If we can eliminate 99 percent of all the false positives, then what's left will be much easier to investigate and act upon." He adds that the SOC must have "skin in the game" — a feedback loop where SOC findings drive control improvements, which in turn reduce noise, which in turn improves SOC effectiveness.

## Evidence

The metrics Harmony wants:
1. False positives reduced (month-over-month and year-over-year, accounting for seasonality)
2. New rules added to runbook and applied in production
3. Attacker progression through MITRE ATT&CK framework stages — are they being disrupted before command and control?
4. Dwell time reduction (the duration an attacker is inside before detection/containment)

Chris connects this to the ZT methodology: "We can align our controls around your defined protect surfaces. This will help us provide better monitoring, but it will also allow us to provide better feedback on what is slipping through your controls. Or in Zero Trust terminology, we can help look for opportunities to remove trust from these different protect surfaces."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The shift from activity-based metrics (tickets, response times) to outcome-based metrics (false positive reduction, dwell time, MITRE stage disruption) is a well-established best practice in SOC management but rarely tied explicitly to ZT.

## Stakes

Vanity metrics create complacency. If the SOC reports "99.9% of tickets closed within SLA," leadership assumes security is working — even if those tickets represent noise while real attacks go undetected. Outcome-based metrics aligned to ZT protect surfaces force accountability.

## Disagreement

**Who disagrees:**

Some argue that outcome-based metrics are harder to measure consistently and that SLA-based metrics provide necessary operational accountability. The counterargument (implicit in Finney's narrative) is that both are needed — SLAs for operational discipline, outcome metrics for strategic effectiveness.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[soc-integration-should-be-pursued-early-in-the|Measuring SOC value by false positive reduction and dwell time (rather than ticket counts) provides concrete metrics to]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

This is the most practical material in Ch7. The specific metrics Harmony requests could serve as a template for any organization's SOC reporting redesign. The key innovation is making MITRE ATT&CK stage progression a ZT metric — if you're seeing attackers reach later stages (credential access, lateral movement, command and control), your ZT controls aren't working, regardless of how many tickets were closed.
