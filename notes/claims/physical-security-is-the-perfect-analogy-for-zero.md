---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-definition
  - topic/zt-network
  - topic/zt-identity
claim_id: "finney-ch1-3.9"
statement: "Physical security is the perfect analogy for Zero Trust"
confidence: "high"
confidence_rationale: "HIGH for the pedagogical value. The physical security analogy is genuinely effective — it makes abstract network concepts concrete and intuitive"
claim_type: "definitional"
source_note: "[[Finney — Ch1-3 — The Zero Trust Story]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch1-3.9: Physical security is the perfect analogy for Zero Trust

**Source:** [[Finney — Ch1-3 — The Zero Trust Story]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"Physical security is the perfect analogy for Zero Trust. It's easier to talk about since we're not talking about imaginary invisible things. And I think people instinctively understand security." The chapter uses physical security failures to teach ZT concepts:

- **Tailgating** → network lateral movement (following someone through a door = pivoting from a compromised host)
- **Propped-open doors** → default-allow firewall rules
- **Unencrypted badge readers** → unencrypted network protocols
- **Shared guard logins** → shared service accounts
- **Cameras on the user network** → flat networks with no segmentation
- **Motion sensor bypass with paper airplane** → exploiting trust assumptions in automated systems
- **Remote access software on security systems** → third-party backdoors

## Evidence

Dylan conducts an informal penetration test: he walks through the building unchallenged (tailgating through multiple doors), reaches the data center, and could have walked out with a server. Peter Liu demonstrates a paper airplane triggering a motion sensor to unlock a door. Harmony discovers the security desk computer runs Windows 7 with shared logins, default camera passwords ("MarchFit"), and third-party remote access software.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH for the pedagogical value. The physical security analogy is genuinely effective — it makes abstract network concepts concrete and intuitive. Finney's insight that "we naturally place controls around the things we're trying to protect" in physical security is exactly the shift ZT requires for cybersecurity.

## Stakes

If the analogy breaks down under scrutiny (physical perimeters are still valuable in ways network perimeters aren't), it could mislead. Finney addresses this with the "teleporter" thought experiment: "Ask yourself what would happen if someone invented a teleporter like in Star Trek. Those perimeter controls would still be important, but you'd need to shift the way you thought about security." In cyberspace, attackers *do* have a teleporter — they can appear anywhere in the network.

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

This is the most pedagogically valuable chapter for non-technical audiences. The physical security walkthrough is something any executive can understand. The specific vulnerabilities found (Windows 7, default passwords, shared logins, remote access backdoors) are depressingly realistic — many organizations have exactly these issues in their physical security systems. The analogy is valid and useful, and the "teleporter" framing elegantly explains why network security is fundamentally different from physical security despite the shared principles.
