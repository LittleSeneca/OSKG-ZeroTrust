#!/usr/bin/env python3
"""
Phase 2 Batch 4 extraction: parse ## Claim N and ### Claim N headings out of
19 Tier 2 chapter notes (Gilman & Barth, Garbis & Chapman, Finney, Green-Ortiz)
and generate one claim file per claim under notes/claims/.

Adapted from extract_batch3.py. Handles 4 distinct claim marker patterns.
"""

import os
import re

BASE = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust")
CONCEPTS_DIR = os.path.join(BASE, "notes/concepts")
CLAIMS_DIR = os.path.join(BASE, "notes/claims")

TODAY = "2026-07-24"

CHAPTERS = [
    # === Gilman & Barth (6 notes, 53 claims) ===
    {"key": "gb-ch2", "file": "Gilman and Barth — Ch2 — Managing Trust.md",
     "note": "Gilman and Barth — Ch2 — Managing Trust", "n": 6,
     "source_tag": "source/gilman-barth-zt-networks",
     "source_line": "Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017"},
    {"key": "gb-ch3", "file": "Gilman and Barth — Ch3 — Network Agents.md",
     "note": "Gilman and Barth — Ch3 — Network Agents", "n": 5,
     "source_tag": "source/gilman-barth-zt-networks",
     "source_line": "Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017"},
    {"key": "gb-ch4-6", "file": "Gilman and Barth — Ch4-6 — Authorization Devices Users.md",
     "note": "Gilman and Barth — Ch4-6 — Authorization Devices Users", "n": 14,
     "source_tag": "source/gilman-barth-zt-networks",
     "source_line": "Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017"},
    {"key": "gb-ch7-8", "file": "Gilman and Barth — Ch7-8 — Applications and Traffic.md",
     "note": "Gilman and Barth — Ch7-8 — Applications and Traffic", "n": 13,
     "source_tag": "source/gilman-barth-zt-networks",
     "source_line": "Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017"},
    {"key": "gb-ch9", "file": "Gilman and Barth — Ch9 — Realizing a Zero Trust Network.md",
     "note": "Gilman and Barth — Ch9 — Realizing a Zero Trust Network", "n": 7,
     "source_tag": "source/gilman-barth-zt-networks",
     "source_line": "Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017"},
    {"key": "gb-ch10", "file": "Gilman and Barth — Ch10 — The Adversarial View.md",
     "note": "Gilman and Barth — Ch10 — The Adversarial View", "n": 8,
     "source_tag": "source/gilman-barth-zt-networks",
     "source_line": "Evan Gilman & Doug Barth, *Zero Trust Networks*, 2017"},
    # === Garbis & Chapman (6 notes, 51 claims) ===
    {"key": "gc-ch1-3", "file": "Garbis and Chapman — Ch1-3 — Introduction and Architecture.md",
     "note": "Garbis and Chapman — Ch1-3 — Introduction and Architecture", "n": 14,
     "source_tag": "source/garbis-chapman-zt-enterprise",
     "source_line": "Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021"},
    {"key": "gc-net-access", "file": "Garbis and Chapman — Network and Access Technologies.md",
     "note": "Garbis and Chapman — Network and Access Technologies", "n": 8,
     "source_tag": "source/garbis-chapman-zt-enterprise",
     "source_line": "Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021"},
    {"key": "gc-iam-policy", "file": "Garbis and Chapman — Practice IAM Policy.md",
     "note": "Garbis and Chapman — Practice IAM Policy", "n": 13,
     "source_tag": "source/garbis-chapman-zt-enterprise",
     "source_line": "Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021"},
    {"key": "gc-cloud", "file": "Garbis and Chapman — Cloud IaaS SaaS.md",
     "note": "Garbis and Chapman — Cloud IaaS SaaS", "n": 6,
     "source_tag": "source/garbis-chapman-zt-enterprise",
     "source_line": "Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021"},
    {"key": "gc-soc-data-iot", "file": "Garbis and Chapman — SOC Data IoT.md",
     "note": "Garbis and Chapman — SOC Data IoT", "n": 5,
     "source_tag": "source/garbis-chapman-zt-enterprise",
     "source_line": "Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021"},
    {"key": "gc-scenarios", "file": "Garbis and Chapman — Scenarios and Conclusion.md",
     "note": "Garbis and Chapman — Scenarios and Conclusion", "n": 5,
     "source_tag": "source/garbis-chapman-zt-enterprise",
     "source_line": "Jason Garbis & Jerry Chapman, *Zero Trust Security: An Enterprise Guide*, 2021"},
    # === Finney (3 notes, 36 claims) ===
    {"key": "finney-ch1-3", "file": "Finney — Ch1-3 — The Zero Trust Story.md",
     "note": "Finney — Ch1-3 — The Zero Trust Story", "n": 12,
     "source_tag": "source/finney-project-zt",
     "source_line": "George Finney, *Project Zero Trust*, 2022"},
    {"key": "finney-ch4-7", "file": "Finney — Ch4-7 — Building the ZT Strategy.md",
     "note": "Finney — Ch4-7 — Building the ZT Strategy", "n": 11,
     "source_tag": "source/finney-project-zt",
     "source_line": "George Finney, *Project Zero Trust*, 2022"},
    {"key": "finney-ch8-11", "file": "Finney — Ch8-11 — Execution and Sustainability.md",
     "note": "Finney — Ch8-11 — Execution and Sustainability", "n": 13,
     "source_tag": "source/finney-project-zt",
     "source_line": "George Finney, *Project Zero Trust*, 2022"},
    # === Green-Ortiz et al. (4 notes, 30 claims) ===
    {"key": "go-intro", "file": "Green-Ortiz — Intro Ch1-2 — Foundations.md",
     "note": "Green-Ortiz — Intro Ch1-2 — Foundations", "n": 8,
     "source_tag": "source/green-ortiz-zt-architecture",
     "source_line": "Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023"},
    {"key": "go-ch3-5", "file": "Green-Ortiz — Ch3-5 — Trust and Policy.md",
     "note": "Green-Ortiz — Ch3-5 — Trust and Policy", "n": 6,
     "source_tag": "source/green-ortiz-zt-architecture",
     "source_line": "Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023"},
    {"key": "go-ch6-8", "file": "Green-Ortiz — Ch6-8 — Implementation.md",
     "note": "Green-Ortiz — Ch6-8 — Implementation", "n": 9,
     "source_tag": "source/green-ortiz-zt-architecture",
     "source_line": "Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023"},
    {"key": "go-ch9-11", "file": "Green-Ortiz — Ch9-11 — Advanced and Future.md",
     "note": "Green-Ortiz — Ch9-11 — Advanced and Future", "n": 7,
     "source_tag": "source/green-ortiz-zt-architecture",
     "source_line": "Cindy Green-Ortiz et al., *Zero Trust Architecture*, 2023"},
]

