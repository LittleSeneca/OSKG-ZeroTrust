---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-network
  - topic/zt-device
  - topic/zt-identity
  - topic/zt-architecture
claim_id: "gc-net-access.4"
statement: "802.1x-based NAC is fundamentally incompatible with Zero Trust's universal scope — it is local-only, coarse-grained (VLAN assignment), provides no encryption, has static posture, and is hardware-dependent."
confidence: "high"
confidence_rationale: "HIGH — The five limitations are architectural rather than implementation-specific, meaning they apply to any 802.1x-based NAC regardless of vendor"
claim_type: "definitional"
source_note: "[[Garbis and Chapman — Network and Access Technologies]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-net-access.4: 802.1x-based NAC is fundamentally incompatible with Zero Trust's universal scope — it is local-only, coarse-grained (VLAN assignment), provides no encryption, has static posture, and is hardware-dependent.

**Source:** [[Garbis and Chapman — Network and Access Technologies]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

The authors deliver their strongest rejection of NAC: "802.1x-based NAC functions are not suitable to use as the core part of any Zero Trust environment." Five fatal limitations are enumerated: (1) local-only scope — supplicant and authenticator must be on same broadcast domain, useless for remote users or cloud; (2) coarse-grained access — VLAN assignment with dozens/hundreds of services visible, "not compatible with the principle-of-least-privilege tenet of Zero Trust"; (3) no encryption or remote access; (4) static posture — once assigned to VLAN, no further involvement beyond periodic reauthentication; (5) hardware-dependent — requires ubiquitously deployed enterprise-owned network hardware.

## Evidence

NAC's legitimate residual roles: guest network access (managed or unmanaged Wi-Fi), device discovery (a byproduct of how NAC works — data can feed ZT policy model as in Google BeyondCorp), and device posture checks (though ZT platforms are better at dynamic policy enforcement based on these attributes). The authors provide a comparison table (Table 7-2): NAC can only serve on-premises users with coarse-grained VLAN access; ZT provides granular, identity-specific access for both on-premises and remote users equally.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The five limitations are architectural rather than implementation-specific, meaning they apply to any 802.1x-based NAC regardless of vendor. The residual roles are clearly scoped. Google BeyondCorp's use of 802.1x alongside an access proxy validates the "complementary component, not core" verdict.

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
