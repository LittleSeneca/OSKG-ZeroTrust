---
tags:
  - type/index
  - oskg-zerotrust
  - notes
  - claims
  - phase2
created: 2026-07-24
updated: 2026-07-24
related:
  - "[[../Notes Index]]"
---

# Claims Index

Extracted claim nodes with typed edges. Each claim is a discrete, individually addressable unit of evidence extracted from a source text.

## Status

**Phase 2 in progress.** Batch 1 complete: 14 claims from 3 chapter notes. ~391 claims remaining across 47 notes.

## Claim Format

Every claim follows the OSKG v2 format:

```yaml
---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/<type>
  - source/<source-slug>
  - topic/<primary-topic>
claim_id: "<source-abbrev>-<note>.<claim-number>"
statement: "<one sentence>"
confidence: "<high|medium|low>"
claim_type: "<definitional|architectural|implementation|threat|migration|governance>"
source_note: "[[<chapter note>]]"
---
```

Sections: The Claim, Evidence, Confidence, Stakes, Disagreement, Edges, Assessment, Zero Trust Taxonomy.

## Extracted Claims by Batch

### Batch 1 — 2026-07-24 (14 claims)

| Claim ID | Slug | Type |
|----------|------|------|
| nist207-ch2.1 | [[zt-positive-tenets]] | definitional |
| nist207-ch2.2 | [[zt-uncertainty-minimization]] | definitional |
| nist207-ch2.3 | [[zt-tenets-aspirational]] | governance |
| nist207-ch2.4 | [[zt-pdp-pep-model]] | architectural |
| nist207-ch2.5 | [[zt-network-assumptions]] | architectural |
| nsa-embrace.1 | [[zt-assume-breach]] | threat |
| nsa-embrace.2 | [[zt-three-guiding-principles]] | architectural |
| nsa-embrace.3 | [[zt-threat-scenarios-illustrative]] | implementation |
| nsa-embrace.4 | [[zt-maturity-incremental]] | migration |
| nsa-embrace.5 | [[zt-organizational-commitment]] | governance |
| gilmanbarth-ch1.1 | [[zt-five-fundamental-assertions]] | definitional |
| gilmanbarth-ch1.2 | [[zt-control-data-plane-split]] | architectural |
| gilmanbarth-ch1.3 | [[zt-perimeter-historical-accident]] | definitional |
| gilmanbarth-ch1.4 | [[zt-phone-home-fatal-flaw]] | threat |

## Edge Network (Batch 1)

```
zt-positive-tenets ──supports──→ zt-five-fundamental-assertions
zt-positive-tenets ←──extends── zt-assume-breach
zt-positive-tenets ←──extends── zt-five-fundamental-assertions
zt-positive-tenets ←──extends── zt-three-guiding-principles

zt-uncertainty-minimization ──supports──→ zt-control-data-plane-split
zt-uncertainty-minimization ──extends──→ zt-assume-breach

zt-tenets-aspirational ──supports──→ zt-maturity-incremental
zt-tenets-aspirational ←──operationalizes── zt-maturity-incremental

zt-pdp-pep-model ──supports──→ zt-control-data-plane-split
zt-pdp-pep-model ──operationalizes──→ zt-control-data-plane-split
zt-pdp-pep-model ←──extends── zt-control-data-plane-split

zt-network-assumptions ──supports──→ zt-phone-home-fatal-flaw
zt-network-assumptions ──supports──→ zt-perimeter-historical-accident
zt-network-assumptions ──extends──→ zt-five-fundamental-assertions

zt-assume-breach ──supports──→ zt-network-assumptions

zt-three-guiding-principles ──supports──→ zt-positive-tenets

zt-threat-scenarios-illustrative ──supports──→ zt-phone-home-fatal-flaw
zt-threat-scenarios-illustrative ──operationalizes──→ zt-assume-breach

zt-five-fundamental-assertions ──supports──→ zt-control-data-plane-split

zt-perimeter-historical-accident ──supports──→ zt-phone-home-fatal-flaw

zt-phone-home-fatal-flaw ──supports──→ zt-perimeter-historical-accident
```

## Expected Claim Count

Target: ~405 claims across 50 chapter notes, 33 sources. Batch 1 covers 14 claims (3.5% complete).
