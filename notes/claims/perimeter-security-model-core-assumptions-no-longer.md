---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/beyondcorp
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-network
  - topic/zt-governance
claim_id: "beyondcorp.1"
statement: "The perimeter security model's core assumptions no longer hold — the internal network is as dangerous as the public Internet, and trust in network location is fundamentally misplaced."
confidence: "high"
confidence_rationale: "HIGH — This is the foundational critique from the canonical ZT implementation at Google, published in USENIX ;login:. The six-component architecture"
claim_type: "implementation"
source_note: "[[BeyondCorp — Research Papers]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondcorp.1: The perimeter security model's core assumptions no longer hold — the internal network is as dangerous as the public Internet, and trust in network location is fundamentally misplaced.

**Source:** [[BeyondCorp — Research Papers]] — Google, *BeyondCorp Research Papers*, 2014-2020

## The Claim

The founding paper articulates the core critique of perimeter security: "Key assumptions of this model no longer hold: The perimeter is no longer just the physical location of the enterprise, and what lies inside the perimeter is no longer a blessed and safe place to host personal computing devices and enterprise applications."

## Evidence

Google's operational experience demonstrated that trust in the internal network is misplaced. The alternative: assume the internal network is as dangerous as the public Internet and build applications accordingly. The paper lays out six foundational components that remain the backbone of BeyondCorp: (1) Device Inventory Database — tracks every managed device through procurement/changes/decommissioning, amalgamating data from multiple source databases; (2) Device Identity via X.509 Certificates — stored in hardware/software TPM, qualification validates certificate store, periodic renewal enforces continued compliance, identifies device but does NOT single-handedly grant access; (3) User and Group Database — tightly integrated with HR processes, updated on join/role-change/leave; (4) SSO — centralized authentication with primary + second-factor credentials, generates short-lived tokens; (5) Unprivileged Network — resembles external network but within private address space, only connects to Internet, limited infrastructure (DNS, DHCP, NTP), and configuration management (Puppet); (6) Internet-Facing Access Proxy — all enterprise applications exposed externally, enforces encryption, global reachability, load balancing, access control checks, health checks, DoS protection.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — This is the foundational critique from the canonical ZT implementation at Google, published in USENIX ;login:. The six-component architecture is the reference design that NIST 800-207's logical components (PDP, PEP, PIP) later abstracted.

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
