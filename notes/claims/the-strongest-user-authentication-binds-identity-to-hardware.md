---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-identity
  - topic/zt-authentication
claim_id: "gb-ch4-6.11"
statement: "The strongest user authentication binds identity to hardware tokens with additional factors"
confidence: "high"
confidence_rationale: "HIGH on the assessment of current mechanisms. The biometric discussion is notably nuanced — the authors flag rotation impossibility, spoofing, and"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch4-6 — Authorization Devices Users]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch4-6.11: The strongest user authentication binds identity to hardware tokens with additional factors

**Source:** [[Gilman and Barth — Ch4-6 — Authorization Devices Users]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"If we want the strongest guarantee that a particular user is who they claim to be, using a security key with additional authentication factors (e.g., a password or biometric sensor) is still strongly recommended."

## Evidence

The chapter surveys the authentication landscape systematically:

| Method | Category | Strength | Weakness |
|--------|----------|----------|----------|
| Passwords | Something you know | Effective when long + unique + not reused | Users choose poor passwords; reuse across services |
| TOTP | Something you have | Good second factor | Shared secret must be protected; SMS is explicitly not recommended |
| X.509 user certificates | Something you have | Rich metadata; computer-verifiable | Private key storage is the weak point |
| Security tokens (YubiKey, smart card) | Something you have | Private key never leaves hardware | Token can be stolen; needs pairing with PIN or biometric |
| Biometrics (fingerprint, face) | Something you are | Convenient; hard to share | Cannot be rotated; can be spoofed; legal issues (Fifth Amendment) |
| U2F/UAF (FIDO) | Something you have | Replay-resistant; per-service keys; phishing-resistant | Requires ecosystem support |

The authors highlight U2F (now FIDO2) as the forward-looking standard: "Open standards like the FIDO Alliance's UAF standard use asymmetric cryptography and local device authentication systems to move trust away from a large number of services to relatively few user-controlled endpoints."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH on the assessment of current mechanisms. The biometric discussion is notably nuanced — the authors flag rotation impossibility, spoofing, and legal compulsion (Fifth Amendment vs. compelled fingerprint) — concerns that remain relevant in 2024.

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
