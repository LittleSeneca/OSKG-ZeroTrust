#!/usr/bin/env python3
"""Phase 4: Structural analysis of the Zero Trust knowledge graph.

Parses all claim files + the Phase 3 edge inventory, then produces five analyses:
1. Hinge Inventory — claims whose removal would most fragment the graph
2. Cascade Trees — downstream dependency chains for top hinges
3. Convergence Points — claims with 5+ cross-source supports
4. Contradiction Clusters — camps around known contradictions
5. Structural Gaps — sparse edges, isolated subgraphs, bridge claims
"""

import json
import os
import re
from collections import defaultdict, deque
from pathlib import Path

BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__))).parent
CLAIMS_DIR = BASE_DIR / "notes" / "claims"
EDGE_INVENTORY = BASE_DIR / "scripts" / "phase3_edge_inventory.json"

CONFIDENCE_MAP = {
    "very-low": 0,
    "low": 1,
    "low-medium": 2,
    "medium": 3,
    "medium-high": 4,
    "high": 5,
    "very-high": 6,
}


# ── Parsing ──────────────────────────────────────────────────────────────────

def parse_frontmatter(text: str) -> dict:
    """Parse YAML frontmatter from markdown text (simple key-value, no PyYAML)."""
    match = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not match:
        return {}
    fm = match.group(1)
    data = {}
    for line in fm.split("\n"):
        kv = re.match(r"^(\w[\w_]*):\s*(.*)", line)
        if kv:
            key = kv.group(1)
            val = kv.group(2).strip().strip('"').strip("'")
            data[key] = val
    return data


def parse_tags(text: str) -> list[str]:
    """Extract tags from frontmatter lines."""
    tags = []
    in_frontmatter = False
    for line in text.split("\n"):
        if line.strip() == "---":
            if not in_frontmatter:
                in_frontmatter = True
                continue
            else:
                break
        if in_frontmatter:
            m = re.match(r"\s*-\s+(\S+)", line)
            if m:
                tags.append(m.group(1))
    return tags


def load_claims(claims_dir: Path) -> dict[str, dict]:
    """Parse all claim files. Returns {slug: {claim_id, statement, confidence, confidence_val, source_note, tags, claim_type, status}}."""
    claims = {}
    for fpath in sorted(claims_dir.glob("*.md")):
        slug = fpath.stem
        text = fpath.read_text()
        fm = parse_frontmatter(text)

        # Skip non-claim files (indexes, templates)
        tags = parse_tags(text)
        if "type/claim" not in tags:
            continue

        status = fm.get("status", "active")
        if status != "active":
            continue

        claim_id = fm.get("claim_id", "")
        if not claim_id:
            continue

        confidence = fm.get("confidence", "medium")
        claims[slug] = {
            "slug": slug,
            "claim_id": claim_id,
            "statement": fm.get("statement", ""),
            "confidence": confidence,
            "confidence_val": CONFIDENCE_MAP.get(confidence, 3),
            "source_note": fm.get("source_note", "unknown"),
            "tags": tags,
            "claim_type": fm.get("claim_type", "unknown"),
            "status": status,
        }
    return claims


def load_edges(edge_path: Path) -> list[dict]:
    """Load the Phase 3 edge inventory."""
    with open(edge_path) as f:
        data = json.load(f)
    return data.get("edges", [])


# ── Graph Building ───────────────────────────────────────────────────────────

def build_graph(claims: dict[str, dict], edges: list[dict]) -> dict[str, dict]:
    """Build adjacency lists for the directed edge graph.

    Returns {slug: {out_edges: {target_slug: [edge_types]}, in_edges: {source_slug: [edge_types]}}}.
    Only includes nodes that exist in the claims dict.
    """
    graph: dict[str, dict] = {}
    for slug in claims:
        graph[slug] = {"out_edges": defaultdict(list), "in_edges": defaultdict(list)}

    for edge in edges:
        a, b = edge["claim_a"], edge["claim_b"]
        etype = edge["edge_type"]

        # Only include edges where both endpoints are active claims
        if a in graph and b in graph:
            graph[a]["out_edges"][b].append(etype)
            graph[b]["in_edges"][a].append(etype)

    return graph


