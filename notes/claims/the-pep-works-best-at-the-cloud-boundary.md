---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-architecture
  - topic/zt-cloud
  - topic/zt-network
  - topic/zt-policy
claim_id: "gc-cloud.2"
statement: "The PEP works best at the cloud boundary — source IP restrictions are the enabling primitive"
confidence: "high"
confidence_rationale: "VERY HIGH. This pattern — ZTNA gateway with source IP allowlisting — is exactly how every major ZTNA product (Zscaler, Cloudflare, Netskope)"
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Cloud IaaS SaaS]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-cloud.2: The PEP works best at the cloud boundary — source IP restrictions are the enabling primitive

**Source:** [[Garbis and Chapman — Cloud IaaS SaaS]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"The PEP works most effectively as an access control point across the cloud boundary (at the ingress point into the cloud environment)." The foundational enabling capability is CSPs' ability to restrict source IP addresses for accessing resources. "This capability, although basic, is all that's necessary for us to achieve our goal: our Zero Trust system (enforced via the PEP) is how we're applying dynamic and identity-centric policies."

## Evidence

Two topologies are presented:

1. **Co-located PEP** (Figure 14-1): PEP runs inside the CSP. IaaS resources assigned private IPs, PaaS resources accessed via public URLs with private prefixes (e.g., `https://abc123def.execute-api.us-east-1.amazonaws.com`). The CSP access gateway is configured so only traffic originating from the PEP can reach the resources. The PEP can make local API calls to retrieve cloud metadata tags for dynamic policy evaluation and auto-detect newly created service instances.

2. **Remote PEP** (Figure 14-2): PEP runs in an arbitrary environment (on-premises, another cloud). Resources need public IPs. The same source IP restriction is enforced, but this topology only works for encrypted protocols (the native app protocol goes PEP → gateway → resource).

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. This pattern — ZTNA gateway with source IP allowlisting — is exactly how every major ZTNA product (Zscaler, Cloudflare, Netskope) integrates with cloud resources. NIST 800-207's enclave-based and cloud-routed models describe the same pattern at a higher level of abstraction. The BeyondCorp Access Proxy operates identically.

## Stakes

If source IP restrictions are treated as a security control on their own (without the ZT PEP in front), they're trivially bypassed. If they're treated as unnecessary because "ZT handles it," cloud resources are left exposed. The correct posture is IP restrictions as the *enforcement mechanism* and the ZT PEP as the *policy mechanism* — two layers that must both be present.

## Disagreement

**Who disagrees:**

API-gateway-based approaches (API keys, signed requests, OAuth tokens) argue that IP-layer restrictions are too coarse. Service mesh advocates argue that mTLS + SPIFFE identities are superior. Both are correct for their domains — API gateways for application-layer access, service meshes for east-west traffic — but neither replaces the need for a boundary PEP for user-to-resource access.

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

This is the most practically useful section of both chapters. The "source IP allowlisting → PEP is the policy gate" pattern is the simplest, most universal integration model for cloud ZT. It works with every CSP, requires no agent on the resource, and maps cleanly to NIST's PDP/PEP architecture. The recommendation to "keep things simple, and externalize the dynamic and identity-centric access controls to your Zero Trust platform" is battle-tested advice.