# Per-claim curated metadata: slug, topic tags (1-3), claim_type
# Auto-generated from claim titles; review before committing.
META = {
    # === Gilman & Barth Ch2 — Managing Trust (6 claims) ===
    ("gb-ch2", 1): {"slug": "zts-threat-model-is-the-internet-threat-model",
                     "topics": ["zt-threats", "zt-definition"], "type": "definitional"},
    ("gb-ch2", 2): {"slug": "private-pki-is-the-non-negotiable-bedrock-of-zt",
                     "topics": ["zt-identity", "zt-encryption"], "type": "implementation"},
    ("gb-ch2", 3): {"slug": "variable-trust-scores-replace-binary-policy-with-continuous",
                     "topics": ["zt-trust", "zt-architecture"], "type": "architectural"},
    ("gb-ch2", 4): {"slug": "least-privilege-in-zt-is-dynamic-multi-attribute-and",
                     "topics": ["zt-access-mgmt", "zt-device"], "type": "implementation"},
    ("gb-ch2", 5): {"slug": "the-control-plane-is-the-trust-grantor-temporary",
                     "topics": ["zt-architecture", "zt-authentication"], "type": "architectural"},
    ("gb-ch2", 6): {"slug": "trust-delegation-via-trust-chains-is-what-makes",
                     "topics": ["zt-trust", "zt-architecture"], "type": "architectural"},

    # === Gilman & Barth Ch3 — Network Agents (5 claims) ===
    ("gb-ch3", 1): {"slug": "the-network-agent-is-the-marriage-of-user",
                     "topics": ["zt-identity", "zt-architecture"], "type": "architectural"},
    ("gb-ch3", 2): {"slug": "agents-are-ephemeral-request-scoped-and-purely-for-authorization",
                     "topics": ["zt-authentication", "zt-access-mgmt"], "type": "implementation"},
    ("gb-ch3", 3): {"slug": "revoke-authorization-first-credentials-second",
                     "topics": ["zt-access-mgmt", "zt-implementation"], "type": "implementation"},
    ("gb-ch3", 4): {"slug": "agent-data-is-sensitive-and-should-be-contained",
                     "topics": ["zt-architecture", "zt-data"], "type": "architectural"},
    ("gb-ch3", 5): {"slug": "no-standard-exists-for-the-agent-format-standardization",
                     "topics": ["zt-architecture", "zt-governance"], "type": "governance"},

    # === Gilman & Barth Ch4-6 — Authorization Devices Users (14 claims) ===
    ("gb-ch4-6", 1): {"slug": "the-authorization-architecture-has-four-distinct-isolated-components",
                       "topics": ["zt-architecture", "zt-access-mgmt"], "type": "architectural"},
    ("gb-ch4-6", 2): {"slug": "the-trust-engine-is-the-novel-contribution-of",
                       "topics": ["zt-trust", "zt-architecture"], "type": "architectural"},
    ("gb-ch4-6", 3): {"slug": "policy-should-be-defined-in-terms-of-logical",
                       "topics": ["zt-policy", "zt-architecture"], "type": "architectural"},
    ("gb-ch4-6", 4): {"slug": "entities-should-be-scored-at-multiple-levels-network",
                       "topics": ["zt-trust", "zt-identity", "zt-device"], "type": "implementation"},
    ("gb-ch4-6", 5): {"slug": "device-identity-requires-binding-software-credentials-to-hardware",
                       "topics": ["zt-device", "zt-encryption"], "type": "implementation"},
    ("gb-ch4-6", 6): {"slug": "certificate-signing-is-a-trust-injection-point-that",
                       "topics": ["zt-access-mgmt", "zt-encryption"], "type": "implementation"},
    ("gb-ch4-6", 7): {"slug": "trust-degrades-over-time-device-age-is-the",
                       "topics": ["zt-device", "zt-trust"], "type": "implementation"},
    ("gb-ch4-6", 8): {"slug": "device-data-contextualizes-and-strengthens-user-authentication",
                       "topics": ["zt-identity", "zt-authentication", "zt-device"], "type": "implementation"},
    ("gb-ch4-6", 9): {"slug": "user-identity-and-device-identity-are-separate-trust",
                       "topics": ["zt-identity", "zt-device"], "type": "definitional"},
    ("gb-ch4-6", 10): {"slug": "trust-score-should-drive-authentication-requirements-not-static",
                        "topics": ["zt-trust", "zt-authentication"], "type": "implementation"},
    ("gb-ch4-6", 11): {"slug": "the-strongest-user-authentication-binds-identity-to-hardware",
                        "topics": ["zt-identity", "zt-authentication"], "type": "implementation"},
    ("gb-ch4-6", 12): {"slug": "out-of-band-and-multi-channel-authentication-raise-the-attackers-cost",
                        "topics": ["zt-authentication", "zt-threats"], "type": "implementation"},
    ("gb-ch4-6", 13): {"slug": "sso-should-not-remove-the-control-plane-from",
                        "topics": ["zt-architecture", "zt-authentication"], "type": "implementation"},
    ("gb-ch4-6", 14): {"slug": "group-authorization-is-the-highest-trust-mechanism-for-extremely",
                        "topics": ["zt-access-mgmt", "zt-security"], "type": "implementation"},

    # === Gilman & Barth Ch7-8 — Applications and Traffic (13 claims) ===
    ("gb-ch7-8", 1): {"slug": "the-application-pipeline-is-a-cryptographic-chain-break",
                       "topics": ["zt-app", "zt-supply-chain"], "type": "implementation"},
    ("gb-ch7-8", 2): {"slug": "gits-content-addressable-storage-provides-tamper-proof-history-but-not",
                       "topics": ["zt-app", "zt-encryption"], "type": "implementation"},
    ("gb-ch7-8", 3): {"slug": "the-build-system-is-the-most-dangerous-attack",
                       "topics": ["zt-app", "zt-threats"], "type": "threat"},
    ("gb-ch7-8", 4): {"slug": "immutable-artifacts-with-decoupled-version-numbers-prevent-masquerade",
                       "topics": ["zt-app", "zt-implementation"], "type": "implementation"},
    ("gb-ch7-8", 5): {"slug": "per-instance-time-bound-secrets-are-the-mechanism-for-authorizing",
                       "topics": ["zt-app", "zt-authentication"], "type": "implementation"},
    ("gb-ch7-8", 6): {"slug": "runtime-security-completes-the-trust-lifecycle-isolation-secure",
                       "topics": ["zt-app", "zt-monitoring"], "type": "implementation"},
    ("gb-ch7-8", 7): {"slug": "encryption-and-authentication-are-separate-concerns-zero-trust",
                       "topics": ["zt-authentication", "zt-encryption"], "type": "definitional"},
    ("gb-ch7-8", 8): {"slug": "the-first-packet-problem-is-solved-by-single",
                       "topics": ["zt-network", "zt-access-mgmt"], "type": "implementation"},
    ("gb-ch7-8", 9): {"slug": "tls-and-ipsec-serve-different-roles-mtls-for",
                       "topics": ["zt-encryption", "zt-network"], "type": "implementation"},
    ("gb-ch7-8", 10): {"slug": "cipher-suite-negotiation-is-an-anti-pattern-newer-protocols",
                        "topics": ["zt-encryption"], "type": "implementation"},
    ("gb-ch7-8", 11): {"slug": "tls-should-be-separated-from-applications-via-a",
                        "topics": ["zt-encryption", "zt-app"], "type": "architectural"},
    ("gb-ch7-8", 12): {"slug": "three-types-of-filtering-form-a-defense-in-depth-network",
                        "topics": ["zt-architecture", "zt-network"], "type": "architectural"},
    ("gb-ch7-8", 13): {"slug": "forwarding-and-routing-authorization-extends-policy-enforcement-into",
                        "topics": ["zt-governance", "zt-network"], "type": "governance"},

    # === Gilman & Barth Ch9 — Realizing a Zero Trust Network (7 claims) ===
    ("gb-ch9", 1): {"slug": "the-shouldmust-list-is-zt-implementations-operational-checklist",
                     "topics": ["zt-implementation", "zt-governance"], "type": "implementation"},
    ("gb-ch9", 2): {"slug": "flow-enumeration-is-the-hardest-requirement-and-the",
                     "topics": ["zt-implementation", "zt-network"], "type": "implementation"},
    ("gb-ch9", 3): {"slug": "configuration-management-is-a-legitimate-stepping-stone-to",
                     "topics": ["zt-migration", "zt-implementation"], "type": "migration"},
    ("gb-ch9", 4): {"slug": "zero-trust-proxies-are-the-bridge-between-zt",
                     "topics": ["zt-migration", "zt-architecture"], "type": "migration"},
    ("gb-ch9", 5): {"slug": "client-to-server-and-server-to-server-migrations-are-different-problems-with",
                     "topics": ["zt-migration"], "type": "migration"},
    ("gb-ch9", 6): {"slug": "log-then-enforce-is-the-migration-procedure-validated-by-two",
                     "topics": ["zt-migration", "zt-monitoring"], "type": "migration"},
    ("gb-ch9", 7): {"slug": "the-two-case-studies-demonstrate-zt-is-cross-domain",
                     "topics": ["zt-implementation"], "type": "implementation"},

    # === Gilman & Barth Ch10 — The Adversarial View (8 claims) ===
    ("gb-ch10", 1): {"slug": "identity-theft-is-the-first-and-most-dangerous",
                      "topics": ["zt-identity", "zt-threats"], "type": "threat"},
    ("gb-ch10", 2): {"slug": "ddos-is-still-a-problem-zt-doesnt-mitigate",
                      "topics": ["zt-threats", "zt-network"], "type": "threat"},
    ("gb-ch10", 3): {"slug": "zt-guarantees-confidentiality-but-not-privacy-endpoint-enumeration",
                      "topics": ["zt-encryption", "zt-network"], "type": "definitional"},
    ("gb-ch10", 4): {"slug": "zt-cannot-defend-against-a-malicious-computing-platform",
                      "topics": ["zt-threats", "zt-device"], "type": "threat"},
    ("gb-ch10", 5): {"slug": "social-engineering-and-physical-coercion-are-the-threats",
                      "topics": ["zt-threats"], "type": "threat"},
    ("gb-ch10", 6): {"slug": "invalidation-is-a-hard-problem-in-computer-science",
                      "topics": ["zt-access-mgmt", "zt-implementation"], "type": "implementation"},
    ("gb-ch10", 7): {"slug": "control-plane-compromise-is-the-worst-case-scenario-and",
                      "topics": ["zt-architecture", "zt-threats"], "type": "threat"},
    ("gb-ch10", 8): {"slug": "the-adversarial-view-reveals-that-zt-is-a",
                      "topics": ["zt-definition", "zt-risk"], "type": "definitional"},

    # === Garbis & Chapman Ch1-3 — Introduction and Architecture (14 claims) ===
    ("gc-ch1-3", 1): {"slug": "traditional-enterprise-security-is-structurally-broken-not-merely",
                       "topics": ["zt-definition", "zt-threats"], "type": "definitional"},
    ("gc-ch1-3", 2): {"slug": "zero-trust-is-a-misnomer-the-real-concept",
                       "topics": ["zt-definition", "zt-trust"], "type": "definitional"},
    ("gc-ch1-3", 3): {"slug": "zero-trust-is-a-philosophy-principles-and-a",
                       "topics": ["zt-definition", "zt-governance"], "type": "definitional"},
    ("gc-ch1-3", 4): {"slug": "zero-trust-amplifies-existing-security-concepts-least-privilege",
                       "topics": ["zt-definition", "zt-access-mgmt"], "type": "definitional"},
    ("gc-ch1-3", 5): {"slug": "the-three-core-principles-secure-all-resources-regardless",
                       "topics": ["zt-definition", "zt-access-mgmt", "zt-network"], "type": "definitional"},
    ("gc-ch1-3", 6): {"slug": "three-expanded-principles-api-integration-automation-and-business",
                       "topics": ["zt-governance", "zt-implementation"], "type": "governance"},
    ("gc-ch1-3", 7): {"slug": "the-working-definition-centers-zt-as-an-integrated",
                       "topics": ["zt-definition", "zt-architecture"], "type": "definitional"},
    ("gc-ch1-3", 8): {"slug": "the-14-platform-requirements-operationalize-the-principles-into",
                       "topics": ["zt-governance", "zt-implementation"], "type": "governance"},
    ("gc-ch1-3", 9): {"slug": "the-nist-pdppep-model-is-the-correct-foundation",
                       "topics": ["zt-architecture"], "type": "architectural"},
    ("gc-ch1-3", 10): {"slug": "there-are-three-distinct-types-of-peps-and",
                        "topics": ["zt-architecture"], "type": "architectural"},
    ("gc-ch1-3", 11): {"slug": "a-component-is-only-a-pep-if-it",
                        "topics": ["zt-architecture", "zt-identity"], "type": "architectural"},
    ("gc-ch1-3", 12): {"slug": "four-deployment-models-cover-the-zt-solution-space",
                        "topics": ["zt-architecture", "zt-implementation"], "type": "architectural"},
    ("gc-ch1-3", 13): {"slug": "the-implicit-trust-zone-is-the-key-architectural",
                        "topics": ["zt-trust", "zt-architecture"], "type": "architectural"},
    ("gc-ch1-3", 14): {"slug": "the-policy-structure-of-subject-criteria-action-target",
                        "topics": ["zt-policy", "zt-identity"], "type": "architectural"},

    # === Garbis & Chapman — Network and Access Technologies (8 claims) ===
    ("gc-net-access", 1): {"slug": "firewalls-persist-under-zero-trust-but-their-role",
                            "topics": ["zt-network", "zt-architecture"], "type": "architectural"},
    ("gc-net-access", 2): {"slug": "dns-is-both-a-critical-infrastructure-component-and",
                            "topics": ["zt-network", "zt-monitoring"], "type": "implementation"},
    ("gc-net-access", 3): {"slug": "wan-reliance-will-diminish-under-zero-trust-zt",
                            "topics": ["zt-network", "zt-implementation"], "type": "implementation"},
    ("gc-net-access", 4): {"slug": "8021x-based-nac-is-fundamentally-incompatible-with-zero-trusts",
                            "topics": ["zt-network", "zt-device"], "type": "definitional"},
    ("gc-net-access", 5): {"slug": "idps-capabilities-remain-essential-but-the-how-changes",
                            "topics": ["zt-network", "zt-monitoring"], "type": "implementation"},
    ("gc-net-access", 6): {"slug": "vpns-must-be-replaced-not-augmented-not-integrated",
                            "topics": ["zt-network", "zt-implementation"], "type": "implementation"},
    ("gc-net-access", 7): {"slug": "ngfws-are-neither-sufficient-as-a-zt-platform",
                            "topics": ["zt-network", "zt-architecture"], "type": "architectural"},
    ("gc-net-access", 8): {"slug": "pam-provides-valuable-functions-secrets-management-session-recording",
                            "topics": ["zt-identity", "zt-access-mgmt"], "type": "implementation"},

    # === Garbis & Chapman — Practice IAM Policy (13 claims) ===
    ("gc-iam-policy", 1): {"slug": "beyondcorp-proved-that-device-trust-can-replace-network-trust-at",
                            "topics": ["zt-device", "zt-architecture"], "type": "implementation"},
    ("gc-iam-policy", 2): {"slug": "server-to-server-zt-is-a-fundamentally-different-problem-than",
                            "topics": ["zt-identity", "zt-architecture"], "type": "architectural"},
    ("gc-iam-policy", 3): {"slug": "the-software-defined-perimeter-architecture-delivers-zt-principles-through",
                            "topics": ["zt-access-mgmt", "zt-network"], "type": "architectural"},
    ("gc-iam-policy", 4): {"slug": "phased-zt-adoption-vpn-replacement-role-based-access-branch",
                            "topics": ["zt-migration"], "type": "migration"},
    ("gc-iam-policy", 5): {"slug": "identity-is-the-keystone-of-zero-trust-but",
                            "topics": ["zt-identity"], "type": "implementation"},
    ("gc-iam-policy", 6): {"slug": "the-three-layer-authorization-model-reveals-why-zt-is",
                            "topics": ["zt-identity", "zt-access-mgmt", "zt-network"], "type": "architectural"},
    ("gc-iam-policy", 7): {"slug": "zero-trust-enhances-legacy-applications-without-modification-its",
                            "topics": ["zt-implementation", "zt-migration", "zt-app"], "type": "implementation"},
    ("gc-iam-policy", 8): {"slug": "zt-can-serve-as-a-catalyst-to-improve",
                            "topics": ["zt-implementation", "zt-identity"], "type": "implementation"},
    ("gc-iam-policy", 9): {"slug": "the-four-component-policy-model-subject-action-target-condition",
                            "topics": ["zt-policy", "zt-architecture"], "type": "architectural"},
    ("gc-iam-policy", 10): {"slug": "dynamic-tag-based-targets-are-the-policy-models-most",
                             "topics": ["zt-policy", "zt-app"], "type": "architectural"},
    ("gc-iam-policy", 11): {"slug": "the-service-desk-ticket-condition-represents-a-paradigm",
                             "topics": ["zt-governance", "zt-access-mgmt"], "type": "governance"},
    ("gc-iam-policy", 12): {"slug": "the-policy-evaluation-flow-pdp-grants-pep-renders",
                             "topics": ["zt-architecture", "zt-policy"], "type": "architectural"},
    ("gc-iam-policy", 13): {"slug": "target-initiated-access-is-a-real-architectural-constraint-that",
                             "topics": ["zt-architecture", "zt-implementation"], "type": "architectural"},

    # === Garbis & Chapman — Cloud IaaS SaaS (6 claims) ===
    ("gc-cloud", 1): {"slug": "iaaspaas-security-hasnt-kept-pace-with-iaaspaas-adoption",
                       "topics": ["zt-cloud", "zt-threats"], "type": "definitional"},
    ("gc-cloud", 2): {"slug": "the-pep-works-best-at-the-cloud-boundary",
                       "topics": ["zt-architecture", "zt-cloud"], "type": "architectural"},
    ("gc-cloud", 3): {"slug": "service-meshes-are-self-contained-zero-trust-microsegmentation-systems",
                       "topics": ["zt-network", "zt-segmentation"], "type": "architectural"},
    ("gc-cloud", 4): {"slug": "zero-trust-does-fewer-things-for-saas-but",
                       "topics": ["zt-cloud"], "type": "implementation"},
    ("gc-cloud", 5): {"slug": "sasezte-converges-networking-and-security-but-ztna-ingress",
                       "topics": ["zt-network", "zt-cloud"], "type": "architectural"},
    ("gc-cloud", 6): {"slug": "the-future-of-zt-saas-is-identity-providers",
                       "topics": ["zt-identity", "zt-authentication", "zt-cloud"], "type": "implementation"},

    # === Garbis & Chapman — SOC Data IoT (5 claims) ===
    ("gc-soc-data-iot", 1): {"slug": "siem-and-soar-integration-with-zt-is-a",
                              "topics": ["zt-monitoring", "zt-governance"], "type": "governance"},
    ("gc-soc-data-iot", 2): {"slug": "soc-integration-should-be-pursued-early-in-the",
                              "topics": ["zt-monitoring", "zt-migration"], "type": "implementation"},
    ("gc-soc-data-iot", 3): {"slug": "data-protection-is-an-advanced-zt-use-case",
                              "topics": ["zt-data", "zt-maturity"], "type": "maturity"},
    ("gc-soc-data-iot", 4): {"slug": "data-classification-spans-a-structured-to-unstructured-continuum-structured-data",
                              "topics": ["zt-data", "zt-implementation"], "type": "implementation"},
    ("gc-soc-data-iot", 5): {"slug": "zt-can-bring-real-value-to-iot-but",
                              "topics": ["zt-device", "zt-network"], "type": "implementation"},

    # === Garbis & Chapman — Scenarios and Conclusion (5 claims) ===
    ("gc-scenarios", 1): {"slug": "seven-zt-scenarios-provide-a-practical-non-exhaustive-framework",
                           "topics": ["zt-implementation"], "type": "implementation"},
    ("gc-scenarios", 2): {"slug": "zt-success-requires-deliberately-blending-top-down-strategic-vision",
                           "topics": ["zt-implementation", "zt-governance"], "type": "governance"},
    ("gc-scenarios", 3): {"slug": "five-business-value-drivers-not-security-alone-justify",
                           "topics": ["zt-governance"], "type": "governance"},
    ("gc-scenarios", 4): {"slug": "common-roadblocks-iam-immaturity-political-resistance-regulatory-constraints",
                           "topics": ["zt-migration", "zt-governance"], "type": "migration"},
    ("gc-scenarios", 5): {"slug": "zt-is-a-journey-not-a-destination-success",
                           "topics": ["zt-definition", "zt-migration"], "type": "definitional"},

    # === Finney Ch1-3 — The Zero Trust Story (12 claims) ===
    ("finney-ch1-3", 1): {"slug": "trust-is-the-root-vulnerability-that-zero-trust",
                           "topics": ["zt-trust", "zt-threats"], "type": "definitional"},
    ("finney-ch1-3", 2): {"slug": "prevention-is-possible-and-more-cost-effective-than-recovery",
                           "topics": ["zt-implementation"], "type": "implementation"},
    ("finney-ch1-3", 3): {"slug": "zero-trust-is-a-strategy-not-a-product",
                           "topics": ["zt-definition"], "type": "definitional"},
    ("finney-ch1-3", 4): {"slug": "executive-sponsorship-and-crisis-create-the-window-for",
                           "topics": ["zt-governance"], "type": "governance"},
    ("finney-ch1-3", 5): {"slug": "defense-in-depth-compliance-and-best-of-breed-are-not",
                           "topics": ["zt-governance", "zt-definition"], "type": "definitional"},
    ("finney-ch1-3", 6): {"slug": "the-four-design-principles-and-five-step-methodology-make",
                           "topics": ["zt-definition", "zt-architecture"], "type": "definitional"},
    ("finney-ch1-3", 7): {"slug": "the-zero-trust-implementation-curve-prevents-boiling-the",
                           "topics": ["zt-implementation", "zt-migration"], "type": "implementation"},
    ("finney-ch1-3", 8): {"slug": "the-kipling-method-replaces-network-centric-policy-with-business-context",
                           "topics": ["zt-policy", "zt-governance"], "type": "governance"},
    ("finney-ch1-3", 9): {"slug": "physical-security-is-the-perfect-analogy-for-zero",
                           "topics": ["zt-definition"], "type": "definitional"},
    ("finney-ch1-3", 10): {"slug": "the-protect-surface-shifts-controls-from-the-perimeter",
                            "topics": ["zt-definition", "zt-architecture"], "type": "definitional"},
    ("finney-ch1-3", 11): {"slug": "incident-management-without-problem-management-creates-a-firefighting",
                            "topics": ["zt-implementation", "zt-governance"], "type": "implementation"},
    ("finney-ch1-3", 12): {"slug": "third-party-integrators-and-multi-vendor-responsibility-gaps-create-systemic",
                            "topics": ["zt-supply-chain", "zt-threats"], "type": "threat"},

    # === Finney Ch4-7 — Building the ZT Strategy (11 claims) ===
    ("finney-ch4-7", 1): {"slug": "the-first-protect-surface-must-be-what-the",
                           "topics": ["zt-implementation"], "type": "implementation"},
    ("finney-ch4-7", 2): {"slug": "erp-systems-are-uniquely-opaque-to-traditional-security",
                           "topics": ["zt-app", "zt-monitoring"], "type": "implementation"},
    ("finney-ch4-7", 3): {"slug": "nist-sp-800-207-provides-the-architectural-tenets-but",
                           "topics": ["zt-definition", "zt-architecture"], "type": "definitional"},
    ("finney-ch4-7", 4): {"slug": "identity-is-simultaneously-the-most-important-protect-surface",
                           "topics": ["zt-identity"], "type": "implementation"},
    ("finney-ch4-7", 5): {"slug": "mfa-is-necessary-but-insufficient-attackers-have-at",
                           "topics": ["zt-authentication", "zt-threats"], "type": "implementation"},
    ("finney-ch4-7", 6): {"slug": "identity-governance-needs-a-cross-functional-stakeholder-group-and",
                           "topics": ["zt-governance", "zt-identity"], "type": "governance"},
    ("finney-ch4-7", 7): {"slug": "devops-culture-can-be-an-ally-or-adversary",
                           "topics": ["zt-app", "zt-governance"], "type": "governance"},
    ("finney-ch4-7", 8): {"slug": "devops-introduces-cloud-native-risks-kubernetes-containers-that-traditional",
                           "topics": ["zt-cloud", "zt-app"], "type": "implementation"},
    ("finney-ch4-7", 9): {"slug": "the-soc-is-itself-a-protect-surface-and",
                           "topics": ["zt-monitoring"], "type": "definitional"},
    ("finney-ch4-7", 10): {"slug": "the-socs-value-is-measured-by-false-positive",
                            "topics": ["zt-monitoring"], "type": "implementation"},
    ("finney-ch4-7", 11): {"slug": "incident-response-must-follow-zt-principles-and-the",
                            "topics": ["zt-definition", "zt-implementation"], "type": "definitional"},

    # === Finney Ch8-11 — Execution and Sustainability (13 claims) ===
    ("finney-ch8-11", 1): {"slug": "the-cloud-is-not-one-protect-surface-its",
                            "topics": ["zt-cloud"], "type": "implementation"},
    ("finney-ch8-11", 2): {"slug": "vendor-contracts-and-third-party-risk-management-are-your",
                            "topics": ["zt-supply-chain", "zt-cloud"], "type": "implementation"},
    ("finney-ch8-11", 3): {"slug": "casb-sasesdp-api-security-form-the-cloud-visibility",
                            "topics": ["zt-monitoring", "zt-cloud"], "type": "implementation"},
    ("finney-ch8-11", 4): {"slug": "container-security-standards-must-be-enforced-as-code",
                            "topics": ["zt-app", "zt-cloud"], "type": "implementation"},
    ("finney-ch8-11", 5): {"slug": "security-awareness-training-is-a-protect-surface-apply",
                            "topics": ["zt-governance", "zt-implementation"], "type": "governance"},
    ("finney-ch8-11", 6): {"slug": "people-are-the-weakest-link-is-a-self-fulfilling",
                            "topics": ["zt-governance"], "type": "definitional"},
    ("finney-ch8-11", 7): {"slug": "culture-change-requires-rituals-not-just-policies-the",
                            "topics": ["zt-governance", "zt-implementation"], "type": "governance"},
    ("finney-ch8-11", 8): {"slug": "tabletop-exercises-are-the-monitor-and-maintain-phase",
                            "topics": ["zt-implementation", "zt-monitoring"], "type": "implementation"},
    ("finney-ch8-11", 9): {"slug": "zt-doesnt-eliminate-trust-relationships-the-penetration-test",
                            "topics": ["zt-implementation", "zt-trust"], "type": "implementation"},
    ("finney-ch8-11", 10): {"slug": "red-herrings-and-the-fog-of-war-the",
                             "topics": ["zt-threats", "zt-implementation"], "type": "implementation"},
    ("finney-ch8-11", 11): {"slug": "zero-trust-never-ends-the-maturity-model-turns",
                             "topics": ["zt-maturity", "zt-migration"], "type": "maturity"},
    ("finney-ch8-11", 12): {"slug": "deception-technologies-invert-zt-selectively-add-trust-back",
                             "topics": ["zt-threats", "zt-monitoring"], "type": "threat"},
    ("finney-ch8-11", 13): {"slug": "the-cisos-measure-of-success-is-not-were",
                             "topics": ["zt-governance"], "type": "governance"},

    # === Green-Ortiz Intro Ch1-2 — Foundations (8 claims) ===
    ("go-intro", 1): {"slug": "zero-trust-originated-from-the-morris-worm-and",
                       "topics": ["zt-definition", "zt-threats"], "type": "definitional"},
    ("go-intro", 2): {"slug": "the-zero-trust-discovery-workshop-is-the-critical",
                       "topics": ["zt-implementation", "zt-governance"], "type": "implementation"},
    ("go-intro", 3): {"slug": "ciscos-five-pillar-model-policy-governance-identity-vulnerability-management",
                       "topics": ["zt-architecture", "zt-governance"], "type": "architectural"},
    ("go-intro", 4): {"slug": "policy-governance-is-the-badge-and-shield-it",
                       "topics": ["zt-governance", "zt-policy"], "type": "definitional"},
    ("go-intro", 5): {"slug": "identity-must-be-contextual-who-what-device-where",
                       "topics": ["zt-identity", "zt-device"], "type": "implementation"},
    ("go-intro", 6): {"slug": "vulnerability-management-must-extend-beyond-cves-to-include",
                       "topics": ["zt-device", "zt-monitoring"], "type": "implementation"},
    ("go-intro", 7): {"slug": "enforcement-must-be-layered-and-applied-as-close",
                       "topics": ["zt-implementation"], "type": "implementation"},
    ("go-intro", 8): {"slug": "analytics-closes-the-loop-the-zt-journey-is",
                       "topics": ["zt-migration", "zt-maturity"], "type": "migration"},

    # === Green-Ortiz Ch3-5 — Trust and Policy (6 claims) ===
    ("go-ch3-5", 1): {"slug": "trust-assessment-is-spatial-the-architecture-location-determines",
                       "topics": ["zt-architecture", "zt-trust"], "type": "architectural"},
    ("go-ch3-5", 2): {"slug": "enclave-design-is-trust-classification-what-criteria-justify",
                       "topics": ["zt-architecture", "zt-segmentation"], "type": "architectural"},
    ("go-ch3-5", 3): {"slug": "trust-assessment-is-multi-layered-identity-posture-and-behavior",
                       "topics": ["zt-identity", "zt-device"], "type": "implementation"},
    ("go-ch3-5", 4): {"slug": "policy-creation-is-data-driven-discovery-before-enforcement-log",
                       "topics": ["zt-policy", "zt-monitoring"], "type": "implementation"},
    ("go-ch3-5", 5): {"slug": "policy-survives-organizational-change-through-the-policy-governance",
                       "topics": ["zt-governance", "zt-policy"], "type": "governance"},
    ("go-ch3-5", 6): {"slug": "automation-bridges-the-gap-between-trust-assessment-and",
                       "topics": ["zt-implementation", "zt-maturity"], "type": "implementation"},

    # === Green-Ortiz Ch6-8 — Implementation (9 claims) ===
    ("go-ch6-8", 1): {"slug": "true-zt-segmentation-requires-enforcement-at-every-osi",
                       "topics": ["zt-network", "zt-segmentation"], "type": "implementation"},
    ("go-ch6-8", 2): {"slug": "east-west-segmentation-controlling-traffic-within-the-same-vlansubnet",
                       "topics": ["zt-network", "zt-segmentation"], "type": "implementation"},
    ("go-ch6-8", 3): {"slug": "the-five-pillar-methodology-for-segmentation-operationalizes-zt-by",
                       "topics": ["zt-governance", "zt-network"], "type": "implementation"},
    ("go-ch6-8", 4): {"slug": "true-contextual-identity-is-never-just-a-device",
                       "topics": ["zt-identity", "zt-device"], "type": "definitional"},
    ("go-ch6-8", 5): {"slug": "the-firewall-is-enough-belief-is-mathematically-disproven-a-network",
                       "topics": ["zt-network", "zt-architecture"], "type": "architectural"},
    ("go-ch6-8", 6): {"slug": "external-access-for-iotendpoints-requires-baseline-creation-through",
                       "topics": ["zt-access-mgmt", "zt-device"], "type": "implementation"},
    ("go-ch6-8", 7): {"slug": "new-endpoint-onboarding-day-2-operations-requires-a",
                       "topics": ["zt-implementation", "zt-device"], "type": "implementation"},
    ("go-ch6-8", 8): {"slug": "top-down-business-aligned-and-bottom-up-traffic-aligned-design-approaches-are",
                       "topics": ["zt-policy", "zt-governance"], "type": "governance"},
    ("go-ch6-8", 9): {"slug": "the-policy-decision-matrix-mapping-source-entities-to",
                       "topics": ["zt-policy", "zt-architecture"], "type": "architectural"},

    # === Green-Ortiz Ch9-11 — Advanced and Future (7 claims) ===
    ("go-ch9-11", 1): {"slug": "the-biggest-mistake-in-zt-implementation-is-rushing",
                        "topics": ["zt-implementation", "zt-migration"], "type": "migration"},
    ("go-ch9-11", 2): {"slug": "distributed-enforcement-applying-policies-as-close-to-the",
                        "topics": ["zt-device", "zt-policy"], "type": "implementation"},
    ("go-ch9-11", 3): {"slug": "brownfield-environments-require-34-the-timeline-of-greenfield",
                        "topics": ["zt-migration", "zt-implementation"], "type": "migration"},
    ("go-ch9-11", 4): {"slug": "nac-eg-cisco-ise-functions-as-the-single",
                        "topics": ["zt-network", "zt-device"], "type": "implementation"},
    ("go-ch9-11", 5): {"slug": "siloed-teams-where-network-security-applications-and-operations",
                        "topics": ["zt-governance", "zt-architecture"], "type": "governance"},
    ("go-ch9-11", 6): {"slug": "the-zero-trust-journey-is-cyclical-not-linear",
                        "topics": ["zt-governance", "zt-maturity"], "type": "governance"},
    ("go-ch9-11", 7): {"slug": "the-sbc-case-study-demonstrates-that-practical-zt",
                        "topics": ["zt-implementation", "zt-device"], "type": "implementation"},
}