# ── Betweenness Centrality (Brandes, directed unweighted) ────────────────────

def compute_betweenness(graph: dict[str, dict]) -> dict[str, float]:
    """Compute betweenness centrality for all nodes.

    Uses Brandes' algorithm on the directed graph. O(nm).
    """
    nodes = list(graph.keys())
    n = len(nodes)
    node_to_idx = {node: i for i, node in enumerate(nodes)}

    betweenness = {node: 0.0 for node in nodes}

    for s in nodes:
        # BFS from s
        stack = []
        pred = {v: [] for v in nodes}
        sigma = {v: 0 for v in nodes}
        dist = {v: -1 for v in nodes}

        sigma[s] = 1
        dist[s] = 0
        q = deque([s])

        while q:
            v = q.popleft()
            stack.append(v)
            for w in graph[v]["out_edges"]:
                if dist[w] < 0:
                    dist[w] = dist[v] + 1
                    q.append(w)
                if dist[w] == dist[v] + 1:
                    sigma[w] += sigma[v]
                    pred[w].append(v)

        # Back-propagation
        delta = {v: 0.0 for v in nodes}
        while stack:
            w = stack.pop()
            for v in pred[w]:
                delta[v] += (sigma[v] / sigma[w]) * (1 + delta[w])
            if w != s:
                betweenness[w] += delta[w]

    return betweenness


# ── Analysis 1: Hinge Inventory ──────────────────────────────────────────────

def hinge_inventory(
    claims: dict[str, dict], graph: dict[str, dict], betweenness: dict[str, float], top_n: int = 15
) -> list[dict]:
    """Find the claims whose removal would most fragment the graph.

    Score = edge_count * betweenness. For each: what subgraphs collapse?
    """
    # Calculate composite score
    scored = []
    for slug in claims:
        degree = len(graph[slug]["out_edges"]) + len(graph[slug]["in_edges"])
        bt = betweenness.get(slug, 0.0)
        score = degree * bt
        scored.append((slug, degree, bt, score))

    scored.sort(key=lambda x: x[3], reverse=True)
    top = scored[:top_n]

    results = []
    for slug, degree, bt, score in top:
        claim = claims[slug]

        # What depends on this claim? (outgoing depends_on + supports + extends)
        downstream = set()
        queue = deque()
        for target, etypes in graph[slug]["out_edges"].items():
            for et in etypes:
                if et in ("supports", "extends", "depends_on"):
                    if target not in downstream:
                        downstream.add(target)
                        queue.append(target)

        # One-hop transitive closure (claims that are 2 hops away)
        hop2 = set()
        for ds in list(downstream):
            for target, etypes in graph[ds]["out_edges"].items():
                for et in etypes:
                    if et in ("supports", "extends", "depends_on"):
                        hop2.add(target)

        # Incoming: who supports/extends this claim?
        incoming = set()
        for source, etypes in graph[slug]["in_edges"].items():
            for et in etypes:
                if et in ("supports", "extends", "depends_on"):
                    incoming.add(source)

        # Topic tags
        topics = [t.replace("topic/", "") for t in claim["tags"] if t.startswith("topic/")]

        results.append({
            "slug": slug,
            "claim_id": claim["claim_id"],
            "statement": claim["statement"][:150],
            "score": round(score, 1),
            "degree": degree,
            "betweenness": round(bt, 2),
            "confidence": claim["confidence"],
            "source_note": claim["source_note"],
            "topics": topics,
            "downstream_count": len(downstream),
            "hop2_count": len(hop2),
            "incoming_count": len(incoming),
            "fragmentation": (
                f"Removing this claim would disconnect {len(downstream)} direct dependents "
                f"and potentially fragment {len(hop2)} second-order claims"
            ),
        })

    return results


