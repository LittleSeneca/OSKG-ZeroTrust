---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-identity
  - topic/zt-implementation
  - topic/zt-governance
  - topic/zt-cloud
  - topic/zt-federation
claim_id: "nist207-ch4.5"
statement: "Cross-enterprise collaboration should use federated identity plus resource-specific PEPs — this scales linearly with partners, while the alternative (bilateral VPNs, shared AD domains, per-partner firewall rules) creates O(n²) complexity."
confidence: "high"
confidence_rationale: "HIGH. The federated identity pattern is well-established and the scaling argument is mathematically sound."
claim_type: "implementation"
source_note: "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch4.5: Cross-enterprise collaboration should use federated identity plus resource-specific PEPs — this scales linearly with partners, while the alternative (bilateral VPNs, shared AD domains, per-partner firewall rules) creates O(n²) complexity.

**Source:** [[NIST 800-207 — Ch4 — Deployment Scenarios]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

Two enterprises (e.g., federal agencies, or a federal agency and a private company — G2G or G2B) collaborate on a project. Enterprise A operates a database but must grant access to certain Enterprise B employees — without granting access to any other Enterprise A resources. This is the **federated identity** scenario.

## Evidence

**How ZTA applies:**

- **Federated ID management** — both organizations enrolled in a federated identity system. Enterprise B subjects authenticate through their own IdP, and Enterprise A's PEP trusts the federated assertion. No separate Enterprise A accounts needed.
- **No complex firewall rules or ACLs** — "there do not need to be complex firewall rules or enterprise-wide access control lists (ACLs) allowing certain IP addresses belonging to Enterprise B to access resources in Enterprise A based on Enterprise A's access policies."
- **Cloud-hosted PE/PA** — "a PE and PA hosted as a cloud service may provide availability to all parties without having to establish a VPN or similar." Cross-enterprise access shouldn't require bilateral network integration.
- **Agent or web gateway access** — Enterprise B employees use an installed agent or a portal, identical to Scenario 4.1.

**Cross-references:**

| Source | How It Relates |
|--------|---------------|
| **BeyondCorp** (Google) | Google's federated access model for partners and acquired companies. BeyondCorp's access proxy can consume federated identity assertions — partners authenticate at their own IdP, and Google's policy engine makes access decisions based on the federated claim. This is exactly NIST's scenario. |
| **DoD ZT Reference Architecture v2** | The DoD RA emphasizes "joint all-domain" operations requiring cross-agency and cross-classification data sharing. The User Pillar explicitly addresses federated identity and attribute-based access control (ABAC) — the mechanism for granting Enterprise B members access to specific Enterprise A resources without full network integration. |
| **Green-Ortiz (Cisco Press)** | Ch 5 ("Enclave Exploration and Consideration") covers cross-organization considerations. Green-Ortiz emphasizes that different organizations may have different ZT maturity levels, and the collaboration boundary must accommodate the least mature partner — a practical constraint NIST doesn't address. |

**Operational implication:**

Cross-enterprise collaboration is the scenario where ZT pays for itself fastest. The alternative — bilateral VPNs, shared AD domains, per-partner firewall rules — creates an O(n²) complexity problem. Federated identity + resource-specific PEPs scales linearly with the number of partners. This is the pattern that enables secure government-to-contractor collaboration without network-level trust.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The federated identity pattern is well-established and the scaling argument is mathematically sound.

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
  - [[ficam-identity-substrate-zta]]

**Extends:**

## Assessment

_Not addressed separately in the source note._
