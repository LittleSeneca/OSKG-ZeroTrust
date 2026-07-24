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

### Claim 1: The first protect surface must be what the business depends on to make money — not what's easiest for security to fix.

**Author's claim (via Aaron):** "We started with the Ides as the first of the primary protect surfaces for one main reason. And it's the first of the Zero Trust design principles. By starting with Ides, we're focusing on the business. We're forcing ourselves to understand how the business makes money."

**Evidence presented:** Dylan's conversation with CFO Donna reveals the ERP system ("Ides," a nod to the Ides of March — "Beware") as the central nervous system of MarchFit's finances: vendor creation, invoice processing, payment authorization, and financial reporting all flow through it. The ERP is where money both enters and leaves the business. Donna's observation captures the symmetry: "I need Ides to understand how the business operates in real time to protect the business from going the wrong direction, and you need to understand how the business operates in order to protect Ides."

**Confidence:** HIGH. This operationalizes the first ZT design principle ("Focus on business outcomes"). The narrative demonstrates that starting with business-critical assets creates natural allies (Donna, finance team) and forces security to learn how the business actually works — rather than applying generic security controls from a distance.

**What's at stake:** If ZT initiatives start with low-stakes systems to build momentum, they risk demonstrating that security doesn't understand the business. Starting with what matters most signals that security is a strategic partner, not a compliance function.

**Who disagrees:** Some frameworks (including aspects of CISA's ZTMM) suggest starting with identity as the foundational pillar. Finney addresses this by having Aaron explain that identity work happens *within* the ERP protect surface first — "we're practicing identity now so it will be that much easier later on." The sequencing is ERP → Identity → DevOps → SOC, each building on the previous.

**My assessment:** This is one of Finney's most important contributions: ZT methodology requires starting with *what creates business value*, not with what's architecturally convenient. The narrative makes this concrete — the ERP is complex, messy, and politically fraught, and that's exactly why it must be first. The alternative (starting with clean, modern cloud workloads that already have good security) teaches nothing about the organization's real risks.

---

### Claim 2: ERP systems are uniquely opaque to traditional security tools and require specialized solutions — but process changes matter more than technology purchases.

**Author's claim (via Peng, the ERP security specialist):** "The internals of an ERP system are usually a blind spot for security teams."

**Evidence presented:** Peng's assessment reveals five specific gaps:
1. **Specialized programming languages** (e.g., ABAP for SAP) are not supported by most security code review tools — vulnerabilities go undetected.
2. **ERP change control is manual** and not built into the ERP itself — separation of duties exists on paper but can be bypassed in code.
3. **Traditional vulnerability scanners** don't scan applications or code within ERP systems.
4. **Compliance management** (password standards, configurations, access controls) isn't native to ERP systems.
5. **Application logs** are not digestible by most SIEMs — SOC teams are blind to ERP activity.

Additionally: the ERP hadn't been patched in five years, real customer data was used in dev/test environments, superuser accounts proliferated, hard-coded passwords existed in the code, and a former developer's finance report was still being emailed to his personal Gmail account.

**Confidence:** HIGH. These findings map directly to real-world ERP security assessments and are consistent with industry reports. The five gaps enumerated in the chapter are specific enough to serve as an assessment checklist.

**What's at stake:** If these gaps aren't addressed, the ERP becomes an attacker's paradise — financial fraud, data exfiltration, and supply chain attacks (shipping treadmills to wrong addresses) are all possible without detection. The ERP is where "more ways to lose money than make it" exist.

**Who disagrees:** ERP vendors emphasize their built-in security features. The counterargument is that those features exist but require expertise to configure and maintain — expertise most organizations don't retain in-house.

**My assessment:** The chapter's genius is in showing that Dylan doesn't just buy a tool and call it done. Aaron specifies a specialized ERP security solution but *also* requires process changes: weekly maintenance windows for patching (negotiated with finance), role cleanup, removal of hard-coded credentials, data masking in dev/test. The tool enables visibility; the process changes prevent recurrence. This is "process before technology" in action — Donna's line, which Finney has her explicitly praise.

---

### Claim 3: NIST SP 800-207 provides the architectural tenets, but Kindervag's design principles and five-step methodology provide the actionable strategy.

**Author's claim (via Aaron):** "NIST 800-207 is focused on architecture, which is important. But there's not much guidance for what to do or where to start if you're going to do the work of maturing your information security program to embrace the strategy of Zero Trust... The design principles and methodology were developed by John Kindervag over a decade of actually doing the work."

**Evidence presented:** Aaron displays the NIST Zero Trust Basic Tenets (all seven) and the NIST network assumptions (all six), but he's explicitly critical: "I get frustrated with the NIST Zero Trust architecture because there's nothing in it about aligning with the business. Remember, Zero Trust is the strategy for preventing a security breach at your unique organization." He warns that NIST recommendations, if implemented literally, "would make it harder for employees to do their work or for consumers to use your products."

The chapter presents both frameworks side by side:
- **NIST 800-207**: seven basic tenets (all resources, secure all communication, per-session access, dynamic policy, monitor integrity, dynamic auth, collect information) + six network assumptions (no implicit trust zone, devices may not be yours, no inherent trust, resources outside enterprise infra, remote networks untrusted, consistent policy across boundaries)
- **Kindervag methodology**: four design principles (focus on business, inside-out, determine access, inspect/log) + five-step methodology (define protect surface → map transaction flows → architect → create policies → monitor/maintain)

**Confidence:** HIGH. This tension between architecture (NIST) and strategy/methodology (Kindervag) is real and underappreciated. NIST tells you *what* to build; Kindervag tells you *how* to do it. Both are necessary.

**What's at stake:** Organizations that follow only NIST risk building technically correct ZT architecture that alienates the business and fails to be adopted. Organizations that follow only Kindervag's methodology without NIST's architectural rigor risk building controls that don't meet compliance or interoperability standards.

**My assessment:** Finney's synthesis is pragmatic and correct. The book doesn't reject NIST — it layers NIST's tenets onto Kindervag's methodology. The architectural tenets become the criteria for evaluating solutions at each step of the methodology. This is the most balanced treatment of the NIST-vs-Kindervag tension in the ZT literature.

---

## Ch5: The Identity Cornerstone

### Claim 4: Identity is simultaneously the most important protect surface AND the most important ZT enabler — it must be both protected and consumed.

**Author's claim (via Aaron):** "Zero Trust consumes identity to help ensure least privilege. But identity is also one of your most important protect surfaces, so you need to protect it just as well as your other critical assets. I would actually argue that while your ERP is your crown, the jewels are the people."

**Evidence presented:** The FBI agent reveals that the breach occurred because MarchFit mixed customer and employee identity data in a single domain. When Bob Paulson left the company, his account wasn't terminated because he remained an active customer — retaining all employee permissions. A phishing email weeks later gave the attacker those permissions. The narrative demonstrates that identity failures cascade: a provisioning failure (Bob's account not deprovisioned) becomes an authentication failure (phished credentials) becomes an authorization failure (retained superuser access).

