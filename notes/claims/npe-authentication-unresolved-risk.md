---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-threats
  - topic/zt-authentication
  - topic/zt-identity
  - topic/zt-architecture
claim_id: "nist207-ch5.7"
statement: 'Non-Person Entities (NPEs) — AI agents and software-based automation managing ZTA security components — introduce unresolved authentication and decision-quality risks, and NIST flags NPE authentication as an "open issue."'
confidence: "medium"
confidence_rationale: "MEDIUM. The threats are plausible but largely hypothetical — NPE-based ZTA administration is nascent and NIST provides no case studies or incident"
claim_type: "threat"
source_note: "[[NIST 800-207 — Ch5 — Threats]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch5.7: Non-Person Entities (NPEs) — AI agents and software-based automation managing ZTA security components — introduce unresolved authentication and decision-quality risks, and NIST flags NPE authentication as an "open issue."

**Source:** [[NIST 800-207 — Ch5 — Threats]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

AI and software-based agents are being deployed to manage ZTA security components (PE, PA), sometimes replacing human administrators. Their authentication and decision-making introduce new threat vectors. (§5.7)

## Evidence

- **Authentication gap:** NPEs typically authenticate via API keys rather than MFA — a lower bar than human users
- **Decision quality:** False positives (innocuous actions mistaken for attacks) and false negatives (attacks mistaken for normal activity) impact security posture — mitigated by regular retuning
- **Agent coercion:** An attacker could trick or coerce an NPE into performing privileged tasks on their behalf
- **Credential impersonation:** An attacker could steal a software agent's credentials and impersonate it

**Status:**

NIST flags this as an "open issue" — how NPEs should authenticate in a ZTA is unresolved.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. The threats are plausible but largely hypothetical — NPE-based ZTA administration is nascent and NIST provides no case studies or incident data.

**Cross-reference — Gilman & Barth**

Gilman & Barth do not address NPEs directly (their 2017 framing predates widespread AI-agent deployment in security operations), but their "Invalidation" section raises a related concern: the speed at which ongoing authorized actions can be revoked. If an NPE grants access that later proves malicious, can the system invalidate it fast enough? This is the "hard problem" of invalidation that Gilman & Barth explore — and it becomes harder when NPEs make authorization decisions at machine speed.

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
- [[stolen-credentials-zta-constrains-blast-radius|stolen-credentials-zta-constrains-blast-radius]]

## Assessment

_Not addressed separately in the source note._
