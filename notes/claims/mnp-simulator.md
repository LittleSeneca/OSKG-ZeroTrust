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
claim_id: "beyondcorp.6"
statement: "The MNP Simulator — translating the network ACL into local iptables rules with logging and enforcement modes — was the operational linchpin that enabled high-velocity migration by testing enforcement at the client level before committing to network-level VLAN changes."
confidence: "high"
confidence_rationale: "HIGH — Primary-source description of a specific operational tool with documented outcomes (50% fleet migration in one year). The Capirca-based"
claim_type: "implementation"
source_note: "[[BeyondCorp — Research Papers]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# beyondcorp.6: The MNP Simulator — translating the network ACL into local iptables rules with logging and enforcement modes — was the operational linchpin that enabled high-velocity migration by testing enforcement at the client level before committing to network-level VLAN changes.

**Source:** [[BeyondCorp — Research Papers]] — Google, *BeyondCorp Research Papers*, 2014-2020

## The Claim

"Without this feature, we wouldn't have gained the confidence we needed to move devices to MNP at nearly the speed (or with the high level of success) that we did." The Managed Non-Privileged (MNP) Simulator translates the actual MNP network ACL into local iptables/Packet Filter rules (using Capirca). Logging mode monitors traffic, logs source/destination of non-MNP-compatible traffic to central repository, identifies failing users and failing services. Enforcement mode actually blocks/drops non-MNP traffic at the client level before network-level VLAN migration.

## Evidence

The simulator enabled: identifying devices with MNP-compliant traffic → automatic VLAN assignment; identifying devices/users/services relying on noncompliant traffic → initiate remediation projects; testing enforcement at client level (easy/fast to toggle) before committing to network-level VLAN migration. The Access Proxy handled most high-usage applications because Google's core philosophy favors browser-based applications — apps behind the Access Proxy have CNAMEs in public DNS, accessible from corporate and public networks with equivalent security, causing VPN usage to "immediately and dramatically decrease." Within one year of activating the automated analysis/verification/migration process, over 50% of the fleet was moved to non-privileged network access. The authors claim: "According to our rough estimates, the resultant productivity gains easily outweigh the implementation costs of BeyondCorp."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — Primary-source description of a specific operational tool with documented outcomes (50% fleet migration in one year). The Capirca-based implementation and two-mode operation (logging/enforcement) are specific technical details.

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
