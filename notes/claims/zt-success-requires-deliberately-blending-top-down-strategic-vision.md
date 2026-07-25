---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-implementation
  - topic/zt-governance
  - topic/zt-cloud
  - topic/zt-architecture
claim_id: "gc-scenarios.2"
statement: "ZT success requires deliberately blending top-down strategic vision with bottom-up tactical execution"
confidence: "high"
confidence_rationale: "HIGH. The sample deployments are idealized but structurally realistic. The emphasis on *deliberately* blending strategic and tactical perspectives is"
claim_type: "governance"
source_note: "[[Garbis and Chapman — Scenarios and Conclusion]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-scenarios.2: ZT success requires deliberately blending top-down strategic vision with bottom-up tactical execution

**Source:** [[Garbis and Chapman — Scenarios and Conclusion]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

"Take a focused and incremental approach while still keeping sight of (and planning for) your larger Zero Trust initiative, and consciously taking the time to build bridges and lines of communication with your peers across the organization." The top-down/bottom-up distinction is "an artificial distinction" — "every Zero Trust project and initiative will combine elements of both." "Deliberately including strategic aspects within a tactical first Zero Trust project is an excellent way to set yourself up for approved and supported second and third projects."

## Evidence

Two detailed sample deployments illustrate the blended approach:

*Tactical Project (transportation services org):* Third-party financial analysts accessing on-prem systems via VPN. Audit findings (MFA requirement, zombie account cleanup) create the catalyst. The 7-step project timeline spans ~3 months: Define Problem → Research Solutions → Review Architecture → POC Two Platforms → Present Results → Production Pilot (1 month) → Full Rollout. The security team deliberately involves the enterprise architecture team at multiple checkpoints, "knowing that they intend to grow the scope and maturity of their Zero Trust initiative over time." Key structural choices: parallel VPN/ZT access during pilot so users can switch back, formal "go/no-go" gate before production, promotion of success to generate momentum.

*Strategic Initiative (pharmaceutical company):* A near-miss ransomware incident creates board-level demand for change. The CISO structures a two-phase program: Phase 1 (immediate) secures highest-value assets with MFA, device posture checks, network segmentation; Phase 2 (longer-term) moves all users "off net," migrates to cloud-based IDaaS, and incorporates IaaS/PaaS. The first project is deliberately focused — addressing the most immediate weaknesses — while establishing the platform for broader rollout. The organization uses five value drivers (Security, Audit/Compliance, Agility, Customer/Partner Integrations, Technology Modernization) on a radar chart to quantify each project's impact. Formal Architecture and Change Management boards are strengthened; a Governance board is deemed unnecessary because the Architecture board already incorporates risk and compliance.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The sample deployments are idealized but structurally realistic. The emphasis on *deliberately* blending strategic and tactical perspectives is the chapter's most important organizational insight.

## Stakes

Organizations that go purely tactical risk building a brittle, one-off solution that can't scale. Organizations that go purely strategic risk "analysis paralysis" — years of planning without production deployment. The blended approach is harder to execute but more likely to deliver sustained value.

## Disagreement

**Who disagrees:**

Forrester's ZTX framework is inherently strategic — it assumes an organization-wide transformation program. Google's BeyondCorp was essentially a top-down initiative (though incremental in rollout). The Software-Defined Perimeter case study from Ch 4 was purely tactical. The tension between "strategic ZT program" and "tactical ZT project" is real, and different organizations in different circumstances will favor one pole. Garbis & Chapman's contribution is acknowledging that the best outcomes come from deliberately mixing both.

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

The blended approach is correct but under-specified. The authors don't provide criteria for *when* to emphasize strategic vs. tactical, or *how much* strategic scaffolding a tactical first project needs. The pharmaceutical company example leans heavily on a crisis catalyst — without it, would the same approach work? The transportation example is more broadly applicable but assumes a receptive enterprise architecture team, which many organizations lack. This gap is where the NIST 800-207 migration chapter (Ch 7) provides complementary guidance at the capability level.
