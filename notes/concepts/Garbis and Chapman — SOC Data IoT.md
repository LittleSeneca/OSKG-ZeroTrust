---
tags:
  - source/books
  - garbis-chapman
  - zt-soc
  - zt-data
  - zt-iot
  - oskg-zerotrust
source: "Garbis & Chapman, *Zero Trust Security: An Enterprise Guide* (Apress, 2021)"
chapters:
  - "Ch11: Security Operations (pp. 143–155)"
  - "Ch13: Data Protection (pp. 163–173)"
  - "Ch16: IoT Devices and 'Things' (pp. 193–207)"
created: 2026-07-24
---

# SOC, Data Protection, and IoT in Zero Trust — Garbis & Chapman

## 1. Security Operations Center (Ch11)

### SIEM and SOAR Foundations

**SIEM (Security Information and Event Management)** tools collect, aggregate, normalize, and correlate log data from across the enterprise — servers, firewalls, IDS/IPS, endpoint management, authentication systems, and more. They provide analytics, filters, and visualizations that help analysts cut through the noise and reduce false positives. SIEMs also help map network infrastructure by synthesizing raw log data, identifying high-value assets that can inform ZT strategy and PEP placement.

**SOAR (Security Orchestration, Automation, and Response)** consumes events and alerts from the SIEM and provides automated or semi-automated response workflows. Its value extends beyond automation: SOAR codifies the "tribal knowledge" that otherwise lives only in senior analysts' heads into repeatable, reliable playbooks. SOAR integrates people, process, and technology — and its reach across the enterprise security infrastructure makes it a natural partner for a Zero Trust platform.

### Zero Trust Integration with the SOC

ZT adoption *increases* the value of SIEM/SOAR in two ways:

1. **Enriched Log Data.** Because ZT is identity-centric, it can log all network access by all users enriched with identity, device, and contextual information — regardless of location, NAT boundaries, protocol, or application-specific identity systems. This makes SIEM correlation and detection far more meaningful.

2. **Orchestration and Automation (Triggers and Events).** ZT systems and SOARs exchange data through bidirectional APIs. The book identifies four primary trigger types:

| Trigger | Description |
|---|---|
| **Authentication** | PDP queries SIEM/SOAR for additional user/environmental context at login |
| **Resource Access** | PEP occasionally queries SIEM/SOAR for attributes that may have changed since auth (e.g., device risk) |
| **Periodic (Session Expiration)** | Session refresh; natural time for PDP to pull updated context |
| **External** | SOAR pushes data into the ZT PDP via inbound API (e.g., "risk level for user sjones2 is now High") |

### Integration Patterns

- **Direct (push) integration:** SIEM/SOAR sends specific attributes to the ZT PDP. Simple but creates bidirectional dependency — policy changes in ZT may require coordinated SIEM changes.
- **Indirect (pull) integration (preferred):** SOAR sends a lightweight signal ("refresh info for user X"), and the ZT PDP *pulls* whatever data it needs from the SOAR. This decouples the policy model from the SIEM's knowledge of which attributes the PDP requires.

### Example Policies
- If `OverallThreatLevel == High` → require MFA
- If `UserRiskLevel != Low` → deny privileged access
- If anomalous device behavior detected → quarantine device, block sensitive workloads

> **Key takeaway:** SOC integration should be part of your ZT journey early — having the SOC team on board accelerates adoption.

---

## 2. Data Protection (Ch13)

### Data Classification

Data falls on a **structured ↔ unstructured continuum**. Structured data (databases, SQL, defined schemas) has implicit classification via column metadata. Unstructured data (documents, files, SaaS) lacks inherent schema, making automatic classification difficult.

**FIPS Pub 199 classification levels:**
- **Low:** Limited adverse effect (marketing content, public website)
- **Moderate:** Serious adverse effect (customer info, price lists, strategy docs)
- **High:** Severe/catastrophic effect (source code, banking credentials, signing keys)

Classification is applied through three methods: **automated** (software at creation time), **user-based** (trained users apply tags — risk of inconsistency), and **discovery** (post-hoc scanning of stored data).

### Data Lifecycle

| Phase | Security Approach |
|---|---|
| **Creation** | Apply metadata/tags/labels for classification; automated, user-based, or discovery |
| **Usage: At-Rest** | Full-disk or database table encryption (protects physical access, not authorization) |
| **Usage: In-Motion** | Encrypted transport (HTTPS, TLS) — simplest to secure; apply to all data |
| **Usage: In-Use** | Hardest phase. In-memory encryption, tokenization, obfuscation; CASBs for SaaS; developer toolkits for custom apps |
| **Destruction** | Retention policies; growing set of SaaS lifecycle management providers |

### Data Security Technologies