HEADING_RE = re.compile(r'^#{2,3}\s*Claim\s+(\d+)(?:\s*\([^)]*\))?\s*:\s*(.+)$')
MARKER_RE = re.compile(r'^\*\*([^*:]+?):\*\*\s*(.*)$')
TRAILING_ANNOTATION_RE = re.compile(r'\s*(?:\(Scenario|\(Step)[^)]*\)\.?\s*$')

# New markers for Batch 4: plural possessive + book-specific markers
CLAIM_MARKERS = {"author's claim", "authors' claim", "nist's claim", "nist's description",
                 "nsa's claim", "cisa's claim", "finney's claim", "green-ortiz's claim"}
EVIDENCE_MARKERS = {"evidence presented"}
CONFIDENCE_MARKERS = {"confidence"}
STAKES_MARKERS = {"what's at stake"}
DISAGREE_WHO_MARKERS = {"who disagrees"}
DISAGREE_ALT_MARKERS = {"alternative reading"}
ASSESSMENT_MARKERS = {"my assessment", "assessment"}


def normalize_marker(name):
    name = name.strip().lower()
    # Strip trailing parentheticals like "(implicit)" or "(Scenario X)"
    name = re.sub(r'\s*\([^)]*\)\s*$', '', name)
    name = re.sub(r'\s*[—-]\s*.*$', '', name)
    return name.strip()


