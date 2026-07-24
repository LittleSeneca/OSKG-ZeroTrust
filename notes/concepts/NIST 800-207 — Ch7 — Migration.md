---
tags:
  - source/standards
  - nist
  - zt-migration
  - zt-implementation
  - brownfield
  - oskg-zerotrust
created: 2026-07-24
related:
  - "[[NIST 800-207 — Overview]]"
  - "[[NIST 800-207 — Ch6 — ZTA Deployment Models]]"
  - "[[Migration Approaches (Finney)]]"
  - "[[Migration (Gilman & Barth)]]"
  - "[[Implementation (Green-Ortiz)]]"
  - "[[DoD ZT Strategy & Roadmap]]"
  - "[[Concepts Index]]"
source: "[[_txt/NIST_SP_800-207_Zero_Trust_Architecture.txt|NIST SP 800-207]] §7, pp. 37–42"
---

# NIST 800-207 — Ch7 — Migrating to a Zero Trust Architecture

> *"Implementing a ZTA is a journey rather than a wholesale replacement of infrastructure or processes."*
> — NIST SP 800-207, §7

## Overview

Chapter 7 shifts from *what* a Zero Trust Architecture is to *how* to get there. NIST explicitly frames ZTA adoption as **incremental, process-driven, and indefinite** — not a one-time forklift upgrade. Most enterprises will operate in a **hybrid zero-trust/perimeter-based mode** for an extended period while continuing IT modernization initiatives. The chapter provides a concrete 7-step deployment cycle that maps to the NIST Risk Management Framework ([[NIST SP 800-37]]).

---

### Claim 1: ZTA migration is an incremental, recurring cycle — not a linear project — and most enterprises will operate in a hybrid zero-trust/perimeter-based mode indefinitely.

**Author's claim:** "Implementing a ZTA is a journey rather than a wholesale replacement of infrastructure or processes." Migration is a **recurring cycle**, not a linear project. After the first business process is migrated, the cycle repeats for each subsequent process, and existing ZTA deployments must be reevaluated whenever the underlying workflow changes. (§7 overview)

**Evidence presented:** The chapter's structure — a 7-step recurring cycle — is itself the evidence. NIST frames the entire process as iterative: after step 7, return to step 1 for the next candidate business process.

**Confidence:** VERY HIGH. This is NIST's explicit framing, and it's the organizing principle of the entire chapter.

---

### Claim 2: Pure greenfield ZTA is rarely viable for existing organizations, but new infrastructure projects (new applications, services, databases) create opportunities to introduce ZT concepts to some degree.

**Author's claim:** In a greenfield scenario, an enterprise can design a pure ZTA from the start: identify workflows, narrow components, engineer against ZT tenets, evaluate trust before access, and establish micro-perimeters. But this is **rarely viable** for federal agencies or any organization with an existing network. (§7.1)

**Evidence presented:**
- NIST acknowledges the greenfield ideal but immediately caveats: "new responsibilities that require building new infrastructure (a new application, service, or database) create opportunities to introduce ZT concepts to some degree."
- Success depends on how dependent the new infrastructure is on existing resources (e.g., identity management systems).
- References [[NIST SP 800-160v1]] (Systems Security Engineering) as the companion framework for greenfield ZT design.

**Confidence:** HIGH. NIST's honesty about greenfield impracticality is notable — most ZT marketing implies greenfield is the target, but NIST says it's the exception.

**Cross-reference:** Finney's [[Project Zero Trust]] structures the entire book around an organizational narrative of how ZT adoption unfolds inside an enterprise — the greenfield scenario maps loosely to the "new initiative" pattern where a team gets to build fresh rather than retrofitting.

---

### Claim 3: The hybrid model — ZTA workflows coexisting with non-ZTA workflows — is the expected indefinite reality, requiring common infrastructure (ID management, device management, logging) to operate in dual mode and migration to proceed one business process at a time.

