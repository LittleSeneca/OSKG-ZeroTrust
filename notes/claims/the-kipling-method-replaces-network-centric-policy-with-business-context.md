---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-policy
  - topic/zt-governance
claim_id: "finney-ch1-3.8"
statement: "The Kipling Method replaces network-centric policy with business-context policy"
confidence: "medium"
confidence_rationale: "MEDIUM. The Kipling Method is conceptually sound and practically useful as a policy design framework. However, implementing it requires"
claim_type: "governance"
source_note: "[[Finney — Ch1-3 — The Zero Trust Story]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch1-3.8: The Kipling Method replaces network-centric policy with business-context policy

**Source:** [[Finney — Ch1-3 — The Zero Trust Story]] — George Finney, *Project Zero Trust*, 2022

## The Claim

Policy should be built around six questions (after Kipling's poem): Who (User ID, Auth type), What (Application ID), When (Time limitations), Where (Device ID, Geolocation), Why (Classification, Data ID), How (Threat Protection, SSL Decryption, URL Filtering). This is "layer seven replacements for an old protocol, source IP, destination IP address, rule set."

## Evidence

Aaron demonstrates this by having Brent identify the correct role group (Who) for the SharePoint site rather than using IP-based access control. "A lot of organizations limit access to sensitive servers by IP address... But this isn't Zero Trust. It turns out in practice that attackers are very good at figuring out where those holes are."

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. The Kipling Method is conceptually sound and practically useful as a policy design framework. However, implementing it requires identity-aware firewalls, application-layer inspection, and device posture assessment — technologies that many organizations don't have deployed. The gap between "write policy this way" and "enforce policy this way" is significant.

## Stakes

If the Kipling Method is aspirational — policies you'd *like* to write but can't enforce — it's just paperwork. If the technology stack supports it (next-gen firewall, identity provider integration, device compliance), it's a genuine advancement over IP-based rules.

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

The Kipling Method is the most underrated concept in these chapters. It's a policy design template that works regardless of enforcement technology — you can start writing Kipling-style policies before you have the tools to enforce them, which drives tool selection. "We need to enforce Who-based rules" → that means identity-aware firewall. "We need When-based rules" → that means time-based access policies. The method drives the architecture, not vice versa.
