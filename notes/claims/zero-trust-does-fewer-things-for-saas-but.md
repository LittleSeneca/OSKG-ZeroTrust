---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-cloud
  - topic/zt-network
  - topic/zt-app
claim_id: "gc-cloud.4"
statement: "Zero Trust does fewer things for SaaS — but what it does is still valuable"
confidence: "high"
confidence_rationale: "HIGH. The observation that SaaS apps are public-by-design and HTTPS-native means ZT can't provide network hiding or encryption — the two functions"
claim_type: "implementation"
source_note: "[[Garbis and Chapman — Cloud IaaS SaaS]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-cloud.4: Zero Trust does fewer things for SaaS — but what it does is still valuable

**Source:** [[Garbis and Chapman — Cloud IaaS SaaS]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"Using Zero Trust to manage and control access to SaaS applications does provide value, even though we do acknowledge that Zero Trust does fewer things for SaaS resources compared with private resources." SaaS apps are publicly accessible by design (no resource hiding needed) and use HTTPS (no encryption needed from the PEP). But ZT can still enforce "identity-centric and context-sensitive access policies" using group membership, identity attributes, device posture, and enterprise system state.

## Evidence

Two native SaaS access control mechanisms exist: (1) source IP address restrictions — the SaaS platform permits access only from a designated IP (the PEP's egress IP), applied per-customer tenancy; (2) federated identity management via SAML/OIDC — the SaaS app delegates authentication to the enterprise IdP. These can be combined: "federated identity system for authentication combined with a Zero Trust network solution to perform deep device posture checks."

However, most SaaS apps "do not currently have mechanisms to consume external contextual information and make authorization decisions based on this" — they rely on internal role-based authorization models. This is the gap ZT can partially fill.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The observation that SaaS apps are public-by-design and HTTPS-native means ZT can't provide network hiding or encryption — the two functions that are most valuable for private resources. What remains is identity-centric policy enforcement, which is genuinely useful but narrower in scope. This is consistent with NIST 800-207's SaaS scenarios (Ch4) and CISA ZTMM's SaaS guidance.

## Stakes

If ZT is sold as a complete SaaS security solution, enterprises get a false sense of security — ZT doesn't address SaaS data security, configuration management, or insider threats within the SaaS app. If ZT is dismissed as irrelevant to SaaS, enterprises miss the opportunity to enforce device posture, session risk scoring, and just-in-time access for SaaS apps.

## Disagreement

**Who disagrees:**

CASB vendors argue that their approach (API-based, inline proxy, or both) provides more value for SaaS than ZTNA alone because they address data-at-rest, DLP, and configuration assessment. SWG vendors argue that their web filtering and threat protection are necessary companions to ZT for SaaS access. Both are correct — ZT + CASB + SWG is the realistic enterprise posture, which Garbis & Chapman acknowledge.

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

The honest assessment — "ZT does fewer things for SaaS" — is the most valuable sentence in this chapter. It prevents overclaiming and helps practitioners understand where ZT fits in their broader SaaS security stack. The gap Garbis & Chapman identify — SaaS apps not consuming external authorization context — remains largely unfilled in 2026, though standards like CAEP (Continuous Access Evaluation Protocol) and products like Microsoft's Conditional Access for SaaS are beginning to address it.
