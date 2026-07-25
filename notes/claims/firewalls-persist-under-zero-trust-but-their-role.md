---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-network
  - topic/zt-architecture
  - topic/zt-policy
  - topic/zt-identity
claim_id: "gc-net-access.1"
statement: "Firewalls persist under Zero Trust but their role bifurcates — rules simplify dramatically as enforcement shifts to ZT PEPs, and the access controls historically attempted with firewalls are achieved more effectively through identity-centric policy."
confidence: "high"
confidence_rationale: "HIGH — The firewall evaluation is systematic across three deployment scenarios. The verdict is measured (persist but simplify) rather than"
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Network and Access Technologies]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-net-access.1: Firewalls persist under Zero Trust but their role bifurcates — rules simplify dramatically as enforcement shifts to ZT PEPs, and the access controls historically attempted with firewalls are achieved more effectively through identity-centric policy.

**Source:** [[Garbis and Chapman — Network and Access Technologies]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

Garbis & Chapman present three scenarios: (A) Traditional IP-centric 5-tuple rules with "impoverished vocabulary" that cannot express identity or context, leading to overprivileged access; (B) PEP behind firewall — firewall rules simplify dramatically as enforcement shifts to the ZT PEP; (C) PEP merged with firewall — functionally equivalent to B. Their verdict: "Firewalls will continue to exist in Zero Trust networks, but with simplified configurations, fewer rules, and reduced management burden. The access controls historically attempted with firewalls are achieved more effectively through Zero Trust PEPs. Organizations can reduce firewall size, complexity, and cost."

## Evidence

The 5-tuple model (`src IP, src port, dest IP, dest port, protocol`) is explicitly critiqued: IP addresses are not identities and get remapped across subnets. The authors provide a figure (6-1) showing the three deployment scenarios and their policy complexity implications. The firewall's retained role is for advanced features that access switches cannot provide (IPS, malware detection, TCP normalization, VPN termination).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The firewall evaluation is systematic across three deployment scenarios. The verdict is measured (persist but simplify) rather than absolutist, consistent with Green-Ortiz and the BeyondCorp papers which also preserve firewalls as one enforcement layer among many.

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
