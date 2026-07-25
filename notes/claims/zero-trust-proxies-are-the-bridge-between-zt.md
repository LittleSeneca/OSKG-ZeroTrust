---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-migration
  - topic/zt-architecture
claim_id: "gb-ch9.4"
statement: "Zero Trust proxies are the bridge between ZT and legacy systems"
confidence: "high"
confidence_rationale: "HIGH. This is exactly the BeyondCorp Access Proxy model and the architecture behind every ZTNA product (Zscaler, Cloudflare Access, AppGate). The"
claim_type: "migration"
source_note: "[[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch9.4: Zero Trust proxies are the bridge between ZT and legacy systems

**Source:** [[Gilman and Barth — Ch9 — Realizing a Zero Trust Network]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

Zero trust proxies "can be used to build a zero trust network" but must be deployed **on the same device as the workload** — not on dedicated appliances. External proxies that handle authentication and then forward to backend services over untrusted links violate the ZT model.

## Evidence

**Two proxy modes:**

| Mode | Use Case | How It Works |
|------|----------|-------------|
| **Reverse proxy** | ZT-enabled clients accessing services | Proxy receives connection, validates authorization, passes request to application |
| **Forward proxy** | Non-ZT-aware legacy components accessing ZT services | Legacy component communicates through co-located proxy that handles authentication |

**The isolation requirement:**

Non-ZT-aware components behind a forward proxy must be **completely isolated** — all network communication to/from that component must go through its authentication proxy. Direct mechanical connection is preferred.

**Cross-reference — NIST 800-207 Ch3:**

The Access Proxy maps to NIST's Policy Enforcement Point (PEP) — the component that "enables, monitors, and eventually terminates connections between a subject and an enterprise resource." Gilman & Barth's insistence on co-located proxies is stricter than NIST's model, which allows the PEP to be a separate component (e.g., the resource gateway deployment variation).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. This is exactly the BeyondCorp Access Proxy model and the architecture behind every ZTNA product (Zscaler, Cloudflare Access, AppGate). The co-location requirement is what distinguishes ZT proxies from traditional reverse proxies.

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

_Not addressed separately in the source note._
