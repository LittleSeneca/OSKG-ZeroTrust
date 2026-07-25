---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-identity
  - topic/zt-threats
  - topic/zt-authentication
  - topic/zt-device
claim_id: "gb-ch10.1"
statement: "Identity theft is the first and most dangerous threat — ZT requires stealing *two* identities"
confidence: "high"
confidence_rationale: "HIGH. The dual-identity requirement is a genuine architectural advantage. However, this claim is weakened if device identity is poorly protected — a"
claim_type: "threat"
source_note: "[[Gilman and Barth — Ch10 — The Adversarial View]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch10.1: Identity theft is the first and most dangerous threat — ZT requires stealing *two* identities

**Source:** [[Gilman and Barth — Ch10 — The Adversarial View]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

"Practically all of the decisions and operations performed within a zero trust network are made on the basis of authenticated identity." Since ZT authenticates both device AND user/application, "it is necessary for an attacker to steal at least two identities in order to gain access to resources within it, raising the bar when compared to traditional approaches."

## Evidence

The argument is structural, not empirical. ZT's dual authentication requirement (device + user) means credential theft alone is insufficient — the attacker also needs a trusted device identity. Trust engine behavioral analysis provides additional mitigation. The authors are careful to note that identity theft is an "industry-wide concern and is not specific to zero trust" but that ZT "naturally mitigates" the threat without claiming elimination.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The dual-identity requirement is a genuine architectural advantage. However, this claim is weakened if device identity is poorly protected — a stolen laptop with cached credentials defeats both checks simultaneously.

## Stakes

The single most important claim for ZT's defensive advantage. If attackers can routinely compromise both identities (e.g., via phishing + malware on a managed device), ZT's advantage collapses to behavioral detection, which is probabilistic, not preventive.

## Disagreement

**Who disagrees:**

NIST 800-207 Ch5 (§5.3) agrees but adds MFA and contextual trust algorithms as additional mitigations. NSA Embracing ZT provides worked examples showing the attack chain failing at device authentication. Google BeyondCorp papers emphasize device health attestation as the critical second factor — an unpatched device should fail even with valid user credentials.

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

The dual-identity requirement is real but fragile. It's only as strong as the weaker of the two authentication systems. If device identity is bound to a TPM and user identity to a hardware token, the combination is genuinely hard to defeat. If both are software-based secrets on the same machine, one malware infection compromises both. This is why device attestation (Ch5) and hardware roots of trust matter — they're the difference between "two identities" and "two secrets stored on the same compromised machine."
