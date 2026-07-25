---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/garbis-chapman-zt-enterprise
  - topic/zt-device
  - topic/zt-network
  - topic/zt-implementation
  - topic/zt-segmentation
claim_id: "gc-soc-data-iot.5"
statement: "ZT can bring real value to IoT, but IoT networks present fundamental limitations — closed systems, unencrypted protocols, weak authentication, and unpatchable firmware mean ZT cannot provide the same robustness as with standard enterprise devices."
confidence: "high"
confidence_rationale: "HIGH — The characterization of IoT limitations is well-supported by the broader cybersecurity literature. The practical guidance reflects real"
claim_type: "implementation"
source_note: "[[Garbis and Chapman — SOC Data IoT]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# gc-soc-data-iot.5: ZT can bring real value to IoT, but IoT networks present fundamental limitations — closed systems, unencrypted protocols, weak authentication, and unpatchable firmware mean ZT cannot provide the same robustness as with standard enterprise devices.

**Source:** [[Garbis and Chapman — SOC Data IoT]] — Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021

## The Claim

The authors' key takeaway states: "ZT can bring real value to IoT, but IoT networks are a minefield of old, inflexible technology. It cannot provide the same robustness as with standard enterprise devices. Approach incrementally."

## Evidence

IoT devices are characterized as IP-addressable but closed systems that cannot install arbitrary third-party software, with common vulnerabilities including unencrypted protocols, hardcoded/default passwords, open listening ports, unremovable backdoors, unpatchable firmware, and physical accessibility. The authors identify three ZT goals for IoT: least privilege (minimize upstream access from devices), device isolation (prevent unauthorized subjects from connecting to listening ports), and traffic encryption (route cleartext device traffic through encrypted tunnels between PEPs). The idealized model places homogeneous devices on an isolated segment with the PEP as default gateway, but real-world networks are typically "heterogeneous, flat, and opaque." Key technical decisions span device-to-network assignment (physical cable, private VLAN, Wi-Fi, NAC/802.1x), device identification (IP/MAC — weak, DHCP fingerprint — moderate, 802.1x certificates — strong but PKI overhead), and traffic routing to the PEP.

Practical guidance: (1) start with homogeneous, well-understood device networks; (2) prefer centrally managed devices; (3) low-hanging fruit is securing remote third-party vendor admin access via ZT gated behind business process; (4) pilot first — IoT is nascent for ZT; (5) not everything must be in scope. Modern IoT platforms (Azure IoT, AWS Greengrass, Google Cloud IoT Core) have well-designed security models and "may be acceptably excluded from ZT scope."

## Confidence

**Rating:** HIGH
**Rationale:** HIGH — The characterization of IoT limitations is well-supported by the broader cybersecurity literature. The practical guidance reflects real deployment constraints documented across multiple sources.

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
- [[firmware-level-patch-management|Unpatchable IoT firmware directly contradicts the requirement that patch management must cover firmware below the OS — t]]
- [[centralized-device-management-enforcement-backbone|IoT's closed systems, weak authentication, and unpatchable firmware fundamentally prevent the universal centralized mana]]

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

_Not addressed separately in the source note._
