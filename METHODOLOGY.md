---
tags:
  - type/meta
  - methodology
  - oskg-zerotrust
  - knowledge-graph
  - pipeline
created: 2026-07-24
updated: 2026-07-24
related:
  - "[[Home]]"
  - "[[Book Guide]]"
  - "[[Paper Guide]]"
  - "[[notes/claims/Claims Index]]"
  - "[[notes/synthesis/Synthesis Index]]"
  - "[[../OSKG-YahWeh/METHODOLOGY]]"
---

# METHODOLOGY

## What This Is

OSKG-ZeroTrust is an **Open Source Knowledge Graph** (OSKG) — a structured, queryable graph of claims about Zero Trust architecture, built from foundational books, NIST standards, government frameworks, Google BeyondCorp implementation papers, and academic research. Every claim, edge, and synthesis artifact is open and reproducible.

The graph does not summarize books. It decomposes them into first-class claim nodes and connects them through typed relationships. The synthesis that emerges — what is settled, what is contested, what is load-bearing — is generated from graph structure, not from reading summaries or relying on author reputation.

## What an OSKG Is

An Open Source Knowledge Graph applies three principles:

1. **Structured extraction.** Source documents are not summarized. They are decomposed into discrete, individually addressable claim nodes with explicit metadata (author, confidence, evidence type, topic).
2. **Typed edges.** Claims are connected through semantic relationships — supports, contradicts, depends on, extends — creating a traversable argument graph, not a flat collection of notes.
3. **Open and reproducible.** Every claim is traceable to its source. Every edge is documented. The synthesis methodology is explicit. Anyone with the same sources can reproduce, audit, or extend the graph.

The canonical academic implementation is the **Open Research Knowledge Graph (ORKG)** at Leibniz University Hannover, which has built the same pipeline architecture for scientific literature since ~2019. OSKG-ZeroTrust applies the same principles to a cybersecurity architecture domain — where Zero Trust is simultaneously a government mandate, a vendor battleground, and a genuine architectural paradigm shift.

## The Pipeline

The project moves through five phases:

```
12 books + 19 papers + 5+ standards → ~85 chapter notes → claims → typed-edge graph → 4-phase synthesis → capstone
```

### Phase 0: Source Acquisition

The Book Guide and Paper Guide define the canonical corpus across four tiers: foundational texts, specialized/complementary works, government standards and frameworks, and adjacent texts. Sources are acquired from digital archives and direct downloads — government PDFs and open-access papers are freely available from their issuing agencies; defense and military sites require wget with browser headers. Raw full-text PDFs are gitignored for copyright. Only structured extraction artifacts (notes, claims, edges) are versioned.

### Phase 1: Reading Notes

Each source is read chapter by chapter (or section by section for standards). Each chapter produces a structured note with the author's arguments, evidence, and positions relative to other texts in the corpus. Notes include explicit frontmatter (author, work, chapter, topics) and inline cross-references to other authors, standards, and primary sources.

Cross-referencing happens during note-taking, not after. When a book describes the policy engine / policy enforcement point split, the note cross-references NIST SP 800-207's original definition of the same concept. When a paper makes an empirical claim about microsegmentation performance, the note cross-references other sources that address the same question.

### Phase 2: Claims Extraction

Each chapter note is decomposed into 5-10 discrete claims. Each claim becomes a standalone file in `notes/claims/` with:

