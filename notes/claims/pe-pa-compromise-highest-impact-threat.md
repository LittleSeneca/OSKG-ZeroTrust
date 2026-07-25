---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-threats
  - topic/zt-architecture
  - topic/zt-network
  - topic/zt-governance
claim_id: "nist207-ch5.1"
statement: "Subversion of the ZTA decision process (PE/PA compromise) is the highest-impact threat because the PE and PA are the linchpins of all resource access — their compromise collapses the entire access control fabric."
confidence: "high"
confidence_rationale: "HIGH. The PE/PA are single points of policy enforcement — this is an architectural fact, not speculation. **Cross-reference — Gilman & Barth: Control"
claim_type: "threat"
source_note: "[[NIST 800-207 — Ch5 — Threats]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch5.1: Subversion of the ZTA decision process (PE/PA compromise) is the highest-impact threat because the PE and PA are the linchpins of all resource access — their compromise collapses the entire access control fabric.

**Source:** [[NIST 800-207 — Ch5 — Threats]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

The PE and PA are the linchpins of a ZTA — no inter-resource communication occurs without their approval. If an attacker subverts these components, the entire access control fabric collapses. (§5.1)

## Evidence

- Configuration abuse: An administrator with PE configuration access can make unapproved changes or errors that disrupt operations.
- Compromised PA: A subverted PA could grant access to otherwise-denied resources (e.g., a personally-owned rogue device).
- Mitigations: Proper configuration, continuous monitoring, logging of all configuration changes, and audit.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The PE/PA are single points of policy enforcement — this is an architectural fact, not speculation.

**Cross-reference — Gilman & Barth: Control Plane Security**

Gilman & Barth devote a full section of Chapter 10 to this exact threat. They warn that compromising the policy engine leads to "a complete compromise of zero trust authorization, allowing the attacker to authorize anything they please." Their mitigations align with NIST's but go further:
- Group authentication/authorization for changes to sensitive control plane systems
- Changes should be infrequent and generate broadly visible alerts
- Administrative isolation (dedicated cloud account, rigorous access control) while keeping systems logically integrated into the network
- Eventually apply zero trust enforcement to the control plane itself ("rewriting the C compiler in C")

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
