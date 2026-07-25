---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-migration
  - topic/zt-governance
claim_id: "gc-scenarios.4"
statement: "Common roadblocks — IAM immaturity, political resistance, regulatory constraints, resource visibility gaps, and analysis paralysis — are predictable, documented, and surmountable"
confidence: "high"
confidence_rationale: "HIGH. These roadblocks are empirically validated by practitioner experience and match patterns observed in other large-scale security transformations"
claim_type: "migration"
source_note: "[[Garbis and Chapman — Scenarios and Conclusion]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-scenarios.4: Common roadblocks — IAM immaturity, political resistance, regulatory constraints, resource visibility gaps, and analysis paralysis — are predictable, documented, and surmountable

**Source:** [[Garbis and Chapman — Scenarios and Conclusion]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"Enterprise IT and security is hard and complex, and some Zero Trust projects will fail. This is unfortunate, but true. The good news is that most will be a success." The five roadblocks can be mitigated with specific countermeasures.

## Evidence

- **IAM Immaturity**: The "our directory is a mess" problem. Counter: Zero Trust doesn't require perfect IAM — it can be a "catalyst for improved maturity and data integrity in your IAM system, even if it's just for a narrow slice." ZT systems consume IAM attributes; you control how many attributes inform policy. Start narrow.

- **Political Resistance**: "People who impose barriers to change, despite the clear benefits." Four counterstrategies: (1) education on concrete benefits, (2) strong executive sponsorship breaking down barriers, (3) line-of-business champions whose projects demonstrate revenue or cost benefits, (4) finding allies within opposing organizations — "Zero Trust systems are inherently integratable, there may be some creative ways to tie into and augment the existing infrastructure, avoiding the perception that you're going to be 'ripping and replacing.'"

- **Regulatory/Compliance Constraints**: Regulations lag behind technology. Counter: "be proactive about engaging with your third-party/external auditor... collaborate with them and educate them, to ensure that they understand your trajectory."

- **Discovery and Visibility of Resources**: "I don't know who is accessing what, how can I control them?" Two valid approaches: (1) the BeyondCorp/PagerDuty observational approach — deploy broadly, collect network data, ensure no productivity interruption, (2) the SDP incremental approach — onboard users and groups incrementally, start with coarser policies, tighten over time. "Don't fall into the trap of assuming that you need perfect visibility of every connection and every data flow before you can begin."

- **Analysis Paralysis**: "Attempting to fully understand, identify risks, and scope out any new technology or approach... has a too-common downside of indefinitely delaying any decision or action." Counter: "collaborate with all relevant stakeholders, and approach their initiative from the perspective of how they can get Zero Trust into pilot or production as quickly as possible, even if it's initially limited in scope." Run ZT in parallel with existing access methods until confidence is high; only then decommission the old approach.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These roadblocks are empirically validated by practitioner experience and match patterns observed in other large-scale security transformations (cloud migration, IAM modernization, SDN adoption).

## Stakes

If these roadblocks are treated as insurmountable, organizations never start. If they're dismissed as trivial, projects fail on non-technical grounds. The authors' approach — naming the roadblocks, providing specific countermeasures, and acknowledging that "perfection is an unattainable goal, but dramatic improvements in security and efficiency are attainable and realistic" — is the right balance.

## Disagreement

**Who disagrees:**

NIST 800-207 doesn't address organizational roadblocks (it's a technical architecture). CISA's ZTMM acknowledges that maturity progression faces organizational challenges but doesn't provide specific countermeasures. The DoD ZT Strategy addresses acquisition and funding challenges specific to the defense ecosystem. Garbis & Chapman's roadblock taxonomy is provider-agnostic and broadly applicable.

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

The roadblock section is where the authors' practitioner experience most clearly shows. The guidance is specific ("run ZT in parallel with existing access methods") rather than abstract ("manage change carefully"). The IAM immaturity counter — ZT as catalyst rather than consumer of perfect IAM — is particularly important because it removes the most common excuse for not starting. The political resistance section is refreshingly honest about organizational reality in a way most technical ZT literature avoids.