**Author's claim:** "It is unlikely that any significant enterprise can migrate to zero trust in a single technology refresh cycle." The hybrid model is the expected reality for the indefinite future. (§7.2)

**Evidence presented (key characteristics):**
- Migration proceeds **one business process at a time**
- Common elements (identity management, device management, event logging) must be **flexible enough to operate in both ZTA and perimeter-based modes**
- Enterprise architects should **restrict ZTA candidate solutions to those that can interface with existing components**
- Migrating an existing workflow to ZTA likely requires at least a **partial redesign**
- The Policy Engine must handle both ZTA and legacy access patterns simultaneously

**Confidence:** VERY HIGH. The hybrid reality is a core NIST assertion and consistent with every major ZT implementation account.

**Cross-reference:** Gilman & Barth's [[Zero Trust Networks]] devotes substantial attention to the migration problem — their proxy-based architecture is explicitly designed to be introduced incrementally at the network boundary, making it one of the more migration-friendly ZTA deployment models. Green-Ortiz et al.'s [[Zero Trust Architecture]] treats migration as a formal lifecycle phase with maturity progression. The [[DoD ZT Strategy & Roadmap]] operationalizes this hybrid concept with target-level milestones for federal systems.

---

### Claim 4: Before the 7-step cycle can begin, the enterprise must establish a foundational inventory of all actors, assets, and business processes — without this, the Policy Engine will deny requests due to insufficient information and shadow IT deployments may break silently.

**Author's claim:** "An enterprise cannot determine what new processes or systems need to be in place if there is no knowledge of the current state of operations." (§7.3 prerequisites)

**Evidence presented:**
- Three parallel surveys form the prerequisite: actor inventory, asset inventory, process/data flow inventory.
- Without this baseline, the Policy Engine will deny requests due to insufficient information — especially problematic for unknown "shadow IT" deployments.
- The surveys map to the [[NIST SP 800-37]] Risk Management Framework (RMF) — ZTA adoption is fundamentally a risk reduction exercise.

**Confidence:** HIGH. The inventory-is-prerequisite claim is structural — it follows directly from the Policy Engine's need for input data to make access decisions.

---

### Claim 5: All enterprise subjects — human users and Non-Person Entities (service accounts, automated processes) — must be identified, with special-privilege users requiring additional scrutiny and stricter confidence levels under ZTA rather than blanket trust. (Step 1 of the deployment cycle)

**Author's claim:** The Policy Engine must have knowledge of **all enterprise subjects** — both human users and Non-Person Entities (NPEs). Special-privilege users (developers, system administrators) require **additional scrutiny**. (§7.3.1)

**Evidence presented:**
- In legacy architectures, privileged accounts often have **blanket permission** to access all enterprise resources.
- ZTA should instead allow sufficient flexibility while using **logs and audit actions** to identify access behavior patterns.
- Administrators may need to satisfy a more stringent confidence level, as outlined in [[NIST SP 800-63A]], Section 5.
- Key shift: from *privileged accounts have implicit trust* to *privileged accounts have stricter verification requirements*.

**Confidence:** HIGH. The inversion of privileged account treatment — from most trusted to most scrutinized — is a fundamental ZTA principle.

**Cross-reference:** Finney's [[Project Zero Trust]] frames this as the "identity is the new perimeter" problem. The [[DoD ZT Strategy]] emphasizes identity as Pillar 1 and requires attribute-based access control (ABAC) for all user authorizations.

---

### Claim 6: The enterprise must identify, catalog, and continuously monitor all assets — hardware, digital artifacts, virtual infrastructure, and shadow IT — because device posture assessment is integral to access decisions and incomplete inventory causes access denials. (Step 2 of the deployment cycle)

**Author's claim:** ZTA requires the ability to **identify and manage devices** — both enterprise-owned and non-enterprise-owned (BYOD, collaborator assets) that access enterprise resources. (§7.3.2)

**Evidence presented:**

