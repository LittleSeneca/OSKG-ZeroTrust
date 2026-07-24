---
tags:
  - source/books
  - yu
  - zt-framework
  - cyber-defense-matrix
  - oskg-zerotrust
created: 2026-07-24
confidence: high
source:
  title: "Cyber Defense Matrix: The Essential Guide to Navigating the Cybersecurity Landscape"
  authors: "Sounil Yu"
  year: 2022
  publisher: "JupiterOne Press"
  local_file: "sources/books/_txt/Cyber_Defense_Matrix_The_Essential_Guide_to_Navigating_the_Cybersecurity_Landsca.txt"
related:
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[NIST 800-207 — Ch3 — Logical Components]]"
  - "[[Concepts Index]]"
---

# Yu — Cyber Defense Matrix

Sounil Yu's Cyber Defense Matrix is a MECE (mutually exclusive, collectively exhaustive) framework for organizing the entire cybersecurity landscape. It combines the five NIST CSF functions (IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) with five asset classes (DEVICES, NETWORKS, APPLICATIONS, DATA, USERS) to create a 5×5 grid of 25 cells. Every cybersecurity capability belongs in exactly one cell. For OSKG-ZeroTrust, the matrix provides the cleanest map of where Zero Trust design patterns fit within the broader defense ecosystem — and by extension, what ZT *doesn't* cover.

## Claim 1: The 5×5 grid is the most parsimonious complete map of cybersecurity

**Yu's claim:** The Cyber Defense Matrix is a MECE representation — every security capability maps to exactly one cell, and the 25 cells collectively cover the entire defensive landscape. The five NIST CSF functions (IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) × five asset classes (DEVICES, NETWORKS, APPLICATIONS, DATA, USERS) = 25 boxes, and "every defensive function against every kind of asset that needs defending" lands in one of them.

**Evidence presented:** The matrix emerged from Yu's practical need as Chief Security Scientist at Bank of America — evaluating hundreds of security startups against a complex enterprise portfolio with no common framework. The grid's simplicity is its strength: it forces practitioners to answer two questions about every capability — *what does it do?* (the function) and *to what?* (the asset class). The internal consistency rules (e.g., IDENTIFY is always left-of-boom, DETECT is always right-of-boom) prevent definitional drift.

**Confidence:** HIGH. The framework has been widely adopted in the practitioner community and maps cleanly to every major ZT standard. The NIST CSF functions are the closest thing cybersecurity has to a universal taxonomy.

**What's at stake:** Without a MECE framework, organizations can't systematically assess coverage gaps. Vendors exploit the ambiguity — a product that "detects" threats against devices vs. networks vs. data may overlap in ways that look like defense-in-depth but are actually redundant spending on one cell while leaving others empty.

**Who disagrees:** MITRE ATT&CK maps the *offensive* landscape (tactics × techniques) rather than the defensive one — complementary, not competing. Forrester's ZTX framework defines seven pillars but doesn't enforce mutual exclusivity. Gartner's CARTA focuses on dynamic risk assessment rather than capability mapping. The Cyber Defense Matrix is unique in its MECE rigor.

**My assessment:** The matrix earns its place as a Tier 4 OSKG-ZeroTrust source precisely because it situates ZT within the full landscape. ZT is not the whole answer — it's one design pattern occupying specific cells. Understanding which cells those are (and which are not) is essential for avoiding ZT scope creep.

---

## Claim 2: The five NIST CSF functions form a strict temporal sequence with clear semantics

**Yu's claim:** The five functions are not interchangeable — each implies the existence of the prior function. IDENTIFY → PROTECT (left of boom); DETECT → RESPOND → RECOVER (right of boom). Actions must be classified consistently across all asset classes. If discovering DATA vulnerabilities is IDENTIFY, then discovering DEVICE vulnerabilities must also be IDENTIFY, not DETECT.

**Evidence presented:** Yu distinguishes between structural awareness (left-of-boom: knowing what assets exist, their configurations, their weaknesses) and situational awareness (right-of-boom: analyzing events, investigating state changes, gathering evidence of exploitation). A vulnerability is a structural weakness — discovering it is IDENTIFY regardless of whether it's been exploited yet. Patching a vulnerability is always PROTECT, even if done in response to an incident. Confusing these distinctions leads to remediation being classified as both PROTECT and RESPOND depending on context.

