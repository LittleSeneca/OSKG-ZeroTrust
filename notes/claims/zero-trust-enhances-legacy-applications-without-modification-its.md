---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-implementation
  - topic/zt-migration
  - topic/zt-app
claim_id: "gc-iam-policy.7"
statement: "Zero Trust enhances legacy applications without modification — it's a security overlay, not a rip-and-replace"
confidence: "high"
confidence_rationale: "HIGH. This is the most practical ZT benefit for brownfield environments. It explains why VPN replacement is the dominant ZT entry point."
claim_type: "implementation"
source_note: "[[Garbis and Chapman — Practice IAM Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-iam-policy.7: Zero Trust enhances legacy applications without modification — it's a security overlay, not a rip-and-replace

**Source:** [[Garbis and Chapman — Practice IAM Policy]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"As an overlay onto existing networks, Zero Trust architectures are uniquely positioned to bring this kind of value while minimizing disruptive changes." The legacy application example shows a thick client using an unencrypted application-specific protocol — impossible to modify — gaining MFA enforcement and encrypted transport through the PEP alone.

## Evidence

Figure 5-5 shows a "before" state with unencrypted application traffic invisible to modern security tools, and an "after" state where the PEP intercepts access, calls the IDP for MFA, and tunnels all traffic encrypted — "without making any modifications to the application server or client." The authors also show three scenarios (Figure 5-4): a standalone siloed app, an LDAP-integrated app, and a ZT-protected app — the ZT variant adds PEP protection, encrypted transport, and MFA while the app itself is unchanged.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is the most practical ZT benefit for brownfield environments. It explains why VPN replacement is the dominant ZT entry point.

## Stakes

If ZT requires application modification to deliver value, most enterprises would never start. The overlay property means ZT adoption can be independent of application modernization timelines.

## Disagreement

**Who disagrees:**

Purists might argue that without application-level integration (the PEP passing identity context to the app), ZT is only solving the network half of the problem. The authors acknowledge this limitation — the app still has its own internal authorization model.

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

The overlay capability is ZT's killer feature for enterprise adoption. But it's a double-edged sword: organizations that _only_ use ZT as an overlay and never progress to application-level integration are leaving security value on the table. The BeyondCorp HTTP header injection pattern shows what the next step looks like.