- **DLP (Data Loss Prevention):** Device control (USB, print, copy-paste), content-aware control, enforced encryption, data discovery. DLP solutions actively enforce controls.
- **DAG (Data Access Governance):** Defines *who* can access *what* data and *when*. Closely related to IAM identity governance. In ZT, DAG policies tie directly into PDP policy evaluation.
- **DRM (Digital Rights Management):** Owner-imposed controls on proprietary/IP data. Some DRM solutions consume ZT context (identity, device attributes).
- **Emerging:** Homomorphic cryptography (compute on encrypted data without decryption), data tokenization.

### Zero Trust Integration with Data

Data is a **resource** protected by PEPs, just like applications. Two integration models:

1. **Enclave model:** Data resources sit inside a resource enclave behind a PEP. A DAG solution feeds labels/tags into the PDP. Policies like "only Customer Care Team can access resources tagged 'Customer Records'" are enforced at the PEP. Applications outside the enclave must authenticate as ZT identities.

2. **Local device model (two variants):**
   - **DAG + User Agent PEP:** DAG informs PDP → PDP instructs local agent PEP to enforce access controls based on data labels/tags.
   - **DLP as mini-PEP:** ZT system provides identity/session context (e.g., geolocation) to local DLP, enabling data residency enforcement. The DLP effectively becomes a Zero Trust PEP.

> **Key takeaway:** Data protection is an advanced ZT use case — not ideal for early projects. Classification maturity and platform capabilities are prerequisites.

---

## 3. IoT Devices and "Things" (Ch16)

### The IoT Security Problem

IoT devices span printers, VOIP phones, IP cameras, badge readers, smartboards, medical devices, HVAC, environmental sensors, and OT/industrial systems. Their common traits:
- IP-addressable but **closed systems** — cannot install arbitrary third-party software
- **Common vulnerabilities:** unencrypted protocols, hardcoded/default passwords, open listening ports, unremovable backdoors, unpatchable firmware, physical accessibility
- **Frequent attack vectors:** footholds for malware, lateral movement, data exfiltration; favored red-team targets

Modern IoT platforms (Azure IoT, AWS Greengrass, Google Cloud IoT Core) have well-designed security models and *may be acceptably excluded from ZT scope*. Most devices sit outside these frameworks and should be included.

### ZT Goals for IoT

| Goal | Mechanism |
|---|---|
| **Least privilege** | Minimize upstream access from devices; constrain what a compromised device can reach |
| **Device isolation** | Prevent unauthorized subjects from connecting to device listening ports |
| **Traffic encryption** | Route native (often cleartext) device traffic through encrypted tunnels between PEPs |

### Idealized Model

Homogeneous devices (e.g., all IP cameras) on an isolated network segment, with the PEP as default gateway. All non-LAN traffic transits the PEP for policy enforcement. Encryption between PEPs overcomes cleartext protocols. Limitations remain: lateral movement *within* the implicit trust zone; weak device authentication enables spoofing.

### Real-World Challenges

Most enterprise networks are **heterogeneous, flat, and opaque** — hundreds or thousands of mixed devices on the same subnet, random IP assignment via DHCP, no accurate CMDB. Key technical decisions:

**Device → Network assignment:**
- Physical cable/switch port (rigid)
- Private VLAN (logical separation)
- Wi-Fi access point (built-in isolation on some systems)
- NAC/802.1x (dynamic VLAN, but expensive and not universally supported)

**Device identification/authentication:**
- IP address (weak, spoofable)
- MAC address (weak, spoofable)
- DHCP fingerprint (moderate, spoofable)
- Certificate via 802.1x (strong, but PKI overhead; many devices can't support it)

**Traffic routing to PEP:**
- Default gateway configured directly on device
- Default gateway via DHCP (ideally device-type-aware)
- Static/dynamic routing on the network router

### Practical Guidance

1. **Start simple:** Homogeneous, well-understood device networks first — not the messy flat network.
2. **Prefer centrally managed devices** that allow network configuration at scale.
3. **Low-hanging fruit:** Secure remote third-party (vendor) admin access to internal devices; ZT can gate access behind a business process (e.g., service desk ticket).
4. **Pilot first:** IoT is nascent for ZT; validate technology compatibility in your environment.
5. **Not everything must be in scope:** Deliberately excluding certain components helps velocity.

> **Key takeaway:** ZT can bring real value to IoT, but IoT networks are a minefield of old, inflexible technology. It cannot provide the same robustness as with standard enterprise devices. Approach incrementally.

---

## Cross-Chapter Themes

1. **Integration is everything.** Whether it's SOC tools, data governance systems, or IoT network infrastructure, ZT's value is unlocked through API-driven integration with the PDP and PEPs.

2. **Identity context is the connective tissue.** SIEM logs enriched with identity; data access policies driven by identity attributes; even IoT device identification (however weak) is the basis for access control.

3. **Start with what's well-understood, not what's most critical.** SOC integration can (and should) come early. Data protection and IoT are more advanced — tackle them after building experience and success.

4. **The PDP is the integration hub.** In all three domains, the pattern is the same: external systems provide context → PDP evaluates policies → PEP enforces decisions. The policy model (Ch17) is therefore the keystone.
