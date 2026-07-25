---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/bsi
  - topic/zt-definition
  - topic/zt-governance
  - topic/zt-architecture
  - topic/zt-policy
claim_id: "bsi-zt.8"
statement: "BSI provides the only government framework for multi-organizational ZT architectures"
confidence: "medium"
confidence_rationale: "MEDIUM. The scenarios are conceptually clear but their practical viability depends on organizational dynamics and legal frameworks that I cannot"
claim_type: "definitional"
source_note: "[[BSI — Zero Trust Position Paper]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# bsi-zt.8: BSI provides the only government framework for multi-organizational ZT architectures

**Source:** [[BSI — Zero Trust Position Paper]] — BSI, *Zero Trust Position Paper*, 2023

## The Claim

Most ZT publications focus on single-organization architectures, but ZT is "especially motivated and driven by efforts toward stronger collaboration across organizational boundaries." The BSI proposes three multi-organizational scenarios:

| Scenario | Architecture | Governance |
|----------|-------------|------------|
| **Scenario 1: Bilateral, individual trust** | Each organization runs its own device management and PDP. Organization 2 provides a device management agent that Organization 1 installs on access-authorized clients. Organization 2's PDP evaluates Organization 1's devices against Organization 2's compliance requirements. | Organization 2 controls both the compliance evaluation and the PDP. Does not scale to many organizations. |
| **Scenario 2: Centralized services, individual PDP** | Device management is a centralized service providing uniform data foundation. Each organization retains its own PDP and decides which attributes to evaluate for its applications. | Flat hierarchy (two levels). Centralized data foundation with decentralized access decisions. |
| **Scenario 3: Centralized services, centralized PDP** | Both device management and PDP are centralized services. Provides unified data foundation and unified access policy management. Centralized vulnerability management also feeds the PDP. Both organizations can verify each other's compliance. | Most efficient for hierarchically structured organizations (e.g., corporations, federal/state administration). Requires clear division of responsibilities between organizations and centralized service operators. |

## Evidence

_No evidence separable from the claim statement in the source note._

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. The scenarios are conceptually clear but their practical viability depends on organizational dynamics and legal frameworks that I cannot fully assess from the text alone.

## Stakes

If multi-organizational ZT is the future (supply chain security, government-to-government data sharing, federated cloud), the BSI's framework is the only game in town. NIST 800-207 mentions cross-enterprise collaboration as one of five deployment scenarios but doesn't provide architectural patterns. CISA's model is single-organization. The BSI's three-scenario taxonomy fills a genuine gap in the ZT standards landscape.

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

Scenario 3 (centralized services + centralized PDP) is the most architecturally ambitious and the most politically challenging. It requires organizations to cede access control decisions to a central authority — something that may be legally impossible for sovereign government agencies or competing corporations. The BSI acknowledges this implicitly by noting that the model is most suitable for "hierarchically structured organizational units" (e.g., within a single corporation or federal administration). For the OSKG, this taxonomy is valuable as a reference for modeling trust relationships between organizations in a ZT context.