| Category | Examples |
|----------|----------|
| **Hardware** | Laptops, phones, IoT devices, servers |
| **Digital artifacts** | User accounts, applications, digital certificates, virtual assets, containers |
| **Physical location** | As best estimated |
| **Network location** | Observed and tracked |

- Beyond cataloging, the enterprise must have **configuration management and monitoring** — the ability to observe the current state of an asset.
- **Shadow IT** presents a special problem: certain ZTA approaches (mainly network-based) may cause shadow IT components to become **unusable** because they are not known and included in network access policies.
- **Federal context:** Agencies with CDM program capabilities (HWAM, SWAM) already have a rich data set. High Value Assets (HVA) identified under [[OMB M-19-03]] provide ZTA candidate lists.

**Confidence:** HIGH. Asset inventory as prerequisite is consistent across NIST, CISA, and DoD frameworks.

**Cross-reference:** Gilman & Barth's [[Zero Trust Networks]] emphasizes that device identity and trust are co-equal to user identity. Green-Ortiz et al.'s [[Zero Trust Architecture]] adds the cloud-native dimension: asset inventory now includes containers, serverless functions, and ephemeral compute that may exist for minutes.

---

### Claim 7: Business process selection for ZTA migration should start with low-risk processes and cloud-based/remote-worker workflows, using the NIST RMF to evaluate tradeoffs in performance, user experience, and workflow fragility. (Step 3 of the deployment cycle)

**Author's claim:** The enterprise must **identify and rank business processes, data flows, and their relation to agency missions**. (§7.3.3)

**Evidence presented (selection strategy):**
- **Start with a low-risk business process** for the first ZTA transition — disruptions will likely not negatively impact the entire organization.
- Once enough experience is gained, **more critical business processes** become candidates.
- **Cloud-based resources** and **remote worker workflows** are often good candidates — rather than projecting the enterprise perimeter into the cloud or using VPNs, clients can request cloud services directly through PEPs.
- **Tradeoffs to consider:** performance degradation, user experience changes, possible increased workflow fragility.
- Risk evaluation should use the NIST Risk Management Framework ([[NIST SP 800-37]]).

**Confidence:** HIGH. The "start low-risk, scale up" pattern is standard migration guidance and well-supported.

**Cross-reference:** This is where the organizational narrative from Finney's [[Project Zero Trust]] is most relevant — selecting the first pilot process is as much a political and organizational decision as a technical one. Green-Ortiz et al.'s [[Zero Trust Architecture]] provides a maturity model that maps candidate processes to organizational readiness levels.

---

### Claim 8: Policy formulation for the ZTA candidate requires evaluating asset value/risk via RMF, identifying all upstream/downstream resources, and choosing between criteria-based (binary) and score-based (confidence-weighted) trust evaluation — a choice with cascading effects on tooling and operational complexity. (Step 4 of the deployment cycle)

**Author's claim:** After identifying a candidate workflow, the enterprise must evaluate value/risk, identify all upstream/downstream resources, and determine access criteria. (§7.3.4)

**Evidence presented:**
1. **Evaluate the value/risk** of the asset or workflow using the NIST RMF ([[NIST SP 800-37]])
2. **Identify all upstream resources** (ID management systems, databases, micro-services), **downstream resources** (logging, security monitoring), and **entities** (subjects, service accounts)
3. **Determine the access criteria** — either criteria-based (TA using binary rules) or score-based (TA using confidence level weights) — see NIST 800-207 §3.3.1
- **Candidate selection influence:** An application used by a specific subset of subjects (e.g., purchasing) may be preferred over one vital to the entire subject base (e.g., email).
- **Tuning:** Administrators may need to adjust criteria or confidence weights during the tuning phase.

**Confidence:** HIGH. The criteria-vs-score choice is a genuine architectural decision point with documented tradeoffs.

