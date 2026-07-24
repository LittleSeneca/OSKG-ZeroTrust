# OSKG-ZeroTrust

An **O**pen **S**tructured **K**nowledge **G**raph applied to Zero Trust architecture — a data-driven investigation into the principles, implementation patterns, and evidence behind the most significant security paradigm shift in two decades.

---

## What This Is

A multi-layered research pipeline that transforms foundational Zero Trust texts — books, NIST standards, government publications, and practitioner guides — into a queryable, edge-connected knowledge graph of evaluated claims. Each claim is a first-class node tagged by topic, author, evidence type, and confidence. Edges are typed: **supports**, **contradicts**, **depends on**, **extends**.

The project applies the same structured evidence synthesis methodology as [OSKG-YahWeh](https://github.com/LittleSeneca/OSKG-YahWeh), independently converged with the Open Research Knowledge Graph (ORKG) at Leibniz University Hannover.

## Why Zero Trust?

Zero Trust is the most significant architectural shift in enterprise security since the perimeter model. But the space is awash in vendor marketing, conflicting definitions, and implementation confusion. The foundational texts exist — they're just scattered across publishers, standards bodies, and government agencies. No single source synthesizes them into a coherent, evidence-backed picture.

This project asks: **what does the weight of evidence actually show about how to implement Zero Trust?**

## The Pipeline

```
N books + standards → chapter notes → claims → typed-edge graph → synthesis
```

| Phase | Artifact | Description |
|-------|----------|-------------|
| **0. Acquisition** | `sources/books/_fulltext/` (gitignored) | Foundational texts acquired and extracted |
| **1. Reading Notes** | `notes/concepts/` | Chapter-by-chapter analysis of every text |
| **2. Claims Extraction** | `notes/claims/` | Each claim extracted as its own file with typed edges |
| **3. Knowledge Graph** | Obsidian graph view | Claims become nodes connected by typed relationships |
| **4. Synthesis** | `notes/synthesis/` | Hinge inventory, cascade trees, convergence points, capstone |

## Repository Structure

```
OSKG-ZeroTrust/
├── Home.md                 # Obsidian home note
├── README.md               # This file
├── METHODOLOGY.md           # Pipeline methodology
├── BOOK-GUIDE.md            # Canonical reading list
├── canvases/                # Obsidian Canvas mind maps
├── notes/
│   ├── claims/              # Extracted claim files
│   ├── concepts/            # Core Zero Trust concepts
│   ├── architecture/        # Architectural patterns
│   ├── evidence-briefs/     # Evidence synthesis
│   ├── questions/           # Open research questions
│   ├── history/             # Evolution of Zero Trust
│   └── synthesis/           # Capstone synthesis documents
├── scripts/                 # Pipeline automation scripts
├── sources/
│   ├── books/               # Book reference files
│   ├── papers/              # Academic papers
│   └── standards/           # NIST, CISA, DoD standards
└── .hermes/                 # Hermes agent skills and scripts
```

## Book Guide

See [BOOK-GUIDE.md](BOOK-GUIDE.md) for the full canonical reading list: 12 books, 4 categories, and the rationale for each.

---

*Built with the OSKG methodology. All claims traceable to their sources. All edges documented.*
