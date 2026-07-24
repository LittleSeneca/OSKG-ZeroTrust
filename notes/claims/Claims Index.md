---
tags:
  - type/index
  - oskg-zerotrust
  - notes
  - claims
created: 2026-07-24
related:
  - "[[../Notes Index]]"
---

# Claims Index

Extracted claim nodes with typed edges. Each claim is a discrete, individually addressable unit of evidence extracted from a source text.

## Claim Format

Every claim follows the standard OSKG format:

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

## Status

**No claims extracted yet.** Claims extraction begins after Phase 1 (Reading Notes) is complete. The pipeline is: books → chapter notes → claims.

## Expected Claim Count

Target: 300-500 claims across all sources. The Zero Trust domain is narrower than the OSKG-YahWeh domain (which produced 723 claims from 17 books), so the claim count will be proportionally smaller. But the architectural/prescriptive nature of the claims means each one will carry higher evidential weight and more complex edge relationships.

---

*Claims will be populated during Phase 2 of the pipeline.*
