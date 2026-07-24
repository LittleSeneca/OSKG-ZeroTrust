---
tags:
  - source/standards
  - nsa
  - zt-definition
  - zt-principles
  - zt-threat-model
  - assume-breach
  - oskg-zerotrust
created: 2026-07-24
updated: 2026-07-24
confidence: high
source:
  title: "Embracing a Zero Trust Security Model"
  authors: "National Security Agency"
  year: 2021
  publisher: "NSA"
  local_file: "sources/standards/_txt/NSA_Embracing_Zero_Trust.txt"
related:
  - "[[NIST 800-207 — Ch2 — Zero Trust Basics]]"
  - "[[CISA ZTMM — Overview and Framework]]"
  - "[[NSA ZT User Pillar]]"
  - "[[NSA ZT Device Pillar]]"
  - "[[NSA ZT Network Environment Pillar]]"
  - "[[Concepts Index]]"
---

# NSA — Embracing a Zero Trust Security Model

The NSA's foundational Zero Trust document. Published February 2021, it predates CISA's maturity model v2 (April 2023) and the NSA pillar-specific guidance (2023-2024). It establishes the threat-centric framing that distinguishes NSA's approach from NIST's more architectural framing. 7 pages.

## Claim 1: Zero Trust is defined by "assume breach," not architecture

**NSA's claim:** "The Zero Trust security model assumes that a breach is inevitable or has likely already occurred, so it constantly limits access to only what is needed and looks for anomalous or malicious activity."

**Evidence presented:** The document opens with the threat landscape — sophisticated adversaries, perimeter defense failure, insider threats — before defining what Zero Trust IS. This is a rhetorical choice: define the problem first, then present Zero Trust as the solution. NIST 800-207 does the opposite: defines the architecture, then discusses threats in Ch 5.

**Confidence:** HIGH. This framing is consistent across all NSA Zero Trust publications.

**What's at stake:** If "assume breach" is the core principle, ZT is fundamentally a threat-response strategy. If architecture is the core (NIST's framing), ZT is a design methodology. Both are true but the emphasis matters for implementation priorities: NSA starts with monitoring and detection; NIST starts with policy engine design.

**Who disagrees:** NIST 800-207 defines ZT as "minimizing uncertainty" — a gentler, more risk-management-oriented framing. DoD ZT Strategy splits the difference: assume breach AND architect accordingly.

**Alternative reading:** The "assume breach" framing could be read as NSA's institutional bias — as a signals intelligence agency, they think in terms of adversaries. NIST's "minimize uncertainty" is more appropriate for civilian agencies that face compliance risk as much as adversarial risk.

**My assessment:** Both framings are correct and complementary. NSA's threat-centric view makes ZT feel urgent and operational. NIST's architecture-centric view makes ZT implementable and auditable. The CISA maturity model synthesizes both: it measures maturity by capability (architecture) against a threat-informed baseline.

---

## Claim 2: The three guiding principles operationalize ZT for defenders

**NSA's claim:** Three principles: (1) Never trust, always verify — treat every user, device, application, and data flow as untrusted; (2) Assume breach — operate as if an adversary already has presence; (3) Verify explicitly — use multiple attributes to derive confidence levels for access decisions.

**Evidence presented:** These principles echo Kindervag's original formulation but with NSA's operational emphasis. "Assume breach" is the NSA addition — it doesn't appear in NIST's seven tenets. "Verify explicitly" maps to NIST's Tenets 4 and 6 (dynamic policy, strict enforcement).

**Confidence:** HIGH. These three principles have become the industry-standard shorthand for ZT, appearing in vendor marketing and government RFPs alike.

**What's at stake:** The principles are simple enough to brief to leadership but operational enough to guide architects. This balance is what made the document influential beyond the DoD.

**Who disagrees:** Google BeyondCorp would add "remove the privileged network" as a fourth principle. NIST's positive-tenet approach avoids the negative "never trust" framing. Both are stylistic differences, not substantive disagreements.

**My assessment:** "Never trust, always verify" is the best three-word summary of Zero Trust ever written. "Assume breach" is the operational imperative. "Verify explicitly" is the implementation requirement. Together they form a complete operational philosophy.

---

## Claim 3: The threat examples demonstrate ZT's value, not ZT's completeness

**NSA's claim:** Three scenarios — compromised credentials, insider threat/remote exploitation, and supply chain compromise — show where ZT detects and contains threats that perimeter-based security misses.

