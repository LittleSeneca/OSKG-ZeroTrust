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

Key architectural insight: migration is a **recurring cycle**, not a linear project. After the first business process is migrated, the cycle repeats for each subsequent process, and existing ZTA deployments must be reevaluated whenever the underlying workflow changes.

---

## 7.1 Pure Zero Trust Architecture (Greenfield)

In a greenfield scenario — building infrastructure from the ground up — an enterprise can design a pure ZTA from the start:

- Identify the workflows, applications, and services needed
- Narrow down the components and map how they interact
- Engineer the infrastructure and configure components against ZT tenets
- Evaluate subjects' trust before granting access
- Establish micro-perimeters around new resources

NIST acknowledges this is **rarely viable** for federal agencies or any organization with an existing network. However, **new responsibilities that require building new infrastructure** (a new application, service, or database) create opportunities to introduce ZT concepts to some degree. Success depends on how dependent the new infrastructure is on existing resources (e.g., identity management systems).

> NIST references [[NIST SP 800-160v1]] (Systems Security Engineering) as the companion framework for greenfield ZT design.

**Cross-reference:** Finney's [[Project Zero Trust]] structures the entire book around an organizational narrative of how ZT adoption unfolds inside an enterprise — the greenfield scenario maps loosely to the "new initiative" pattern where a team gets to build fresh rather than retrofitting.

---

## 7.2 Hybrid ZTA and Perimeter-Based Architecture (Brownfield)

> *"It is unlikely that any significant enterprise can migrate to zero trust in a single technology refresh cycle."*

The **hybrid model** — where ZTA workflows coexist with non-ZTA workflows — is the expected reality for the indefinite future. Key characteristics:

- Migration proceeds **one business process at a time**
- Common elements (identity management, device management, event logging) must be **flexible enough to operate in both ZTA and perimeter-based modes**
- Enterprise architects should **restrict ZTA candidate solutions to those that can interface with existing components**
- Migrating an existing workflow to ZTA likely requires at least a **partial redesign**
- Enterprises can use this as an opportunity to adopt [[NIST SP 800-160v1|secure system engineering]] practices

The hybrid model implies that the Policy Engine (PE) must handle both ZTA and legacy access patterns simultaneously, and that the organization's ID management, device management, and logging infrastructure must serve both worlds during the transition.

**Cross-reference:** Gilman & Barth's [[Zero Trust Networks]] devotes substantial attention to the migration problem — their proxy-based architecture is explicitly designed to be introduced incrementally at the network boundary, making it one of the more migration-friendly ZTA deployment models. Green-Ortiz et al.'s [[Zero Trust Architecture]] treats migration as a formal lifecycle phase with maturity progression. The [[DoD ZT Strategy & Roadmap]] operationalizes this hybrid concept with target-level milestones for federal systems.

---

## 7.3 Steps to Introducing ZTA to a Perimeter-Based Architected Network

### Prerequisites: The Foundational Inventory

Before the 7-step cycle can begin, NIST mandates a **baseline of competence**: the enterprise must have **detailed knowledge of its assets (physical and virtual), subjects (including user privileges), and business processes**. Without this inventory, the Policy Engine will deny requests due to insufficient information — especially problematic for unknown "shadow IT" deployments.

> *"An enterprise cannot determine what new processes or systems need to be in place if there is no knowledge of the current state of operations."*

These surveys can be conducted in parallel, and the entire process maps to the [[NIST SP 800-37]] Risk Management Framework (RMF) — ZTA adoption is fundamentally a risk reduction exercise.

### The 7-Step Deployment Cycle

The deployment cycle (visualized in Figure 12 of the standard) is a **recurring loop**: after step 7, the enterprise returns to step 1 for the next candidate business process. After the initial inventory is created, there is a regular cycle of **maintenance and updating** — even changes that seem minor (e.g., switching digital certificate providers) require reevaluation because they may involve certificate root store management, Certificate Transparency log monitoring, and other non-obvious factors.

---

### Step 1: Identify Actors on the Enterprise (§7.3.1)

The Policy Engine must have knowledge of **all enterprise subjects** — both human users and Non-Person Entities (NPEs) such as service accounts that interact with resources.

**Special-privilege users** (developers, system administrators) require **additional scrutiny** when being assigned attributes or roles:

- In legacy architectures, these accounts often have **blanket permission** to access all enterprise resources
- ZTA should instead allow sufficient flexibility while using **logs and audit actions** to identify access behavior patterns
- Administrators may need to satisfy a more stringent confidence level, as outlined in [[NIST SP 800-63A]], Section 5

> The key shift: from *privileged accounts have implicit trust* to *privileged accounts have stricter verification requirements*.

**Cross-reference:** Finney's [[Project Zero Trust]] frames this as the "identity is the new perimeter" problem — understanding who your actors are across human, service, and machine identities is the foundational first step. The [[DoD ZT Strategy]] emphasizes identity as Pillar 1 and requires attribute-based access control (ABAC) for all user authorizations.