# ── Analysis 2: Cascade Trees ────────────────────────────────────────────────

def cascade_trees(
    claims: dict[str, dict], graph: dict[str, dict], hinges: list[dict], depth: int = 4, top_n: int = 8
) -> str:
    """Build human-readable dependency cascade trees for top hinges."""
    top = hinges[:top_n]
    lines = []

    for i, hinge in enumerate(top):
        slug = hinge["slug"]
        claim = claims[slug]
        lines.append(f"## Cascade {i+1}: {claim['claim_id']}")
        lines.append(f"**{claim['statement'][:120]}**")
        lines.append(f"Confidence: {claim['confidence']} | Source: {claim['source_note']}")
        lines.append("")

        seen = {slug}
        tree_lines = _build_tree(slug, graph, claims, depth=depth, prefix="", seen=seen)
        if tree_lines:
            lines.extend(tree_lines)
        else:
            lines.append("  (no downstream dependents)")
        lines.append("")

    return "\n".join(lines)


def _build_tree(
    slug: str, graph: dict[str, dict], claims: dict[str, dict],
    depth: int, prefix: str, seen: set
) -> list[str]:
    """Recursively build tree lines."""
    if depth <= 0:
        return [f"{prefix}└── ..."]

    # Gather all downstream edges (supports, extends, depends_on)
    downstream = []
    for target, etypes in graph[slug]["out_edges"].items():
        if target in seen:
            continue
        relevant = [et for et in etypes if et in ("supports", "extends", "depends_on")]
        if relevant:
            downstream.append((target, relevant))

    if not downstream:
        return []

    lines = []
    for i, (target, etypes) in enumerate(downstream):
        is_last = (i == len(downstream) - 1)
        connector = "└── " if is_last else "├── "
        child_prefix = "    " if is_last else "│   "

        claim = claims.get(target, {"claim_id": target, "statement": ""})
        cid = claim.get("claim_id", target)
        stmt = claim.get("statement", "")[:80]
        etype_str = "+".join(sorted(set(et[:3] for et in etypes)))  # sup+ext+dep
        lines.append(f"{prefix}{connector}{cid} ({etype_str}): {stmt}")

        seen.add(target)
        child_lines = _build_tree(target, graph, claims, depth - 1, prefix + child_prefix, seen)
        lines.extend(child_lines)

    return lines


# ── Analysis 3: Convergence Points ───────────────────────────────────────────

def convergence_points(
    claims: dict[str, dict], graph: dict[str, dict], min_supporters: int = 5
) -> list[dict]:
    """Claims with 5+ supports from DIFFERENT source notes."""
    results = []

    for slug, claim in claims.items():
        supporters = set()
        for source, etypes in graph[slug]["in_edges"].items():
            if source not in claims:
                continue
            for et in etypes:
                if et in ("supports", "extends"):
                    supporters.add(source)
                    break

        # Count unique source_notes among supporters
        source_notes: set[str] = set()
        for s in supporters:
            sn = claims[s].get("source_note", "unknown")
            # Normalize: strip wikilink brackets if present
            sn = sn.replace("[[", "").replace("]]", "").strip()
            source_notes.add(sn)

        if len(source_notes) >= min_supporters:
            # Also tally contradictors
            contradictors = set()
            for source, etypes in graph[slug]["in_edges"].items():
                if source not in claims:
                    continue
                for et in etypes:
                    if et == "contradicts":
                        contradictors.add(source)
                        break

            # Direct edges from the claim to others (contradicts)
            for target, etypes in graph[slug]["out_edges"].items():
                for et in etypes:
                    if et == "contradicts":
                        contradictors.add(target)

            results.append({
                "slug": slug,
                "claim_id": claim["claim_id"],
                "statement": claim["statement"][:150],
                "confidence": claim["confidence"],
                "source_notes": sorted(source_notes),
                "source_diversity": len(source_notes),
                "total_supporters": len(supporters),
                "contradictions": len(contradictors),
            })

    results.sort(key=lambda x: (x["source_diversity"], x["total_supporters"]), reverse=True)
    return results


