---
tags:
  - source/standards
  - oskg-zerotrust
  - nist
  - zt-definition
  - zt-history
created: 2026-07-24
updated: 2026-07-24
confidence: high
source:
  title: "NIST SP 800-207 — Zero Trust Architecture"
  authors: "Scott Rose, Oliver Borchert, Stu Mitchell, Sean Connelly"
  year: 2020
  publisher: "National Institute of Standards and Technology"
  local_file: "sources/standards/_txt/NIST_SP_800-207_Zero_Trust_Architecture.txt"
  chapter_lines: "335–456"
related:
  - "[[NIST 800-207 Index]]"
  - "[[Concepts Index]]"
  - "[[History Index]]"
  - "[[Notes Index]]"
  - "[[Standards Index]]"
---

# NIST SP 800-207 — Ch 1: Introduction

The Introduction chapter establishes why Zero Trust exists (perimeter-based security has failed), defines ZT and ZTA in NIST's authoritative voice, traces the concept's intellectual lineage from DISA and Jericho Forum through Kindervag, and previews the document structure. It is the orienting chapter for the U.S. federal government's formal adoption of Zero Trust as a cybersecurity paradigm.

---

## §1.0: Opening Definition and Motivation (Lines 337–387)

### Claim 1: Perimeter-based network security has been rendered obsolete by enterprise complexity.

**Author's claim:** "A typical enterprise's infrastructure has grown increasingly complex... This complexity has outstripped legacy methods of perimeter-based network security as there is no single, easily identified perimeter for the enterprise. Perimeter-based network security has also been shown to be insufficient since once attackers breach the perimeter, further lateral movement is unhindered." (lines 337–342)

**Evidence presented:**
- Multiple internal networks, remote offices, mobile individuals, and cloud services all coexist in a single enterprise — no single boundary encloses them.
- Attackers who breach the perimeter face no further barriers to lateral movement.
- The evidence is observational/descriptive rather than empirical — NIST cites no breach statistics or studies.

**Confidence:** HIGH. The factual premise — enterprise infrastructure has become multi-perimeter — is publicly verifiable. Nearly every enterprise operates hybrid on-premises/cloud environments. The lateral-movement observation is also well-attested in breach forensics (Mandiant M-Trends, Verizon DBIR). However, NIST offers no quantitative evidence here; the confidence rests on widely accepted operational reality, not NIST's specific argumentation.

**What's at stake:** If this claim is false — if perimeter-based security remains adequate for some enterprise architectures — then the entire Zero Trust project is unnecessary for those enterprises. The urgency of ZT adoption depends on accepting that the perimeter model is fundamentally broken, not merely inconvenient. This claim is the *casus belli* for everything that follows in NIST 800-207.

**Who disagrees:** Perimeter-defense vendors (traditional firewall/VPN companies) have an economic interest in disputing this. The "defense in depth" school argues perimeter security remains a valid layer within a broader strategy, not an obsolete paradigm. Gartner's Secure Access Service Edge (SASE) framework preserves some perimeter concepts within a cloud-delivered model. See also [[History Index#Key Debates]] — Greenfield vs. Brownfield debate.

**Alternative reading:** The perimeter hasn't disappeared — it has multiplied and become dynamic. Rather than "no perimeter," modern enterprise has many micro-perimeters (cloud VPCs, SaaS boundaries, endpoint perimeters). The failure is not of perimeter *concept* but of *static, single-perimeter enforcement*.