---

### Step 2: Identify Assets Owned by the Enterprise (§7.3.2)

ZTA requires the ability to **identify and manage devices** — both enterprise-owned and non-enterprise-owned (BYOD, collaborator assets) that access enterprise resources. This includes:

| Category | Examples |
|----------|----------|
| **Hardware** | Laptops, phones, IoT devices, servers |
| **Digital artifacts** | User accounts, applications, digital certificates, virtual assets, containers |
| **Physical location** | As best estimated |
| **Network location** | Observed and tracked |

Beyond cataloging, the enterprise must have **configuration management and monitoring** — the ability to observe the current state of an asset is part of the process of evaluating access requests. This means the enterprise must be able to **configure, survey, and update** assets, including virtual assets and containers.

**Non-enterprise-owned assets and "shadow IT"** must also be cataloged as well as possible (MAC address, network location, augmented by administrator data entry). Shadow IT presents a special problem: certain ZTA approaches (mainly network-based) may cause shadow IT components to become **unusable** because they are not known and included in network access policies.

**Federal context:** Agencies that have established **CDM (Continuous Diagnostics and Mitigation)** program capabilities — such as HWAM (Hardware Asset Management) and SWAM (Software Asset Management) — already have a rich data set to draw from. Agencies may also have lists of ZTA candidate processes involving **High Value Assets (HVA)** identified under [[OMB M-19-03]].

**Cross-reference:** Gilman & Barth's [[Zero Trust Networks]] emphasizes that device identity and trust are co-equal to user identity — the network must know *what* is connecting, not just *who*. Green-Ortiz et al.'s [[Zero Trust Architecture]] adds the cloud-native dimension: asset inventory now includes containers, serverless functions, and ephemeral compute that may exist for minutes.

---

### Step 3: Identify Key Processes and Evaluate Risks (§7.3.3)

The enterprise must **identify and rank business processes, data flows, and their relation to agency missions**. Business processes should inform the circumstances under which resource access requests are granted and denied.

**Selection strategy:**

- **Start with a low-risk business process** for the first ZTA transition — disruptions will likely not negatively impact the entire organization
- Once enough experience is gained, **more critical business processes** become candidates
- **Cloud-based resources** and **remote worker workflows** are often good candidates — rather than projecting the enterprise perimeter into the cloud or using VPNs, clients can request cloud services directly through PEPs

**Tradeoffs to consider:**
- Performance degradation
- User experience changes
- Possible increased workflow fragility

> The risk evaluation should use the NIST Risk Management Framework ([[NIST SP 800-37]]).

**Cross-reference:** This is where the organizational narrative from Finney's [[Project Zero Trust]] is most relevant — selecting the first pilot process is as much a political and organizational decision as a technical one. Green-Ortiz et al.'s [[Zero Trust Architecture]] provides a maturity model that maps candidate processes to organizational readiness levels.

---

### Step 4: Formulate Policies for the ZTA Candidate (§7.3.4)

After identifying a candidate service or business workflow, the enterprise must:

1. **Evaluate the value/risk** of the asset or workflow using the NIST RMF ([[NIST SP 800-37]])
2. **Identify all upstream resources** (ID management systems, databases, micro-services), **downstream resources** (logging, security monitoring), and **entities** (subjects, service accounts) used by or affected by the workflow
3. **Determine the access criteria** — either criteria-based (TA using binary rules) or score-based (TA using confidence level weights) — for the resources in the candidate business process (see NIST 800-207 §3.3.1)

**Candidate selection influence:** An application used by a specific subset of enterprise subjects (e.g., a purchasing system) may be preferred over one vital to the entire subject base (e.g., email).

**Tuning:** Administrators may need to adjust criteria or confidence weights during the tuning phase to ensure policies are effective but do not hinder legitimate access.

> *Key architectural decision point:* whether to use criteria-based or score-based trust evaluation. This choice has cascading effects on tooling, logging requirements, and operational complexity.

**Cross-reference:** Gilman & Barth's [[Zero Trust Networks]] provides detailed guidance on constructing trust scores and policy logic for the proxy model. The [[DoD ZT Strategy]] mandates automated policy decision points with continuous runtime authorization.

---

### Step 5: Identify Candidate Solutions (§7.3.5)

With the candidate business process and policies defined, enterprise architects compose a list of candidate solutions. Different deployment models (see NIST 800-207 §3.1) suit different workflows and enterprise ecosystems.

**Evaluation factors:**

