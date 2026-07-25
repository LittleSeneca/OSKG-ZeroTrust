---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-definition
  - topic/zt-threats
claim_id: "gc-ch1-3.1"
statement: "Traditional enterprise security is structurally broken — not merely insufficient, but actively perpetuating vulnerability."
confidence: "high"
confidence_rationale: "HIGH. The factual premise is verified by every breach report and penetration test. The \"you'd never choose to design a system like this\" framing is"
claim_type: "definitional"
source_note: "[[Garbis and Chapman — Ch1-3 — Introduction and Architecture]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-ch1-3.1: Traditional enterprise security is structurally broken — not merely insufficient, but actively perpetuating vulnerability.

**Source:** [[Garbis and Chapman — Ch1-3 — Introduction and Architecture]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"By not enforcing the principle of least privilege at both the network and application levels, organizations are leaving themselves incredibly vulnerable to attacks. This is true both for internal networks and for public Internet-facing remote access services such as VPNs... Given today's threat landscape, you'd never choose to design a system like this. And yet, traditional security and networking systems, which remain in widespread use, continue to perpetuate this model."

## Evidence

The authors observe that enterprise networks grant far too much access by default — internally (anyone can reach any server) and externally (VPNs expose entry points to the entire internet). This is asserted as self-evident to practitioners rather than proven through data. The book's later chapters provide architectural evidence.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The factual premise is verified by every breach report and penetration test. The "you'd never choose to design a system like this" framing is rhetorically powerful and diagnostically accurate: enterprise networks evolved into their current state through accretion and convenience, not deliberate security design.

## Stakes

If this claim is wrong, ZT adoption is unnecessary effort. If right, every organization operating a traditional perimeter model is structurally vulnerable regardless of how well they configure their firewalls.

## Disagreement

**Who disagrees:**

The claim is not seriously disputed. Perimeter-defense vendors have shifted from defending the perimeter model to offering ZT-adjacent products. The debate is about *how* to fix the problem, not whether it exists.

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

The structural diagnosis is sound. The innovation is in stating it plainly — not "your firewall rules need tuning" but "the model itself is the vulnerability." This is a stronger claim than NIST's more diplomatic phrasing (SP 800-207 says perimeter security has been "shown to be insufficient") and closer to Kindervag's original "no more chewy centers" argument.