def clean_title(title):
    title = TRAILING_ANNOTATION_RE.sub('', title).strip()
    return title


def split_claim_blocks(text):
    """Return {claim_num: {"title": str, "lines": [str, ...]}} for a chapter."""
    lines = text.split('\n')
    headings = []
    for i, line in enumerate(lines):
        m = HEADING_RE.match(line.strip())
        if m:
            headings.append((i, int(m.group(1)), m.group(2)))

    blocks = {}
    for idx, (line_i, num, raw_title) in enumerate(headings):
        end = len(lines)
        for j in range(line_i + 1, len(lines)):
            stripped = lines[j].strip()
            if stripped == '---':
                end = j
                break
            if HEADING_RE.match(stripped):
                end = j
                break
        blocks[num] = {"title": clean_title(raw_title), "lines": lines[line_i + 1:end]}
    return blocks


def scan_markers(block_lines):
    segments = []
    current_marker = None
    current_lines = []
    for line in block_lines:
        m = MARKER_RE.match(line.strip())
        if m:
            if current_marker is not None:
                segments.append((current_marker, current_lines))
            current_marker = m.group(1)
            current_lines = [m.group(2)] if m.group(2) else []
        else:
            if current_marker is not None:
                current_lines.append(line)
    if current_marker is not None:
        segments.append((current_marker, current_lines))
    return segments


