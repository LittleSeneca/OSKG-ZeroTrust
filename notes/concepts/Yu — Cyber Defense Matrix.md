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
claims_status: extracted
claims_extracted: 2026-07-24
---

# Yu — Cyber Defense Matrix

Sounil Yu's Cyber Defense Matrix is a MECE (mutually exclusive, collectively exhaustive) framework for organizing the entire cybersecurity landscape. It combines the five NIST CSF functions (IDENTIFY, PROTECT, DETECT, RESPOND, RECOVER) with five asset classes (DEVICES, NETWORKS, APPLICATIONS, DATA, USERS) to create a 5×5 grid of 25 cells. Every cybersecurity capability belongs in exactly one cell. For OSKG-ZeroTrust, the matrix provides the cleanest map of where Zero Trust design patterns fit within the broader defense ecosystem — and by extension, what ZT *doesn't* cover.

**Claim 1 —** The 5×5 grid is the most parsimonious complete map of cybersecurity → [[grid-most-parsimonious-complete-map-cybersecurity]]
---

**Claim 2 —** The five NIST CSF functions form a strict temporal sequence with clear semantics → [[five-nist-csf-functions-form-strict-temporal]]
---

**Claim 3 —** The dependency curves reveal ZT's operational limits → [[dependency-curves-reveal-zt-operational-limits]]
---

**Claim 4 —** ZT maps to specific PROTECT cells — not the whole matrix → [[zt-maps-specific-protect-cells]]
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
