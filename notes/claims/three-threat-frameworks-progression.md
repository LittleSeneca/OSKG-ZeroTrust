---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-threats
  - topic/zt-network
  - topic/zt-implementation
claim_id: "nist207-ch5.8"
statement: "The three major ZT threat frameworks — NIST 800-207, NSA Embracing ZT, and Gilman & Barth — form a progression from architectural taxonomy through operational threat model to engineering-level adversarial analysis, and together cover threats from implementation detail through architecture to operational philosophy."
confidence: "medium"
confidence_rationale: "MEDIUM. The synthesis is this note's analytical claim. The progression pattern is visible in the sources but NIST doesn't make this argument itself."
claim_type: "threat"
source_note: "[[NIST 800-207 — Ch5 — Threats]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch5.8: The three major ZT threat frameworks — NIST 800-207, NSA Embracing ZT, and Gilman & Barth — form a progression from architectural taxonomy through operational threat model to engineering-level adversarial analysis, and together cover threats from implementation detail through architecture to operational philosophy.

**Source:** [[NIST 800-207 — Ch5 — Threats]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

The chapter's synthesis is an analytical claim by this note's author rather than NIST's, synthesizing the three sources.

## Evidence

| Threat Category | NIST 800-207 (2020) | NSA Embracing ZT (2021) | Gilman & Barth (2017) |
|---|---|---|---|
| **Decision process subversion** | §5.1 — PE/PA compromise | Implicit in "assume breach" | Control plane security (Ch10) |
| **DoS / disruption** | §5.2 — DoS against PEP/PA, cloud outages | Assume breach → recovery ops | DDoS still a problem; policy-driven upstream filtering |
| **Stolen credentials / insider** | §5.3 — MFA, contextual TA, no lateral movement | Worked examples: compromised creds, remote exploitation, supply chain | Identity theft (two identities required), social engineering, physical coercion |
| **Visibility / monitoring gaps** | §5.4 — Encrypted traffic, metadata, ML | Not addressed directly | Endpoint enumeration, confidentiality vs. privacy distinction |
| **Data storage as target** | §5.5 — Monitoring data, policy management tools | Not addressed directly | Control plane data store compromise, falsifying access patterns |
| **Proprietary lock-in** | §5.6 — Vendor interoperability, switching costs | Not addressed | Not addressed |
| **NPEs / automated agents** | §5.7 — API auth, false positives/negatives, agent coercion | Not addressed | Invalidation speed (adjacent concern) |

**Key insight:**

The three documents form a progression. Gilman & Barth (2017) provide the **engineering-level adversarial analysis** — what specific attacks look like and how to mitigate them at the implementation level. NIST 800-207 (2020) provides the **architectural threat taxonomy** — what an enterprise must account for at the system-design level. NSA Embracing ZT (2021) provides the **operational threat model** — the "assume breach" mindset and worked examples that connect threats to ZT's defensive advantages. Together they cover threats from implementation detail through architecture to operational philosophy.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. The synthesis is this note's analytical claim. The progression pattern is visible in the sources but NIST doesn't make this argument itself.

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

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
