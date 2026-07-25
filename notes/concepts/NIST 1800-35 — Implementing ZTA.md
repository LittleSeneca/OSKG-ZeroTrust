---
tags:
  - source/standards
  - nist
  - zt-implementation
  - zt-vendors
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
claims_status: extracted
claims_extracted: 2026-07-24
confidence: high
source:
  title: "NIST SP 1800-35 — Implementing a Zero Trust Architecture (Final v2)"
  authors: "Oliver Borchert, Gema Howell, Alper Kerman, Scott Rose, Murugiah Souppaya (NIST); Jason Ajmo, Yemi Fashina, Parisa Grayeli et al. (MITRE); Karen Scarfone (Scarfone Cybersecurity); William Barker (Dakota Consulting); plus 24 vendor collaborators"
  year: 2025
  publisher: "NIST National Cybersecurity Center of Excellence (NCCoE)"
  local_file: "sources/papers/_txt/NIST_SP_1800-35_FINAL_v2.txt"
related:
  - "[[NIST 800-207 — Ch1 — Introduction]]"
  - "[[NIST 800-207 — Ch7 — Migration]]"
  - "[[NIST 800-207A — Cloud-Native Access Control]]"
  - "[[CISA ZTMM — Overview and Framework]]"
  - "[[Concepts Index]]"
  - "[[Standards Index]]"
  - "[[Notes Index]]"
---

# NIST SP 1800-35 — Implementing a Zero Trust Architecture

NIST SP 1800-35 is the most comprehensive vendor-neutral ZTA implementation guide ever published. Produced by the NCCoE with 24 commercial technology collaborators under CRADAs, it documents 19 end-to-end ZTA example implementations ("builds") deployed across four simulated enterprise environments in a physical laboratory. Published June 2025, it is the practical companion to SP 800-207 — where 800-207 defines *what* ZTA is, 1800-35 demonstrates *how* to build it with commercially available technology. The guide spans four ZTA deployment approaches (EIG, SDP, Microsegmentation, SASE) across three maturity phases, exhaustively documents integration patterns and pitfalls, and provides a seven-step ZTA journey framework. It is the definitive reference for organizations that need to *build* ZTA, not just understand it.

---

## §1: Project Structure — Four Enterprises, Three Phases, Four Architectural Approaches (§2–§3)

**Claim 1 —** ZTA implementation is not a single architecture but a spectrum of deployment approaches — EIG, SDP, Microsegmentation, and SASE — each appropriate for different organizational contexts and maturity levels. The most complete ZTAs combine multiple approaches. → [[zta-implementation-single-architecture-spectrum-deployment-approaches]]
---

## §2: The 19 Builds — Implementation Patterns and Vendor Landscape (§3.6, §4)

**Claim 2 —** The 19 builds demonstrate that ZTA can be implemented with diverse vendor combinations, but integration gaps between PDPs, PEPs, and supporting components remain the primary practical challenge — not the ZTA concept itself. → [[19-builds-demonstrate-zta-implemented-diverse-vendor]]
---

## §3: Key Findings — What Actually Works and What's Still Broken (§5)

**Claim 3 —** The EIG crawl phase proved that legacy ICAM solutions can serve as PDPs for basic ZTA, but resource management (authenticating and verifying the health of the endpoint hosting the resource) is beyond current out-of-the-box integration capabilities. → [[eig-crawl-phase-proved-legacy-icam-solutions]]
---

## §4: The Seven-Step ZTA Journey (§8)

**Claim 4 —** ZTA implementation is a continuous improvement journey, not a one-time project — seven sequential steps, with discovery and identity as the non-negotiable foundations. → [[zta-implementation-continuous-improvement-journey-one]]
---

## §5: Demonstration Methodology and Use Cases (§6)

**Claim 5 —** The project's eight use case categories (A–H) provide a comprehensive ZTA testing framework — from discovery through data-level security — that organizations can adapt for their own validation. → [[project-eight-use-case-categories]]
---

## §6: Risk and Compliance Mappings (§7)

