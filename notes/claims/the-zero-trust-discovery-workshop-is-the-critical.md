---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/green-ortiz-zt-architecture
  - topic/zt-implementation
  - topic/zt-governance
  - topic/zt-cloud
  - topic/zt-architecture
claim_id: "go-intro.2"
statement: "The Zero Trust Discovery Workshop is the critical first step — skip it at your peril"
confidence: "medium"
confidence_rationale: "MEDIUM. Confidence not explicitly stated in source."
claim_type: "implementation"
source_note: "[[Green-Ortiz — Intro Ch1-2 — Foundations]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# go-intro.2: The Zero Trust Discovery Workshop is the critical first step — skip it at your peril

**Source:** [[Green-Ortiz — Intro Ch1-2 — Foundations]] — Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023

## The Claim

The Zero Trust Discovery Workshop is the critical first step — skip it at your peril

## Evidence

The authors' collective experience across "tens of organizations, hundreds across their respective careers." The workshop framework (Figure 1-2: Planning → Collect Data → Analyze Data → Presentation) with artifacts including 90-day short-term and 360-day long-term improvement plans. The SBC Healthcare fictional use case provides a worked example showing how business requirements (prevent PHI data loss, minimize ransomware impact) translate into technical requirements (AAA to ISE, device profiling, east-west traffic control, endpoint lifecycle management).

**Green-Ortiz's claim:**

Most organizations fail at Zero Trust because they skip the business-understanding phase and jump directly to technology implementation. A structured Discovery Workshop with four attendee categories (principal stakeholders, cross-functional SMEs, key strategists/decision makers, end-user experience representatives) is the mechanism to align business units, surface risks, and create an actionable roadmap before any enforcement is applied.

**Key dynamics:**

- **Top-down + bottom-up discovery must be combined.** Business unit interviews establish context (what data is sensitive, what processes are critical); traffic discovery tools (NetFlow, taps, firewall logs, endpoint telemetry) validate the actual communication patterns. Either alone produces blind spots.
- **Traffic discovery must span the "busy season."** Capturing only off-hours traffic misses quarterly financial reporting, end-of-month batch processing, and other critical-but-infrequent communication patterns. Change freezes should be carefully planned around data collection windows.
- **Artifacts are concrete deliverables.** The workshop should produce: policy documentation for endpoint types, identification flows (how users/devices are authenticated), endpoint requirements for network access, access restrictions per use case, and locations for storing/analyzing monitoring data.
- **The "Problem? What problem?" syndrome is the most dangerous.** Organizations that don't recognize ZT as needed have the worst gaps. Marketing dilution of the term — where vendors claim a single product delivers ZT "with a click of a button" — fuels skepticism. The response: ZT is an *architectural strategy*, not a product strategy.
- **"Cloud is Zero Trust by default" is false.** Cloud providers' shared responsibility model means organizations must bring their own tools, solutions, and visibility. Moving to the cloud without ZT principles is just moving the problem.

**Cross-reference — NIST 800-207:**

NIST 800-207 Ch7 (Migration) defines a 7-step deployment cycle (identify actors → assets → business processes → policies → candidate solutions → deploy/monitor → expand). Green-Ortiz's workshop maps to NIST's first four steps but adds the crucial organizational dynamics dimension (stakeholder buy-in, executive sponsorship, competing teams) that NIST's technical focus omits.

**Cross-reference — Gilman & Barth Ch1:**

Gilman & Barth's five assertions (the network is hostile, locality doesn't determine trust, every flow is authenticated, etc.) are what the workshop participants need to *internalize* before planning. The workshop is the process; the assertions are the principles that guide the process.

## Confidence

**Rating:** MEDIUM
**Rationale:** MEDIUM. Confidence not explicitly stated in source.

## Stakes

_Not addressed separately in the source note._

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

This is the most operationally valuable section of the book. The workshop methodology addresses the #1 ZT failure mode — treating it as a technology project rather than an organizational transformation. The four attendee categories are particularly well-chosen: they ensure authority, technical knowledge, and frontline impact awareness are all represented.
