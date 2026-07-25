---
tags:
  - source/books
  - finney
  - zt-strategy
  - zt-measurement
  - zt-methodology
  - zt-identity
  - zt-devops
  - zt-soc
  - zt-governance
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
claims_status: extracted
claims_extracted: 2026-07-24
confidence: high
source:
  title: "Project Zero Trust: A Story about a Strategy for Aligning Security and the Business"
  author: "George Finney"
  year: 2022
  publisher: "Wiley"
  local_file: "sources/books/_txt/Project_Zero_Trust_A_Story_about_a_Strategy_for_Aligning_Security_and_the_Busine.txt"
  chapter_lines: "1954–4272"
  chapters: "4–7"
related:
  - "[[Concepts Index]]"
  - "[[Books Index]]"
  - "[[Finney — Ch1-3 — Introducing Zero Trust]]"
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[Garbis and Chapman — Ch1-3 — Introduction and Architecture]]"
  - "[[CISA ZTMM — Identity Pillar]]"
---

# Finney — Ch4–7: Building the Zero Trust Strategy

These four chapters form the operational core of Finney's narrative: the Zero Trust team at MarchFit moves from theory to execution, tackling protect surfaces from the inside out — starting with the ERP system (the "crown jewels"), then identity (the "cornerstone"), then DevOps (the new product pipeline), and finally the SOC (the monitoring and response layer). Each chapter applies Kindervag's five-step ZT methodology to a different protect surface, and each reveals a different dimension of how ZT strategy aligns security with the business.

---

## Ch4: The Crown Jewels — ERP as the First Protect Surface

**Claim 1 —** The first protect surface must be what the business depends on to make money — not what's easiest for security to fix. → [[the-first-protect-surface-must-be-what-the]]

---

**Claim 2 —** ERP systems are uniquely opaque to traditional security tools and require specialized solutions — but process changes matter more than technology purchases. → [[erp-systems-are-uniquely-opaque-to-traditional-security]]

---

**Claim 3 —** NIST SP 800-207 provides the architectural tenets, but Kindervag's design principles and five-step methodology provide the actionable strategy. → [[nist-sp-800-207-provides-the-architectural-tenets-but]]

---

## Ch5: The Identity Cornerstone

**Claim 4 —** Identity is simultaneously the most important protect surface AND the most important ZT enabler — it must be both protected and consumed. → [[identity-is-simultaneously-the-most-important-protect-surface]]

---

**Claim 5 —** MFA is necessary but insufficient — attackers have at least three distinct bypass strategies that ZT must address. → [[mfa-is-necessary-but-insufficient-attackers-have-at]]

---

**Claim 6 —** Identity governance needs a cross-functional stakeholder group, and GDPR/privacy assessments can jump-start the data flow mapping that ZT requires. → [[identity-governance-needs-a-cross-functional-stakeholder-group-and]]

---

## Ch6: Zero Trust DevOps

**Claim 7 —** DevOps culture can be an ally or adversary to ZT — the difference is whether security integrates with existing developer workflows or imposes new ones. → [[devops-culture-can-be-an-ally-or-adversary]]

---

**Claim 8 —** DevOps introduces cloud-native risks (Kubernetes, containers) that traditional perimeter security cannot address — ZT provides the model for securing them. → [[devops-introduces-cloud-native-risks-kubernetes-containers-that-traditional]]

---

## Ch7: Zero Trust SOC

**Claim 9 —** The SOC is itself a protect surface — and most organizations don't treat it as one, creating a critical blind spot in their ZT strategy. → [[the-soc-is-itself-a-protect-surface-and]]

---

**Claim 10 —** The SOC's value is measured by false positive reduction and dwell time containment, not by ticket counts or response SLAs. → [[the-socs-value-is-measured-by-false-positive]]

---

**Claim 11 —** Incident response must follow ZT principles, and the NIST Cybersecurity Framework provides a timeline-based structure that maps cleanly to ZT protect surfaces. → [[incident-response-must-follow-zt-principles-and-the]]

---

## Cross-Cutting Themes Across Ch4–7

### The ZT Methodology as a Reusable Pattern

Each chapter applies the same five-step methodology to a different protect surface, demonstrating that the methodology is domain-agnostic:

| Step | Ch4: ERP | Ch5: Identity | Ch6: DevOps | Ch7: SOC |
|---|---|---|---|---|
| 1. Define protect surface | ERP system (Ides) | Employee identity domain | DevOps pipeline + cloud | SOC + incident response |
| 2. Map transaction flows | Purchase-to-pay, vendor management, financial reporting | Provisioning → auth → authorization → deprovisioning | Commit → CI/CD → container → deploy | IR plan stages, alert → investigate → respond |
| 3. Architect ZT environment | ERP security tool, maintenance windows, patching | Separate domains, SSO, MFA, PAM, role cleanup | SSO integration, secrets mgmt, K8s RBAC, WAF | API access, SOAR, deception tech |
| 4. Create policies | Identity-based access rules, misuse case mitigations | Reauth frequency, access reviews, HR feed automation | Security-as-code, automated testing, bug bounty | CSIRT access, containment rules, vendor mgmt |
| 5. Monitor/maintain | ERP logs → SIEM, SOC alerting | Audit logs, attribute change detection, quarterly reviews | Logging pipeline, static/dynamic analysis | Weekly SOC briefings, false positive tracking, ATT&CK disruption |

### "Process Before Technology"

Donna's line in Ch4 — "Process before technology. Can I steal that?" — becomes the book's operational mantra. Every protect surface chapter shows the team defining the process first, then selecting or configuring technology to support it, never the reverse. This is the antidote to "shiny new technology" syndrome that Dylan explicitly warns against.

### "Trust Is a Vulnerability"

Brent's refrain appears in every chapter and serves as the book's ZT definition in five words. It's the diagnostic question for every architectural decision: "Where is trust being placed implicitly, and how can we remove it?" The chapters demonstrate this across domains — trusting that developers won't hard-code credentials, trusting that former employees' accounts will be deprovisioned, trusting that ERP code doesn't contain backdoors, trusting that SOC analysts' credentials won't be compromised.

### Stakeholder Alignment as ZT Strategy

The narrative shows Dylan building relationships with finance (Donna), HR (Mia), sales/executive (Vic), development (Boris), and the SOC (Chris, Jefferson, Luis). Each relationship produces a concrete ZT outcome: maintenance windows, role cleanup, budget justification, SSO adoption, and SOC integration. Aaron's advice in Ch4 is proven out: "The people in the business are the business, and you have to align with them."