- **YAML frontmatter**: claim ID (ZT-###), author, source work, confidence rating (high to speculative), evidence type (architectural, empirical, theoretical, anecdotal), topic tags
- **Claim statement**: one atomic, falsifiable assertion
- **Edges section**: explicit wikilinks to other claims the claim supports, contradicts, depends on, or extends

Claims are first-class nodes. They are not summaries of what an author said. They are testable assertions extracted from architectural argumentation and empirical evidence, tagged with metadata that makes the graph queryable.

### Phase 3: Graph Construction

Edges are created in two passes:

1. **Intra-source edges (Phase 2):** Claims from the same source are connected during extraction — what depends on what, what supports what, within a single book or standard.
2. **Cross-source edges (Phase 3):** Claims are connected across sources — who contradicts whom, who extends whom, where do independent sources converge on the same finding. This produces the contradiction pairs, support clusters, and convergence patterns that drive synthesis.

Edge types:

- **Supports** — Claim A provides evidence or reasoning for Claim B
- **Contradicts** — Claim A asserts the opposite of Claim B (same topic, incompatible conclusions)
- **Depends on** — Claim B logically requires Claim A to be true
- **Extends** — Claim A builds on Claim B with additional specificity or a new domain

### Phase 4: Structural Analysis (Synthesis Phases 1-4)

The completed graph is analyzed through four passes, following the methodology established by OSKG-YahWeh:

**Phase 1 — Hinge Inventory:** Identifies load-bearing claims by counting how many other claims depend on them. The top hinges are ranked by dependency count. In Zero Trust, candidate hinges might include "the policy engine / policy enforcement point split is the core architectural pattern" or "device trust is a continuous property, not a binary state."

**Phase 2 — Cascade Trees:** Traces full collapse radii for the top hinges using breadth-first search. Maps what claims become unsupported if a hinge is falsified. Identifies critical children — claims deep in the dependency chain that also face active contradiction from other sources.

**Phase 3 — Counter-Position Stress Tests:** Tests the graph against the strongest counter-positions. For Zero Trust, this might include: "perimeter-based security remains viable with proper segmentation," "Zero Trust is a vendor marketing framework, not a coherent architecture," or "true Zero Trust is impossible at enterprise scale." Produces survival rates and identifies single points of failure.

**Phase 4 — Unknowns and Convergence:** Identifies settled convergences (5+ HIGH confidence supports with zero MEDIUM+ contradictions) and genuine unknowns (bidirectional HIGH+ contradictions where both sides are confident). Produces the evidence-density map that drives the capstone.

### Phase 5: Capstone Synthesis

The capstone synthesizes the structural analysis into a document that reports what the graph shows: what is settled about Zero Trust architecture, what is genuinely contested, what the graph's architecture reveals about evidence density and vendor influence, and where the fragilities lie. The capstone does not summarize books or recommend products. It reports graph structure.

## How This Aligns with OSKG Principles

The pipeline converges with the ORKG approach. Both implement the same architecture: structured claim extraction → typed edges → graph querying → synthesis from structure. The convergence across a cybersecurity domain (Zero Trust) and the original humanities domain (biblical studies) further validates the pattern as a general solution to scholarly and technical synthesis.

| OSKG Principle | ORKG Implementation | OSKG-ZeroTrust Implementation |
|---------------|-------------------|-------------------------------|
| **Structured extraction** | LLM + human-in-the-loop extraction from scientific papers | LLM (Hermes) + human review from chapter notes |
| **Claim nodes** | Semantic frontmatter on structured claim objects | Standalone claim files with YAML frontmatter in `notes/claims/` |
| **Typed edges** | Semantic relations between claims | Supports, contradicts, depends on, extends |
| **Quality gate** | Automated validation | Human evaluation of every claim and edge during extraction |
| **Edge creation** | Cross-paper inference + curator review | Intra-source (Phase 2) + cross-source (Phase 3) |
| **Query layer** | SPARQL / semantic search | Obsidian graph view + tag filtering + wikilink traversal |
| **Synthesis** | Evidence synthesis from graph structure | Convergence scoring, fault line detection, cascade trees, stress tests |
| **Openness** | Open-access knowledge graph | Open-source GitHub repo, all claims and edges documented |

## Where This Differs from the Standard OSKG Approach

| Dimension | ORKG Standard | OSKG-ZeroTrust |
|-----------|--------------|----------------|
| **Scale** | Millions of papers, tens of millions of claims | ~36 sources, projected hundreds of claims |
| **Granularity** | Paper-level or finding-level claims | Chapter-level claims with direct source traceability |
| **Domain** | Scientific literature (biomedical, CS, engineering) | Cybersecurity architecture: standards, practitioner books, government frameworks |
| **Fidelity** | Statistical (~70% extraction accuracy at scale) | High (every claim traced to a specific passage in a specific chapter) |
| **Human involvement** | Curator reviews LLM output on samples | Author evaluates every claim inline during extraction |
| **Edge density** | Sparse (cross-paper connections scale poorly) | Dense (small corpus enables comprehensive cross-referencing) |
| **Synthesis depth** | Broad coverage across many topics | Deep analysis of one domain: "What does the evidence actually show about Zero Trust?" |
| **Query mechanism** | Formal semantic queries (SPARQL) | Filesystem graph traversal (wikilinks + Obsidian graph view) |
| **Source types** | Peer-reviewed papers | Books, government standards, white papers, implementation narratives, academic papers |

### The Cybersecurity-Specific Challenge

The standard OSKG approach was designed for scientific literature, where claims are empirical, falsifiable, and relatively self-contained. Cybersecurity architecture — particularly Zero Trust — presents different challenges:

- **Claims are often prescriptive, not descriptive.** "Organizations should implement microsegmentation at Layer 7" is a recommendation, not a falsifiable finding. The evidence is architectural reasoning, case studies, and operational experience — different evidence types that carry different weight.
- **Vendor influence is real.** Many books are published by Cisco Press. Google's BeyondCorp papers document a real implementation but also serve Google Cloud's commercial interests. The graph must distinguish between architectural claims supported by evidence and architectural claims that serve a product strategy.
- **The domain is actively evolving.** NIST SP 800-207 was published in 2020. CISA's maturity model was updated in 2023. New books appear annually. Claims are not static — they have a temporal dimension that the graph must capture.
- **Government standards carry genuine authority.** NIST, CISA, DoD, and NSA documents are not just another source — they are the regulatory and architectural bedrock that the rest of the industry builds on. The graph must reflect this asymmetry without treating government standards as infallible.
- **Implementation evidence is scarce.** Unlike medicine or physics, cybersecurity lacks controlled experiments. The BeyondCorp papers are the closest thing to empirical evidence in the field, and even they document a single organization's experience. Most claims rest on architectural reasoning, not empirical validation.

OSKG-ZeroTrust addresses these by maintaining explicit evidence-type metadata (architectural vs. empirical vs. theoretical vs. anecdotal), tracking source provenance (vendor-affiliated vs. independent vs. government), and capturing temporal context (when was this claim made, and has subsequent work confirmed or challenged it).

### Query Layer Differences

The standard OSKG uses formal semantic queries (SPARQL) over RDF triples. OSKG-ZeroTrust uses the Obsidian vault as its graph database — wikilinks are edges, files are nodes, tag filtering is the query language, and graph view is the visualization layer. For a corpus of this size, this is sufficient. It enables queries like "show me every HIGH-confidence claim about microsegmentation that has contradicting evidence" through tag intersection and wikilink traversal. For larger corpora, a formal semantic layer would be necessary.

## Fair Use and Copyright

The OSKG methodology depends on working with full-text sources — books, papers, and government publications — to produce structured claim extraction. The legal basis for this work is fair use under 17 U.S.C. § 107. This is not a legal technicality. It is a deliberate methodological position: the knowledge graph is a transformative scholarly work, not a reproduction of the sources.

### The Four-Factor Analysis

**Factor 1: Purpose and Character of Use.** The knowledge graph is a work of scholarship and research. It does not reproduce books. It decomposes them into atomic, individually addressable claim nodes with explicit metadata and typed edges — a fundamentally different purpose and character from the original works. A person reading claim node ZT-047 ("NIST SP 800-207 defines the policy engine as the component responsible for the ultimate decision to grant access") is not reading NIST SP 800-207. They are consulting a structured knowledge graph that points back to NIST SP 800-207. The use is transformative.

**Factor 2: Nature of the Copyrighted Work.** The corpus consists of factual and technical works: architecture books, government standards, implementation narratives, academic papers. These are precisely the type of works that fair use doctrine protects most strongly for scholarly extraction. They are not creative fiction. They describe technology patterns, architectural principles, and operational practices. The factual nature of the material weighs heavily in favor of fair use.

**Factor 3: Amount and Substantiality.** Claims extraction takes the minimum necessary from each source: short, atomic assertions extracted at chapter granularity. No chapter is reproduced in full. No book is reproduced in any form. The claims are the smallest extractable units of meaning — typically one to three sentences each. The "heart" of a Zero Trust book is its argument architecture, not any individual sentence. The knowledge graph maps that architecture without reproducing the prose.

**Factor 4: Effect on the Market.** The knowledge graph does not substitute for the original works. No one reads claim nodes instead of buying *Zero Trust Networks* (O'Reilly) or *Zero Trust Architecture* (Cisco Press). The knowledge graph is a research tool — it fills a different market niche entirely. If anything, it increases demand for the original works by demonstrating their value and making their argument architecture visible. A reader who discovers through the graph that Gilman and Barth's authenticating proxy pattern is foundational to ZTNA is more likely to buy the book, not less.

### Government Works: Public Domain

A substantial portion of the Zero Trust corpus consists of United States government publications: NIST SP 800-207 and 800-207A, CISA's Zero Trust Maturity Model, the DoD Zero Trust Reference Architecture, and NSA guidance documents. Under 17 U.S.C. § 105, "copyright protection under this title is not available for any work of the United States Government." These documents are in the public domain. No fair use analysis is required — they can be extracted, quoted, and analyzed without restriction.

### Academic Papers: Open Access and Fair Use

The Google BeyondCorp papers were published in Usenix ;login: and are freely available from Google Research. The academic papers in the corpus are a mix of open-access (MDPI, Springer Open) and paywalled (Elsevier) publications. For paywalled papers, the same four-factor analysis applies: the knowledge graph extracts atomic claims, not full papers, for scholarly research purposes. This is well within established academic fair use norms.

### Why This Matters

The OSKG methodology is only viable if fair use protects the extraction pipeline. If every book required publisher permission, the knowledge graph could not exist — not because of cost, but because the transaction overhead would make systematic synthesis impossible. The fair use analysis here is transparent and specific, not a hand-waving assertion. Anyone who wants to audit, reproduce, or extend the graph can evaluate the legal basis for themselves.

## Key References (ORKG Literature)

The ORKG literature provides the academic scaffolding for this methodology:

1. **Auer, D'Souza & Farfar (2025).** "Open Research Knowledge Graph: A Large-Scale Neuro-Symbolic Knowledge Organization System." *Frontiers in AI and Knowledge Organization*. The flagship paper describing structured claim extraction → typed edges → semantic synthesis.

2. **Tan & D'Souza (2026).** "Diagnosing structural failures in LLM-based evidence extraction for meta-analysis." arXiv:2602.10881. Uses ORKG schema for claim-level extraction. Validates the LLM + human-in-loop approach.

3. **Aggarwal (2026).** "Interactive Knowledge Extraction: A Human-in-the-Loop Approach for PDF Structuring and Knowledge Graph Integration." Leibniz University Hannover. The human-in-the-loop extraction model.

4. **Sander (2025).** "ORKG ASK Deep Research: Enhancing Scientific Search through LLM-based Reasoning over Research Papers." Uses ORKG graphs for "evidence synthesis that are difficult to achieve through traditional retrieval."

## Convergence with ORKG

The ORKG literature validates the architecture at scale (millions of papers, tens of millions of claims). OSKG-YahWeh validated it at depth in a humanities domain (17 books, 723 claims, biblical studies). OSKG-ZeroTrust extends the validation to a third domain — cybersecurity architecture — with different source types (government standards, practitioner books, implementation narratives), different evidence types (architectural reasoning, case studies, empirical measurement), and different synthesis challenges (vendor influence, active evolution, prescriptive claims).

The pattern holds across all three domains: structured claim extraction → typed edges → graph querying → synthesis from structure. This is not a domain-specific technique. It is a general solution to the problem of synthesizing large bodies of argumentation where claims are contested, evidence types are diverse, and the sources themselves cannot be taken at face value.

## Why This Matters

The standard mode of technical synthesis in cybersecurity is narrative: a practitioner reads widely and writes a survey or a framework that identifies patterns. This works but has limits. The synthesizer's own judgments — which authors to trust, which vendors to discount, which arguments feel compelling — are invisible. The reader cannot audit the synthesis. The synthesizer cannot query the evidence base.

An OSKG makes synthesis auditable. Every claim is individually addressable. Every edge is explicit. The synthesis does not say "the industry agrees that microsegmentation is essential" — it says "14 claims at HIGH confidence support microsegmentation as a core ZT principle; 3 claims at MEDIUM confidence challenge its feasibility at scale; the contradiction is concentrated in claims about Layer 7 microsegmentation specifically." The confidence is structural, not rhetorical.

This is particularly valuable for Zero Trust, where the landscape is dense with vendor claims, government mandates, and practitioner experience — and where the gap between what is asserted and what is demonstrated is wide. The graph does not resolve these tensions. But it makes them visible — as contradiction edges, as evidence-type asymmetries, as claims that are heavily supported by architectural reasoning but have zero empirical backing.

## Domain Adaptation

Zero Trust differs from the OSKG-YahWeh domain in ways that affect methodology at every phase:

| Dimension | OSKG-YahWeh | OSKG-ZeroTrust |
|-----------|-------------|-----------------|
| **Source type** | Scholarly monographs, archaeological reports | Technical books, government standards, practitioner guides, white papers |
| **Evidence type** | Archaeological, epigraphic, textual, iconographic | Architectural, empirical (case studies), theoretical, anecdotal |
| **Consensus** | Centuries of scholarship with established schools | Rapidly evolving field with significant vendor influence |
| **Temporality** | Ancient history (static evidence) | Active development (evidence still being produced, claims becoming obsolete) |
| **Primary sources** | Ancient inscriptions, artifacts, texts | NIST standards, CISA frameworks, DoD reference architectures, Google BeyondCorp |
| **Claims nature** | Historical/descriptive (what happened, when) | Architectural/prescriptive (how to build, what to do) |
| **Authority structure** | Peer review and scholarly reputation | Government mandate, vendor market position, practitioner consensus |

These differences are not deficiencies. They are the domain. The methodology adapts to them while preserving the core OSKG principles: structured extraction, typed edges, and reproducibility.

## Related Project Documents

- [[Home]] — Project philosophy, structure, and status
- [[Book Guide]] — Tiered reading list with acquisition status
- [[Paper Guide]] — Papers and white papers with acquisition status
- [[notes/claims/Claims Index]] — Claim file format, tag taxonomy, and edge type specification
- [[notes/synthesis/Synthesis Index]] — Synthesis phase index and methodology
- [[notes/evidence-briefs/Evidence Briefs Index]] — Synthesized evidence on specific questions
- [[notes/questions/Questions Index]] — Open research questions
- [[notes/history/History Index]] — Evolution of Zero Trust thinking (2010–present)
- [[../OSKG-YahWeh/METHODOLOGY]] — The methodology that established this pipeline architecture

---

*Built on the OSKG methodology, independently converged with ORKG. For the origin pipeline and the humanities validation, see [[../OSKG-YahWeh/METHODOLOGY|OSKG-YahWeh]].*