def join_content(lines):
    text = '\n'.join(lines).strip()
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def extract_sections(block_lines):
    split_idx = None
    for i, line in enumerate(block_lines):
        if line.strip().startswith('#### '):
            split_idx = i
            break
    if split_idx is not None:
        main_lines = block_lines[:split_idx]
        extended_lines = block_lines[split_idx:]
    else:
        main_lines = block_lines
        extended_lines = []

    buckets = {
        "claim": [], "evidence": [], "confidence": [],
        "stakes": [], "disagree_who": [], "disagree_alt": [], "assessment": [],
    }
    evidence_extra = []

    for raw_marker, content_lines in scan_markers(main_lines):
        norm = normalize_marker(raw_marker)
        if norm in CLAIM_MARKERS:
            buckets["claim"].append(join_content(content_lines))
        elif norm in EVIDENCE_MARKERS:
            buckets["evidence"].append(join_content(content_lines))
        elif norm in CONFIDENCE_MARKERS:
            buckets["confidence"].append(join_content(content_lines))
        elif norm in STAKES_MARKERS:
            buckets["stakes"].append(join_content(content_lines))
        elif norm in DISAGREE_WHO_MARKERS:
            buckets["disagree_who"].append(join_content(content_lines))
        elif norm in DISAGREE_ALT_MARKERS:
            buckets["disagree_alt"].append(join_content(content_lines))
        elif norm in ASSESSMENT_MARKERS:
            buckets["assessment"].append(join_content(content_lines))
        else:
            content = join_content(content_lines)
            if content:
                evidence_extra.append("**%s:**\n\n%s" % (raw_marker.strip(), content))
            else:
                evidence_extra.append("**%s:**" % raw_marker.strip())

    extended_text = join_content(extended_lines)
    if extended_text:
        evidence_extra.append(extended_text)

    evidence_parts = buckets["evidence"] + evidence_extra
    return {
        "claim": "\n\n".join(buckets["claim"]).strip(),
        "evidence": "\n\n".join(evidence_parts).strip(),
        "confidence": "\n\n".join(buckets["confidence"]).strip(),
        "stakes": "\n\n".join(buckets["stakes"]).strip(),
        "disagree_who": "\n\n".join(buckets["disagree_who"]).strip(),
        "disagree_alt": "\n\n".join(buckets["disagree_alt"]).strip(),
        "assessment": "\n\n".join(buckets["assessment"]).strip(),
    }


