#!/usr/bin/env python3
"""Prep cluster payloads for Phase 3 Pass 2 LLM edge detection.

For each cluster in the manifest, reads all claim files and extracts
the essential content (claim_id, statement, short evidence excerpt).
Saves one payload file per cluster under scripts/phase3_payloads/.
"""

import json
import os
import re

MANIFEST_PATH = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/scripts/phase3_clusters.json")
CLAIMS_DIR = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/notes/claims")
OUT_DIR = os.path.expanduser("~/Projects/Personal/OSKG-ZeroTrust/scripts/phase3_payloads")


def parse_frontmatter(text):
    match = re.match(r'^---\s*\n(.*?)\n---', text, re.DOTALL)
    if not match:
        return {}
    fm = match.group(1)
    data = {}
    current_key = None
    for line in fm.split('\n'):
        kv = re.match(r'^(\w[\w_]*):\s*(.*)', line)
        if kv:
            current_key = kv.group(1)
            val = kv.group(2).strip().strip('"').strip("'")
            data[current_key] = val
        elif current_key and line.strip().startswith('- '):
            val = line.strip()[2:].strip().strip('"').strip("'")
            existing = data.get(current_key)
            if not isinstance(existing, list):
                data[current_key] = [existing] if existing else []
            data[current_key].append(val)
    return data


def extract_claim_content(slug):
    """Extract statement + short evidence excerpt from a claim file."""
    fpath = os.path.join(CLAIMS_DIR, slug + '.md')
    text = open(fpath).read()
    fm = parse_frontmatter(text)

    claim_id = fm.get('claim_id', 'unknown')
    statement = fm.get('statement', '')
    claim_type = fm.get('claim_type', '')
    confidence = fm.get('confidence', 'medium')

    # Extract first 300 chars of evidence section
    evidence = ''
    ev_match = re.search(r'## Evidence\s*\n(.*?)(?=\n## |\Z)', text, re.DOTALL)
    if ev_match:
        evidence = ev_match.group(1).strip()[:400]

    return {
        'slug': slug,
        'claim_id': claim_id,
        'statement': statement,
        'claim_type': claim_type,
        'confidence': confidence,
        'evidence_excerpt': evidence,
    }


def main():
    with open(MANIFEST_PATH) as f:
        manifest = json.load(f)

    os.makedirs(OUT_DIR, exist_ok=True)

    for cluster in manifest['clusters']:
        claims = []
        for slug in cluster['claim_slugs']:
            claims.append(extract_claim_content(slug))

        payload = {
            'cluster_id': cluster['id'],
            'cluster_label': cluster['label'],
            'size': cluster['size'],
            'claims': claims,
        }

        out_path = os.path.join(OUT_DIR, f"{cluster['id']}.json")
        with open(out_path, 'w') as f:
            json.dump(payload, f, indent=2)

        print(f"  {cluster['id']:15s} | {cluster['size']:3d} claims → {out_path}")

    print(f"\nPrepped {len(manifest['clusters'])} cluster payloads in {OUT_DIR}")


if __name__ == '__main__':
    main()