The chapter walks through the full identity life cycle:
- **Provisioning/deprovisioning**: automated HR feeds, role-based permissions tied to job descriptions, multi-channel account claiming with identity verification questions
- **Authentication**: MFA with multiple registered methods, no SMS for employees (SIM-jacking risk), reauthentication requirements, SSO for all applications
- **Authorization**: role cleanup to eliminate permission bloat, owner/sponsor for every account, quarterly user access reviews
- **Federation**: allowed for customers (BYO identity from social/email), forbidden for employees
- **Privileged Access Management (PAM)**: separate admin accounts, no email on admin accounts, credential rotation, temp logins
- **Monitoring**: basic + advanced auditing, object/attribute change detection, all identity events to SIEM

**Confidence:** HIGH. Finney captures the dual nature of identity in ZT better than most technical treatments. The "crown and jewels" metaphor is rhetorically effective and diagnostically accurate — organizations that secure the ERP but neglect identity have protected the vault but left every key on the floor.

**What's at stake:** Identity is where ZT succeeds or fails. Getting identity wrong means every other protect surface inherits a compromised foundation. Getting it right means every downstream control can consume identity signals for policy decisions.

**Who disagrees:** Some frameworks (Google BeyondCorp) treat identity primarily as an enabler rather than a protect surface. The distinction matters for resource allocation — if identity is "just" an enabler, it gets funded as infrastructure; if it's a crown jewel, it gets protected with equivalent rigor.