**Confidence:** VERY HIGH. This function taxonomy is the backbone of the NIST CSF and is adopted by CISA's ZT Maturity Model, which organizes capabilities by function within each pillar.

**What's at stake:** If organizations conflate IDENTIFY with DETECT (as NIST CSF itself sometimes does — ID.RA-1 and DE.CM-8 both reference vulnerability scanning), they lose the ability to measure coverage and maturity. Each cell in the matrix needs distinct metrics.

**Who disagrees:** The NIST CSF itself contains definitional ambiguities (using "identify" to describe DETECT activities). Yu's matrix imposes stricter internal consistency than NIST does, which is both a strength (clarity) and a limitation (some real-world activities legitimately span functions).

**My assessment:** This function-level rigor is what makes the matrix useful as a ZT mapping tool. ZTNA (NETWORK-PROTECT), ZTAA (APPLICATION-PROTECT), and ZTDA (DEVICE-PROTECT) are all PROTECT functions — they control access to resources. They are not DETECT or RESPOND. This clarifies that ZT is primarily a PROTECT strategy, not a complete security program.

---

## Claim 3: The dependency curves reveal ZT's operational limits

**Yu's claim:** TECHNOLOGY dependency is highest in IDENTIFY and PROTECT, then diminishes as we move right toward DETECT, RESPOND, and RECOVER where PEOPLE dependency grows. PROCESS dependency remains constant across all five functions. This has profound implications for ZT investment: the most technology-intensive part (ZT access proxies) occupies the left side of the matrix, but the most people-intensive part (incident response) is on the right.

**Evidence presented:** Yu cites research on the "ironies of automation" — the more we automate, the more critical human operators become for handling edge cases. Left-of-boom activities (inventory, vulnerability management, access control) benefit heavily from technology. Right-of-boom activities (triage, investigation, containment) still depend on human judgment, especially for novel attack patterns that evade automated detection.

**Confidence:** MODERATE. The dependency curves are Yu's own synthesis and he acknowledges they are debatable. AI/ML advances in SOAR and XDR may shift the curves rightward over time.

**What's at stake:** Organizations that invest exclusively in ZT technology (PROTECT) without commensurate investment in SOC capabilities (DETECT/RESPOND) have a lopsided security posture. ZT reduces the attack surface but does not eliminate the need for detection and response.

**Who disagrees:** Vendors of AI-driven SOAR platforms argue that technology can increasingly handle RESPOND functions. The trend toward autonomous response (automated containment, playbook-driven remediation) challenges the steepness of Yu's PEOPLE curve on the right side.

**My assessment:** The dependency curves are conceptually valuable even if the exact slope is debatable. For OSKG-ZeroTrust, the key insight is that ZT frameworks (NIST 800-207, CISA ZTMM, DoD ZT RA) are heavily weighted toward IDENTIFY and PROTECT — the left side. The right side (DETECT, RESPOND, RECOVER) is under-theorized in ZT literature, creating a gap that future standards will need to address.

---

## Claim 4: ZT maps to specific PROTECT cells — not the whole matrix

**Yu's claim:** Zero Trust is a design pattern for PROTECT, not a complete security framework. The ZT access proxy maps to three boxes: DEVICE-PROTECT, NETWORK-PROTECT, and APPLICATION-PROTECT. A DATA-PROTECT access proxy (Data Access Security Broker) is emerging. There is no USER-PROTECT access proxy because users are subjects, not resources — "a good executive assistant does the job well."

**Evidence presented:** Yu maps the old perimeter-based model (single trust boundary at NETWORK G, implicit transitive trust to all internal assets) against the ZT model (each resource has its own trust boundary, identity assertions are verified by an access proxy before granting access to that specific resource). He shows how ZTNA (NETWORK-PROTECT), ZTAA (APPLICATION-PROTECT), and ZTDA (DEVICE-PROTECT) are distinct patterns within the same PROTECT column. Identity attributes for establishing trustworthiness come from multiple asset classes: DEVICE-IDENTIFY (certs, patch level), NETWORK-IDENTIFY (IP, identity-based IP), APPLICATION-IDENTIFY (mTLS certs, API keys), DATA-IDENTIFY (hashes, classifications), USER-IDENTIFY (passwords, tokens, 2FA, location).

