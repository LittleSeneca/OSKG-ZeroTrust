---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/gilman-barth-zt-networks
  - topic/zt-encryption
  - topic/zt-network
  - topic/zt-implementation
  - topic/zt-device
claim_id: "gb-ch7-8.9"
statement: "TLS and IPsec serve different roles — mTLS for client/server, IPsec for server/server datacenter"
confidence: "high"
confidence_rationale: "HIGH. The pragmatic split has held up remarkably well. Service meshes (Istio, Linkerd) operationalize mTLS for server-to-server in cloud-native"
claim_type: "implementation"
source_note: "[[Gilman and Barth — Ch7-8 — Applications and Traffic]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gb-ch7-8.9: TLS and IPsec serve different roles — mTLS for client/server, IPsec for server/server datacenter

**Source:** [[Gilman and Barth — Ch7-8 — Applications and Traffic]] — Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017

## The Claim

TLS lives at the application layer (OSI 5–6), is protocol-dependent (TCP, with DTLS for UDP), and requires applications to support client certificate presentation. IPsec lives at the internet layer (OSI 3), is implemented in the kernel, and secures _all_ IP traffic "for free" from the application's perspective. The pragmatic recommendation: mutually authenticated TLS for client/server interactions (browsers presenting client certificates to access proxies), IPsec for server/server datacenter communication.

## Evidence

IPsec's advantages — kernel-level implementation, protocol-agnostic (handles TCP, UDP, ICMP, anything over IP), no application awareness needed. IPsec's disadvantages — complex configuration, network support issues (AWS blocks ESP/AH, public hotspots often block IPsec), device support variability, slow cipher suite progression. mTLS advantages — universal support, mature ecosystem, browser-native client certificates. mTLS disadvantages — protocol-dependent, requires application configuration, library fragmentation across languages.

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The pragmatic split has held up remarkably well. Service meshes (Istio, Linkerd) operationalize mTLS for server-to-server in cloud-native environments, while IPsec remains the backbone of site-to-site VPNs and some government/military deployments. The authors' recommendation for Windows environments (Microsoft Server Isolation via Active Directory + Group Policy + IPsec) is exactly the path many enterprises took.

## Stakes

If you pick the wrong protocol for your environment, you'll either fail to deploy (IPsec in heterogeneous client environments) or fail to secure (TLS without mutual authentication in server-to-server flows). The split recommendation is operationally critical.

## Disagreement

**Who disagrees:**

The service mesh movement argues that mTLS at the application layer is sufficient and preferable for server-to-server in cloud-native environments — IPsec's kernel-level integration is less valuable when orchestrators manage the entire network stack. Google's BeyondCorp/BeyondProd model uses application-layer identity (not network-layer) for all communication.

**Cross-reference — NIST 800-207 Ch4: BeyondCorp → BeyondProd.** NIST's deployment scenarios reference Google's BeyondProd, which extends the BeyondCorp model to service-to-service communication in cloud-native environments using mutual TLS between services, workload identity rather than network identity, and continuous trust evaluation at the service boundary. This is the modern evolution of the authors' server-to-server recommendation.

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[true-zt-segmentation-requires-enforcement-at-every-osi|Assigning mTLS to client/server and IPsec to server/server demonstrates layered encryption at different OSI levels, supp]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The authors' TLS/IPsec split was prescient but the landscape has shifted. Service meshes have made mTLS the dominant server-to-server protocol in cloud-native environments, with IPsec increasingly relegated to network infrastructure (site-to-site tunnels, government classified networks). The core insight — that you need different tools for different contexts — remains correct. The authors' recommendation for Windows shops (Microsoft Server Isolation) is still the pragmatic answer for Active Directory-centric enterprises.