**My assessment:** The chapter's most important operational insight is the separation of customer and employee identity domains. This is not just a technical decision — it's a strategic one that affects every downstream ZT policy. The narrative shows why: mixing domains creates an unclosable vulnerability (former employees who are current customers retain access). The decision to create a *new* employee domain (rather than migrating customers) is a masterclass in change management — consumers hate service disruption, so move the smaller, more controllable population.

---

### Claim 5: MFA is necessary but insufficient — attackers have at least three distinct bypass strategies that ZT must address.

**Author's claim (via FBI Agent Smecker):** "Bob has three ways to deal with MFA. He can disable or weaken MFA. He can directly bypass MFA. Or he can exploit an existing exception to MFA."

**Evidence presented:**

| Bypass Strategy | Specific Techniques |
|---|---|
| **Disable/Weaken** | Modify trusted IP configurations; weaken MFA enforcement policies |
| **Directly Bypass** | SMS intercepts (SIM-jacking); compromise an already-authenticated device; stolen certificates (SolarWinds-style); golden ticket attacks (forged Kerberos tickets) |
| **Exploit Exceptions** | Target service accounts without MFA; attack legacy protocols (POP/IMAP) that don't support MFA; session reuse (30-day default reauth windows) |

Agent Smecker also warns that stolen certificates and golden ticket attacks are "a real challenge to detect since the requests look legitimate."

**Confidence:** HIGH. These bypass techniques are well-documented in the threat intelligence literature and validated by real-world breach reports. The taxonomy (disable/bypass/exploit exceptions) is useful for threat modeling.

**What's at stake:** Organizations that treat MFA deployment as "done" without addressing these bypass vectors are operating with a false sense of security. The 30-day default session window alone gives attackers a month of unrestricted access after compromising a device with an authenticated session.

**Who disagrees:** MFA vendors emphasize that these are edge cases and that MFA still blocks the vast majority of credential-based attacks. This is true but misleading — sophisticated attackers (the ones most likely to cause material damage) specifically target these bypass vectors.

**My assessment:** Finney's treatment of MFA is unusually honest for an introductory book. Most ZT literature presents MFA as a solved problem; Finney devotes significant narrative time to showing how it fails. This is important because it forces readers to think about compensating controls: reauthentication frequency, PAM, certificate hygiene, legacy protocol retirement, and session monitoring — all of which are more architecturally demanding than "turn on MFA."

---

### Claim 6: Identity governance needs a cross-functional stakeholder group, and GDPR/privacy assessments can jump-start the data flow mapping that ZT requires.

**Author's claim (via Aaron):** "The goal of identity is to ensure uniqueness of every human or non-human in our environment... The best way to ensure we're employing least privilege across all our systems is to start with the data, what services are connected to the data, and then decide who needs access to it."

**Evidence presented:** The Identity Governance group includes Noor (CISO), Kofi (Legal), Kim Self (Compliance), Vic (Sales, soon-to-be CEO), Mia (HR), and April (Marketing/Communications). Dylan presents the ZT identity strategy to this group and gets specific policy commitments:
- MFA required for all applications by default before rollout
- Daily reauthentication, with more frequent triggers for high-value transactions (payments, code deployments)
- Role cleanup tied to HR job descriptions, not titles
- Quarterly user access reviews with increasing frequency over time
- Orphaned account detection and remediation

The chapter also shows that MarchFit's GDPR data mapping project (hundreds of rows of data flows and role-based access) had already done the heavy lifting for the "map transaction flows" step — "probably took about a year off that time frame."

**Confidence:** HIGH for the governance model. The GDPR leverage insight is one of the most practical in the book — many organizations have done privacy assessments without realizing they've already completed the hardest part of ZT data flow mapping.

**What's at stake:** Without a governance group, identity decisions are made in isolation by IT, leading to permission bloat, orphaned accounts, and resistance from business units. The cross-functional model creates shared ownership.

**Who disagrees:** The IDSA framework (Identity-Defined Security Alliance) pushes the "seven components" model (Identity, Device, Network, Compute, Application, Storage, Data) as a more comprehensive reference architecture. The chapter presents this as complementary.

