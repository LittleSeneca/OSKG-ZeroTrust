---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-threats
  - topic/zt-definition
  - topic/zt-network
  - topic/zt-governance
claim_id: "gb-ch2.1"
statement: "ZT's threat model is the Internet Threat Model plus endpoint compromise"
confidence: "high"
confidence_rationale: 'HIGH. RFC 3552 is a foundational IETF document and the expansion to endpoints is logically consistent with the "network is always hostile" assertion'
claim_type: "definitional"
source_note: "[[Gilman and Barth — Ch2 — Managing Trust]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch2.1: ZT's threat model is the Internet Threat Model plus endpoint compromise

**Source:** [[Gilman and Barth — Ch2 — Managing Trust]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"Zero trust networks, as a result of their control over endpoints in the network, expand upon the Internet Threat Model to consider compromises at the endpoints." The Internet Threat Model (RFC 3552) assumes attackers have "nearly complete control of the communications channel" — they can read, remove, change, or inject packets. ZT expands this to include compromised endpoints. The goal is to mitigate attacks "up to and including attacks originating from a 'trusted insider' level of access" but not all state-level actors.

## Evidence

The RFC 3552 excerpt is quoted directly — the standard model assumes end-systems themselves are uncompromised, but ZT drops that assumption. The attacker categorization (opportunistic → targeted → insider → trusted insider → state-level) provides a ladder of increasing capability, and ZT draws the line below state-level actors because "an attacker with unlimited resources is essentially impossible to defend against."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. RFC 3552 is a foundational IETF document and the expansion to endpoints is logically consistent with the "network is always hostile" assertion from Ch1. Every major ZT implementation (BeyondCorp, DoD ZT RA) makes the same assumption.

## Stakes

The threat model determines what ZT is designed to protect against — and, crucially, what it explicitly does NOT protect against. If state-level actors are out of scope, ZT is not a complete security architecture for national security systems. The authors are candid about this: "defending against these localized threats is exceedingly expensive, requiring dedicated physical hardware."

## Disagreement

**Who disagrees:**

NSA's guidance does include state-level actors in scope and treats "assume breach" as a separate organizing principle that covers endpoint compromise more comprehensively. NIST 800-207 doesn't explicitly enumerate threat actors but its continuous monitoring tenet (Tenet 5) implicitly addresses the same concern.

**Alternative reading:**

The threat model could be read as a pragmatic admission by practitioners — not a theoretical limit of ZT but a statement about where the ROI of additional controls drops off. State-level mitigations exist (hardware roots of trust, air-gapped PKI) but they're deployment-specific add-ons, not core ZT requirements.

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

This is a refreshingly honest threat model. Most security frameworks either claim universal protection (dishonest) or avoid the question (useless). Gilman & Barth draw a clear line — we defend against everything up to trusted insiders, and state-level actors require additional, specialized controls beyond the scope of this book. That clarity is valuable for resource allocation and honest risk communication.
