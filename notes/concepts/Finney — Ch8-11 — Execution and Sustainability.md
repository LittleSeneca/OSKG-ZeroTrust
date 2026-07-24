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
---

# Finney — Ch8–11: Execution and Sustainability

The final section of *Project Zero Trust* covers the operational endgame: how MarchFit executes its ZT strategy in the cloud, builds a sustainable security culture, pressure-tests everything in a live-fire tabletop exercise, and then faces the reality that Zero Trust never actually "finishes." These four chapters are where theory meets practice — the team moves from designing protect surfaces to actually defending them, from building controls to building a culture that sustains them, and from a six-month project to a multi-year maturity journey.

This note covers Ch8 (cloud execution), Ch9 (culture and awareness), Ch10 (the tabletop exercise), and Ch11 (the long-term journey and maturity model). Cross-references are drawn to NIST 800-207 Ch7 (migration), Gilman & Barth Ch9–10 (implementation and adversarial view), CISA ZTMM (maturity model), and NIST 800-84 (tabletop methodology).

---

## Ch8: Cloudy with a Chance of Trust

Narrative: Dylan, Isabelle, Kofi (legal), and Dave (purchasing) map MarchFit's sprawling cloud footprint in a conference room covered wall-to-wall in Post-it notes. Rose is contacted directly by the hacker 3nc0r3 with a $5M bribe offer — she decides to turn it into a sting. Aaron introduces SDP/SASE. Boris and Dylan establish container security standards.

### Claim 1: The cloud is not one protect surface — it's many, and the real protect surface is the project management process

**Finney's claim:** Isabelle's key insight: "I don't think the cloud is a protect surface. It's a lot of different protect surfaces." Rather than trying to wrap security around the entire cloud ecosystem, the team should secure the **project management process** itself. By inserting security phase-gates into every project lifecycle — vendor due diligence, secure configuration requirements, SOC notification — security becomes the default, not an afterthought.

**Evidence presented:** The Post-it note wall exercise revealed three categories of cloud services (AWS/Amazon, Azure, SaaS) spanning dozens of vendors. The purchasing department found even more via P-card spend. Shadow IT (Dropbox alongside sanctioned OneDrive, free PDF converters, Vimeo/YouTube/Twitch) proved that simply blocking unknown services breaks business processes. The project process as a protect surface means: every new vendor onboarding triggers security review, every project hits phase-gates before proceeding to production.

**Confidence:** HIGH. This is one of the most operationally practical claims in the book. The insight that governance processes *are* protect surfaces is a natural extension of the ZT design methodology — it applies the same logic (define the surface, map flows, architect controls) to the organizational process layer.

**What's at stake:** If project governance isn't treated as a protect surface, every cloud service deployed outside the security review pipeline becomes a blind spot. The scale argument — you can't review every cloud service individually — is defeated by securing the *pipeline* instead.

**Who disagrees:** Most ZT literature (NIST, Gilman & Barth, Garbis & Chapman) focuses on technical protect surfaces. Finney extends the concept upward to organizational process — this is a distinctive contribution. NIST 800-207 Ch7 discusses migration planning but doesn't frame project governance as a protect surface per se.

**My assessment:** This is Finney's most original architectural contribution. It bridges the gap between "ZT is a technical architecture" and "ZT requires organizational change." The project management protect surface is what keeps ZT sustainable beyond the initial implementation phase.

---

### Claim 2: Vendor contracts and third-party risk management are your primary defense against cloud risk — because the cloud is outsourcing

**Finney's claim:** "The cloud is just another way of saying we're outsourcing a service to another company." Standard contract terms (insurance, encryption, breach costs, security monitoring, annual audits, right to exit after breach) are the first line of defense. Vendor security ratings, Shared Assessments SIG, and CSA STAR/CAIQ provide due diligence without requiring a 15-person internal audit team.

**Evidence presented:** Kofi describes three contract processes (PO with standard terms, negotiated contracts, standard MarchFit contract) with escalating security rigor. The book cites that two-thirds of all breaches are caused by vendors. Contract provisions should include: no limitations of liability for direct damages (vendors often cap damages at fees paid), cyber insurance requirement, vendor-paid breach notification costs, and right to exit after a breach.

**Confidence:** HIGH. The contract-as-security-control approach is operationally realistic for most organizations. The specific contract provisions enumerated are actionable.

