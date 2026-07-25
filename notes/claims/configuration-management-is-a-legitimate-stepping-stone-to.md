---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-migration
  - topic/zt-implementation
  - topic/zt-cloud
  - topic/zt-architecture
claim_id: "gb-ch9.3"
statement: "Configuration management is a legitimate stepping stone to the control plane"
confidence: "high"
confidence_rationale: "HIGH. This pattern is validated by PagerDuty's production ZT network (2013–2014, still running) and mirrors the NIST 800-207 hybrid approach"
claim_type: "migration"
source_note: "[[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch9.3: Configuration management is a legitimate stepping stone to the control plane

**Source:** [[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

The mature ZT control plane systems (policy engine, trust engine, controller) are ideal but unnecessary at the start. Configuration management tools (Chef, Puppet, Ansible) can serve as a "temporary stepping stone" — driving host-based firewalls, cryptographic configuration, and policy distribution — while the network matures.

## Evidence

- Chef was already deployed on every VM; extending it to generate iptables rules required no new infrastructure
- Role-based iptables chains enumerated expected IPs for each server role, providing per-host microsegmentation
- Benefits: network compute power scales with instance count; failures are isolated (many small firewalls instead of "the firewall")
- Downsides: eventual consistency means policy changes aren't instantaneous; constant validation of expected state is required
- **Maturation path:** as the system grew, IPsec configuration graduated out of Chef into a dedicated service that could converge faster

**Cross-reference — NIST 800-207 Ch7:**

NIST's Step 5 (Identify Candidate Solutions) explicitly considers client footprint, protocol support, and deployment model. The CM-driven approach maps to the agent-based gateway model in NIST's taxonomy — it requires components on the client asset but doesn't require new central infrastructure.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This pattern is validated by PagerDuty's production ZT network (2013–2014, still running) and mirrors the NIST 800-207 hybrid approach. CM-driven policy distribution is how most organizations will start their ZT journey — it doesn't require buying new infrastructure.

## Stakes

CM as a stepping stone is pragmatic but insufficient for mature ZT. Host-based enforcement is vulnerable if the host is compromised. Mature systems push enforcement across an isolation boundary (hypervisor, host OS in containerized systems, network security groups).

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
