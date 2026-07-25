---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-architecture
  - topic/zt-policy
claim_id: "gc-iam-policy.12"
statement: "The policy evaluation flow — PDP grants, PEP renders and enforces — establishes a clear division of labor with specific attribute refresh implications"
confidence: "high"
confidence_rationale: "HIGH. This flow is consistent with NIST 800-207's PDP/PEP model and the control plane / data plane split from Gilman & Barth. The trigger taxonomy is"
claim_type: "architectural"
source_note: "[[Garbis and Chapman — Practice IAM Policy]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-iam-policy.12: The policy evaluation flow — PDP grants, PEP renders and enforces — establishes a clear division of labor with specific attribute refresh implications

**Source:** [[Garbis and Chapman — Practice IAM Policy]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"The PDP takes as input the set of attributes for the identity, device, and system, and uses them to evaluate the set of policies in the policy store." The PEP is then responsible for "fully rendering any targets" by interrogating its environment and "enforcing any access-time conditions."

## Evidence

Figure 17-6 shows the complete flow: PDP evaluates Subject Criteria against identity/device/system attributes → transmits granted policies (actions, targets, conditions) to PEP → PEP finishes rendering dynamic targets (DNS resolution, tag matching) → PEP evaluates conditions at access time. Figure 17-7 identifies four trigger types: Authentication (~once/day), Access (many times/day — every packet, connection, or periodically), Session Expiration (~2–3 hours), and External (arbitrary API-driven). The attribute permanence table (Table 17-6) maps attributes from Permanent (biometrics, OS) to Frequent (geolocation, IP address, network risk level) — guiding which are evaluated at PDP time (session establishment) vs. PEP time (access).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This flow is consistent with NIST 800-207's PDP/PEP model and the control plane / data plane split from Gilman & Barth. The trigger taxonomy is the most complete in ZT literature.

## Stakes

The PDP/PEP division determines where attributes are refreshed. If frequently-changing attributes (device IP, geolocation) are only evaluated at PDP authentication time, policies can be stale for hours. The condition mechanism in PEPs solves this.

## Disagreement

**Who disagrees:**

The authors present the criteria-based approach (all criteria must be satisfied) vs. NIST's score-based approach (weighted trust score). They don't endorse one over the other but note that criteria-based is "simpler to think about." In practice, criteria-based maps to ABAC policies; score-based enables graduated access (e.g., read vs. read/write based on trust level).

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

The trigger taxonomy is the most operationally useful framework in Ch17. Security architects can use it to plan: "Which attributes change fast enough to require PEP-level condition evaluation? Which can we batch at session refresh?" The 2–3 hour session duration recommendation for users (with configurable MFA prompting) is a practical starting point that balances security with user experience.
