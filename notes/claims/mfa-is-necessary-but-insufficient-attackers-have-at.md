---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-authentication
  - topic/zt-threats
  - topic/zt-identity
  - topic/zt-monitoring
claim_id: "finney-ch4-7.5"
statement: "MFA is necessary but insufficient — attackers have at least three distinct bypass strategies that ZT must address."
confidence: "high"
confidence_rationale: "HIGH. These bypass techniques are well-documented in the threat intelligence literature and validated by real-world breach reports. The taxonomy"
claim_type: "implementation"
source_note: "[[Finney — Ch4-7 — Building the ZT Strategy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch4-7.5: MFA is necessary but insufficient — attackers have at least three distinct bypass strategies that ZT must address.

**Source:** [[Finney — Ch4-7 — Building the ZT Strategy]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"Bob has three ways to deal with MFA. He can disable or weaken MFA. He can directly bypass MFA. Or he can exploit an existing exception to MFA."

## Evidence

| Bypass Strategy | Specific Techniques |
|---|---|
| **Disable/Weaken** | Modify trusted IP configurations; weaken MFA enforcement policies |
| **Directly Bypass** | SMS intercepts (SIM-jacking); compromise an already-authenticated device; stolen certificates (SolarWinds-style); golden ticket attacks (forged Kerberos tickets) |
| **Exploit Exceptions** | Target service accounts without MFA; attack legacy protocols (POP/IMAP) that don't support MFA; session reuse (30-day default reauth windows) |

Agent Smecker also warns that stolen certificates and golden ticket attacks are "a real challenge to detect since the requests look legitimate."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These bypass techniques are well-documented in the threat intelligence literature and validated by real-world breach reports. The taxonomy (disable/bypass/exploit exceptions) is useful for threat modeling.

## Stakes

Organizations that treat MFA deployment as "done" without addressing these bypass vectors are operating with a false sense of security. The 30-day default session window alone gives attackers a month of unrestricted access after compromising a device with an authenticated session.

## Disagreement

**Who disagrees:**

MFA vendors emphasize that these are edge cases and that MFA still blocks the vast majority of credential-based attacks. This is true but misleading — sophisticated attackers (the ones most likely to cause material damage) specifically target these bypass vectors.

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

Finney's treatment of MFA is unusually honest for an introductory book. Most ZT literature presents MFA as a solved problem; Finney devotes significant narrative time to showing how it fails. This is important because it forces readers to think about compensating controls: reauthentication frequency, PAM, certificate hygiene, legacy protocol retirement, and session monitoring — all of which are more architecturally demanding than "turn on MFA."
