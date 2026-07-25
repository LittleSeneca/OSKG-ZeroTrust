#!/usr/bin/env python3
"""
Tag enrichment: add 1-2 topic tags to claims with ≤2 tags,
using co-occurrence affinity + content keyword validation.
Target: 3-4 topic tags per claim.
"""
import os, re
from collections import Counter

BASE = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust")
CLAIMS = os.path.join(BASE, "notes/claims")

# Keyword hints for each tag — claim must contain ≥1 of these to qualify
TAG_KEYWORDS = {
    "zt-identity": ["identity", "authenticate", "credential", "MFA", "IAM", "ICAM", "FIDO", "user", "PIV", "CAC", "SSO"],
    "zt-device": ["device", "endpoint", "hardware", "firmware", "asset", "inventory", "BYOD", "laptop", "mobile"],
    "zt-network": ["network", "segment", "perimeter", "VPN", "SDN", "packet", "traffic", "route", "gateway", "switch"],
    "zt-architecture": ["architecture", "component", "PEP", "PDP", "control plane", "data plane", "logical", "design"],
    "zt-policy": ["policy", "rule", "authorization", "ABAC", "RBAC", "attribute", "decision", "dynamic"],
    "zt-cloud": ["cloud", "AWS", "Azure", "GCP", "SaaS", "IaaS", "PaaS", "workload", "hybrid", "on-prem"],
    "zt-data": ["data", "encrypt", "classif", "label", "DLP", "dataset", "information", "file"],
    "zt-threats": ["threat", "attack", "adversar", "compromise", "breach", "vulnerab", "exploit", "malware", "APT"],
    "zt-monitoring": ["monitor", "detect", "SIEM", "log", "visib", "analytic", "EDR", "XDR", "telemetry", "alert"],
    "zt-migration": ["migrat", "transition", "adopt", "journey", "increment", "legacy", "brownfield", "phased", "roadmap"],
    "zt-governance": ["govern", "complian", "regulation", "executive order", "OMB", "mandate", "framework", "standard"],
    "zt-trust": ["trust", "confidence", "verify", "assume breach", "implicit", "zero", "explicit"],
    "zt-app": ["application", "app", "API", "microservice", "container", "DevSecOps", "CI/CD", "workload"],
    "zt-definition": ["defin", "concept", "principle", "tenet", "meaning", "scope", "fundamental"],
    "zt-implementation": ["implement", "deploy", "build", "operational", "practice", "configure", "setup", "install"],
    "zt-access-mgmt": ["access", "privilege", "JIT", "JEA", "PAM", "least privilege", "RBAC", "permission"],
    "zt-authentication": ["authenticate", "MFA", "phish", "password", "FIDO", "PIV", "token", "biometric", "AAL"],
    "zt-encryption": ["encrypt", "TLS", "cryptograph", "cipher", "PKI", "certificate", "key", "decrypt"],
    "zt-segmentation": ["segment", "micro", "macro", "isolat", "VLAN", "zone", "partition"],
    "zt-maturity": ["maturity", "stage", "level", "phase", "progress", "evolv", "advance"],
    "zt-supply-chain": ["supply chain", "procure", "vendor", "SBOM", "third-party", "supplier"],
    "zt-tenets": ["tenet", "principle", "axiom", "assumption"],
    "zt-inventory": ["inventory", "catalog", "register", "enumerate", "CMDB"],
    "zt-risk": ["risk", "assess", "likelihood", "impact", "probability"],
    "zt-firmware": ["firmware", "UEFI", "BIOS", "TPM", "boot", "microcode"],
    "zt-federation": ["federat", "partner", "cross-domain", "coalition", "mission partner"],
    "zt-remote-access": ["remote", "home", "telework", "BYOD", "off-site"],
    "zt-sdn": ["SDN", "software-defined", "controller", "orchestrat"],
    "zt-microsegmentation": ["micro-segment", "host-based", "workload isolation"],
    "zt-organizational": ["organiz", "culture", "change management", "sponsor", "training"],
}


def claim_keywords(text):
    """Extract lowercase tokens from claim text for keyword matching."""
    lower = text.lower()
    words = set(re.findall(r'[a-z]{3,}', lower))
    # Also check for bigrams
    bigrams = set()
    tokens = re.findall(r'[a-z]+', lower)
    for i in range(len(tokens)-1):
        bigrams.add(f"{tokens[i]} {tokens[i+1]}")
    return words | bigrams


