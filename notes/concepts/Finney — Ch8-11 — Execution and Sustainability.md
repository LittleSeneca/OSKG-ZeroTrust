---
tags:
  - source/books
  - finney
  - zt-execution
  - zt-sustainability
  - zt-culture
  - zt-tabletop
  - zt-maturity-model
  - zt-cloud
  - zt-people
  - oskg-zerotrust
created: 2026-07-24
source:
  title: "Project Zero Trust: A Story about a Strategy for Aligning Security and the Business"
  author: "George Finney"
  year: 2022
  publisher: "Wiley"
  local_file: "sources/books/_txt/Project_Zero_Trust_A_Story_about_a_Strategy_for_Aligning_Security_and_the_Busine.txt"
  lines: "L4273–L6627"
related:
  - "[[NIST 800-207 — Ch7 — Migration]]"
  - "[[NIST 800-207 — Ch5 — Threats]]"
  - "[[CISA ZTMM — Identity Pillar]]"
  - "[[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]]"
  - "[[Gilman and Barth — Ch10 — The Adversarial View]]"
  - "[[Books Index]]"
  - "[[Concepts Index]]"
claims_status: extracted
claims_extracted: 2026-07-24
  - topic/zt-implementation
  - topic/zt-governance
  - topic/zt-architecture
---

# Finney — Ch8–11: Execution and Sustainability

The final section of *Project Zero Trust* covers the operational endgame: how MarchFit executes its ZT strategy in the cloud, builds a sustainable security culture, pressure-tests everything in a live-fire tabletop exercise, and then faces the reality that Zero Trust never actually "finishes." These four chapters are where theory meets practice — the team moves from designing protect surfaces to actually defending them, from building controls to building a culture that sustains them, and from a six-month project to a multi-year maturity journey.

This note covers Ch8 (cloud execution), Ch9 (culture and awareness), Ch10 (the tabletop exercise), and Ch11 (the long-term journey and maturity model). Cross-references are drawn to NIST 800-207 Ch7 (migration), Gilman & Barth Ch9–10 (implementation and adversarial view), CISA ZTMM (maturity model), and NIST 800-84 (tabletop methodology).

---

## Ch8: Cloudy with a Chance of Trust

Narrative: Dylan, Isabelle, Kofi (legal), and Dave (purchasing) map MarchFit's sprawling cloud footprint in a conference room covered wall-to-wall in Post-it notes. Rose is contacted directly by the hacker 3nc0r3 with a $5M bribe offer — she decides to turn it into a sting. Aaron introduces SDP/SASE. Boris and Dylan establish container security standards.

**Claim 1 —** The cloud is not one protect surface — it's many, and the real protect surface is the project management process → [[the-cloud-is-not-one-protect-surface-its]]

---

**Claim 2 —** Vendor contracts and third-party risk management are your primary defense against cloud risk — because the cloud is outsourcing → [[vendor-contracts-and-third-party-risk-management-are-your]]

---

**Claim 3 —** CASB + SASE/SDP + API security form the cloud visibility and control triad → [[casb-sasesdp-api-security-form-the-cloud-visibility]]

---

**Claim 4 —** Container security standards must be enforced as code, with negative checks → [[container-security-standards-must-be-enforced-as-code]]

---

## Ch9: A Sustainable Culture

Narrative: Dylan presents to the board ($200M ransomware cost, recovery time reduced from 36 to 8 hours). Rose applies ZT methodology to security awareness. The team builds a culture through "security minutes," HR wellness integration, and ISAC membership. The "people are the weakest link" myth is dismantled. Rose's FBI sting takes down 3nc0r3.

**Claim 5 —** Security awareness training is a protect surface — apply the ZT design methodology to people → [[security-awareness-training-is-a-protect-surface-apply]]

---

**Claim 6 —** "People are the weakest link" is a self-fulfilling prophecy — we trust people, not packets → [[people-are-the-weakest-link-is-a-self-fulfilling]]

---

**Claim 7 —** Culture change requires rituals, not just policies — the "security minute" as cultural signal → [[culture-change-requires-rituals-not-just-policies-the]]

---

## Ch10: The Tabletop Exercise

Narrative: The Project Zero Trust team runs a live-fire purple team exercise, scripted via NIST 800-84's MSEL. A penetration tester moves laterally from a compromised treadmill through the update server to the vulnerability scanning server, eventually exfiltrating data via a computer's LED to a drone. The exercise reveals remaining trust relationships in IoT devices and security tools themselves.

**Claim 8 —** Tabletop exercises are the "monitor and maintain" phase operationalized — they test controls and culture simultaneously → [[tabletop-exercises-are-the-monitor-and-maintain-phase]]