**My assessment:** This claim reveals an uncomfortable truth: for SaaS-heavy organizations, contract language may be the *only* security control you can enforce against a vendor's inadequate internal practices. A CASB can tell you data is exposed; a contract gives you recourse. Both are necessary.

---

### Claim 3: CASB + SASE/SDP + API security form the cloud visibility and control triad

**Finney's claim:** Three technology layers are needed for cloud ZT: (1) CASB for SaaS visibility (proxy or API-based), (2) SASE/SSE with SDP agents for endpoint-to-cloud policy enforcement and remote browser isolation, and (3) API security tools for discovering and monitoring the API layer that interconnects everything.

**Evidence presented:**
- **CASB:** Dave describes proxy-mode (all traffic flows through, enables logging) and API-mode (native integrations for OneDrive, SharePoint, Box, Salesforce — easier to deploy but less coverage). Can detect sensitive data in cloud storage.
- **SASE/SDP:** Aaron maps it to NIST 800-207's policy engine concept — agent on client connects to policy engine, allows/denies per role. Also provides device isolation (prevents lateral movement) and remote browser isolation (malware detonated in cloud sandbox).
- **API security:** APIs are both protect surface AND control. OWASP API Top 10 vulnerabilities (broken object-level auth, excessive data exposure, mass assignment) have caused breaches at Peloton, Parler, Facebook. Need API discovery scans, continuous monitoring, long-term data retention for threat hunting.

**Confidence:** HIGH. This triad is pragmatic and maps to real product categories. The API layer is correctly identified as the biggest blind spot — most orgs have a WAF for the front end but nothing for the back-end API traffic.

**What's at stake:** Without API visibility, ZT in the cloud is incomplete. Attackers can bypass front-end controls entirely by targeting the API layer.

---

### Claim 4: Container security standards must be enforced as code, with negative checks

**Finney's claim:** Boris and Dylan define container security requirements that can be enforced programmatically in the CI/CD pipeline: Unix sockets (not TCP), no privileged mode, no privilege escalation, resource limits, no inter-container communication, read-only filesystem, and automated validation of third-party images.

**Evidence presented:** The conversation is practical and developer-facing. Docker's security model allows these controls, but they must be explicitly configured. The "negative check" concept — test that something *isn't* present (e.g., privileged mode flag) — is the most operationally valuable idea here.

**My assessment:** This section is thin compared to Gilman & Barth's treatment of application trust (Ch7), but it serves the narrative purpose — showing security being pushed left into the development pipeline.

---

## Ch9: A Sustainable Culture

Narrative: Dylan presents to the board ($200M ransomware cost, recovery time reduced from 36 to 8 hours). Rose applies ZT methodology to security awareness. The team builds a culture through "security minutes," HR wellness integration, and ISAC membership. The "people are the weakest link" myth is dismantled. Rose's FBI sting takes down 3nc0r3.

### Claim 5: Security awareness training is a protect surface — apply the ZT design methodology to people

**Finney's claim:** Rose applies the five-step ZT methodology to security awareness: **protect surface = people**, **transaction flow = employee lifecycle** (from interview/hire through career progression to departure/retirement). This yields progressive, role-specific training that meets employees where they are in their career.

**Evidence presented:**
- New hire orientation: security introduced at onboarding
- Role-specific tracks: engineering gets different training than finance than content creators
- Progressive: training grows with career advancement
- Integration with IT/HR training: security woven into Excel training, management training, etc.
- "Security minute": 60 seconds at the start of every meeting (like airline safety briefing) — the ritual signals that security is a cultural value, not a compliance checkbox

**Confidence:** HIGH. This is the most thoughtful security awareness framework in the ZT literature. Most sources treat awareness as a checkbox; Finney treats it as a protect surface.

**What's at stake:** If security awareness is not designed with the same rigor as a technical protect surface, it becomes the weakest link in the ZT chain — because every technical control ultimately depends on human behavior.

**Cross-reference — CISA ZTMM Identity Pillar:** CISA's maturity model emphasizes identity governance but doesn't address security awareness as a protect surface. Finney fills this gap.

---

### Claim 6: "People are the weakest link" is a self-fulfilling prophecy — we trust people, not packets

