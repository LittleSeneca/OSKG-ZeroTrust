---
tags:
  - type/claim
  - oskg-zerotrust
  - evidence/secondary-book
  - source/finney-project-zt
  - topic/zt-definition
  - topic/zt-architecture
  - topic/zt-network
  - topic/zt-governance
claim_id: "finney-ch1-3.6"
statement: "The Four Design Principles and Five-Step Methodology make ZT repeatable"
confidence: "high"
confidence_rationale: "HIGH for the principles/methodology. This is Kindervag's original ZT framework, refined by ON2IT (the company Aaron represents in the narrative)"
claim_type: "definitional"
source_note: "[[Finney — Ch1-3 — The Zero Trust Story]]"
created: 2026-07-24
updated: 2026-07-24
status: active
---
# finney-ch1-3.6: The Four Design Principles and Five-Step Methodology make ZT repeatable

**Source:** [[Finney — Ch1-3 — The Zero Trust Story]] — George Finney, *Project Zero Trust*, 2022

## The Claim

"There are only nine things you need to know to do Zero Trust. Nine things. That's all." The framework:

## Evidence

The team immediately applies the methodology to a "learning protect surface" — a non-critical SharePoint site for the training team. They discover: (a) firewall rules allowing ports that aren't running on the server (decommissioned server, IP reused, no one told firewall admins), (b) no outbound restrictions (the server can talk to anything on the Internet — the command-and-control vector that enables ransomware), (c) the architecture was copy-pasted from another application (one-size-fits-all doesn't work for ZT). By the end, they've reduced access to only the training team's role group, restricted outbound traffic, and established monitoring.

**Four Design Principles:**

1. Focus on business outcomes
2. Design from the inside out
3. Determine who/what needs access
4. Inspect and log all traffic

**Five-Step Methodology:**

1. Define the protect surface
2. Map the transaction flows
3. Architect a Zero Trust environment
4. Create Zero Trust policies (using the Kipling Method: Who, What, When, Where, Why, How)
5. Monitor and maintain

## Confidence

**Rating:** HIGH
**Rationale:** HIGH for the principles/methodology. This is Kindervag's original ZT framework, refined by ON2IT (the company Aaron represents in the narrative). It's been field-tested across hundreds of implementations. The Kipling Method (Who/What/When/Where/Why/How) is a genuine innovation — it replaces "source IP, destination IP, port" firewall thinking with business-context policy thinking.

## Stakes

If the methodology is too abstract (nine steps sound simple but each contains hidden complexity), organizations will abandon it. The narrative addresses this by showing the team discovering real problems (stale firewall rules, missing outbound restrictions) within hours of starting — demonstrating that even a "learning" protect surface produces immediate value.

## Disagreement

**Who disagrees:**

_None identified._

**Alternative reading:**

_None identified._

## Edges

**Depends on:**

**Supports:**
- [[nist-sp-800-207-provides-the-architectural-tenets-but|Repeatability of the methodology is evidence that Kindervag provides actionable strategy.]]

**Contradicts:**

**Challenged by:**

**Operationalizes:**

**Extends:**

## Assessment

The four design principles are excellent — they're memorable, correctly ordered (business outcomes first), and cover the essential shift from perimeter to protect surface thinking. The five-step methodology is pragmatic but undersells the difficulty of steps 2 (mapping transaction flows) and 4 (creating policies) at scale. The Kipling Method is the most valuable practical tool in these chapters — it's a template security teams can literally put on a whiteboard. The claim that "anyone can remember nine things" is clever marketing but the real value is having a repeatable process, not memorability.