**My assessment:** The Identity Governance group is the most underappreciated element of ZT strategy. Technical ZT implementations fail not because the technology doesn't work but because no one owns the identity life cycle end-to-end. Finney embeds this governance lesson in the narrative rather than stating it as a principle — the group meeting where Brent brings a Bundt cake to celebrate completing the user access review workflow is both humanizing and instructive: ZT governance requires sustained, cross-functional commitment, and celebrating wins builds momentum.

---

## Ch6: Zero Trust DevOps

### Claim 7: DevOps culture can be an ally or adversary to ZT — the difference is whether security integrates with existing developer workflows or imposes new ones.

**Author's claim (via Dylan):** "We're here to help find ways to secure our code, but one of the first steps is to understand the process and how information flows through the organization."

**Evidence presented:** CTO Boris initially dismisses ZT as "a fad" and declares "we can't operate without trust." The turning point comes when Nigel (the embedded security-minded developer) demonstrates how OWASP Top 10 vulnerabilities all exploit different forms of trust in digital systems: SQL injection (trusting user input), broken authentication (trusting identity claims), broken access control (trusting client-side enforcement), security misconfiguration (trusting defaults), hard-coded secrets (trusting code privacy). Boris concedes: "I see how Zero Trust makes sense."

The chapter then applies ZT methodology to the DevOps protect surface:
- **Define protect surface**: the entire development pipeline — code repository → CI/CD → container orchestration (Kubernetes) → cloud
- **Map transaction flows**: developer commits → CI/CD builds → containers → orchestration → deployment
- **Architect ZT environment**: integrate all tools with SSO (remove local accounts), secrets management (no hard-coded credentials), RBAC in Kubernetes, network segmentation for control/data planes
- **Create policies**: automated security testing in CI/CD pipeline (OWASP scanning, authentication testing, hard-coded data detection), security policies as code (version-controlled, auditable), MFA reauthentication at code push
- **Monitor and maintain**: logging pipeline from code repository to cloud infra, correlate with identity for SOC, static + dynamic code analysis, managed bug bounty program

**Confidence:** HIGH. The DevSecOps integration pattern shown here is industry-standard but rarely explained through a ZT lens. The "security policies as code" idea, proposed by Boris himself after Dylan's persuasion, demonstrates how ZT principles can be adopted by developers when framed as process improvement rather than restriction.

**What's at stake:** DevOps teams deploy hundreds of changes per week. If security slows this down, the business loses competitive advantage. If security is bypassed to maintain velocity, the product ships with vulnerabilities. The only sustainable path is security integrated into the pipeline — "Shift Left" applied to ZT.

**Who disagrees:** Some security practitioners argue that automated security testing gives a false sense of security and that manual code review is irreplaceable. The chapter addresses this with Boris's complaint that previous code reviews "didn't really discover anything" — the solution is a belt-and-suspenders approach: automated scanning, periodic manual reviews, AND bug bounties.

**My assessment:** The chapter's most important contribution is demonstrating that ZT doesn't require developers to become security experts — it requires removing trust from the *process*, not the *people*. "Trust is a vulnerability" applies to systems, not to colleagues. When Nigel argues that SSO integration would save developers "twenty minutes a day just typing passwords," he's making a productivity argument, not a security one — and Boris, who previously resisted ZT, becomes an advocate. This is the ZT adoption pattern in microcosm: show how removing trust from digital systems *improves* the user experience.

---

### Claim 8: DevOps introduces cloud-native risks (Kubernetes, containers) that traditional perimeter security cannot address — ZT provides the model for securing them.

**Author's claim (via Boris):** "Kubernetes isn't secure at all by default. So we've done a lot already to make sure it's secure."

**Evidence presented:** Boris enumerates Kubernetes security controls: network segmentation between clusters and workloads, isolation of control plane from data plane traffic, firewalls between control and data planes. Dylan adds: RBAC enabled and integrated with the (now-separated) identity system. They also discuss:
- **Runtime security**: detecting privileged containers, monitoring file access, audit trails of all commands/sessions
- **Container image integrity**: preventing compromised images from being deployed
- **Web Application Firewall (WAF)**: described as "a Band-Aid" — useful for blocking OWASP attacks and credential stuffing while vulnerabilities are being fixed, but not a substitute for secure code
- **Secrets management**: millions of API keys leaked annually via hard-coding; secret managers eliminate sharing over Slack/Teams/email