| Factor | Question |
|--------|----------|
| **Client footprint** | Does the solution require components installed on the client asset? This may limit BYOD or cross-agency collaboration use cases. |
| **Traffic pattern** | Does the solution work where resources exist on enterprise premises (east-west traffic), or does it assume cloud-resident resources (north-south traffic)? |
| **Logging and analysis** | Does the solution provide a means to log interactions for analysis that feeds back into the Policy Engine? |
| **Protocol support** | Does the solution support a broad range of protocols (web, SSH, etc.) and transports (IPv4, IPv6), or is it narrowly focused? |
| **Subject behavior** | Does the solution require changes to how enterprise subjects perform their workflow? |

**Recommended approach:** Model the existing business process as a **pilot program** rather than just a replacement. The pilot serves as a "proving ground" for ZTA before transitioning subjects away from legacy process infrastructure. A pilot can be general (applying to several business processes) or specific (one use case).

**Cross-reference:** This solution-selection phase corresponds to the architecture decisions that Gilman & Barth's [[Zero Trust Networks]] addresses through detailed protocol-level analysis. Green-Ortiz et al.'s [[Zero Trust Architecture]] provides vendor-neutral evaluation criteria and decision matrices. The [[DoD ZT Reference Architecture v2.0]] specifies approved deployment patterns for federal environments.

---

### Step 6: Initial Deployment and Monitoring (§7.3.6)

Once the candidate workflow and ZTA components are chosen, initial deployment begins with an **observation and monitoring mode** — NOT immediate enforcement.

**Key principle: few policy sets are complete on the first iteration.** Important accounts (e.g., administrator accounts) may be denied access they need, or may retain more privileges than required.

**Recommended approach: reporting-only mode**
- Grant access for most requests initially
- Log and trace all connections
- Compare actual access patterns against the initial developed policy
- Enforce only the most basic policies: deny requests that fail MFA or appear from known attacker-controlled/subverted IP addresses

**Why lenient initial deployment?** To collect data from actual interactions of the ZT workflow. Once a baseline of activity patterns is established, anomalous behavior can be more easily identified.

If reporting-only mode is not possible, operators must **monitor logs closely and be prepared to modify access policies** based on operational experience.

> This step is where theory meets reality. The initial policy set is a hypothesis about how the workflow operates; the monitoring phase tests that hypothesis.

**Cross-reference:** Gilman & Barth's [[Zero Trust Networks]] strongly advocates for a logging-first, enforce-later approach to avoid breaking critical workflows during migration. This mirrors the **observe → monitor → enforce** progression in Green-Ortiz et al.'s [[Zero Trust Architecture]] implementation methodology.

---

### Step 7: Expand the ZTA (§7.3.7)

When enough confidence is gained and the workflow policy set is refined, the enterprise enters the **steady operational phase**:

- Network and assets are still monitored, traffic is logged
- Responses and policy modifications are done at a **lower tempo** (they should not be severe)
- Subjects and stakeholders provide **feedback** to improve operations
- Enterprise administrators begin planning the **next phase** of ZT deployment

**The cycle repeats:** Like the previous rollout, a candidate workflow and solution set must be identified, and initial policies developed.

**Change management:** If a significant change occurs to the workflow — new devices, major software updates (especially ZT logical components), or shifts in organizational structure — the **entire process should be reconsidered**. However, not all steps need to be repeated from scratch. For example, if new devices are purchased but no new user accounts are created, only the device inventory needs updating.

> The deployment cycle is **both iterative and triggered**: it cycles through new business processes continuously, but is also triggered reactively by significant changes to existing ZTA-protected workflows.

**Cross-reference:** The [[DoD ZT Strategy & Roadmap]] structures expansion as a phased progression through **target levels** (zero through advanced) across seven pillars, with explicit timelines and capability milestones. This operationalizes NIST's conceptual cycle into a concrete federal implementation plan. Finney's [[Project Zero Trust]] frames expansion as an organizational change management problem — each new process brought into ZTA is another team that must adapt their workflow.

---

## Architecture Implications

### The Foundational Inventory Problem

The single biggest barrier to ZTA migration is **incomplete knowledge of the enterprise**. NIST identifies three parallel surveys that form the prerequisite:

1. **Actor inventory** — human users + NPEs (service accounts, automated processes)
2. **Asset inventory** — hardware, digital artifacts, virtual infrastructure, shadow IT
3. **Process/data flow inventory** — business processes ranked by mission criticality

Without these, the Policy Engine cannot make accurate access decisions, and shadow IT deployments may break silently when ZTA policies are applied.

### The Hybrid Reality

NIST is explicit that **pure ZTA is aspirational in most cases**. The indefinite hybrid period means:
- ID management, device management, and logging must be dual-mode (ZTA + perimeter)
- ZTA solutions should interface with existing enterprise components
- Common infrastructure must not be ZTA-only during transition
- Migration proceeds at the granularity of individual business processes

### The Policy Engine as Migration Bottleneck

The PE's ability to evaluate access requests depends directly on the quality of the three inventories. Incomplete inventories → denied access requests → business process failure. This creates a chicken-and-egg problem: you need complete inventories to migrate, but you need to migrate to justify building complete inventories.

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