**Claim 6 —** The project mapped ZTA security capabilities to NIST CSF 1.1/2.0, NIST SP 800-53r5, and NIST critical software security measures — demonstrating that ZTA implementations support, rather than replace, existing compliance frameworks. → [[project-mapped-zta-security-capabilities-nist-csf]]
---

## Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| 1: Four deployment approaches (EIG, SDP, Microseg, SASE) are a spectrum | HIGH | Market convergence blurring approach boundaries |
| 2: 19 builds demonstrate ZTA is buildable; integration gaps are the real barrier | HIGH (buildability) / HIGH (gaps) | Vendors closing integration gaps faster than anticipated |
| 3: EIG crawl proves legacy ICAM can do basic ZTA; resource management is the gap | HIGH | Resource management tools evolving faster than projected |
| 4: Seven-step ZTA journey framework | HIGH | Resource-constrained organizations finding steps infeasible |
| 5: Eight use case categories as comprehensive ZTA testing framework | HIGH | New attack patterns requiring additional use cases |
| 6: ZTA supports existing compliance frameworks (CSF, 800-53) | MEDIUM | Conflicts between ZTA principles and specific SP 800-53 controls |

**Strongest contributions:**
1. **The 19-build matrix** — proof that ZTA can be built with commercially available technology. The single most valuable artifact for organizations seeking to understand what's possible.
2. **The integration gap findings (§5)** — honest documentation of what didn't work. More valuable than the successes because they shape procurement requirements.
3. **The incremental journey framework (§8)** — seven steps that make ZTA feel achievable rather than overwhelming.
4. **The eight use case categories (§6)** — exportable testing framework for any ZTA implementation.

**Weakest areas:**
1. **No cost data.** The document doesn't address what any of these builds cost — hardware, software licenses, integration labor, ongoing operations. For organizations making investment decisions, this is the missing variable.
2. **No performance benchmarking.** The lab environment is controlled — no data on how ZTA enforcement affects application latency, user experience, or operational overhead at scale.
3. **Limited legacy integration testing.** The lab started clean — real enterprises have mainframes, legacy applications, OT systems. The document acknowledges OT/IoT is out of scope, but even legacy IT (not just OT) poses integration challenges not represented.
4. **The supplement dependency.** Critical details (build architecture, implementation instructions, detailed demonstration results, compliance mappings) are in the online supplement only. The PDF is an executive summary, not the complete guide. Organizations must use the web format for implementation.

**Cross-cutting observations:**
- **The document is a marketing counterweight.** By demonstrating 19 builds with 24 vendors, NIST shows that ZTA isn't a single-vendor play. This undercuts vendor claims that ZTA requires their specific platform while still giving each vendor a showcase.
- **Identity is the gravitational center.** Every build, regardless of approach, has ICAM at its core. SDP builds still need Okta/Ping/Azure AD. SASE builds still need identity federation. This validates SP 800-207's identity-centric framing.
- **The lab is both a strength and a limitation.** The controlled environment enables rigorous, reproducible testing. But it also means the builds haven't faced the chaos of real enterprise environments — shadow IT, legacy systems, political resistance, budget constraints.
- **The phased approach is a political tool.** By showing that EIG crawl (legacy ICAM) is a valid starting point, NIST gives CISOs cover to begin their ZTA journey without requesting massive new budgets. The crawl → run → advanced framing is as much about organizational change management as it is about technology.
- **Mandiant MSV integration is significant.** By embedding security validation into every build, NIST demonstrates that ZTA isn't just about preventing access — it's about continuously verifying that controls work. This is an operational pattern that most ZTA guidance omits.

**Open questions:**
- Will the online supplement remain available and maintained? Practice guides that depend on linked web content risk link rot.
- How do these builds perform at enterprise scale (10,000+ users, 1,000+ applications)?
- What is the migration path from an EIG crawl build to an SDP + SASE build? The document shows they can both exist but doesn't describe the transition.
- How do these approaches handle the non-standard enterprise: IoT/OT environments, air-gapped systems, classified networks?
- What happens when a key component in a multi-vendor build reaches EOL or the vendor is acquired? The Broadcom/VMware/Omnissa footnote (line 322–324) hints at this risk without exploring it.
