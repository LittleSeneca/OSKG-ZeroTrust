---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/primary-standard
  - source/ncsc
  - topic/zt-cloud
  - topic/zt-implementation
  - topic/zt-architecture
  - topic/zt-network
claim_id: "ncsc.5"
statement: "Cloud-native monitoring (Security Command Center, Chronicle, Cloud Logging) enables ZT-appropriate monitoring focused on users/devices/services rather than network boundaries."
confidence: "high"
confidence_rationale: "HIGH. The monitoring toolchain is comprehensive and cloud-native. Chronicle's ability to ingest on-premise telemetry via forwarders and third-party"
claim_type: "implementation"
source_note: "[[NCSC — ZT Principles on Google Cloud]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# ncsc.5: Cloud-native monitoring (Security Command Center, Chronicle, Cloud Logging) enables ZT-appropriate monitoring focused on users/devices/services rather than network boundaries.

**Source:** [[NCSC — ZT Principles on Google Cloud]] — NCSC, *Zero Trust Principles on Google Cloud*, 2023

## The Claim

"Cloud native monitoring solutions provide a richer set of protective monitoring capabilities than traditional network boundary logging — e.g. at a VPN chokepoint. Comprehensive protective monitoring in a zero trust environment will likely involve a range of teams — from those who are supporting users and devices through to service and product owners."

## Evidence

Google provides two primary monitoring locations:
- **Cloud Identity Security Center:** Device and user configurations and behavior; login attempt reports; suspicious sign-in activity alerts; device security health events
- **Security Command Center (SCC):** Asset discovery/inventory; threat prevention (web app vulnerabilities, misconfigurations); threat detection (container attacks, suspicious binaries, reverse shells); integrates with Chronicle for long-term security telemetry analysis

Additional monitoring capabilities include VPC Flow Logs, Packet Mirroring, Cloud IDS (built with Palo Alto Networks threat detection), and the Network Forensics & Telemetry blueprint (Packet Mirroring → Zeek → Pub/Sub → datalake → Chronicle).

## Confidence

**Rating:** HIGH
**Rationale:** HIGH. The monitoring toolchain is comprehensive and cloud-native. Chronicle's ability to ingest on-premise telemetry via forwarders and third-party integrations (Office 365, Azure AD) addresses hybrid environments.

## Stakes

ZT monitoring must shift from "what's happening at the network perimeter?" to "what are users, devices, and services doing, and does it match policy?" Google's monitoring architecture enables this shift. The integration of device health signals (rooted/jailbroken detection, account registration changes) into policy enforcement (device management rules that can automatically block/wiped devices) closes the monitoring-to-enforcement loop.

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[zta-monitoring-framework-cover-resource-categories-enterprise|Google's cloud-native monitoring services (SCC, Chronicle, Cloud Logging) fulfill the comprehensive monitoring framework]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The monitoring section reveals Google's architectural advantage: because the platform owns both the enforcement (IAP, IAM) and the monitoring (SCC, Chronicle, Cloud Logging), telemetry is natively integrated rather than bolted on. The device management rules — "block a device when the account registration state changes" — demonstrate automated response, not just detection. The BYOD/guest device handling via work profiles (Android) and Context-Aware access levels is pragmatic and recognizes that not all devices can be fully managed.