RATING_RE = re.compile(r'^(VERY HIGH|HIGH|MEDIUM-HIGH|MEDIUM-LOW|MEDIUM|LOW)', re.IGNORECASE)


def parse_confidence(confidence_text):
    m = RATING_RE.match(confidence_text.strip())
    if not m:
        return "medium", confidence_text.strip()
    raw = m.group(1).upper()
    if raw in ("VERY HIGH", "HIGH"):
        rating = "high"
    elif raw == "LOW":
        rating = "low"
    else:
        rating = "medium"
    return rating, confidence_text.strip()


def truncate_rationale(text, limit=150):
    text = ' '.join(text.split())
    if len(text) <= limit:
        return text
    truncated = text[:limit]
    if ' ' in truncated:
        truncated = truncated.rsplit(' ', 1)[0]
    return truncated.rstrip('.,;:—- ')


def yaml_quote(s):
    s = s.replace('\n', ' ').strip()
    has_dq = '"' in s
    has_sq = "'" in s
    if has_dq and has_sq:
        escaped = s.replace('\\', '\\\\').replace('"', '\\"')
        return '"%s"' % escaped
    if has_dq:
        return "'%s'" % s.replace("'", "''")
    return '"%s"' % s.replace('\\', '\\\\')


FALLBACK_STAKES = "_Not addressed separately in the source note._"
FALLBACK_DISAGREE = "_None identified._"
FALLBACK_ASSESSMENT = "_Not addressed separately in the source note._"
FALLBACK_EVIDENCE = "_No evidence separable from the claim statement in the source note._"


