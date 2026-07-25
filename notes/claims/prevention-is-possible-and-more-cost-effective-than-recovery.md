---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-threats
claim_id: "finney-ch1-3.2"
statement: "Prevention is possible and more cost-effective than recovery"
confidence: "medium"
confidence_rationale: 'MEDIUM. The "prevention is cheaper than cure" claim is intuitively appealing and has supporting evidence from breach cost studies (IBM/Ponemon'
claim_type: "implementation"
source_note: "[[Finney — Ch1-3 — The Zero Trust Story]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch1-3.2: Prevention is possible and more cost-effective than recovery

**Source:** [[Finney — Ch1-3 — The Zero Trust Story]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"The primary goal of Zero Trust is to prevent breaches. Prevention is possible. In fact, it's more cost effective from a business perspective to prevent a breach than it is to attempt to recover from a breach, pay a ransom, and deal with the costs of downtime or lost customers." The CEO Olivia Reynolds frames this with: "An ounce of prevention is worth a pound of cure."

## Evidence

The MarchFit breach response is expensive: free month of credit to all subscribers, unknown recovery costs, customer "melt" concerns, potential lawsuits. The company has backups, a Business Continuity Plan, cyber risk insurance, and breach response contracts — all of which let them *recover* without paying ransom, but none of which *prevented* the breach. The cost of the reactive response is portrayed as vastly exceeding what prevention would have cost.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. The "prevention is cheaper than cure" claim is intuitively appealing and has supporting evidence from breach cost studies (IBM/Ponemon reports consistently find higher costs for breaches with longer dwell times), but Finney provides no quantitative evidence in these chapters. The narrative *dramatizes* the cost of breach but doesn't *calculate* the cost of prevention. This is a rhetorical claim, not an empirical one.

## Stakes

If prevention isn't actually cheaper (if ZT implementation costs exceed breach costs for most organizations), the business case collapses. This is the argument security leaders most need to win, and Finney gives them narrative ammunition but no numbers.

## Disagreement

**Who disagrees:**

The "assume breach" school (which includes many ZT practitioners) argues that prevention is impossible and ZT should focus on containment and detection. Finney's response: prevention *is* possible if you eliminate implicit trust, but this is a logical argument, not an empirical demonstration.

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

Finney is making a strategic claim dressed as an economic one. The real argument isn't "ZT costs less than breach recovery" but "ZT is the only strategy that gives you a measurable path to reducing breach probability." The cost argument is a sales pitch for executives; the strategic argument is the substance. Security leaders should use the cost framing with CFOs but not mistake it for a TCO analysis.