# ── Analysis 4: Contradiction Clusters ───────────────────────────────────────

def contradiction_clusters(
    claims: dict[str, dict], graph: dict[str, dict],
    pairs: list[tuple[str, str]]
) -> list[dict]:
    """Build camps around known contradiction pairs.

    For each side: find all claims that support it (transitive, depth 2).
    """
    results = []

    for slug_a, slug_b in pairs:
        claim_a = claims.get(slug_a, {})
        claim_b = claims.get(slug_b, {})

        # Camp A: claims that support slug_a (incoming + outgoing, depth 2)
        camp_a = _gather_supporters(slug_a, graph, claims, depth=2)

        # Camp B: claims that support slug_b
        camp_b = _gather_supporters(slug_b, graph, claims, depth=2)

        # Also find claims that directly contradict the other side (cross-fire)
        cross_a = set()
        cross_b = set()
        for c in camp_a:
            if slug_b in graph[c].get("out_edges", {}):
                for et in graph[c]["out_edges"][slug_b]:
                    if et == "contradicts":
                        cross_a.add(c)
                        break
        for c in camp_b:
            if slug_a in graph[c].get("out_edges", {}):
                for et in graph[c]["out_edges"][slug_a]:
                    if et == "contradicts":
                        cross_b.add(c)
                        break

        # Also find claims that support slug_a's position AND contradict slug_b or vice versa
        cross_support_a = []
        cross_support_b = []

        # Source diversity in each camp
        sources_a = set()
        for s in camp_a:
            sn = claims.get(s, {}).get("source_note", "unknown")
            sn = sn.replace("[[", "").replace("]]", "").strip()
            sources_a.add(sn)
        sources_b = set()
        for s in camp_b:
            sn = claims.get(s, {}).get("source_note", "unknown")
            sn = sn.replace("[[", "").replace("]]", "").strip()
            sources_b.add(sn)

        results.append({
            "slug_a": slug_a,
            "claim_id_a": claim_a.get("claim_id", slug_a),
            "statement_a": claim_a.get("statement", "")[:150],
            "confidence_a": claim_a.get("confidence", ""),
            "camp_a": sorted(camp_a),
            "camp_a_count": len(camp_a),
            "cross_a_count": len(cross_a),
            "sources_a": sorted(sources_a),
            "slug_b": slug_b,
            "claim_id_b": claim_b.get("claim_id", slug_b),
            "statement_b": claim_b.get("statement", "")[:150],
            "confidence_b": claim_b.get("confidence", ""),
            "camp_b": sorted(camp_b),
            "camp_b_count": len(camp_b),
            "cross_b_count": len(cross_b),
            "sources_b": sorted(sources_b),
        })

    return results


def _gather_supporters(slug: str, graph: dict[str, dict], claims: dict[str, dict], depth: int) -> set[str]:
    """Gather all claims that support or are supported by a given claim, up to given depth.

    Camp = incoming supporters + outgoing downstream claims (what the position supports).
    """
    supporters = set()
    queue = deque([(slug, 0, "both")])
    seen = {slug}

    while queue:
        current, d, direction = queue.popleft()
        if d >= depth:
            continue

        if direction in ("in", "both"):
            # Claims that support/extends the current node
            for source, etypes in graph[current]["in_edges"].items():
                if source in seen:
                    continue
                for et in etypes:
                    if et in ("supports", "extends", "depends_on"):
                        supporters.add(source)
                        seen.add(source)
                        queue.append((source, d + 1, "both"))
                        break

        if direction in ("out", "both"):
            # Claims that the current node supports/extends
            for target, etypes in graph[current]["out_edges"].items():
                if target in seen:
                    continue
                for et in etypes:
                    if et in ("supports", "extends", "depends_on"):
                        supporters.add(target)
                        seen.add(target)
                        queue.append((target, d + 1, "both"))
                        break

    return supporters