**Finney's claim:** The security industry's mantra "people are the weakest link" is both wrong and damaging. It's wrong because people are actually "the only link" — every process, every technology, every control depends on human action. It's damaging because of the **Pygmalion effect** (Rosenthal & Jacobson, 1968): beliefs about people shape actions toward them, which shape their self-beliefs, which reinforce the original belief. If you believe people are the weakest link, you make it true.

The correct framing: **We trust people, not packets.** Zero Trust removes trust from digital systems (packets, devices, networks) — it does NOT remove trust from human relationships. Trust between people is the currency of business and the foundation of collaboration.

**Evidence presented:**
- Stephen Covey's *Speed of Trust*: high trust + analysis = good judgment. Skepticism without trust = indecision. Cynicism = shortcut to avoid critical thinking.
- Pygmalion study: teachers told worst students were best → those students outperformed their peers by year's end.
- Centola (UPenn): only 25% of a group needs to adopt new behaviors for collective behavior change.
- 50% of human behavior is habit-based → security must become a habit, integrated into wellness programs.

**Confidence:** MODERATE. The psychology is well-sourced, but the empirical link between the "weakest link" belief and measurable security outcomes is asserted, not demonstrated. The rhetorical shift from "weakest link" to "only link" is powerful framing, not a testable proposition.

**What's at stake:** If security teams adopt cynicism ("users will always click"), they stop designing usable security, which drives shadow IT, which creates real vulnerabilities. The belief becomes the cause of the outcome it predicts.

**Cross-reference — Gilman & Barth Ch10:** Gilman & Barth's adversarial view treats social engineering and physical coercion as genuine threat vectors, but doesn't address the cultural/psychological dimension of how security teams relate to users. Finney adds the human-factors layer that Gilman & Barth's engineering-focused threat model lacks.

**My assessment:** This is the most distinctive claim in the book — and the most controversial among security practitioners. It's easy to dismiss as "soft skills" content, but Finney's argument is structural: if you design your security program around the assumption that people will fail, you design for failure. If you design around the assumption that people can succeed with the right tools and habits, you design for resilience. The difference is not sentiment — it's architecture.

---

### Claim 7: Culture change requires rituals, not just policies — the "security minute" as cultural signal

**Finney's claim:** The "security minute" — 60 seconds of security content at the start of every meeting — functions like an airline safety briefing. It may not convey new information to everyone, but it signals that security is the first thing the organization values. The ritual, not the content, is the message.

**Evidence presented:** Isabelle and Rose deliver this as a pilot during project management training. HR adopts it. The analogy to airline safety briefings is deliberate — repetitive, ritualized, brief, and universal.

**My assessment:** This is operationally brilliant in its simplicity. It costs almost nothing, scales to any organization size, and creates a consistent cultural signal. It also creates a forcing function — someone has to prepare the security minute each week, which means security stays on the agenda.

---

## Ch10: The Tabletop Exercise

Narrative: The Project Zero Trust team runs a live-fire purple team exercise, scripted via NIST 800-84's MSEL. A penetration tester moves laterally from a compromised treadmill through the update server to the vulnerability scanning server, eventually exfiltrating data via a computer's LED to a drone. The exercise reveals remaining trust relationships in IoT devices and security tools themselves.

### Claim 8: Tabletop exercises are the "monitor and maintain" phase operationalized — they test controls and culture simultaneously

**Finney's claim:** "Part of the monitor and maintain phase means we need to be regularly evaluating whether our controls are good enough or whether we have any blind spots. A tabletop exercise is a great way of doing that." Tabletop exercises serve three functions: test technical controls, test incident response procedures, and build cross-departmental trust relationships that are essential during a real incident.