def build_claim_file(chapter, num, block):
    meta = META[(chapter["key"], num)]
    sections = extract_sections(block["lines"])

    statement = block["title"]
    claim_id = "%s.%d" % (chapter["key"], num)

    confidence_raw = sections["confidence"] or "MEDIUM. Confidence not explicitly stated in source."
    rating, rationale_full = parse_confidence(confidence_raw)
    rationale = truncate_rationale(rationale_full)

    claim_text = sections["claim"] or statement
    evidence_text = sections["evidence"] or FALLBACK_EVIDENCE
    stakes_text = sections["stakes"] or FALLBACK_STAKES
    disagree_who = sections["disagree_who"] or FALLBACK_DISAGREE
    disagree_alt = sections["disagree_alt"] or FALLBACK_DISAGREE
    assessment_text = sections["assessment"] or FALLBACK_ASSESSMENT

    tags_lines = [
        "  - type/claim",
        "  - oskg-zerotrust",
        "  - evidence/secondary-book",
        "  - %s" % chapter["source_tag"],
    ]
    for topic in meta["topics"]:
        tags_lines.append("  - topic/%s" % topic)

    front_matter = "\n".join([
        "---",
        "tags:",
        "\n".join(tags_lines),
        'claim_id: "%s"' % claim_id,
        "statement: %s" % yaml_quote(statement),
        'confidence: "%s"' % rating,
        "confidence_rationale: %s" % yaml_quote(rationale),
        'claim_type: "%s"' % meta["type"],
        "source_note: %s" % yaml_quote("[[%s]]" % chapter["note"]),
        "created: %s" % TODAY,
        "updated: %s" % TODAY,
        "status: active",
        "---",
    ])

    body = "\n".join([
        "",
        "# %s: %s" % (claim_id, statement),
        "",
        "**Source:** [[%s]] — %s" % (chapter["note"], chapter["source_line"]),
        "",
        "## The Claim",
        "",
        claim_text,
        "",
        "## Evidence",
        "",
        evidence_text,
        "",
        "## Confidence",
        "",
        "**Rating:** %s" % rating.upper(),
        "**Rationale:** %s" % rationale_full,
        "",
        "## Stakes",
        "",
        stakes_text,
        "",
        "## Disagreement",
        "",
        "**Who disagrees:**",
        "",
        disagree_who,
        "",
        "**Alternative reading:**",
        "",
        disagree_alt,
        "",
        "## Edges",
        "",
        "**Depends on:**",
        "",
        "**Supports:**",
        "",
        "**Contradicts:**",
        "",
        "**Challenged by:**",
        "",
        "**Operationalizes:**",
        "",
        "**Extends:**",
        "",
        "## Assessment",
        "",
        assessment_text,
        "",
    ])

    return meta["slug"], front_matter + body


def main():
    os.makedirs(CLAIMS_DIR, exist_ok=True)
    total = 0
    summary = []

    for chapter in CHAPTERS:
        path = os.path.join(CONCEPTS_DIR, chapter["file"])
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        blocks = split_claim_blocks(text)
        written = 0
        for num in range(1, chapter["n"] + 1):
            if num not in blocks:
                print("MISSING claim %d in %s" % (num, chapter["file"]))
                continue
            slug, content = build_claim_file(chapter, num, blocks[num])
            out_path = os.path.join(CLAIMS_DIR, "%s.md" % slug)
            with open(out_path, "w", encoding="utf-8") as out:
                out.write(content)
            written += 1

        print("%s: %d/%d claims written" % (chapter["key"], written, chapter["n"]))
        summary.append((chapter["key"], written))
        total += written

    print("\n=== EXTRACTION COMPLETE ===")
    for key, count in summary:
        print("%s: %d claims" % (key, count))
    print("Total: %d claims written to notes/claims/" % total)
    print("=== END ===")


if __name__ == "__main__":
    main()