**Cross-reference:** Gilman & Barth's [[Zero Trust Networks]] provides detailed guidance on constructing trust scores and policy logic. The [[DoD ZT Strategy]] mandates automated policy decision points with continuous runtime authorization.

---

### Claim 9: Candidate solution selection must evaluate client footprint, traffic patterns, logging/analysis capabilities, protocol support, and subject behavior changes — with a recommended pilot approach that serves as a proving ground before full transition. (Step 5 of the deployment cycle)

**Author's claim:** Enterprise architects compose a list of candidate solutions, evaluating them against five factors. (§7.3.5)

**Evidence presented (evaluation factors):**

| Factor | Question |
|--------|----------|
| **Client footprint** | Does the solution require components installed on the client asset? This may limit BYOD or cross-agency collaboration. |
| **Traffic pattern** | Does the solution work where resources exist on enterprise premises (east-west traffic), or does it assume cloud-resident resources (north-south traffic)? |
| **Logging and analysis** | Does the solution provide a means to log interactions for analysis that feeds back into the Policy Engine? |
| **Protocol support** | Does the solution support a broad range of protocols (web, SSH, etc.) and transports (IPv4, IPv6), or is it narrowly focused? |
| **Subject behavior** | Does the solution require changes to how enterprise subjects perform their workflow? |

- **Recommended approach:** Model the existing business process as a **pilot program** rather than just a replacement. The pilot serves as a "proving ground" for ZTA before transitioning subjects away from legacy process infrastructure.

**Confidence:** HIGH. The evaluation factors are concrete and operational — they reflect genuine deployment tradeoffs.

**Cross-reference:** This solution-selection phase corresponds to the architecture decisions that Gilman & Barth's [[Zero Trust Networks]] addresses through detailed protocol-level analysis. Green-Ortiz et al.'s [[Zero Trust Architecture]] provides vendor-neutral evaluation criteria and decision matrices. The [[DoD ZT Reference Architecture v2.0]] specifies approved deployment patterns for federal environments.

---

### Claim 10: Initial ZTA deployment should operate in reporting-only (observation) mode — not immediate enforcement — because few policy sets are complete on the first iteration, and the monitoring phase collects real access pattern data to establish a baseline against which anomalous behavior can be identified. (Step 6 of the deployment cycle)

**Author's claim:** Initial deployment begins with an **observation and monitoring mode** — NOT immediate enforcement. "Few enterprise policy sets are complete in their first iterations." (§7.3.6)

**Evidence presented:**
- Important accounts may be denied access they need, or may retain more privileges than required.
- **Recommended approach: reporting-only mode** — grant access for most requests initially, log and trace all connections, compare actual access patterns against initial policy, enforce only the most basic policies (deny requests that fail MFA or appear from known attacker-controlled IPs).
- **Why lenient?** To collect data from actual interactions. Once a baseline of activity patterns is established, anomalous behavior can be more easily identified.
- If reporting-only mode is not possible, operators must **monitor logs closely and be prepared to modify access policies** based on operational experience.

**Confidence:** HIGH. The observe-before-enforce pattern is a well-established migration principle, also advocated by Gilman & Barth and Green-Ortiz.

**Cross-reference:** Gilman & Barth's [[Zero Trust Networks]] strongly advocates for a logging-first, enforce-later approach. This mirrors the **observe → monitor → enforce** progression in Green-Ortiz et al.'s [[Zero Trust Architecture]] implementation methodology.

---

### Claim 11: ZTA expansion follows the same iterative cycle — each new business process repeats steps 1–7 — and significant workflow changes trigger reevaluation of existing ZTA deployments, making the cycle both iterative and reactive. (Step 7 of the deployment cycle)

**Author's claim:** When enough confidence is gained, the enterprise enters the **steady operational phase** and begins planning the **next phase** of ZT deployment. (§7.3.7)

