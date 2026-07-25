---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-device
  - topic/zt-trust
  - topic/zt-access-mgmt
  - topic/zt-definition
claim_id: "gb-ch4-6.7"
statement: "Trust degrades over time — device age is the strongest negative signal"
confidence: "high"
confidence_rationale: "HIGH on the principle, MODERATE on specific renewal mechanisms. Remote vulnerability scanning and local agents are both acknowledged as flawed (\"it's"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch4-6 — Authorization Devices Users]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch4-6.7: Trust degrades over time — device age is the strongest negative signal

**Source:** [[Gilman and Barth — Ch4-6 — Authorization Devices Users]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"The natural progression is that the longer a device is operating, the greater its chances of being compromised. This is why device age is a heavily weighted trust signal."

## Evidence

Trust renewal mechanisms: reimaging (logically rotates device — removes "majority of persistent threats"), hardware rotation (tear down and rebuild cloud instances), TPM remote attestation (hardware-backed, "highly reliable" but limited to low-level software), software-based local measurement (agent reporting — "generally futile" against privileged attackers), remote vulnerability scanning (external probing — benefits from separation of duty but "relies on interrogation of the endpoint").

**Cross-reference — NSA Device Pillar:**

NSA's four-phase maturity model makes this explicit: Preparation phase establishes inventory; Basic mandates TPM and secure boot; Intermediate requires remote attestation and continuous monitoring; Advanced integrates SBOM/RIM with cryptographically proven firmware integrity. Gilman & Barth's 2017 guidance anticipates all four phases, though with less specificity about auditability requirements.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the principle, MODERATE on specific renewal mechanisms. Remote vulnerability scanning and local agents are both acknowledged as flawed ("it's the difference between asking someone if they robbed a bank, and watching them rob a bank").

## Stakes

If trust never decays, a device compromised on Day 1 retains full access indefinitely. The decay function is the security model's immune system. Getting the decay rate wrong means either too many false positives (locking out legitimate users) or false negatives (allowing compromised devices to persist).

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[continuous-risk-based-device-authorization|Trust degradation over time is a specific risk factor that continuous authorization must account for — device age is fra]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