---

**Claim 9 —** ZT doesn't eliminate trust relationships — the penetration test exposed two that remained → [[zt-doesnt-eliminate-trust-relationships-the-penetration-test]]

---

**Claim 10 —** Red herrings and the fog of war — the tabletop must simulate confusion, not just attack → [[red-herrings-and-the-fog-of-war-the]]

---

## Ch11: Every Step Matters

Narrative: The 360Tread gaming treadmill launches at CES to acclaim. Dylan learns from Aaron that ZT is never "finished" — the maturity model extends the journey indefinitely. Noor offers Dylan the CISO role. He accepts and builds his team. The book closes by restating the four design principles, five-step methodology, and maturity model.

**Claim 11 —** Zero Trust never ends — the maturity model turns a six-month project into a multi-year strategic journey → [[zero-trust-never-ends-the-maturity-model-turns]]

---

**Claim 12 —** Deception technologies invert ZT — selectively add trust back to detect and disrupt attackers → [[deception-technologies-invert-zt-selectively-add-trust-back]]

---

**Claim 13 —** The CISO's measure of success is not \"were we hacked?\" but \"how did we respond?\ → [[the-cisos-measure-of-success-is-not-were]]

---

## Synthesis: Execution and Sustainability Across the ZT Journey

| Dimension | Ch8 (Cloud) | Ch9 (Culture) | Ch10 (Tabletop) | Ch11 (Journey) |
|-----------|-------------|---------------|-----------------|----------------|
| **ZT Phase** | Architect + Policy | Culture building | Monitor + Maintain | Maturity Model |
| **Protect Surface** | Cloud services, project process, APIs, containers | People (employee lifecycle) | All — exercised simultaneously | Per-surface maturity tracking |
| **Key Tool/Process** | CASB, SASE, API security, vendor contracts | Security minute, wellness integration, ISAC | NIST 800-84 MSEL, purple teaming | CMM-based maturity model, BAS, deception |
| **Human Element** | Cross-functional team (legal, purchasing, IT) | Culture shift, habit formation, Pygmalion effect | Business + IT collaboration, fog of war | CISO leadership, team building |
| **Trust Removed** | Implicit cloud trust, container privileges, unmonitored APIs | Trust in "people are weakest link" narrative, cynicism | IoT trust, scanner trust, protocol downgrade | Complacency — "we're done" trust |
| **Trust Added** | Contract-based vendor trust, SDP policy enforcement | Trust in people, trust in team, trust through rituals | Cross-departmental trust built through exercise | Deception breadcrumbs (selectively) |

**Key insight:** These four chapters reveal the full arc of ZT as an organizational discipline, not a technical deployment. Ch8 shows that ZT execution requires governance and contracts as much as technology. Ch9 shows that ZT sustainability depends on culture change — specifically, shifting from cynicism ("people are the weakest link") to enablement ("people are the only link"). Ch10 demonstrates that even a well-implemented ZT architecture has remaining trust relationships that only adversarial testing can reveal. Ch11 reveals that ZT is never finished — the maturity model provides the framework for continuous improvement across budget cycles.

Finney's distinctive contribution to the ZT literature is this: **ZT is a people problem solved with technical tools, not a technical problem solved with people compliance.** The four design principles (define business outcomes, design from the inside out, determine who needs access, inspect/log all traffic) are technical, but the organizational execution — building a coalition across IT, legal, HR, finance, and the board; creating cultural rituals; exercising the team under pressure; and measuring maturity over time — is where ZT succeeds or fails. Every step matters.

---

## References Within the Text

- **NIST 800-207** — Aaron references the policy engine / policy enforcement point architecture when introducing SDP (p. 108-109)
- **NIST 800-84** — Chris references this as the standard for tabletop exercise development (p. 135)
- **OWASP API Top 10** — Referenced for API security vulnerabilities (p. 109)
- **MITRE ATT&CK / Engage** — Aaron introduces the Engage framework for deception-based active defense (p. 156-157)
- **Rosenthal & Jacobson (1968)** — *Pygmalion in the Classroom*, the original study on self-fulfilling prophecies (p. 131)
- **Stephen Covey** — *Speed of Trust* (2006), on the relationship between trust, analysis, and judgment (p. 131)
- **David Centola (UPenn)** — Research on tipping points: 25% adoption threshold for collective behavior change (p. 130)
- **Verizon DBIR 2021** — Cited: rogue insiders responsible for 22% of data breaches (p. 163)
- **Shared Assessments SIG, CSA STAR/CAIQ** — Vendor security assessment frameworks (p. 107)
- **Cloud Security Alliance** — STAR registry for vendor security certification (p. 106)