**Evidence presented:**
- Network and assets are still monitored, traffic is logged.
- Responses and policy modifications are done at a **lower tempo**.
- Subjects and stakeholders provide **feedback** to improve operations.
- **Change management:** If a significant change occurs to the workflow — new devices, major software updates, or shifts in organizational structure — the **entire process should be reconsidered**. However, not all steps need to be repeated from scratch.
- The deployment cycle is **both iterative and triggered**: it cycles through new business processes continuously, but is also triggered reactively by significant changes to existing ZTA-protected workflows.

**Confidence:** HIGH. The cyclical nature follows directly from the one-process-at-a-time migration model established in Claim 1.

**Cross-reference:** The [[DoD ZT Strategy & Roadmap]] structures expansion as a phased progression through **target levels** (zero through advanced) across seven pillars, with explicit timelines and capability milestones. Finney's [[Project Zero Trust]] frames expansion as an organizational change management problem — each new process brought into ZTA is another team that must adapt their workflow.

---

## Architecture Implications

### Claim 12: The single biggest barrier to ZTA migration is incomplete knowledge of the enterprise — the three foundational inventories (actors, assets, processes) create a chicken-and-egg problem where you need complete inventories to migrate but need to migrate to justify building complete inventories.

**Author's claim:** The foundational inventory problem is the single biggest barrier to ZTA migration. (§7, architecture implications)

**Evidence presented:**
- Three parallel surveys form the prerequisite: actor inventory, asset inventory, process/data flow inventory.
- Without these, the Policy Engine cannot make accurate access decisions, and shadow IT deployments may break silently when ZTA policies are applied.
- The PE's ability to evaluate access requests depends directly on the quality of the three inventories. Incomplete inventories → denied access requests → business process failure.
- This creates a chicken-and-egg problem: you need complete inventories to migrate, but you need to migrate to justify building complete inventories.

**Confidence:** MEDIUM-HIGH. The inventory dependency is structural, but whether it's the *single biggest* barrier is debatable — organizational resistance, budget, and vendor lock-in are also significant.

---

### Claim 13: The indefinite hybrid period imposes dual-mode requirements on common infrastructure — ID management, device management, and logging must serve both ZTA and perimeter-based workflows simultaneously, and ZTA solutions must interface with existing enterprise components without requiring ZTA-only infrastructure.

**Author's claim:** NIST is explicit that pure ZTA is aspirational. The indefinite hybrid period means common infrastructure must operate in dual mode. (§7.2, architecture implications)

**Evidence presented:**
- ID management, device management, and logging must be dual-mode (ZTA + perimeter).
- ZTA solutions should interface with existing enterprise components.
- Common infrastructure must not be ZTA-only during transition.
- Migration proceeds at the granularity of individual business processes.

**Confidence:** HIGH. The dual-mode requirement is a direct consequence of the hybrid model NIST establishes.

---

## Key Quotes

> "Implementing a ZTA is a journey rather than a wholesale replacement of infrastructure or processes."

> "Most enterprises will continue to operate in a hybrid zero-trust/perimeter-based mode for an indefinite period while continuing to invest in ongoing IT modernization initiatives."

> "An enterprise cannot determine what new processes or systems need to be in place if there is no knowledge of the current state of operations."

> "Few enterprise policy sets are complete in their first iterations: important user accounts may be denied access to resources they need or may not need all the access privileges they have been assigned."

> "The new ZT business workflow could be operated in reporting-only mode for some time to make sure the policies are effective and workable."

---

## See Also

- [[NIST 800-207 — Ch6 — ZTA Deployment Models]] — the deployment models (device agent, enclave gateway, resource portal, sandboxing) that step 5 selects among
- [[NIST 800-37]] — Risk Management Framework that the 7-step cycle maps to
- [[NIST 800-63A]] — Digital Identity Guidelines referenced for administrator confidence levels
- [[NIST 800-160v1]] — Systems Security Engineering referenced for greenfield ZT design
- [[OMB M-19-03]] — High Value Assets program that provides asset inventory for federal ZTA migration
- [[Concepts Index]] — parent index