def tag_matches_keywords(tag, keywords):
    """Check if any keyword for this tag appears in the claim text."""
    hints = TAG_KEYWORDS.get(tag, [])
    for hint in hints:
        if hint in keywords:
            return True
        # Check individual words of multi-word hints
        if ' ' in hint:
            if hint in keywords:
                return True
        elif hint in keywords:
            return True
    return False


def main():
    # --- Phase 1: Build co-occurrence data ---
    all_claims = []
    tag_co_occurrence = Counter()  # (tag_a, tag_b) -> count
    tag_freq = Counter()

    for fname in sorted(os.listdir(CLAIMS)):
        if not fname.endswith(".md") or fname == "Claims Index.md":
            continue
        fpath = os.path.join(CLAIMS, fname)
        with open(fpath) as f:
            content = f.read()

        topics = [m.group(1) for m in re.finditer(r'^\s*-\s+topic/(\S+)', content, re.MULTILINE)]
        for t in topics:
            tag_freq[t] += 1

        all_claims.append({
            "file": fname,
            "path": fpath,
            "content": content,
            "topics": topics,
        })

        # Count co-occurrences
        for i in range(len(topics)):
            for j in range(i+1, len(topics)):
                pair = tuple(sorted([topics[i], topics[j]]))
                tag_co_occurrence[pair] += 1

    # --- Phase 2: Compute affinity scores per tag ---
    # For each tag, which other tags co-occur with it most?
    tag_affinity = {}
    for tag in tag_freq:
        affinities = []
        for other in tag_freq:
            if other == tag:
                continue
            pair = tuple(sorted([tag, other]))
            co_count = tag_co_occurrence.get(pair, 0)
            if co_count > 0:
                affinities.append((other, co_count))
        affinities.sort(key=lambda x: -x[1])
        tag_affinity[tag] = [a[0] for a in affinities]

    # --- Phase 3: Enrich claims with ≤2 tags ---
    enriched = 0
    tags_added = Counter()

    for claim in all_claims:
        if len(claim["topics"]) >= 3:
            continue

        existing = set(claim["topics"])
        # Get candidate tags: union of top affinities for each existing tag
        candidates = {}
        for etag in existing:
            for i, aff_tag in enumerate(tag_affinity.get(etag, [])):
                if aff_tag not in existing:
                    score = len(tag_affinity[etag]) - i  # higher = more relevant
                    candidates[aff_tag] = max(candidates.get(aff_tag, 0), score + tag_freq[aff_tag] * 0.01)

        # Sort candidates by score
        ranked = sorted(candidates.items(), key=lambda x: -x[1])

        # Validate with content keywords
        text_for_kw = claim["content"]
        # Focus on claim + evidence sections for keyword matching
        kw_text = text_for_kw
        ck = claim_keywords(kw_text)

        to_add = []
        for tag, score in ranked:
            if len(to_add) >= 2:
                break
            if tag_matches_keywords(tag, ck):
                to_add.append(tag)
            # Fallback: if no keyword match but tag is very high affinity,
            # add it anyway if this is a common co-occurrence
            elif score > 50 and tag_freq[tag] > 10:
                to_add.append(tag)

        if not to_add:
            continue

        # Add tags to frontmatter
        content = claim["content"]
        # Find the last topic tag line and insert after it
        last_topic_pos = 0
        for m in re.finditer(r'^(\s*-\s+topic/\S+.*)$', content, re.MULTILINE):
            last_topic_pos = m.end()

        if last_topic_pos == 0:
            continue

        new_tag_lines = "\n".join(["  - topic/%s" % t for t in to_add])
        content = content[:last_topic_pos] + "\n" + new_tag_lines + content[last_topic_pos:]

        with open(claim["path"], "w") as f:
            f.write(content)

        enriched += 1
        for t in to_add:
            tags_added[t] += 1

    print(f"Enriched {enriched} claims (added {sum(tags_added.values())} total tags)")
    print(f"\nTags added (by frequency):")
    for tag, count in tags_added.most_common():
        print(f"  {tag}: +{count}")

    # Post-enrichment stats
    new_dist = Counter()
    for fname in sorted(os.listdir(CLAIMS)):
        if not fname.endswith(".md") or fname == "Claims Index.md":
            continue
        with open(os.path.join(CLAIMS, fname)) as f:
            content = f.read(1000)
        n = len([m.group(1) for m in re.finditer(r'^\s*-\s+topic/(\S+)', content, re.MULTILINE)])
        new_dist[n] += 1

    print(f"\nPost-enrichment tag distribution:")
    for count in sorted(new_dist):
        print(f"  {count} tags: {new_dist[count]} claims")


if __name__ == "__main__":
    main()