**Confidence:** HIGH. Kubernetes default insecurity is well-documented. The specific controls mentioned (network segmentation, RBAC, runtime security, image scanning) align with the CNCF's security best practices and CIS benchmarks.

**What's at stake:** Cloud-native workloads are the fastest-growing attack surface. Organizations that apply perimeter-model thinking to cloud (firewall at the edge, trust everything inside) are structurally vulnerable. ZT's inside-out approach — treating each container and service as its own protect surface — is the correct model.

**Who disagrees:** Some argue that cloud providers' shared responsibility model shifts enough security to the provider that organizations don't need to implement Kubernetes-level controls themselves. The chapter implicitly rejects this: Boris and Dylan discuss controls at the Kubernetes layer, not relying on cloud provider defaults.

**My assessment:** The DevOps chapter is where the ZT strategy starts to demonstrate compound returns. Because identity is now clean (separate domains, SSO, MFA, PAM), the DevOps pipeline can consume identity for every control decision. Because the ERP taught the team about protect surfaces, they can model the DevOps pipeline the same way. Each protect surface makes the next one easier — this is the ZT flywheel that Finney is quietly demonstrating across chapters.

---

## Ch7: Zero Trust SOC

### Claim 9: The SOC is itself a protect surface — and most organizations don't treat it as one, creating a critical blind spot in their ZT strategy.

**Author's claim (via Dylan, after calling Aaron):** "The SOC is another protect surface. You need to incorporate Zero Trust into the incident response process itself. The incident response process is the main way that you'll interact with a SOC."

**Evidence presented:** The chapter opens with SOC analyst Jefferson discovering anomalous PSExec activity after hours — an attacker had been inside the network, testing hardware specs before installing a cryptominer. The SOC had detected the activity but:
- Couldn't resolve multiple IP addresses to a single device (no CMDB integration)
- Couldn't see which user owned which devices (no identity integration)
- Couldn't access internal security tools for investigation (no API access)
- Had to send tickets to the help desk and wait for someone else to investigate

**Aaron's post-hoc insight:** "Two-thirds of breaches come from your vendors. If you haven't started looking at third-party vendor management, you might add that to the list, particularly for cloud service providers." The MSSP (Managed Security Service Provider) is a vendor with access to the most sensitive parts of the network — and therefore must be subjected to Zero Trust itself.

The chapter then applies the ZT methodology to the SOC as a protect surface:
- **Protect surface**: the SOC itself, its connectivity, and the incident response process
- **Transaction flows**: the incident response plan (IR plan becomes the map)
- **Architecture**: CMDB, disaster recovery tools, orchestration platform
- **Policies**: who on the CSIRT team needs what access, when
- **Monitor/maintain**: weekly SOC briefings aligned to ZT controls

**Confidence:** HIGH. This is one of the most original insights in the book. Almost no ZT literature treats the SOC as a protect surface — it's always positioned as the consumer of ZT outputs, not as an asset that itself needs protection. Finney's framing closes a critical loop.

**What's at stake:** If the SOC isn't treated as a protect surface, the organization's monitoring capability can be the very thing an attacker compromises to hide their tracks. MSSPs, with connectivity into hundreds or thousands of customer networks, are prime targets. ZT principles must apply to *how* the SOC connects, what it can access, and how its own activities are monitored.

**Who disagrees:** Most SOC operational models assume the SOC is trusted by definition — it's the "defender" side. The ZT response is that trusted status is earned per session, not granted per role. An MSSP analyst's credentials could be compromised; their access should be scoped, monitored, and subject to reauthentication just like any other user.

**My assessment:** This is the chapter that completes the ZT strategy loop. Without it, ZT is a set of defensive controls with no feedback mechanism. With it, ZT becomes a continuous improvement cycle: the SOC monitors protect surfaces → detects failures or gaps → feeds recommendations back to the architecture/policy steps → controls improve → SOC has less noise to filter → detection improves. This is the operationalization of the fifth ZT methodology step ("Monitor and maintain") that most organizations skip.

---

### Claim 10: The SOC's value is measured by false positive reduction and dwell time containment, not by ticket counts or response SLAs.

**Author's claim (via Harmony and Chris, the MSSP owner):** Harmony: "We don't want reporting that says you responded to tickets within five minutes or how many cases you opened. That doesn't tell us that we're more secure or more effective. If we're going to have a Zero Trust SOC, we want to report on how many false positives we've reduced."