# ── Analysis 5: Structural Gaps ──────────────────────────────────────────────

def structural_gaps(
    claims: dict[str, dict], graph: dict[str, dict]
) -> dict:
    """Identify structural weaknesses in the knowledge graph.

    - Orphan claims (zero edges)
    - Bridge claims (only edge connecting two otherwise-separate clusters)
    - Isolated subgraphs
    - Topics with sparse edges
    """
    # Orphans: claims with zero edges
    orphans = []
    for slug in claims:
        out_count = len(graph[slug]["out_edges"])
        in_count = len(graph[slug]["in_edges"])
        if out_count == 0 and in_count == 0:
            claim = claims[slug]
            orphans.append({
                "slug": slug,
                "claim_id": claim["claim_id"],
                "statement": claim["statement"][:120],
                "source_note": claim["source_note"],
            })

    # Bridge detection: remove each node, check if graph partitions increase
    # Use articulation point detection on the undirected projection
    bridges = _find_bridges(graph, claims)

    # Connected components (undirected projection)
    components = _find_connected_components(graph)

    # Topic sparsity: topics with few edges per claim
    topic_edge_counts: dict[str, list[int]] = defaultdict(list)
    topic_claim_counts: dict[str, int] = defaultdict(int)
    for slug, claim in claims.items():
        edge_count = len(graph[slug]["out_edges"]) + len(graph[slug]["in_edges"])
        for tag in claim["tags"]:
            if tag.startswith("topic/"):
                topic = tag.replace("topic/", "")
                topic_edge_counts[topic].append(edge_count)
                topic_claim_counts[topic] += 1

    sparse_topics = []
    for topic, counts in topic_edge_counts.items():
        avg_edges = sum(counts) / len(counts) if counts else 0
        if topic_claim_counts[topic] >= 3 and avg_edges < 2.0:
            sparse_topics.append({
                "topic": topic,
                "claim_count": topic_claim_counts[topic],
                "avg_edges": round(avg_edges, 1),
            })

    sparse_topics.sort(key=lambda x: x["avg_edges"])

    # Isolated components
    isolated_components = []
    for comp in components:
        if 1 < len(comp) <= 5:  # Small isolated clusters
            isolated_components.append(sorted(comp))

    return {
        "orphan_count": len(orphans),
        "orphans": orphans,
        "bridge_count": len(bridges),
        "bridges": bridges[:10],  # Top 10 by impact
        "component_count": len(components),
        "isolated_components": isolated_components,
        "sparse_topics": sparse_topics[:10],
    }


def _find_bridges(graph: dict[str, dict], claims: dict[str, dict]) -> list[dict]:
    """Find bridge claims: nodes whose removal would disconnect the graph.

    Uses articulation point detection on the undirected projection.
    """
    nodes = list(graph.keys())
    n = len(nodes)
    node_to_idx = {node: i for i, node in enumerate(nodes)}

    # Build undirected adjacency
    adj = {v: set() for v in nodes}
    for v in nodes:
        for w in graph[v]["out_edges"]:
            adj[v].add(w)
            adj[w].add(v)
        for w in graph[v]["in_edges"]:
            adj[v].add(w)
            adj[w].add(v)

    visited = {v: False for v in nodes}
    disc = {v: 0 for v in nodes}
    low = {v: 0 for v in nodes}
    parent = {v: None for v in nodes}
    ap = set()
    time = [0]

    def dfs(u):
        children = 0
        visited[u] = True
        time[0] += 1
        disc[u] = low[u] = time[0]

        for v in adj[u]:
            if not visited[v]:
                children += 1
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])

                if parent[u] is None and children > 1:
                    ap.add(u)
                if parent[u] is not None and low[v] >= disc[u]:
                    ap.add(u)
            elif v != parent[u]:
                low[u] = min(low[u], disc[v])

    for v in nodes:
        if not visited[v]:
            dfs(v)

    # Score bridges by degree
    bridge_list = []
    for slug in ap:
        claim = claims.get(slug, {})
        degree = len(adj[slug])
        bridge_list.append({
            "slug": slug,
            "claim_id": claim.get("claim_id", slug),
            "statement": claim.get("statement", "")[:120],
            "degree": degree,
        })

    bridge_list.sort(key=lambda x: x["degree"], reverse=True)
    return bridge_list


