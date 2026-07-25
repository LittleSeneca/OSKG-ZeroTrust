---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-identity
  - topic/zt-implementation
  - topic/zt-access-mgmt
claim_id: "finney-ch4-7.4"
statement: "Identity is simultaneously the most important protect surface AND the most important ZT enabler — it must be both protected and consumed."
confidence: "high"
confidence_rationale: 'HIGH. Finney captures the dual nature of identity in ZT better than most technical treatments. The "crown and jewels" metaphor is rhetorically'
claim_type: "implementation"
source_note: "[[Finney — Ch4-7 — Building the ZT Strategy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch4-7.4: Identity is simultaneously the most important protect surface AND the most important ZT enabler — it must be both protected and consumed.

**Source:** [[Finney — Ch4-7 — Building the ZT Strategy]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"Zero Trust consumes identity to help ensure least privilege. But identity is also one of your most important protect surfaces, so you need to protect it just as well as your other critical assets. I would actually argue that while your ERP is your crown, the jewels are the people."

## Evidence

The FBI agent reveals that the breach occurred because MarchFit mixed customer and employee identity data in a single domain. When Bob Paulson left the company, his account wasn't terminated because he remained an active customer — retaining all employee permissions. A phishing email weeks later gave the attacker those permissions. The narrative demonstrates that identity failures cascade: a provisioning failure (Bob's account not deprovisioned) becomes an authentication failure (phished credentials) becomes an authorization failure (retained superuser access).

The chapter walks through the full identity life cycle:
- **Provisioning/deprovisioning**: automated HR feeds, role-based permissions tied to job descriptions, multi-channel account claiming with identity verification questions
- **Authentication**: MFA with multiple registered methods, no SMS for employees (SIM-jacking risk), reauthentication requirements, SSO for all applications
- **Authorization**: role cleanup to eliminate permission bloat, owner/sponsor for every account, quarterly user access reviews
- **Federation**: allowed for customers (BYO identity from social/email), forbidden for employees
- **Privileged Access Management (PAM)**: separate admin accounts, no email on admin accounts, credential rotation, temp logins
- **Monitoring**: basic + advanced auditing, object/attribute change detection, all identity events to SIEM

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. Finney captures the dual nature of identity in ZT better than most technical treatments. The "crown and jewels" metaphor is rhetorically effective and diagnostically accurate — organizations that secure the ERP but neglect identity have protected the vault but left every key on the floor.

## Stakes

Identity is where ZT succeeds or fails. Getting identity wrong means every other protect surface inherits a compromised foundation. Getting it right means every downstream control can consume identity signals for policy decisions.

## Disagreement

**Who disagrees:**

Some frameworks (Google BeyondCorp) treat identity primarily as an enabler rather than a protect surface. The distinction matters for resource allocation — if identity is "just" an enabler, it gets funded as infrastructure; if it's a crown jewel, it gets protected with equivalent rigor.

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

The chapter's most important operational insight is the separation of customer and employee identity domains. This is not just a technical decision — it's a strategic one that affects every downstream ZT policy. The narrative shows why: mixing domains creates an unclosable vulnerability (former employees who are current customers retain access). The decision to create a *new* employee domain (rather than migrating customers) is a masterclass in change management — consumers hate service disruption, so move the smaller, more controllable population.