Chris elaborates: "If we can eliminate 99 percent of all the false positives, then what's left will be much easier to investigate and act upon." He adds that the SOC must have "skin in the game" — a feedback loop where SOC findings drive control improvements, which in turn reduce noise, which in turn improves SOC effectiveness.

**Evidence presented:** The metrics Harmony wants:
1. False positives reduced (month-over-month and year-over-year, accounting for seasonality)
2. New rules added to runbook and applied in production
3. Attacker progression through MITRE ATT&CK framework stages — are they being disrupted before command and control?
4. Dwell time reduction (the duration an attacker is inside before detection/containment)

Chris connects this to the ZT methodology: "We can align our controls around your defined protect surfaces. This will help us provide better monitoring, but it will also allow us to provide better feedback on what is slipping through your controls. Or in Zero Trust terminology, we can help look for opportunities to remove trust from these different protect surfaces."

**Confidence:** HIGH. The shift from activity-based metrics (tickets, response times) to outcome-based metrics (false positive reduction, dwell time, MITRE stage disruption) is a well-established best practice in SOC management but rarely tied explicitly to ZT.

**What's at stake:** Vanity metrics create complacency. If the SOC reports "99.9% of tickets closed within SLA," leadership assumes security is working — even if those tickets represent noise while real attacks go undetected. Outcome-based metrics aligned to ZT protect surfaces force accountability.

**Who disagrees:** Some argue that outcome-based metrics are harder to measure consistently and that SLA-based metrics provide necessary operational accountability. The counterargument (implicit in Finney's narrative) is that both are needed — SLAs for operational discipline, outcome metrics for strategic effectiveness.

**My assessment:** This is the most practical material in Ch7. The specific metrics Harmony requests could serve as a template for any organization's SOC reporting redesign. The key innovation is making MITRE ATT&CK stage progression a ZT metric — if you're seeing attackers reach later stages (credential access, lateral movement, command and control), your ZT controls aren't working, regardless of how many tickets were closed.

---

### Claim 11: Incident response must follow ZT principles, and the NIST Cybersecurity Framework provides a timeline-based structure that maps cleanly to ZT protect surfaces.

**Author's claim (via Luis, SOC team lead):** The NIST CSF five functions (Identify, Protect, Detect, Respond, Recover) map to a pre-incident/post-incident timeline. ZT applies across the entire timeline — not just to the pre-incident phases.

**Evidence presented:** The chapter presents both the NIST CSF and NIST SP 800-61 (Incident Handling Guide) as frameworks. When Dylan asks whether a compromised computer should be powered off or monitored ("Do we monitor the compromised computer to see what other devices it may be connecting to?"), Luis walks through the Containment/Eradication/Recovery considerations: potential damage, data theft risk, evidence preservation, impact on critical services, resource availability, and the permanence risk of emergency workarounds.

Aaron's final phone call adds: "You need to incorporate Zero Trust into the incident response process itself." The implication: every step of IR — who is authorized to declare an incident, who can isolate systems, who can access forensic data, who approves recovery — requires ZT policies. The CSIRT team interacts with the SOC as a protect surface.

**Confidence:** HIGH. The NIST CSF mapping is standard. The novel contribution is treating the IR process itself through a ZT lens — scoping access, removing implicit trust from IR workflows, applying the five-step methodology to incident response as its own protect surface.

**What's at stake:** IR processes that operate with implicit trust (any CSIRT member can isolate any system, forensic data is shared without access controls, recovery procedures bypass normal change control) create opportunities for attackers who've compromised IR credentials or for insider threats. And yet almost no organizations apply ZT to their IR process.

**Who disagrees:** Incident responders often argue that speed is paramount and that ZT-style access controls introduce friction during time-critical responses. The ZT response: access can be pre-provisioned, scoped to specific systems, and triggered by incident declaration — it doesn't require manual approval during an active incident.

**My assessment:** The IR-as-protect-surface insight is Finney's most forward-looking contribution in this section. It's underdeveloped in the chapter (Aaron raises it in a brief phone call and it's not fully explored), but the seed is planted: every process that touches a ZT environment must itself be subject to ZT principles, including the processes designed to respond to ZT failures.

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
