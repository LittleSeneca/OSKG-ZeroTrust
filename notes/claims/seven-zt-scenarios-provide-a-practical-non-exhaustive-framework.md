---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-implementation
  - topic/zt-cloud
  - topic/zt-architecture
claim_id: "gc-scenarios.1"
statement: "Seven ZT scenarios provide a practical, non-exhaustive framework for identifying and prioritizing projects"
confidence: "high"
confidence_rationale: "HIGH. These seven scenarios reflect real enterprise patterns seen across the industry, and the consistent analytical framework (Considerations →"
claim_type: "implementation"
source_note: "[[Garbis and Chapman — Scenarios and Conclusion]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-scenarios.1: Seven ZT scenarios provide a practical, non-exhaustive framework for identifying and prioritizing projects

**Source:** [[Garbis and Chapman — Scenarios and Conclusion]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

The seven scenarios — VPN Replacement, Third-Party Access, Cloud Migration, Service-to-Service Access, DevOps, Mergers & Acquisitions/Divestiture, and Full Zero Trust Network/Network Transformation — "cover most of the major scenarios" and arm readers with "an understanding of how and when these different scenarios would be applicable in your environment, and to provide you with relevant recommendations for how to approach them."

## Evidence

Each scenario is analyzed through a consistent lens: Considerations (examining Resources, Users/User Experience, Identity Providers, and Networking/Architecture angles) followed by Recommendations. The analysis across all seven yields several recurring patterns:

1. **VPN Replacement** (Ch 18, scenario 1): The most common first ZT project. VPNs perpetuate perimeter-based models, create identity silos, struggle with distributed resources, and impose WAN costs. ZT provides multiple secure connections to distributed PEPs, better IdP integration, fine-grained policies, and can be deployed incrementally — group by group or application by application. Key recommendation: be aware of "webs of interdependent tools" built around legacy VPNs that may complicate incremental rollout.

2. **Third-Party Access** (Ch 18, scenario 2): Non-employees with a legal relationship to the enterprise, using unmanaged devices. The enterprise "cannot impose internal policies on external actors" (quoting NIST) but "may be able to implement some Zero Trust-based policies on nonenterprise users who have a special relationship with the organization." Key recommendations: use the third party's IdP for authentication if confidence in their maturity exists; enforce MFA under your control; consider tying access to business processes (e.g., service desk ticket state); agentless access is often required.

3. **Cloud Migration** (Ch 18, scenario 3): Four migration categories — Forklift, Refactor, Rewrite, Adopt SaaS — each presenting different ZT integration opportunities. ZT's dynamic and context-sensitive nature "can take advantage of the rich set of APIs presented by cloud platforms." Key recommendation: "be proactive and collaborate with your application owner colleagues. Exposing them to your Zero Trust platform architecture and roadmap can in fact be a catalyst for accelerating cloud migration projects."

4. **Service-to-Service Access** (Ch 18, scenario 4): Legitimate and important, but typically lower priority than user-to-service because servers are more controlled environments. The key value: Zero Trust enforces least privilege, provides "top-down visibility and control of service-to-service communications," and serves as "a form of referential integrity for the network" — unexpected communications are blocked, improving deployment maturity. Three architectural approaches: microsegmentation (all servers are identities), asymmetric service-to-service (one authenticated identity, one target behind a PEP), and IoT-style (neither authenticated — not recommended).

5. **DevOps** (Ch 18, scenario 5): ZT and DevOps are "both modern and effective approaches" that should be integrated. ZT applies across all DevOps phases — Plan/Code (educate developers on platform capabilities), Build/Test (automated policies granting access based on workload attributes), Release/Deploy (policies controlling production access via change windows), Operate/Monitor (identity-enriched logs). A ZT system "can be connected to an organization's DevOps platforms, and automatically adjust access as workloads flow through the full application lifecycle."

6. **M&A and Divestiture** (Ch 18, scenario 6): ZT provides a "unifying or normalizing layer on top of heterogeneous resources and networks" — near-immediate cross-domain access, IP address conflict mitigation, and avoidance of WAN deployment costs. For divestiture, ZT manages transitional access during the months-long technical unwinding.

7. **Full Zero Trust Network/Network Transformation** (Ch 18, scenario 7): The composite end-state — all users off the enterprise network, most private services behind PEPs (enclave-based model), some microsegmentation, some implicit trust zones. The key mindset shift: "the problem to be solved isn't 'remote access' — it's just 'access.'" "Be sure to define limits and have a realistic vision for your end state in mind."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. These seven scenarios reflect real enterprise patterns seen across the industry, and the consistent analytical framework (Considerations → Recommendations) makes them actionable.

## Stakes

If these seven scenarios are framed as an exhaustive taxonomy (which the authors explicitly deny), organizations may miss emerging use cases (IoT, OT, AI/ML workloads). If they're treated as independent silos, organizations miss the compounding value of a unified ZT platform. The authors acknowledge the scenarios are connected — "each of the previous six use cases is a microcosm of the ideas, approaches, and challenges of the full Zero Trust network scenario."

## Disagreement

**Who disagrees:**

NIST 800-207's five deployment scenarios (Ch 4) overlap substantially but differ in framing — NIST is topology-driven (satellite facilities, multi-cloud, contractors, cross-enterprise, public-facing), while Garbis & Chapman are use-case-driven (VPN replacement, third-party, cloud migration, etc.). Both are correct; they're different organizing principles. Green-Ortiz (Cisco Press) adds IoT/OT scenarios that Garbis & Chapman only address in Ch 16. Forrester's ZTX model organizes around pillars (data, networks, people, workloads, devices, visibility/automation) rather than scenarios.

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

The seven-scenario framework is the most useful practitioner-oriented ZT taxonomy in the literature. NIST's deployment scenarios answer "where should the PE/PA live?" while Garbis & Chapman answer "what business problem am I solving?" — and the second question is what actually gets projects funded. The consistent structure (considerations by Resources, Users, Identity Providers, Networking, and Architecture; followed by recommendations) makes this chapter directly usable as a project evaluation template.
