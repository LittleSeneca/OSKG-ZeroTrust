---
tags:
  - source/books
  - green-ortiz
  - zt-introduction
  - zt-components
  - zt-networking
  - zt-history
  - five-pillars
  - oskg-zerotrust
created: 2026-07-24
confidence: high
source:
  title: "Zero Trust Architecture (Networking Technology: Security)"
  authors: "Cindy Green-Ortiz, Brandon Fowler, David Houck, Hank Hensel, Patrick Lloyd, Andrew McDonald, Jason Frazier"
  year: 2024
  publisher: "Cisco Press"
  local_file: "sources/books/_txt/Zero_Trust_Architecture_Networking_Technology_Security.txt"
  sections: "Introduction, Chapter 1 — Overview of Zero Trust, Chapter 2 — Zero Trust Capabilities"
  lines: "1313–3743"
related:
  - "[[Gilman and Barth — Ch1 — Zero Trust Fundamentals]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[Concepts Index]]"
claims_status: extracted
claims_extracted: 2026-07-24
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-governance
---

# Green-Ortiz et al. — Intro + Ch1–2: Foundations and Core Components

The most detailed single-source treatment of Zero Trust architecture from a networking and infrastructure perspective. Green-Ortiz and her six co-authors bring 85 combined years of security and architectural experience, organized around Cisco's five-pillar capability model. This combined note covers the book's introduction (audience, approach, executive sponsorship), Chapter 1 (historical origins, discovery workshop methodology, organizational dynamics, the five pillars), and Chapter 2 (the full "dictionary of capabilities" within each pillar). Where NIST 800-207 defines what ZT *is* and Gilman & Barth define how to *build* it, Green-Ortiz defines how to *plan, assess, and operationalize* it in enterprise environments.

---

**Claim 1 —** Zero Trust originated from the Morris Worm and Stephen Marsh's thesis, not from a vendor marketing campaign → [[zero-trust-originated-from-the-morris-worm-and]]

---

**Claim 2 —** The Zero Trust Discovery Workshop is the critical first step — skip it at your peril → [[the-zero-trust-discovery-workshop-is-the-critical]]

---

**Claim 3 —** Cisco's five-pillar model (Policy & Governance, Identity, Vulnerability Management, Enforcement, Analytics) provides a comprehensive capability taxonomy for ZT assessment → [[ciscos-five-pillar-model-policy-governance-identity-vulnerability-management]]

---

**Claim 4 —** Policy & Governance is the "badge and shield" — it authorizes enforcement and defines the rules → [[policy-governance-is-the-badge-and-shield-it]]

---

**Claim 5 —** Identity must be contextual — WHO, WHAT device, WHERE, HOW, and WHEN all matter → [[identity-must-be-contextual-who-what-device-where]]

---

**Claim 6 —** Vulnerability Management must extend beyond CVEs to include communication baselines and device behavior → [[vulnerability-management-must-extend-beyond-cves-to-include]]

---

**Claim 7 —** Enforcement must be layered and applied as close to the source as possible → [[enforcement-must-be-layered-and-applied-as-close]]

---

**Claim 8 —** Analytics closes the loop — the ZT journey is cyclical, not linear → [[analytics-closes-the-loop-the-zt-journey-is]]

---

## Synthesis: Three Frameworks, Three Perspectives

| Dimension | Green-Ortiz (2024) | NIST 800-207 (2020) | Gilman & Barth (2017) |
|---|---|---|---|
| **Organizing model** | Five operational pillars | Logical components (PE/PA/PEP) | Control plane / data plane |
| **Primary audience** | Enterprise architects, operations teams | Federal agencies, standards bodies | Engineers, implementers |
| **Identity treatment** | Contextual identity: WHO/WHAT/WHERE/HOW/WHEN | ID Management data source + ICAM integration | Authentication of every device, user, and flow |
| **Governance treatment** | Standalone foundational pillar (Policy & Governance) | Industry Compliance data source | Implicit in trust engine policy |
| **Vulnerability treatment** | Full program: scanning, endpoint protection, malware, database | CDM system (posture input to PE) | Device trust (Ch4, posture signals) |
| **Enforcement treatment** | Catalog of technologies (firewalls, IPS, proxy, VPN, SOAR, FIM) | PEP — logical abstraction, no technology enumeration | Data plane — accepts configuration from control plane |
| **Analytics treatment** | Cyclical feedback loop modifying all pillars | Inputs to PE (SIEM, activity logs, threat intel) | Trust engine computation (Ch4) |
| **Key contribution** | Operational framework for assessing and planning ZT maturity | Canonical architectural definitions (PE/PA/PEP) | Implementation blueprint (assertions, architecture, protocols) |
| **Weakness** | Cisco-specific in technology enumeration; light on protocol-level detail | Static component model; no operational guidance | Pre-dates enterprise ZT maturity; no governance treatment |

**Key insight:** The three sources form a progression from *principle* (Gilman & Barth: how to build ZT) to *definition* (NIST: what ZT is) to *operation* (Green-Ortiz: how to plan, assess, and run ZT in an enterprise). Gilman & Barth's 2017 book established the control-plane/data-plane architecture that all subsequent frameworks assume. NIST 800-207 in 2020 canonized the PE/PA/PEP component model and provided the standards vocabulary. Green-Ortiz in 2024 completes the picture by addressing the organizational, governance, and operational dimensions that neither of the earlier sources covers adequately. Read together, they answer: *why* ZT (history and threat landscape), *what* ZT (architecture and definitions), *how* to build it (implementation), and *how* to run it (operations and continuous improvement).

The most important practical insight from Green-Ortiz that neither NIST nor Gilman & Barth provide: **the Discovery Workshop methodology.** The technical architecture (NIST, Gilman & Barth) is necessary but insufficient; the organizational alignment (Green-Ortiz) determines whether the architecture ever gets deployed successfully.
