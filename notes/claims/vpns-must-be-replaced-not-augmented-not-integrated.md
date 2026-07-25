---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-network
  - topic/zt-implementation
  - topic/zt-cloud
  - topic/zt-architecture
claim_id: "gc-net-access.6"
statement: "VPNs must be replaced — not augmented, not integrated, but retired. This is the authors' strongest and most unequivocal verdict, grounded in five architectural flaws that Zero Trust inherently solves."
confidence: "high"
confidence_rationale: "HIGH — The strongest claim in the book, supported by five specific architectural flaws that are inherent to VPN design rather than"
claim_type: "implementation"
source_note: "[[Garbis and Chapman — Network and Access Technologies]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-net-access.6: VPNs must be replaced — not augmented, not integrated, but retired. This is the authors' strongest and most unequivocal verdict, grounded in five architectural flaws that Zero Trust inherently solves.

**Source:** [[Garbis and Chapman — Network and Access Technologies]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"VPNs provide an outdated and frankly insecure approach to remote access, and must be retired or replaced as organizations move to Zero Trust." The authors argue: "Your enterprise shouldn't contain a remote access solution (enterprise VPN). It should just be an access solution, which is deployed so that it enforces access control for both remote and on-premises users, based on a unified platform and policy model."

## Evidence

Five fatal VPN flaws: (1) static identity model — access identical regardless of device, location, or risk context; (2) static resource model — access granted to fixed subnets/IPs, cannot dynamically resolve targets in DevOps environments, leading to "too-broad network access, in order to keep users productive"; (3) single entry point — forces perimeter-based model, one ingress, all resources connected via internal LAN/WAN, technically impossible in distributed cloud; (4) exposed attack surface — open ports on Internet, "an inviting target for attackers worldwide," citing "many, many recent and widely publicized VPN vulnerabilities"; (5) remote-access silo — cannot enforce for on-premises users, creating duplicated expenses and inconsistent policies. The ZT replacement is contrasted point-by-point: dynamic contextual access, distributed PEPs, cloaked entry points (SPA), unified access control for all users.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The strongest claim in the book, supported by five specific architectural flaws that are inherent to VPN design rather than implementation-specific. This is one of the most convergent claims across the ZT literature — every major source (NIST, CISA, NSA, Gilman & Barth, BeyondCorp) advocates VPN replacement or retirement.

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
