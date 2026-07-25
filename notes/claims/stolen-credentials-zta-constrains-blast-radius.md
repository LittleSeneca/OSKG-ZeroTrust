---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-threats
  - topic/zt-identity
  - topic/zt-governance
  - topic/zt-device
claim_id: "nist207-ch5.3"
statement: "Stolen credentials remain a threat under ZTA, but ZTA's \"no implicit trust\" principle constrains the blast radius — compromised accounts cannot move laterally to resources outside their authorized scope, and contextual trust algorithms detect anomalous access patterns faster."
confidence: "high"
confidence_rationale: 'HIGH. The "no lateral movement" claim is architecturally true — it follows directly from per-session, per-resource access evaluation'
claim_type: "threat"
source_note: "[[NIST 800-207 — Ch5 — Threats]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch5.3: Stolen credentials remain a threat under ZTA, but ZTA's "no implicit trust" principle constrains the blast radius — compromised accounts cannot move laterally to resources outside their authorized scope, and contextual trust algorithms detect anomalous access patterns faster.

**Source:** [[NIST 800-207 — Ch5 — Threats]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

ZT's "no implicit trust based on network location" means attackers must compromise an existing account or device to gain a foothold. A properly implemented ZTA prevents that compromised account from accessing resources outside its normal purview — but within its authorized scope, damage is still possible. (§5.3)

## Evidence

- Attackers target accounts with access policies aligned to their objectives (admin accounts for control, financial accounts for monetary gain)
- Phishing, social engineering, or combined attacks to obtain credentials
- MFA reduces risk of information loss but does not eliminate it — a valid-credentialed attacker still accesses resources the account is authorized for
- **ZTA advantage:** No lateral movement. If credentials aren't authorized for a resource, access is denied regardless of network position
- **Contextual trust algorithm (Section 3.3.1):** Detects out-of-normal access patterns faster than perimeter-based networks, can deny the compromised account access to sensitive resources

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The "no lateral movement" claim is architecturally true — it follows directly from per-session, per-resource access evaluation.

**Cross-reference — NSA Embracing ZT**

NSA provides two worked examples that directly parallel Section 5.3:

1. **Compromised user credentials:** A malicious actor uses stolen credentials on an unauthorized device. In a traditional network, credentials alone suffice. In ZT, the unknown device fails authentication/authorization, access is denied, and the activity is logged. MFA makes credential theft harder in the first place.

2. **Remote exploitation / insider threat:** A compromised device or malicious insider uses valid credentials to enumerate the network and move laterally. In ZT, network segmentation limits enumeration and lateral movement. Even authenticated, access is capped by policy, user role, and device attributes. Analytics continuously monitor for anomalous activity — damage is limited and detection time is reduced.

**Cross-reference — Gilman & Barth: Identity Theft**

Gilman & Barth identify identity theft as the **first threat** in their adversarial view: "Practically all of the decisions and operations performed within a zero trust network are made on the basis of authenticated identity." Key insights:
- ZT requires theft of **at least two identities** (device + user/application) to gain access — raising the bar compared to traditional approaches
- Trust engine behavioral analysis provides additional mitigation
- Identity theft is an industry-wide concern, not ZT-specific, but its importance is "large enough to justify calling it out"
- They also address **social engineering** (phishing, face-to-face coercion) and **physical coercion** as vectors for identity compromise, recommending group authentication for critical assets to prevent single-individual compromise

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
