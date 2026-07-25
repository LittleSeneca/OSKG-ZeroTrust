---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/nist-sp-800-207
  - topic/zt-implementation
  - topic/zt-architecture
claim_id: "nist207-ch4.6"
statement: "Public-facing services expose ZTA's boundary — ZT tenets do not directly apply to anonymous public resources, and for registered users the enterprise is constrained in what cybersecurity policies can be enforced on nonenterprise-owned devices, limiting ZTA to behavioral monitoring and graduated enforcement."
confidence: "high"
confidence_rationale: "VERY HIGH. NIST's honesty about ZTA's limits here is as important as its prescriptions — this is the boundary condition that prevents ZT overreach"
claim_type: "implementation"
source_note: "[[NIST 800-207 — Ch4 — Deployment Scenarios]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# nist207-ch4.6: Public-facing services expose ZTA's boundary — ZT tenets do not directly apply to anonymous public resources, and for registered users the enterprise is constrained in what cybersecurity policies can be enforced on nonenterprise-owned devices, limiting ZTA to behavioral monitoring and graduated enforcement.

**Source:** [[NIST 800-207 — Ch4 — Deployment Scenarios]] — Scott Rose et al., *NIST SP 800-207 — Zero Trust Architecture*, 2020

## The Claim

Public-facing services that may or may not require user registration. This covers anonymous public resources (e.g., a public web page), registered customers with business relationships, and special users (e.g., employee dependents). The key constraint: **requesting assets are not enterprise-owned, and the enterprise is limited in what cybersecurity policies it can enforce.**

## Evidence

**How ZTA applies:**

- **Anonymous public resources**: ZT tenets "do not directly apply." The enterprise cannot control the state of requesting assets, and anonymous resources don't require credentials. NIST is honest here: ZT has limits.
- **Registered public users**: The enterprise can enforce password policies, MFA, and credential lifecycle management. But it "is constrained as to what internal cybersecurity polices can be enforced on nonenterprise-owned devices."
- **Behavioral monitoring for attack detection**: "A sudden increase in access requests from unknown browser types or known outdated versions could indicate an automated attack of some kind, and the enterprise could take steps to limit requests from these identified clients." This is ZT-adjacent — using telemetry from incoming requests for threat detection, even without device trust.
- **Legal/regulatory constraints**: "The enterprise should also be aware of any statutes or regulations regarding what information can be collected and recorded about the requesting users and assets." Privacy limitations on user/device data collection constrain ZT telemetry in this scenario.

**Cross-references:**

| Source | How It Relates |
|--------|---------------|
| **BeyondCorp** (Google) | Google's public-facing services (Gmail, G Suite) use the same access proxy infrastructure as internal services. Registered users (customers) authenticate and the proxy evaluates device/browser signals. Anonymous services (google.com) don't route through the proxy. This mirrors NIST's split: registered = ZT applies, anonymous = ZT doesn't apply. |
| **DoD ZT Reference Architecture v2** | The DoD RA's Data Pillar addresses public-facing data access through encryption, DRM, and DLP. For registered users accessing DoD data portals (e.g., veteran benefits), attribute-based access control and continuous monitoring apply — but DoD can mandate CAC/PIV for military users, while public users can't be required to use government-issued hardware. |
| **Green-Ortiz (Cisco Press)** | Ch 9 ("Zero Trust Enforcement") addresses graduated enforcement: different policy strictness for managed vs. unmanaged devices. For registered public users with unmanaged devices, Green-Ortiz would apply baseline policies (MFA, geolocation checks, behavioral analytics) without requiring device agents. This is the practical implementation of NIST's "limited to what can be enforced." |

**Operational implication:**

Scenario 4.5 is NIST's admission that ZT has a boundary. You can't enforce device trust on a customer's personal laptop. The best you can do is behavioral analytics at the application layer. This is the scenario where ZTA blurs into traditional application security — WAF, bot detection, rate limiting — which NIST doesn't dwell on. The chapter's honesty about this limitation is as important as its prescriptions for the other four scenarios.

## Confidence

**Rating:** HIGH
**Rationale:** VERY HIGH. NIST's honesty about ZTA's limits here is as important as its prescriptions — this is the boundary condition that prevents ZT overreach claims.

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
  - [[zt-network-assumptions]]

## Assessment

_Not addressed separately in the source note._
