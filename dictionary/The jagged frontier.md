---
description: AI capability is uneven across tasks, and the boundary between what a model handles and what it botches follows no predictable line.
origin: borrowed
---

The uneven boundary of AI capability: models handle some tasks well and fail at adjacent ones, and no clean line separates the two. The term comes from the 2023 Harvard Business School / BCG working paper [Navigating the Jagged Technological Frontier](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321) (Dell'Acqua et al.), which measured consultants on tasks just inside and just outside the boundary; [Ethan Mollick](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged) popularized it. The frontier runs differently through every domain, and every model release moves it.

The symptom: the agent that refactored an auth module without a slip hallucinates a database migration, or the one that solved the hard algorithmic problem botches a config file. The failure surprises because difficulty predicted the wrong place.

| Assumption                     | Reality                                                             |
| ------------------------------ | ------------------------------------------------------------------- |
| AI handles the routine tasks   | Some routine tasks fail; some complex tasks succeed                 |
| Difficulty predicts capability | Easy tasks fail and hard tasks work, with no line between           |
| Capability improves uniformly  | Each model version shifts the frontier somewhere new                |
| One evaluation generalises     | Benchmark performance does not predict performance on your codebase |

Two strategies fail against it. "Let the agent handle everything below this line" assumes the line exists; delegation by perceived difficulty produces failures at random. "We tested it and it works" assumes the frontier holds still; it shifts between model versions, prompting strategies, and codebases, so evaluation is continuous rather than one-time.

The remedy is empirical boundaries. Map your own frontier — which tasks succeed in this codebase, which fail — because benchmarks and other teams answer a different question. Design boundaries for adjustment rather than as permanent capability lines; [structured autonomy](./Structured%20autonomy.md) depends on redrawing them as the frontier moves. Spend review at the edge: failures cluster at the frontier, not deep in either territory, and when agents chain outputs a jagged failure becomes [compounding error](./Compounding%20error.md).

Delegate where a failure is cheap and reviewable; keep control where a failure is expensive to reverse. Developers who lean on agents for generation and keep deployment by hand are reading the frontier correctly.

_Usage:_

"It rewrote the whole auth module without a mistake, then wrote a cron expression that fires every minute instead of every day."

"Jagged frontier. Difficulty doesn't tell you where it fails — the boundary is wherever it is. Add cron expressions to the list of things you check by hand."