**Evidence presented:**
- The exercise followed NIST 800-84 methodology: defined objectives, developed MSEL, identified audience, conducted exercise, held hotwash debrief.
- Three objectives: (1) Can the team keep the organization operational? (2) Can they distinguish real issues from false positives? (3) Identify gaps in controls, procedures, resources, or training.
- The "red herrings" (protest, call center volume spike) simulated the fog of war — "Our brains will naturally start to connect the dots to draw conclusions, but often we don't have all the information."
- Key personnel removal (Noor's "family emergency") tested continuity and backup readiness.

**Confidence:** HIGH. The MSEL-based approach is the industry standard (NIST 800-84, CISA templates). The specific scenario design choices — IoT as initial vector, tool compromise for lateral movement, physical exfiltration — are well-calibrated to test ZT-specific controls.

**Cross-reference — NIST 800-207 Ch7:** NIST's migration chapter discusses the 7-step deployment cycle (actors → assets → processes → policies → solutions → deploy/monitor → expand) but doesn't specify how to test the deployed controls. Finney's tabletop chapter fills this operational gap.

---

### Claim 9: ZT doesn't eliminate trust relationships — the penetration test exposed two that remained

**Finney's claim:** Even after the full ZT implementation, two trust relationships were exploitable: (1) **IoT devices** (treadmills) were implicitly trusted by the internal update server, and (2) the **vulnerability scanning server** was trusted to communicate with nearly every device in the organization. Trust relationships in your own security tools are among the most dangerous.

**Evidence presented:**
- **IoT vector:** The treadmill's firmware update mechanism allowed the attacker to pivot from an IoT device to an internal server. Peter recommended memory-safe languages (Rust) for IoT firmware and device-to-device isolation.
- **Scanner vector:** The vulnerability scanner had broad network access because uncredentialed scans need open ports. Peter recommended: credentialed scans (fewer ports needed), time-limited firewall rules (only open during scan windows), and locking down what printers and other IoT devices can reach.
- **Physical exfiltration:** LED data exfiltration at ~4Kbps (<100 feet), memory bus as antenna at ~1Kbps (100+ feet), burner cell phones. These are real techniques, not hypothetical.
- **Protocol downgrade:** Attacker could force TLS downgrade to SSL 3.0 on vulnerable servers — disable everything below TLS 1.2.

**Confidence:** HIGH. These are not theoretical — they're common penetration testing findings. The scanner-as-attack-vector is particularly important because it's a trust relationship that security teams create themselves.

**Cross-reference — Gilman & Barth Ch10:** Gilman & Barth's adversarial view chapter catalogs similar trust exploitation vectors (identity theft, control plane compromise, endpoint enumeration). Finney operationalizes these as tabletop injects rather than theoretical threat categories. The scanner compromise maps to Gilman & Barth's "invalidation" category — using a trusted component to undermine the system.

**My assessment:** The scanner trust relationship is the most important finding in the exercise. It's a form of "eating your own dog food" — security tools must themselves be secured with ZT principles. A vulnerability scanner that can talk to everything is a vulnerability scanner that, if compromised, gives an attacker a map and keys to every door.

---

### Claim 10: Red herrings and the fog of war — the tabletop must simulate confusion, not just attack

**Finney's claim:** Real incidents are messy. Multiple things go wrong simultaneously, some of which are unrelated to the attack. The tabletop deliberately injected unrelated events (protest, call center spike) to test whether the team could distinguish signal from noise and avoid premature conclusions. "The best way to combat the fog of war is to communicate, ask questions, be transparent, but most of all, don't stick with your conclusions when you receive new information."

**Evidence presented:** The protest (labor conditions, drone, media) was a red herring that consumed leadership attention and created a plausible cover story for the drone. The call center spike was a red herring that could have been a real indicator but was contextual (Tuesday before Thanksgiving). The MFA acceptance by a user's child was a false positive that initially looked like a compromise.

**My assessment:** This is sophisticated tabletop design. Most exercises focus only on the attack chain; Finney adds operational noise. The lesson is that incident response isn't just about technical forensics — it's about maintaining situational awareness while the organization is under multiple simultaneous pressures.

---

## Ch11: Every Step Matters

Narrative: The 360Tread gaming treadmill launches at CES to acclaim. Dylan learns from Aaron that ZT is never "finished" — the maturity model extends the journey indefinitely. Noor offers Dylan the CISO role. He accepts and builds his team. The book closes by restating the four design principles, five-step methodology, and maturity model.

### Claim 11: Zero Trust never ends — the maturity model turns a six-month project into a multi-year strategic journey

**Finney's claim:** The six-month timeline was chosen because it aligns with corporate budget cycles, not because ZT can be "completed" in six months. The **Zero Trust Maturity Model** (CMM-based: Initial → Repeatable → Defined → Managed → Optimized) maps each of the five design methodology steps against five maturity levels per protect surface. Organizations should baseline, set strategic goals per protect surface, and phase improvements across budget cycles. Not every protect surface needs the same maturity level.

**Evidence presented:**
- Aaron: "I recommend to all our clients that we focus our efforts into six-to-nine-month initiatives. The biggest reason is the corporate budget cycle."
- The maturity model (Appendix B) provides a 5×5 matrix: each methodology step (define protect surface, map transaction flows, architect environment, create policy, monitor/maintain) measured at five maturity levels.
- The **transaction flow matrix** shows how protect surfaces interact — blast radius from a compromise in one protect surface affects others. This forces holistic prioritization, not isolated per-surface maturity.
- Next-phase recommendations: BAS (Breach and Attack Simulation) for continuous flow mapping, deception technologies (MITRE Engage) for active defense.

**Confidence:** HIGH. The CMM-based maturity model is standard practice (CISA ZTMM uses a similar approach). The 6-9 month budget-cycle alignment is operationally realistic and addresses the biggest reason ZT initiatives fail — loss of funding between phases.

**Cross-reference — CISA ZTMM:** CISA's maturity model operates across five pillars (Identity, Device, Network, Application, Data) with four maturity stages. Finney's model operates across the five methodology steps per protect surface. They are complementary: CISA tells you *what* to mature, Finney tells you *how* to mature each protect surface's design. Together, they provide orthogonal maturity measurement.

**Cross-reference — NIST 800-207 Ch7:** NIST's migration chapter describes the 7-step cycle but doesn't provide a maturity measurement framework. Finney's CMM model fills this gap.

**My assessment:** The maturity model is the book's structural answer to "what comes after the initial implementation." Without it, ZT is a one-time project that decays. With it, ZT becomes an operational discipline that improves over time.

---

### Claim 12: Deception technologies invert ZT — selectively add trust back to detect and disrupt attackers

**Finney's claim:** Aaron introduces deception as a natural extension of ZT: "With Zero Trust, we've focused on removing all the trusts we can. But with deception, we can selectively add trusts back into the network using lures, beacons, breadcrumbs, and decoys." The **MITRE Engage** framework provides a structured approach to active defense: expose breadcrumbs → lure attackers → disrupt their visibility → induce them to reveal toolkits → feed threat intel back into protect surface controls.

**Evidence presented:**
- NSA study: Penetration testers told deception was in use began doubting their own tools and questioned whether vulnerable targets were decoys. This effect persisted even when deception was NOT actually deployed.
- Analogy: "Like when people put a home alarm monitoring company sign on their house but don't actually have an alarm."
- The psychology: "Deception brings the fight to the mind of the adversary" — disrupts the attacker's trust in their own telemetry and tools.

**Confidence:** MODERATE. The NSA study is compelling anecdotal evidence, but the broader empirical case for deception effectiveness is still developing. The MITRE Engage framework is well-structured but less battle-tested than ATT&CK.

**Cross-reference — Gilman & Barth Ch10:** Where Gilman & Barth analyze threats through the adversary's lens (what can they do?), Finney extends the adversarial view into the defender's active response (what can we do *to* them?). This is a natural progression from passive ZT to active defense.

**My assessment:** Deception is the operationalization of the "assume breach" mindset. If you assume an attacker is already inside, you need more than preventive controls — you need detection mechanisms that work even when the attacker believes they're undetected. Deception turns the attacker's own assumptions (trust in their tools, trust in what they see) against them. This is the logical endpoint of the ZT philosophy applied to the offense/defense relationship.

---

### Claim 13: The CISO's measure of success is not "were we hacked?" but "how did we respond?"

**Finney's claim:** Dylan's onboarding speech to new security team members: "The first thing I want you all to know is that we're not measured on whether we are hacked or not. We're measured on how we respond to those challenges. We're measured on whether we rise to the challenge. Every step matters."

**Evidence presented:** This is thematic, not empirical. The entire book arc leads to this conclusion: MarchFit was hacked (ransomware), responded by building ZT, was targeted again (3nc0r3), responded by turning the attacker's bribe attempt into an FBI sting, and emerged with a stronger security posture and market position. The creed "Every Step Matters" is both MarchFit's corporate motto and Finney's thesis for ZT — everything you do has purpose, and incremental improvement compounds.

**What's at stake:** This reframes the CISO role from "prevent all breaches" (impossible) to "build organizational resilience" (achievable). It's a psychological shift that determines whether security teams burn out or sustain.

**My assessment:** This is the book's emotional and philosophical conclusion. It's not a technical claim — it's a leadership principle. But it has technical implications: if you measure success by breach prevention, you optimize for false certainty. If you measure by response quality, you optimize for detection, containment, and recovery — which are ZT's actual strengths.

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
