---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-architecture
  - topic/zt-network
  - topic/zt-implementation
  - topic/zt-policy
claim_id: "gb-ch7-8.12"
statement: "Three types of filtering form a defense-in-depth network security architecture"
confidence: "high"
confidence_rationale: "HIGH. This three-tier filtering model is architecturally sound and operationally validated. Calico and similar CNI plugins implement host + bookended"
claim_type: "architectural"
source_note: "[[Gilman and Barth — Ch7-8 — Applications and Traffic]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch7-8.12: Three types of filtering form a defense-in-depth network security architecture

**Source:** [[Gilman and Barth — Ch7-8 — Applications and Traffic]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

Filtering in zero trust operates at three levels: (1) **Host filtering** — every endpoint filters its own traffic via on-host firewalls (iptables, BPF, Windows Firewall). (2) **Bookended filtering** — egress filtering is applied alongside ingress, so both sender and receiver enforce policy, providing "herd immunity" against misconfiguration. (3) **Intermediary filtering** — network devices between endpoints (perimeter devices, SDN fabric) apply additional filtering, particularly for high-volume attack traffic that would overwhelm software firewalls if it reached the host.

## Evidence

Host filtering: all modern OSes include firewalls (except iOS and Android, which the authors note as a gap). Bookended filtering example: a database server's ingress rules are accidentally loosened by an administrator. If application servers also have egress rules that only allow connections to the database, the misconfiguration is contained. Intermediary filtering: EC2 Security Groups implement filtering outside the VM for isolation (Figure 8-9). Project Calico demonstrates distributed host + bookended filtering at scale. UPnP is contrasted: unlike ZT-derived perimeter policies, UPnP allows _any_ application to reconfigure the perimeter without a chain of trust.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This three-tier filtering model is architecturally sound and operationally validated. Calico and similar CNI plugins implement host + bookended filtering. Cloud security groups implement intermediary filtering isolated from guest VMs.

## Stakes

Without all three filtering tiers, there are gaps. Host-only filtering means the network incurs cost to transport packets that are ultimately dropped, and a compromised host can disable its own firewall. Intermediary-only filtering is the perimeter model the authors spent Chapter 1 dismantling. Bookended filtering is the least common but provides the "herd immunity" property — it's the safety net for human error.

## Disagreement

**Who disagrees:**

The tension is between the authors' "start at the host and work outward" philosophy and traditional network engineering's "filter at the perimeter first" instinct. The authors explicitly address this: they don't throw out perimeter concepts, but they reorder the priority — host filtering is the foundation, intermediary filtering is an enhancement.

**Cross-reference — NSA Network Pillar: Granular traffic filtering.** NSA's Network pillar specifies microsegmentation based on application profiles and data flows, with continuous authentication of connectivity. At Advanced maturity, central management platforms provide automated visibility and security monitoring including alerting on anomalous behavior. This aligns with the authors' vision of programmable network fabric driven by application-aware policy.

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

The three-tier model is the chapter's most durable architectural contribution. It resolves the false dichotomy between "firewalls are dead" (extreme ZT) and "just add more firewalls" (perimeter thinking). The correct answer: filtering everywhere, at every tier, with host filtering as the foundation and intermediary filtering as the optimization layer.