**Confidence:** HIGH. This mapping is Yu's most significant contribution to ZT discourse — it shows exactly where ZT fits and, more importantly, what it doesn't cover. ZT is not IDENTIFY (though it consumes IDENTIFY outputs). ZT is not DETECT (continuous monitoring is an input to policy decisions, but the access proxy itself is a PROTECT mechanism).

**What's at stake:** Vendors and frameworks that claim ZT is a "comprehensive security strategy" are claiming coverage of cells they don't occupy. The Cyber Defense Matrix exposes this — if your ZT strategy doesn't address DETECT and RESPOND for each asset class, you have gaps. ZT is necessary but not sufficient.

**Who disagrees:** Forrester's ZTX framework treats ZT as spanning all seven pillars, including detect and respond functions. CISA's ZT Maturity Model includes visibility and analytics capabilities that edge into DETECT territory. Yu would argue these are consumed by ZT policies but are not themselves ZT.

**Alternative reading:** One could argue that continuous verification (a ZT hallmark) *is* a form of DETECT — you're detecting changes in trustworthiness. Yu would counter that this is still PROTECT: you're making access decisions based on observed state, not investigating incidents.

**My assessment:** This precise mapping is the single most valuable thing the Cyber Defense Matrix contributes to OSKG-ZeroTrust. It prevents ZT scope creep while showing how ZT integrates with the rest of the security ecosystem. Every ZT note in this project should be traceable to specific cells in this matrix.

---

## Cross-Reference: Yu × NIST 800-207 × CISA ZTMM

| ZT Concept | Yu Matrix Cell | NIST 800-207 | CISA ZTMM Pillar |
|---|---|---|---|
| ZTNA (network access proxy) | NETWORK-PROTECT | PEP at network boundary | Network/Environment |
| ZTAA (application access proxy) | APPLICATION-PROTECT | PEP at application layer | Application Workload |
| Device trust (certs, posture) | DEVICE-IDENTIFY | Device identity + compliance | Device |
| User identity (MFA, behavioral) | USER-IDENTIFY | Subject identity attributes | Identity |
| Data classification/inventory | DATA-IDENTIFY | Data asset management | Data |
| Continuous monitoring | Cross-cutting (feeds all cells) | Continuous diagnostics | Visibility/Analytics |
| Policy decision point | Cross-cutting (orchestrates PROTECT) | PDP/PE architecture | Policy & Governance |
| Incident response | DETECT/RESPOND/RECOVER (all assets) | Not in ZTA scope per NIST | Not a ZT pillar per CISA |

**Key insight:** Yu's matrix reveals that NIST 800-207 and CISA ZTMM are primarily about the IDENTIFY and PROTECT columns. The DETECT, RESPOND, and RECOVER columns — incident response, forensics, recovery, business continuity — are outside ZT's scope but essential to a complete defense. This is not a flaw in ZT; it's a scope boundary. Organizations need both ZT (PROTECT) and SOC capabilities (DETECT/RESPOND/RECOVER).

---

## Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|---|---|---|
| 5×5 grid is a complete MECE map | HIGH | New asset classes (AI models? supply chain?) requiring grid expansion |
| NIST CSF functions form strict temporal sequence | VERY HIGH | Hybrid activities that legitimately span left/right of boom |
| Dependency curves reveal ZT's operational limits | MODERATE | AI/ML automation shifting the PEOPLE curve rightward |
| ZT maps to specific PROTECT cells, not the whole matrix | HIGH | Vendors and frameworks claiming ZT spans all 25 cells |

**Strongest contribution:** The ZT-to-PROTECT mapping (Claim 4). This is the most parsimonious explanation of where ZT fits in the security landscape, and it resolves the tension between "ZT is everything" (vendor marketing) and "ZT is nothing new" (skepticism).

**Weakest contribution:** The dependency curves (Claim 3) are conceptually interesting but empirically thin. Yu acknowledges this — he welcomes evidence to suggest the curves are wrong.

**Value to OSKG-ZeroTrust:** Tier 4 placement is correct. The Cyber Defense Matrix is not a ZT framework — it's a framework for understanding *where ZT frameworks fit*. As a navigational tool, it helps this project avoid scope creep (claiming ZT covers everything) while identifying integration points with non-ZT capabilities (SOC, IR, recovery).