def _find_connected_components(graph: dict[str, dict]) -> list[set[str]]:
    """Find connected components in the undirected projection."""
    nodes = list(graph.keys())
    adj = {v: set() for v in nodes}
    for v in nodes:
        for w in graph[v]["out_edges"]:
            adj[v].add(w)
            adj[w].add(v)
        for w in graph[v]["in_edges"]:
            adj[v].add(w)
            adj[w].add(v)

    visited = set()
    components = []

    for v in nodes:
        if v not in visited:
            comp = set()
            queue = deque([v])
            visited.add(v)
            while queue:
                cur = queue.popleft()
                comp.add(cur)
                for nb in adj[cur]:
                    if nb not in visited:
                        visited.add(nb)
                        queue.append(nb)
            components.append(comp)

    return components


# ── Output ───────────────────────────────────────────────────────────────────

def format_output(
    hinges: list[dict],
    cascades: str,
    convergence: list[dict],
    contradiction_results: list[dict],
    gaps: dict,
) -> str:
    """Format all results as a readable report."""
    lines = []
    sep = "=" * 80
    sub = "-" * 60

    # ── Header ──
    lines.append(sep)
    lines.append("PHASE 4: ZERO TRUST KNOWLEDGE GRAPH — STRUCTURAL ANALYSIS")
    lines.append(sep)
    lines.append("")

    # ── 1. Hinge Inventory ──
    lines.append(sep)
    lines.append("1. HINGE INVENTORY — Top 15 Claims by Structural Impact")
    lines.append("   Score = edge_count × betweenness_centrality")
    lines.append(sep)
    lines.append("")

    for i, h in enumerate(hinges):
        lines.append(f"--- Hinge #{i+1}: {h['claim_id']} ---")
        lines.append(f"  Statement: {h['statement']}")
        lines.append(f"  Score: {h['score']} | Degree: {h['degree']} | Betweenness: {h['betweenness']}")
        lines.append(f"  Confidence: {h['confidence']} | Source: {h['source_note']}")
        lines.append(f"  Topics: {', '.join(h['topics'][:5])}")
        lines.append(f"  Direct dependents: {h['downstream_count']} | Second-order: {h['hop2_count']}")
        lines.append(f"  Incoming support: {h['incoming_count']} claims")
        lines.append(f"  Fragmentation: {h['fragmentation']}")
        lines.append("")

    # ── 2. Cascade Trees ──
    lines.append(sep)
    lines.append("2. CASCADE TREES — Downstream Dependency Chains (depth 4)")
    lines.append(sep)
    lines.append("")
    lines.append(cascades)

    # ── 3. Convergence Points ──
    lines.append(sep)
    lines.append("3. CONVERGENCE POINTS — Where 5+ Different Sources Agree")
    lines.append(sep)
    lines.append("")
    lines.append(f"Found {len(convergence)} convergence points with 5+ unique source notes.")
    lines.append("")

    for i, cp in enumerate(convergence):
        lines.append(f"--- Convergence #{i+1}: {cp['claim_id']} ---")
        lines.append(f"  Statement: {cp['statement']}")
        lines.append(f"  Confidence: {cp['confidence']}")
        lines.append(f"  Source diversity: {cp['source_diversity']} unique sources")
        lines.append(f"  Total supporters: {cp['total_supporters']}")
        lines.append(f"  Contradictions: {cp['contradictions']}")
        lines.append(f"  Sources: {', '.join(cp['source_notes'][:8])}")
        if cp["contradictions"] > 0:
            lines.append(f"  ⚠ Has {cp['contradictions']} contradiction(s) — not pure convergence")
        lines.append("")

    # ── 4. Contradiction Clusters ──
    lines.append(sep)
    lines.append("4. CONTRADICTION CLUSTERS — Camps Around Known Tensions")
    lines.append(sep)
    lines.append("")

    for cr in contradiction_results:
        lines.append(f"CONTRADICTION: {cr['claim_id_a']} ↔ {cr['claim_id_b']}")
        lines.append("")

        lines.append(f"  SIDE A: {cr['statement_a'][:120]}")
        lines.append(f"    Confidence: {cr['confidence_a']} | Camp size: {cr['camp_a_count']} | Cross-fire: {cr['cross_a_count']}")
        lines.append(f"    Sources: {', '.join(cr['sources_a']) or 'none'}")
        if cr["camp_a"]:
            lines.append(f"    Camp members: {', '.join(cr['camp_a'][:8])}")
        lines.append("")

        lines.append(f"  SIDE B: {cr['statement_b'][:120]}")
        lines.append(f"    Confidence: {cr['confidence_b']} | Camp size: {cr['camp_b_count']} | Cross-fire: {cr['cross_b_count']}")
        lines.append(f"    Sources: {', '.join(cr['sources_b']) or 'none'}")
        if cr["camp_b"]:
            lines.append(f"    Camp members: {', '.join(cr['camp_b'][:8])}")
        lines.append("")

        # Determine if this is genuine domain tension or an edge case
        camp_a = cr["camp_a_count"]
        camp_b = cr["camp_b_count"]
        if camp_a >= 3 and camp_b >= 3:
            shared = set(cr["sources_a"]) & set(cr["sources_b"])
            if shared:
                lines.append(f"  ASSESSMENT: Genuine domain tension — both positions have multi-source support, with {len(shared)} shared source(s).")
            else:
                lines.append("  ASSESSMENT: Genuine domain tension — both positions have multi-source support from different sources. Likely different scope or context.")
        elif camp_a <= 1 and camp_b <= 1:
            lines.append("  ASSESSMENT: Structurally isolated contradiction — neither side has a supporting camp. This is likely an edge-case disagreement, not a domain-scale tension.")
        elif camp_b == 0 or (camp_a > 0 and camp_a > camp_b * 3):
            lines.append(f"  ASSESSMENT: Asymmetric — Side A has significantly more support ({camp_a} vs {camp_b}). Side B's position is the outlier.")
        elif camp_a == 0 or (camp_b > 0 and camp_b > camp_a * 3):
            lines.append(f"  ASSESSMENT: Asymmetric — Side B has significantly more support ({camp_b} vs {camp_a}). Side A's position is the outlier.")
        else:
            lines.append("  ASSESSMENT: Moderate tension — both sides have meaningful but asymmetric support.")
        lines.append("")

    # ── 5. Structural Gaps ──
    lines.append(sep)
    lines.append("5. STRUCTURAL GAPS — Where the Graph Is Thin")
    lines.append(sep)
    lines.append("")

    lines.append(f"Orphans (zero edges): {gaps['orphan_count']}")
    for o in gaps["orphans"]:
        lines.append(f"  • {o['claim_id']}: {o['statement'][:100]}")
        lines.append(f"    Source: {o['source_note']}")
    lines.append("")

    lines.append(f"Bridges (articulation points): {gaps['bridge_count']}")
    for b in gaps["bridges"]:
        lines.append(f"  • {b['claim_id']} (degree={b['degree']}): {b['statement'][:100]}")
    lines.append("")

    lines.append(f"Connected components: {gaps['component_count']}")
    if gaps["isolated_components"]:
        lines.append("Small isolated clusters:")
        for comp in gaps["isolated_components"]:
            lines.append(f"  Cluster ({len(comp)} claims): {', '.join(comp[:5])}")
    lines.append("")

    lines.append("Sparse topics (avg edges < 2.0, ≥3 claims):")
    for st in gaps["sparse_topics"]:
        lines.append(f"  • topic/{st['topic']}: {st['claim_count']} claims, avg {st['avg_edges']} edges")
    lines.append("")

    lines.append(sep)
    lines.append("END OF PHASE 4 ANALYSIS")
    lines.append(sep)

    return "\n".join(lines)


