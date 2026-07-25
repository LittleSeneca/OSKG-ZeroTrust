---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-network
  - topic/zt-device
  - topic/zt-identity
  - topic/zt-architecture
claim_id: "go-ch9-11.4"
statement: "NAC (e.g., Cisco ISE) functions as the single source of truth for access decisions across all connection mediums, but each medium (wired, wireless, VPN) has distinct rollout characteristics."
confidence: "high"
confidence_rationale: "HIGH — Detailed, medium-specific rollout guidance with concrete configuration examples. The caution against workaround policies is consistent with"
claim_type: "implementation"
source_note: "[[Green-Ortiz — Ch9-11 — Advanced and Future]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-ch9-11.4: NAC (e.g., Cisco ISE) functions as the single source of truth for access decisions across all connection mediums, but each medium (wired, wireless, VPN) has distinct rollout characteristics.

**Source:** [[Green-Ortiz — Ch9-11 — Advanced and Future]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

The NAC system is positioned as the identity engine for ZT enforcement, serving as the authoritative source for access decisions across wired, wireless, and VPN connections.

## Evidence

Wired is the easiest starting point — passive profiling via DHCP/DNS/HTTP/CDP without changing user experience, with switch port configurations ranging from `authentication open` (monitor) to no `authentication open` (full enforcement). Wireless is harder because WLCs enforce authorization results immediately upon RADIUS completion; workaround is standing up a new SSID for managed devices. VPN is mid-difficulty — tunnel group auth source migration is trivial (3 lines), and a "permit any" authorization result provides a soft start. The authors explicitly warn against "workaround" policies that grant partial access to failed-authentication users: instead, force MAC Authentication Bypass → captive portal → verified registration → Internet-only ACL.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — Detailed, medium-specific rollout guidance with concrete configuration examples. The caution against workaround policies is consistent with the broader ZT literature's emphasis on not creating exceptions.

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
