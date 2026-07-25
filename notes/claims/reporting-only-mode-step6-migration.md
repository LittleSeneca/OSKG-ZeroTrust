---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-migration
  - topic/zt-monitoring
  - topic/zt-implementation
  - topic/zt-governance
claim_id: "nist207-ch7.10"
statement: "Initial ZTA deployment should operate in reporting-only (observation) mode — not immediate enforcement — because few policy sets are complete on the first iteration, and the monitoring phase collects real access pattern data to establish a baseline against which anomalous behavior can be identified."
confidence: "high"
confidence_rationale: "HIGH. The observe-before-enforce pattern is a well-established migration principle, also advocated by Gilman & Barth and Green-Ortiz."
claim_type: "migration"
source_note: "[[NIST 800-207 — Ch7 — Migration]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch7.10: Initial ZTA deployment should operate in reporting-only (observation) mode — not immediate enforcement — because few policy sets are complete on the first iteration, and the monitoring phase collects real access pattern data to establish a baseline against which anomalous behavior can be identified.

**Source:** [[NIST 800-207 — Ch7 — Migration]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

Initial deployment begins with an **observation and monitoring mode** — NOT immediate enforcement. "Few enterprise policy sets are complete in their first iterations." (§7.3.6)

## Evidence

- Important accounts may be denied access they need, or may retain more privileges than required.
- **Recommended approach: reporting-only mode** — grant access for most requests initially, log and trace all connections, compare actual access patterns against initial policy, enforce only the most basic policies (deny requests that fail MFA or appear from known attacker-controlled IPs).
- **Why lenient?** To collect data from actual interactions. Once a baseline of activity patterns is established, anomalous behavior can be more easily identified.
- If reporting-only mode is not possible, operators must **monitor logs closely and be prepared to modify access policies** based on operational experience.

**Cross-reference:**

Gilman & Barth's [[Zero Trust Networks]] strongly advocates for a logging-first, enforce-later approach. This mirrors the **observe → monitor → enforce** progression in Green-Ortiz et al.'s [[Zero Trust Architecture]] implementation methodology.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The observe-before-enforce pattern is a well-established migration principle, also advocated by Gilman & Barth and Green-Ortiz.

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
- [[log-then-enforce-is-the-migration-procedure-validated-by-two|Reporting-only mode is the NIST 7-step framing of the log phase in the log-then-enforce pattern independently validated]]

## Assessment

_Not addressed separately in the source note._