**Evidence presented:** Each scenario walks through the attack chain in a traditional vs. ZT environment. In every case, ZT either prevents the attack (compromised credentials → device authentication fails), limits the blast radius (insider threat → microsegmentation), or provides detection that perimeter security lacks (supply chain → deny-by-default blocks C2).

**Confidence:** MEDIUM-HIGH. The scenarios are well-constructed and plausible, but they're illustrative, not empirical. NSA doesn't provide data on how often ZT actually prevents these attacks vs. how often attackers find workarounds.

**What's at stake:** These scenarios are the evidence base for ZT adoption in the DoD. If they're idealized, agencies may overestimate ZT's protective value. If they're realistic, they make a strong case.

**Who disagrees:** Academic research (see ZTA Enterprise Implementation paper, IJCA 2025) provides empirical evidence but at smaller scale. NIST 800-207 Ch 5 covers threats more systematically but less vividly.

**My assessment:** The scenarios are effective communication, not rigorous evidence. They're designed to persuade, not to prove. For claims about ZT effectiveness, the academic papers (Phase 1, Tier 4) will provide better evidence. But as a teaching tool, they're excellent — every CISO should be able to explain these three scenarios.

---

## Claim 4: ZT maturity is incremental, not binary

**NSA's claim:** "Incorporating Zero Trust functionality incrementally as part of a strategic plan can reduce risk accordingly at each step." Maturity progresses from preparation to basic, intermediate, and advanced stages.

**Evidence presented:** Figure 2 shows a maturity curve that directly anticipates CISA's four-level model (Traditional → Initial → Advanced → Optimal). NSA published this in February 2021; CISA published v1 in August 2021 and v2 in April 2023. NSA's maturity model was the template.

**Confidence:** HIGH. The incremental maturity approach is now universal — CISA, DoD, and NSA all use it.

**What's at stake:** If maturity is binary ("you're either ZT or you're not"), adoption stalls because full ZT is impossible. If incremental, every step reduces risk and builds toward the goal. This is the single most important implementation insight in the document.

**Who disagrees:** Purists argue that "partial Zero Trust" is an oxymoron — if you still have implicit trust zones, you don't have Zero Trust. The counter is that perfect is the enemy of better, and incremental adoption with measurable maturity levels is how complex systems actually change. The CISA maturity model explicitly endorses the incremental approach.

---

## Claim 5: Organizational commitment is the primary implementation challenge

**NSA's claim:** "The first potential challenge is a lack of full support throughout the enterprise, possibly from leadership, administrators, or users. The mindset required for Zero Trust must be embraced fully for any solution to be successful."

**Evidence presented:** NSA identifies three challenges: (1) lack of enterprise-wide buy-in, (2) scalability of continuous access decisions, (3) persistent adherence to the ZT mindset over time ("administrators and defenders may become fatigued"). Notably, technology is not listed as a primary challenge.

**Confidence:** MEDIUM-HIGH. Consistent with Finney's Project Zero Trust (which is entirely about organizational change). But NSA provides no data on how often organizational failure vs. technical failure causes ZT initiatives to fail.

**Who disagrees:** Vendor literature emphasizes technology challenges (legacy systems, integration complexity). The truth is probably both: organizational resistance AND technical debt. NSA's emphasis on mindset reflects their experience with defense organizations where cultural inertia is the harder problem.

---

## Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| ZT defined by "assume breach" | HIGH | Overemphasis on threat vs. architecture |
| Three guiding principles | HIGH | Oversimplification of complex implementation |
| Threat scenarios as evidence | MEDIUM-HIGH | Lack of empirical validation |
| Incremental maturity | HIGH | Purist objection to "partial ZT" |
| Organizational commitment as primary challenge | MEDIUM-HIGH | Technology challenges understated |

**Strongest section:** The three guiding principles and the threat scenarios. These are the most cited and most operationally useful parts of the document.

**Weakest section:** "Potential challenges." Three paragraphs is too thin for the hardest part of ZT adoption. Compare to NIST 800-207 Ch 7 (the full 7-step migration process) or Finney's Project Zero Trust (224 pages on organizational change).

**Historical significance:** This document, published in February 2021, sits between EO 14028 (May 2021) and the federal ZT mandate. It gave NSS owners and operators a threat-centric rationale for ZT adoption before the executive order made it mandatory. It also introduced the maturity framework that CISA later refined.
