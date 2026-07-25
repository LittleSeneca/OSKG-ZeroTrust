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
claims_status: extracted
claims_extracted_date: 2026-07-24
claims_count: 13
claims_files:
  - "[[zta-migration-incremental-recurring-cycle]]"
  - "[[greenfield-zta-rarely-viable]]"
  - "[[hybrid-model-indefinite-reality]]"
  - "[[foundational-inventory-before-migration]]"
  - "[[identify-all-subjects-step1-migration]]"
  - "[[identify-catalog-assets-step2-migration]]"
  - "[[business-process-selection-step3-migration]]"
  - "[[policy-formulation-step4-migration]]"
  - "[[candidate-solution-selection-step5-migration]]"
  - "[[reporting-only-mode-step6-migration]]"
  - "[[zta-expansion-iterative-cycle-step7]]"
  - "[[incomplete-knowledge-chicken-egg-barrier]]"
  - "[[dual-mode-infrastructure-indefinite-hybrid]]"
  - topic/zt-migration
  - topic/zt-governance
  - topic/zt-implementation
---

# NIST 800-207 — Ch7 — Migrating to a Zero Trust Architecture

> *"Implementing a ZTA is a journey rather than a wholesale replacement of infrastructure or processes."*
> — NIST SP 800-207, §7

## Overview

Chapter 7 shifts from *what* a Zero Trust Architecture is to *how* to get there. NIST explicitly frames ZTA adoption as **incremental, process-driven, and indefinite** — not a one-time forklift upgrade. Most enterprises will operate in a **hybrid zero-trust/perimeter-based mode** for an extended period while continuing IT modernization initiatives. The chapter provides a concrete 7-step deployment cycle that maps to the NIST Risk Management Framework ([[NIST SP 800-37]]).

---

**Claim 1 —** ZTA migration is an incremental, recurring cycle — not a linear project — and most enterprises will operate in a hybrid zero-trust/perimeter-based mode indefinitely. → [[zta-migration-incremental-recurring-cycle]]

---

**Claim 2 —** Pure greenfield ZTA is rarely viable for existing organizations, but new infrastructure projects (new applications, services, databases) create opportunities to introduce ZT concepts to some degree. → [[greenfield-zta-rarely-viable]]

---

**Claim 3 —** The hybrid model — ZTA workflows coexisting with non-ZTA workflows — is the expected indefinite reality, requiring common infrastructure (ID management, device management, logging) to operate in dual mode and migration to proceed one business process at a time. → [[hybrid-model-indefinite-reality]]

---

**Claim 4 —** Before the 7-step cycle can begin, the enterprise must establish a foundational inventory of all actors, assets, and business processes — without this, the Policy Engine will deny requests due to insufficient information and shadow IT deployments may break silently. → [[foundational-inventory-before-migration]]

---

**Claim 5 —** All enterprise subjects — human users and Non-Person Entities (service accounts, automated processes) — must be identified, with special-privilege users requiring additional scrutiny and stricter confidence levels under ZTA rather than blanket trust. (Step 1 of the deployment cycle) → [[identify-all-subjects-step1-migration]]

---

**Claim 6 —** The enterprise must identify, catalog, and continuously monitor all assets — hardware, digital artifacts, virtual infrastructure, and shadow IT — because device posture assessment is integral to access decisions and incomplete inventory causes access denials. (Step 2 of the deployment cycle) → [[identify-catalog-assets-step2-migration]]

---

**Claim 7 —** Business process selection for ZTA migration should start with low-risk processes and cloud-based/remote-worker workflows, using the NIST RMF to evaluate tradeoffs in performance, user experience, and workflow fragility. (Step 3 of the deployment cycle) → [[business-process-selection-step3-migration]]

---

**Claim 8 —** Policy formulation for the ZTA candidate requires evaluating asset value/risk via RMF, identifying all upstream/downstream resources, and choosing between criteria-based (binary) and score-based (confidence-weighted) trust evaluation — a choice with cascading effects on tooling and operational complexity. (Step 4 of the deployment cycle) → [[policy-formulation-step4-migration]]

---

**Claim 9 —** Candidate solution selection must evaluate client footprint, traffic patterns, logging/analysis capabilities, protocol support, and subject behavior changes — with a recommended pilot approach that serves as a proving ground before full transition. (Step 5 of the deployment cycle) → [[candidate-solution-selection-step5-migration]]

---

**Claim 10 —** Initial ZTA deployment should operate in reporting-only (observation) mode — not immediate enforcement — because few policy sets are complete on the first iteration, and the monitoring phase collects real access pattern data to establish a baseline against which anomalous behavior can be identified. (Step 6 of the deployment cycle) → [[reporting-only-mode-step6-migration]]

---

**Claim 11 —** ZTA expansion follows the same iterative cycle — each new business process repeats steps 1–7 — and significant workflow changes trigger reevaluation of existing ZTA deployments, making the cycle both iterative and reactive. (Step 7 of the deployment cycle) → [[zta-expansion-iterative-cycle-step7]]

---

## Architecture Implications

**Claim 12 —** The single biggest barrier to ZTA migration is incomplete knowledge of the enterprise — the three foundational inventories (actors, assets, processes) create a chicken-and-egg problem where you need complete inventories to migrate but need to migrate to justify building complete inventories. → [[incomplete-knowledge-chicken-egg-barrier]]

---

**Claim 13 —** The indefinite hybrid period imposes dual-mode requirements on common infrastructure — ID management, device management, and logging must serve both ZTA and perimeter-based workflows simultaneously, and ZTA solutions must interface with existing enterprise components without requiring ZTA-only infrastructure. → [[dual-mode-infrastructure-indefinite-hybrid]]

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