# ── Main ─────────────────────────────────────────────────────────────────────

def main() -> str:
    print("Loading claims...")
    claims = load_claims(CLAIMS_DIR)
    print(f"  Loaded {len(claims)} active claims")

    print("Loading edges...")
    raw_edges = load_edges(EDGE_INVENTORY)
    print(f"  Loaded {len(raw_edges)} edges")

    print("Building graph...")
    graph = build_graph(claims, raw_edges)

    # Count nodes with edges
    nodes_with_edges = sum(1 for v, g in graph.items() if g["out_edges"] or g["in_edges"])
    print(f"  Nodes with edges: {nodes_with_edges} / {len(graph)}")

    print("Computing betweenness centrality (this may take a moment)...")
    betweenness = compute_betweenness(graph)
    max_bt = max(betweenness.values()) if betweenness else 0
    print(f"  Max betweenness: {max_bt:.2f}")

    print("\n--- Analysis 1: Hinge Inventory ---")
    hinges = hinge_inventory(claims, graph, betweenness, top_n=15)
    for i, h in enumerate(hinges[:5]):
        print(f"  #{i+1}: {h['claim_id']} (score={h['score']:.0f})")

    print("\n--- Analysis 2: Cascade Trees ---")
    cascades = cascade_trees(claims, graph, hinges, depth=4, top_n=8)
    # Print first few lines as preview
    for line in cascades.split("\n")[:20]:
        print(f"  {line}")

    print("\n--- Analysis 3: Convergence Points ---")
    convergence = convergence_points(claims, graph, min_supporters=5)
    print(f"  Found {len(convergence)} convergence points (5+ cross-source supports)")
    for cp in convergence[:5]:
        print(f"  {cp['claim_id']}: {cp['source_diversity']} sources, {cp['total_supporters']} supporters")

    print("\n--- Analysis 4: Contradiction Clusters ---")
    contradiction_pairs = [
        ("zt-can-bring-real-value-to-iot-but", "firmware-level-patch-management"),
        ("iaaspaas-security-hasnt-kept-pace-with-iaaspaas-adoption", "beyondcorp-google-implementation-zt-model-provides-architectural"),
    ]
    contra_results = contradiction_clusters(claims, graph, contradiction_pairs)
    for cr in contra_results:
        print(f"  {cr['claim_id_a']} (camp={cr['camp_a_count']}) ↔ {cr['claim_id_b']} (camp={cr['camp_b_count']})")

    print("\n--- Analysis 5: Structural Gaps ---")
    gaps = structural_gaps(claims, graph)
    print(f"  Orphans: {gaps['orphan_count']}")
    print(f"  Bridges: {gaps['bridge_count']}")
    print(f"  Components: {gaps['component_count']}")

    # ── Build output ──
    output_text = format_output(hinges, cascades, convergence, contra_results, gaps)

    # Save output
    output_path = BASE_DIR / "scripts" / "phase4_analysis_output.txt"
    output_path.write_text(output_text)
    print(f"\nFull report saved to: {output_path}")

    # Also save JSON summary
    json_output = {
        "hinges": hinges,
        "convergence": convergence,
        "contradiction_clusters": contra_results,
        "structural_gaps": {
            k: v for k, v in gaps.items()
            if k not in ("orphans", "bridges", "isolated_components", "sparse_topics")
        },
        "structural_gaps_detail": gaps,
    }
    json_path = BASE_DIR / "scripts" / "phase4_analysis.json"
    json_path.write_text(json.dumps(json_output, indent=2))
    print(f"JSON summary saved to: {json_path}")

    return output_text


if __name__ == "__main__":
    main()
