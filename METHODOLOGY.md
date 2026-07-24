---
tags:
  - type/meta
  - methodology
  - oskg-zerotrust
  - knowledge-graph
  - pipeline
created: 2026-07-24
related:
  - "[[Home]]"
  - "[[Book Guide]]"
  - "[[../OSKG-YahWeh/METHODOLOGY]]"
---

# METHODOLOGY

## What This Is

OSKG-ZeroTrust is an **Open Source Knowledge Graph** (OSKG) — a structured, queryable graph of claims about Zero Trust architecture, built from foundational books, NIST standards, government publications, and practitioner guides. Every claim, edge, and synthesis artifact is open and reproducible.

The graph does not summarize books. It decomposes them into first-class claim nodes and connects them through typed relationships. The synthesis that emerges — what is settled, what is contested, what is load-bearing — is generated from graph structure, not from reading summaries or relying on author reputation.

## What an OSKG Is

An Open Source Knowledge Graph applies three principles:

1. **Structured extraction.** Source documents are not summarized. They are decomposed into discrete, individually addressable claim nodes with explicit metadata (author, confidence, evidence type, topic).
2. **Typed edges.** Claims are connected through semantic relationships — supports, contradicts, depends on, extends — creating a traversable argument graph, not a flat collection of notes.
3. **Open and reproducible.** Every claim is traceable to its source. Every edge is documented. The synthesis methodology is explicit. Anyone with the same sources can reproduce, audit, or extend the graph.

The canonical academic implementation is the **Open Research Knowledge Graph (ORKG)** at Leibniz University Hannover. OSKG-ZeroTrust applies the same principles to a cybersecurity domain where the approach has not been previously tested.

## The Pipeline

```
N books + standards → chapter notes → claims → typed-edge graph → synthesis
```

### Phase 0: Source Acquisition

Foundational texts are acquired and extracted to plaintext (gitignored for copyright). The Book Guide defines the canonical reading list across four tiers: foundational, specialized, government standards, and adjacent frameworks.

### Phase 1: Reading Notes

Each text is read chapter by chapter (or section by section for standards). Each chapter produces a structured note with the author's arguments, evidence, and positions relative to other texts. Notes include explicit frontmatter (author, work, chapter, topics) and inline cross-references to other authors and primary sources.

### Phase 2: Claims Extraction

Each chapter note is decomposed into discrete claim nodes. Each claim is a separate markdown file with structured frontmatter and typed edges to other claims. Claims capture: what is asserted, what evidence supports it, how confident the author is, what happens if the claim is false, and who agrees/disagrees.

### Phase 3: Knowledge Graph

Claims become a traversable graph in Obsidian. Typed edges connect claims across sources. Tags filter by topic, author, evidence type, and confidence. The graph can answer questions like: "show me every claim about microsegmentation," "which claims about SDP vs. ZTNA contradict each other," "how many authors converge on the policy engine / policy enforcement point split?"

### Phase 4: Synthesis

Structured synthesis in four sub-phases:

1. **Hinge inventory.** Identify which claims are load-bearing — if they fall, what downstream claims collapse?
2. **Cascade trees.** Map the dependency chains for critical claims. What evidence does each claim depend on?
3. **Counter-position stress tests.** What would the strongest opponent of each major position argue? What survives the stress test?
4. **Convergence and unknowns.** Where do sources genuinely converge? What remains genuinely unsettled?

### Phase 5: Capstone

The culminating synthesis document: What does the evidence actually show about Zero Trust? Written in evidence-forward voice — reporting what the graph reports, not adjudicating what it means.

## Claim Format

Every claim follows this structure:

```yaml
---
claim_id: ZT-### 
statement: "What is being claimed"
confidence: high | medium | low | speculative
topic: [tags]
author: [source author]
source: [book/section]
evidence_type: architectural | empirical | anecdotal | theoretical
edges:
  supports: [claim-ids]
  contradicts: [claim-ids]
  depends_on: [claim-ids]
  extends: [claim-ids]
---
```

## Edge Types

| Edge | Meaning | Example |
|------|---------|---------|
| **supports** | Claim A provides evidence for Claim B | "ZTNA replaces VPNs" supports "perimeter-based security is obsolete" |
| **contradicts** | Claim A and Claim B cannot both be true | "SDP is a subset of ZT" contradicts "SDP is equivalent to ZT" |
| **depends on** | Claim A requires Claim B to be true | "Microsegmentation at Layer 7" depends on "identity-aware proxies are feasible at scale" |
| **extends** | Claim A builds on Claim B with additional specificity | "CISA maturity model Level 3" extends "NIST SP 800-207 logical components" |

## Domain Adaptations

Zero Trust differs from the OSKG-YahWeh domain in important ways that affect methodology:

| Dimension | OSKG-YahWeh | OSKG-ZeroTrust |
|-----------|-------------|-----------------|
| **Source type** | Scholarly monographs, archaeological reports | Technical books, government standards, practitioner guides |
| **Evidence type** | Archaeological, epigraphic, textual | Architectural, empirical (case studies), theoretical |
| **Consensus** | Centuries of scholarship with established schools | Rapidly evolving field with vendor influence |
| **Temporality** | Ancient history (static evidence) | Active development (evidence still being produced) |
| **Primary sources** | Ancient inscriptions, artifacts, texts | NIST standards, government frameworks, reference architectures |
| **Claims nature** | Historical/descriptive | Architectural/prescriptive |

The methodology adapts to these differences while preserving the core OSKG principles: structured extraction, typed edges, and reproducibility.

---

*Built on the OSKG methodology, independently converged with ORKG. For the full methodological lineage, see [[../OSKG-YahWeh/METHODOLOGY]].*
