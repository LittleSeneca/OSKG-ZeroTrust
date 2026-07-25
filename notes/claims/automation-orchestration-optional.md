---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/halley-resilient-cloud
  - topic/zt-cloud
  - topic/zt-implementation
  - topic/zt-migration
  - topic/zt-governance
claim_id: "halley.4"
statement: "Automation and orchestration are not optional — they are ZT prerequisites at scale"
confidence: "high"
confidence_rationale: "HIGH. The automation-as-prerequisite claim is supported by every major ZT implementation (BeyondCorp, PagerDuty) and is implicit in NIST 800-207's"
claim_type: "implementation"
source_note: "[[Halley — Zero Trust in Resilient Cloud]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# halley.4: Automation and orchestration are not optional — they are ZT prerequisites at scale

**Source:** [[Halley — Zero Trust in Resilient Cloud]] — Andrew Halley et al., *Zero Trust in Resilient Cloud*, 2023

## The Claim

Manual security processes are incompatible with ZT at enterprise scale. Continuous verification requires automated trust scoring. Least-privilege access requires automated policy enforcement across thousands of workloads. Assume breach requires automated incident response. Automation is not a nice-to-have; it's the operational backbone of ZT.

## Evidence

The book's Part 2 (Ch5-11) covers the automation substrate: DHCP security (snooping, Option 82 for device identity), zero-touch provisioning (assuring device integrity from first boot), API security (northbound/southbound/east-west APIs as attack surface), and Infrastructure as Code (Terraform, Ansible) for consistent security configuration. Part 6 (Ch22) covers third-party SDN integrations — ZT requires automation that spans vendor boundaries.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The automation-as-prerequisite claim is supported by every major ZT implementation (BeyondCorp, PagerDuty) and is implicit in NIST 800-207's continuous diagnostics requirement.

## Stakes

Organizations that treat ZT as a product purchase (buy a ZTNA solution, deploy it, done) will fail at scale. ZT is an operational model that requires automation to sustain. Without automation, continuous verification becomes periodic verification; least privilege becomes role-bloat; assume breach becomes hope-for-the-best.

## Disagreement

**Who disagrees:**

Smaller organizations may argue that manual processes work at their scale. This is true for 50 users and 20 applications — you can manually review access. But the ZT model is designed for environments where manual review is impossible. Small orgs can adopt ZT principles without full automation, but they're not getting the continuous verification benefit.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[multi|Multi-cluster global control planes across environments require automation to manage policies consistently at scale.]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

This claim exposes a gap in NIST 800-207: the standard describes *what* ZTA does but not *how* to operate it at scale. Halley fills this gap with concrete automation patterns. For OSKG-ZeroTrust, this means automation and orchestration should be treated as cross-cutting concerns that enable every ZT capability.