**My assessment:** The claim is fundamentally correct as stated but imprecise. The problem isn't that perimeters are obsolete — it's that *static, implicit-trust-inside* perimeters are obsolete. NIST later acknowledges this nuance by describing hybrid ZT/perimeter-based operations (line 371–373). The stronger version of this claim (perimeter security is broken) holds up; the weaker version (perimeters don't exist) overstates the case.

---

### Claim 2: Zero Trust assumes breach and eliminates implicit trust — every access request must be continuously authenticated, authorized, and risk-evaluated.

**Author's claim:** "Zero trust security models assume that an attacker is present in the environment and that an enterprise-owned environment is no different—or no more trustworthy—than any nonenterprise-owned environment. In this new paradigm, an enterprise must assume no implicit trust and continually analyze and evaluate the risks to its assets and business functions and then enact protections to mitigate these risks." (lines 349–357)

**Evidence presented:**
- Definitional — NIST is establishing the concept, not proving it with evidence.
- The definition is operationalized: "minimizing access to resources... to only those subjects and assets identified as needing access as well as continually authenticating and authorizing the identity and security posture of each access request." (lines 354–357)
- References FIPS 199 for classification/sensitivity levels to which ZT applies (line 366).

**Confidence:** HIGH as a *definition* (NIST is the authoritative definer for federal purposes), MEDIUM as an *empirical claim* about effectiveness. The definition is NIST's to make — there's no factual dispute about what NIST *says* ZT means. Whether ZT *works* as defined is a separate question requiring empirical evidence from Sections 4–5.

**What's at stake:** This is the core definitional claim of the entire document. If "assume breach" is too extreme a posture, ZT becomes infeasibly expensive. If "no implicit trust" is impossible to operationalize (every access decision requires context that can't always be evaluated), ZTA designs may be unrealizable. Conversely, if this definition is too weak, ZTA becomes indistinguishable from existing defense-in-depth.

**Who disagrees:** Practitioners who argue that "assume breach" is a useful thought experiment but not an operational stance — you can't effectively run an enterprise while acting as if every component is already compromised. The "trust but verify" school retains a role for baseline trust. See Garbis & Chapman's critique in "Zero Trust Security: An Enterprise Guide" — they argue for pragmatic trust levels rather than absolute zero. Finney ("Project Zero Trust") frames ZT as a *strategy* that tolerates progressive implementation, not an absolute state.

**Alternative reading:** "Assume breach" is aspirational framing, not literal operational guidance. NIST itself walks this back by describing hybrid ZT/perimeter operations (line 371–373). The practical reading is "don't assume safety behind the perimeter" rather than "assume everything is already compromised."

**My assessment:** The definition is crisp and has proven durable — subsequent NIST publications (800-207A, 2024) retain essentially the same formulation. The tension between the absolute language ("no implicit trust") and the pragmatic implementation guidance ("hybrid mode," "incremental") is a feature, not a bug: NIST sets the aspirational target while acknowledging real-world constraints. The definition's strength is that it closes the door on "trusted internal network" thinking.

---

### Claim 3: ZTA is an enterprise cybersecurity architecture designed specifically to prevent data breaches and limit internal lateral movement.

**Author's claim:** "A zero trust architecture (ZTA) is an enterprise cybersecurity architecture that is based on zero trust principles and designed to prevent data breaches and limit internal lateral movement." (lines 358–360)

**Evidence presented:**
- None — this is a design-intent statement, not an efficacy claim.
- The document previews that it "discusses ZTA, its logical components, possible deployment scenarios, and threats" and "presents a general road map for organizations wishing to migrate" (lines 360–363) — evidence is deferred to later sections.

**Confidence:** MEDIUM. This is a *design goal* statement. Whether ZTA *achieves* this goal depends on implementation fidelity, threat model accuracy, and operational realities that NIST has not yet demonstrated in this chapter. The claim is testable: do enterprises with mature ZTA implementations experience fewer breaches and less lateral movement?

**What's at stake:** If ZTA cannot actually prevent breaches or limit lateral movement — if it only shifts the attack surface — then the entire architectural paradigm may be a costly reallocation of resources rather than a genuine security improvement. This is the core efficacy question for ZT.

**Who disagrees:** Critics who argue ZT shifts complexity rather than eliminating it — attackers adapt to policy engines, identity systems become the new high-value targets, and the attack surface of the ZTA control plane itself becomes the vulnerability. The "ZT creates a single point of failure at the policy engine" critique. See [[Questions Index]] — "Does ZTA actually reduce risk or just move it?"

**Alternative reading:** ZTA doesn't *prevent* breaches — it *contains* them. The design is about blast-radius reduction, not breach prevention. "Limit internal lateral movement" is the achievable goal; "prevent data breaches" is aspirational.

**My assessment:** The claim conflates two different goals. "Limit internal lateral movement" is architecturally plausible given ZTA's microsegmentation and per-session authentication. "Prevent data breaches" is a much stronger claim that requires evidence from deployed systems. Google's BeyondCorp papers provide some evidence for lateral-movement limitation; comprehensive breach-prevention evidence remains sparse in the public literature. I'd treat "limit lateral movement" as the credible claim and "prevent data breaches" as the aspirational framing.

---

