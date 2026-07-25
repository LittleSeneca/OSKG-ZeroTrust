---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-network
  - topic/zt-monitoring
claim_id: "gc-net-access.5"
statement: 'IDPS capabilities remain essential but the *how* changes — network-based IDPS is challenged by encrypted ZT tunnels, host-based IDPS gains relative advantage, and IDPS will increasingly be "baked in" to the ZT platform.'
confidence: "high"
confidence_rationale: "HIGH — The encryption problem is a well-defined technical constraint (mTLS between PEPs blinds intermediate inspection). The three solution paths are"
claim_type: "implementation"
source_note: "[[Garbis and Chapman — Network and Access Technologies]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-net-access.5: IDPS capabilities remain essential but the *how* changes — network-based IDPS is challenged by encrypted ZT tunnels, host-based IDPS gains relative advantage, and IDPS will increasingly be "baked in" to the ZT platform.

**Source:** [[Garbis and Chapman — Network and Access Technologies]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

The authors' central technical argument: Zero Trust typically uses mTLS with short-lived certificates between PEPs. A standard network IDPS between PEPs cannot decrypt this traffic — even if it has application-level certificates, it lacks the ZT tunnel certificates. TLS 1.3 makes this worse by encrypting additional handshake portions. Their verdict: IDPS capabilities are "more likely going to be 'baked in' to an enterprise's Zero Trust platform, as opposed to being a standalone tool."

## Evidence

Three solution paths: (1) make the NIDPS "Zero Trust-aware" — part of the ZT system with access to decryption keys; (2) deploy NIDPS within the implicit trust zone behind the PEP; (3) shift toward host-based IDPS operating below the encryption layer. Deployment across ZT models (Figure 8-1): resource-based requires ZT-aware NIDPS between PEPs; enclave-based allows standard NIDPS within the implicit trust zone; microsegmentation makes HIDPS the primary option. The vision: IDPS → PDP integration where IDPS provides threat detection events, PDP adjusts risk scores and triggers broader actions (step-up auth, device quarantine), and ZT context informs IDPS scrutiny level to reduce false positives.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The encryption problem is a well-defined technical constraint (mTLS between PEPs blinds intermediate inspection). The three solution paths are architecturally sound and map to specific ZT deployment models.

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
