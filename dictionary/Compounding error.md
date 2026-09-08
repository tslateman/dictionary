---
description: Drift in meaning across a chain of handoffs. Every step looks locally correct and the aggregate misses the intent.
origin: coined
---

Semantic drift across a chain of handoffs, where each step is locally correct and the aggregate misses the intent. No single actor fails; the failure lives between actors. It differs from two failures existing tooling already catches:

| Type              | Mechanism                         | Concerns     | Detection          |
| ----------------- | --------------------------------- | ------------ | ------------------ |
| Cascading failure | A dependency chain breaks         | Availability | Monitoring, alerts |
| Error propagation | Bad data flows through a pipeline | Data         | Validation         |
| Compounding error | Meaning drifts at each handoff    | Meaning      | Integration review |

The arithmetic understates it. Three agents at a 5% individual error rate give a 14.3% aggregate failure probability (1 − 0.95³), and that model assumes independent failures. Agents fail dependently: each accepts flawed peer output as valid input and builds on it, so errors reinforce rather than accumulate.

The symptom: a swarm merges cleanly and the codebase now has three date-parsing utilities, two naming schemes, and a disagreement about which layer owns retries. Every output passed its local checks. Semantic merge conflicts are worse than textual ones because no tool flags them. [DORA's 2025 report](https://dora.dev/research/2025/dora-report/) found AI adoption correlating with higher throughput and lower stability: each change passes CI alone, and the interactions introduce bugs no single test covers. Maintainers see the same shape in AI-generated pull requests — each plausible in isolation, the aggregate eroding coherence, evaluation cost transferred to whoever still understands the invariants. Organizations had it first: requirements pass from PM to designer to engineer to QA, each translation reasonable, the product wrong.

[Premature decomposition](./Premature%20decomposition.md) sets it up: work split before the invariants were named leaves each worker to invent their own. Compounding error is autonomy without feedback, and [structured autonomy](./Structured%20autonomy.md) is the antidote. Three mechanisms reduce it:

1. Integration checkpoints. Review the aggregate, not only the parts. The merge button exists because someone has to hold the whole picture.
2. Shared invariants. Actors that reference one specification have a correction signal for drift. Without one, each actor invents its own.
3. Early feedback. CI catches textual conflicts and review catches semantic ones; the sooner drift is seen, the less it compounds.

_Usage:_

"Every one of the six PRs reviewed fine. Merged together, the checkout flow charges tax twice."

"Compounding error. Nothing in any one PR was wrong — two agents each added tax because neither saw the other's. Review the merged whole, not six diffs."