### Claim 4: ZT is an architectural paradigm, not a product — adoption is a journey of risk evaluation, incremental, and most enterprises will operate in hybrid mode.

**Author's claim:** "ZT is not a single architecture but a set of guiding principles for workflow, system design and operations... Transitioning to ZTA is a journey concerning how an organization evaluates risk in its mission and cannot simply be accomplished with a wholesale replacement of technology... Most enterprise infrastructures will operate in a hybrid zero trust/perimeter-based mode while continuing to invest in IT modernization initiatives." (lines 364–373)

**Evidence presented:**
- Many organizations "already have elements of a ZTA in their enterprise infrastructure today" (lines 368–369) — suggests ZT is a continuum, not a binary state.
- Organizations should "incrementally implement zero trust principles, process changes, and technology solutions... by use case." (lines 370–371)
- The hybrid-mode claim is presented as a descriptive forecast, not an empirical finding.

**Confidence:** HIGH on the definitional component (ZT is principles, not a product) — this is NIST's authoritative framing and aligns with Kindervag's original conception. MEDIUM on the hybrid-mode forecast — it's plausible given historical adoption patterns for major architectural shifts, but NIST offers no evidence.

**What's at stake:** This claim directly contradicts vendor marketing that positions ZT as something you can buy in a box. If NIST is correct, procurement decisions based on "buying ZT" are misguided. If vendors are correct (ZT is deliverable as an integrated platform), NIST's incrementalism may slow adoption of more effective solutions. This is the central tension in the ZT marketplace — see [[History Index#Key Debates]] ("Product vs. Strategy").

**Who disagrees:** ZTNA vendors (Zscaler, Cloudflare, Netskope) position their platforms as delivering ZT outcomes. SDP vendors argue that a properly deployed SDP *is* ZTA. The vendor community generally accepts NIST's definitional authority while positioning products as "enabling" or "accelerating" ZT adoption — a rhetorical accommodation rather than genuine disagreement.

**Alternative reading:** ZT *is* a set of principles, but mature product platforms can operationalize those principles at scale without requiring every organization to architect from scratch. The "journey" framing may overstate the difficulty and understate what's achievable with modern platforms.

**My assessment:** This is one of the most important claims in the chapter and potentially the most durable. NIST walks a careful line — establishing ZT as principles-based to prevent vendor capture of the definition, while acknowledging that technology solutions exist. The hybrid-mode prediction has been validated: five years after publication, few enterprises claim to be fully ZT-compliant; most describe themselves as "on the journey." The claim ages well.

---

## §1.1: History of Zero Trust Efforts Related to Federal Agencies (Lines 388–413)

### Claim 5: The concept of zero trust predates the term — DISA "black core" and the Jericho Forum were conceptual predecessors focused on per-transaction security and de-perimeterization.

**Author's claim:** "The concept of zero trust has been present in cybersecurity since before the term 'zero trust' was coined. The Defense Information Systems Agency (DISA) and the Department of Defense published their work on a more secure enterprise strategy dubbed 'black core' [BCORE]. Black core involved moving from a perimeter-based security model to one that focused on the security of individual transactions. The work of the Jericho Forum in 2004 publicized the idea of de-perimeterization—limiting implicit trust based on network location and the limitations of relying on single, static defenses over a large network segment [JERICHO]." (lines 390–396)

**Evidence presented:**
- DISA's "black core" [BCORE] — DoD strategy for per-transaction security (date not specified in this text; DISA black core work dates to early 2000s).
- Jericho Forum (2004) — industry consortium that coined "de-perimeterization" [JERICHO].
- NIST cites these as precursors, establishing intellectual lineage for the federal audience.

**Confidence:** HIGH. The existence of DISA black core and the Jericho Forum is publicly verifiable. The Jericho Forum's papers on de-perimeterization are archived and accessible. The claim that these concepts *preceded* the ZT term is factually correct — Kindervag's first ZT paper came in 2010, while Jericho Forum was active from 2004.

**What's at stake:** Establishing ZT as having *military and defense roots* rather than being a vendor invention gives it institutional legitimacy for federal adoption. It's harder for agencies to dismiss ZT as a Forrester marketing term when the DoD was exploring the same concepts independently. The intellectual lineage also protects ZT from being dismissed as a fad — it's presented as the culmination of 15+ years of thinking.

**Who disagrees:** No serious scholarly disagreement with the chronology. Some might argue that DISA black core and Jericho Forum were qualitatively different from ZT — they addressed network architecture, not the full identity/data/device scope that ZT encompasses. Kindervag added the explicit "zero trust" framing that transformed a network architecture concept into a comprehensive security paradigm.

**Alternative reading:** The lineage is real but NIST may be retroactively claiming ancestors to build legitimacy. DISA black core was a specific DoD program, not a general cybersecurity movement. Jericho Forum failed to achieve widespread adoption — de-perimeterization remained a niche concept until Kindervag rebranded it. The true conceptual breakthrough was Kindervag's synthesis, not the isolated predecessor efforts.

**My assessment:** NIST's history is accurate but compressed. The Jericho Forum's importance is probably overstated here for rhetorical purposes — de-perimeterization had limited industry impact compared to what ZT achieved. DISA black core is genuinely underappreciated and deserves the acknowledgment NIST gives it. The most significant omission: NIST doesn't mention Google's BeyondCorp (2014), which was arguably the most influential ZT predecessor, because that history is in §1.2's scope limitation (federal focus). The cross-reference to [[History Index]] is essential for the full timeline.

---

### Claim 6: John Kindervag at Forrester coined the term "zero trust," which then became the dominant term for security solutions that evaluate trust per-transaction rather than by network location.

**Author's claim:** "The concepts of de-perimeterization evolved and improved into the larger concept of zero trust, which was later coined by John Kindervag while at Forrester. Zero trust then became the term used to describe various cybersecurity solutions that moved security away from implied trust based on network location and instead focused on evaluating trust on a per-transaction basis. Both private industry and higher education have also undergone this evolution from perimeter-based security to a security strategy based on zero trust principles." (lines 397–402)

**Evidence presented:**
- Kindervag at Forrester as the source of the term (footnote cites https://go.forrester.com/blogs/next-generation-access-and-zero-trust/).
- NIST explicitly notes its non-endorsement of commercial products (footnote 2, lines 424–425) — distancing itself from Forrester as a commercial entity while crediting the intellectual contribution.
- The claim that "both private industry and higher education" adopted ZT is asserted without evidence.

**Confidence:** HIGH on Kindervag coining the term — this is well-documented and universally acknowledged in the literature. MEDIUM on "private industry and higher education have also undergone this evolution" — NIST provides no evidence for the breadth or depth of private-sector adoption.

**What's at stake:** Crediting Kindervag establishes ZT's origin as an industry analyst concept rather than an academic or government one — this shapes the intellectual history. If Kindervag's contribution is overstated, the concept may have deeper roots that would change how we evaluate ZT's theoretical foundations. The footnote disclaimer about commercial endorsement reflects NIST's institutional caution about appearing to promote Forrester.

**Who disagrees:** Some argue that ZT's real intellectual father is the Jericho Forum, and Kindervag's contribution was marketing/branding rather than conceptual innovation. Others point to earlier academic work on capability-based security and least-privilege architectures that anticipated ZT principles. Chase Cunningham (Kindervag's successor at Forrester) has positioned himself as extending and operationalizing Kindervag's concept, not merely inheriting it.

**Alternative reading:** Kindervag didn't "coin" ZT so much as synthesize existing ideas (de-perimeterization, least privilege, need-to-know) under a memorable brand. The term's power was in making an abstract security philosophy sellable to CISOs — it was a marketing triumph as much as a conceptual one.

**My assessment:** NIST's attribution is correct and appropriately hedged. The footnote disclaimer is telling — NIST is careful to credit the intellectual contribution without endorsing Forrester's commercial ecosystem. The claim about private industry and higher education adoption is the weakest part — it's asserted without evidence and serves primarily to broaden ZT's legitimacy beyond the federal context. For a fuller account of Kindervag's contribution, see the Forrester papers indexed in [[Papers Index]].

---

### Claim 7: Federal agencies have been building toward ZT for over a decade through foundational programs (FISMA, RMF, FICAM, TIC, CDM) that were initially limited by technology but are now maturing toward dynamic, granular access control.

**Author's claim:** "Federal agencies have been urged to move to security based on zero trust principles for more than a decade, building capabilities and policies such as the Federal Information Security Modernization Act (FISMA) followed by the Risk Management Framework (RMF); Federal Identity, Credential, and Access Management (FICAM); Trusted Internet Connections (TIC); and Continuous Diagnostics and Mitigation (CDM) programs. All of these programs aim to restrict data and resource access to authorized parties. When these programs were started, they were limited by the technical capabilities of information systems. Security policies were largely static and were enforced at large 'choke points' that an enterprise could control to get the largest effect for the effort. As technology matures, it is becoming possible to continually analyze and evaluate access requests in a dynamic and granular fashion to a 'need to access' basis to mitigate data exposure due to compromised accounts, attackers monitoring a network, and other threats." (lines 403–413)

**Evidence presented:**
- Enumeration of existing federal security programs (FISMA, RMF, FICAM, TIC, CDM) — their existence is publicly verifiable.
- Characterization of these programs as "building capabilities and policies" toward ZT — this is NIST's interpretive framing.
- The technology-limitation argument: earlier programs were "static" and enforced at "choke points" — this is asserted without historical evidence.
- The maturation claim: technology now enables "dynamic and granular" access decisions.

**Confidence:** HIGH on the existence of these programs and their access-restriction goals. MEDIUM-LOW on the claim that these programs were *designed* as building blocks toward ZT — this reads as retroactive reframing. FISMA (2002) and TIC (2007) predate the ZT term by years; characterizing them as ZT precursors is historically convenient but may not reflect original intent.

**What's at stake:** If federal agencies have already invested in ZT-enabling capabilities for a decade, then ZT adoption is not a radical break but a natural continuation — lowering the perceived cost and risk of adoption. Conversely, if these programs are fundamentally incompatible with ZT principles (e.g., TIC's choke-point model is the antithesis of distributed ZT enforcement), then the legacy investment may be an obstacle rather than a foundation.

**Who disagrees:** The TIC program in particular has been criticized as enforcing exactly the kind of perimeter-based choke-point architecture that ZT seeks to eliminate. TIC 3.0 (released after SP 800-207) attempted to reconcile this by introducing "use cases" for cloud and remote access, but the tension remains. CDM's focus on continuous monitoring aligns well with ZT; FICAM's identity federation is foundational. The claim works better for some programs than others.

**Alternative reading:** These programs weren't "building toward ZT" — they were separate, sometimes contradictory efforts that ZT now provides a unifying framework to rationalize. NIST is engaged in the standard bureaucratic practice of presenting new policy as the logical culmination of existing efforts rather than a departure.

**My assessment:** This is the most rhetorically interesting claim in the chapter because it reveals NIST's institutional strategy: make ZT adoption feel like continuation rather than disruption. The characterization is partially true (identity programs like FICAM are genuinely ZT-enabling) and partially revisionist (TIC's perimeter model was the problem ZT solves). The "technology maturation" argument is the strongest element — it's objectively true that dynamic, attribute-based access control (ABAC) is more feasible now than when these programs launched. The weakest element is the implication that these programs were conceived with ZT in mind.

---

## §1.2: Structure of This Document (Lines 414–446)

### Claim 8 (Structural): The document's organization — definitions → components → use cases → threats → federal guidance → migration roadmap — represents the essential framework for understanding and implementing ZTA.

**Author's claim:** This is an implicit claim conveyed through document organization rather than explicitly argued. The structure (lines 416–445):
- Section 2: ZT/ZTA definitions and design tenets
- Section 3: Logical components (building blocks)
- Section 4: Use cases (remote employees, cloud services, guest networks)
- Section 5: Threats to ZTA
- Section 6: Alignment with existing federal guidance
- Section 7: Migration roadmap

**Evidence presented:** The structure itself is the evidence — NIST is asserting, by organizational choice, that these are the essential elements of ZTA understanding. No meta-level justification is offered for why this particular sequence is correct.

**Confidence:** LOW as a claim about *optimal* organization — document structure reflects institutional and editorial choices as much as conceptual necessity. HIGH as a *descriptive* claim — this is indeed how the document is organized, and the structure has been influential (CISA's Maturity Model follows a similar pattern).

**What's at stake:** The structure shapes how readers understand ZTA. Definitions-before-components privileges conceptual clarity over operational urgency. Threats-after-use-cases suggests threats are architectural rather than fundamental. Migration-last positions ZTA as implementable. A different ordering (threats first, migration first) would produce different reader priorities. Organizations adopting this structure as their own ZT roadmap inherit NIST's priorities.

**Who disagrees:** Practitioners might argue for threats-first (understand the problem before the solution). Sales/marketing approaches put migration/use-cases first (start with what's actionable). Gilman & Barth's "Zero Trust Networks" organizes around the control plane/data plane architecture rather than the definitional approach NIST uses.

**Alternative reading:** The structure is driven by standards-document conventions (define, decompose, apply, caution, align, deploy) rather than pedagogical or architectural logic. It reflects how NIST writes standards, not necessarily how ZTA should be understood or implemented.

**My assessment:** The structure is conventional for a NIST SP and benefits from that familiarity for its federal audience. The most consequential choice is placing threats (Section 5) after use cases (Section 4) — this signals that ZTA threats are implementation-specific rather than inherent to the paradigm. This ordering may understate the risks of ZTA adoption. The structure has proven influential: subsequent ZT guidance documents across multiple jurisdictions follow a similar pattern, suggesting the organization was well-chosen even if NIST doesn't argue for it explicitly.

---

## Chapter 1 Overall Assessment

| Claim | Confidence | Most Vulnerable To |
|-------|-----------|-------------------|
| 1: Perimeter security obsolete | HIGH | Empirical counter-examples of effective perimeter-only architectures |
| 2: ZT = assume breach, no implicit trust, continuous evaluation | HIGH (definitional) / MEDIUM (efficacy) | Operational evidence that "assume breach" is infeasible |
| 3: ZTA designed to prevent breaches and limit lateral movement | MEDIUM | Lack of breach-prevention evidence at scale; policy-engine-as-single-point-of-failure |
| 4: ZT is principles, not product; adoption is incremental journey | HIGH | Platform vendors demonstrating "ZT in a box" works at scale |
| 5: ZT predates the term — DISA black core + Jericho Forum as precursors | HIGH | Disputing the conceptual continuity between these programs and modern ZT |
| 6: Kindervag coined "zero trust" at Forrester | HIGH | Earlier documented uses of the term (none known) |
| 7: Federal programs (FISMA, RMF, FICAM, TIC, CDM) built toward ZT | MEDIUM-LOW | Evidence that these programs were conceived independently and only retroactively aligned with ZT |
| 8: Document structure represents essential ZTA framework | LOW (as optimal) / HIGH (as descriptive) | Alternative organizations proving more effective for adoption or understanding |

**Strongest section:** §1.1 (History) — the intellectual lineage from DISA black core through Jericho Forum to Kindervag is well-sourced, properly hedged, and establishes federal legitimacy for ZT without erasing the contributions of industry and DoD. The chronology is accurate and the citations ([BCORE], [JERICHO]) point to verifiable primary sources.

**Weakest section:** §1.0's Claim 7 (federal program alignment) — the characterization of FISMA, RMF, FICAM, TIC, and CDM as building toward ZT is the most vulnerable to challenge. TIC in particular represents the antithesis of ZT principles (centralized choke-point enforcement), and retroactively claiming it as a ZT precursor strains credibility. The technology-maturation argument rescues the claim partially but doesn't address the fundamental architectural tension.

**Cross-cutting observations:**
- NIST writes for a federal audience; the chapter's emphasis on federal programs and DoD heritage reflects this institutional positioning. Non-federal readers may find the history parochial — missing Google's BeyondCorp, the Cloud Security Alliance's contributions, and international ZT efforts.
- The chapter performs significant *legitimation work* — establishing ZT as having military roots, as the natural culmination of existing federal investment, and as principles-based rather than vendor-driven. This is strategically important but analytically selective.
- The tension between absolutist language ("no implicit trust," "assume breach") and pragmatic guidance ("hybrid mode," "incremental," "by use case") runs throughout the chapter and is never resolved. This tension persists through the entire document and through subsequent ZT guidance.
- Claims 4 and 7 together produce an interesting paradox: if federal agencies have been building toward ZT for a decade, why is wholesale technology replacement not needed? The answer — because ZT is principles, not technology — is definitionally true but may understate the architectural changes required.

**Open questions for subsequent chapters:**
- Does Section 2's formal ZT definition resolve the absolutist/pragmatic tension?
- Does Section 5's threat model address the "policy engine as single point of failure" critique?
- Does Section 7's migration roadmap reconcile with the claim that existing federal programs are ZT-enabling?
- How does NIST's definition compare with concurrent definitions from CISA, DoD, and international standards bodies? (See [[Questions Index]])
