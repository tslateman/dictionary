---
description: Concurrent writers get their own file, key, or branch before anyone reaches for a lock.
origin: coined
---

The rule that, when concurrent actors might write the same file, branch, key, or object, the first question is whether they need the same mutable thing at all. Usually they are publishing independent facts, and the remedy is to give each its own target and merge at the read boundary. Two workers writing their own field into one `state.json` still share mutable state; `indexer-state.json` beside `metrics-state.json` does not.

The failure it prevents arrives in two forms. Two agents append to a shared notes file and the second write erases the first. Or a lock is added, works, and now every writer waits on the slowest, and the run that took four minutes in parallel takes eleven. The lock treated a design problem as a scheduling problem.

| Option                          | When it fits                                                     |
| ------------------------------- | ---------------------------------------------------------------- |
| Separate targets, merge on read | Writers publish independent facts. The default.                  |
| Sequential phases               | Later writes depend on earlier ones; order them structurally.    |
| Single-writer actor             | One shared target is a real invariant; funnel writes through it. |
| Lockfile or compare-and-swap    | The target must be shared and the writers must run concurrently. |

Serialize only when one shared write target is a real invariant, and then serialize structurally. Treat "we need a lock" as a design smell worth checking before accepting.

Instructions are not concurrency control. Telling agents to take turns does not make them take turns. An agent told to "wait until the other agent finishes" has no way to observe the other agent and proceeds when its own reasoning says the time has come. The constraint has to live where the agent cannot reason past it, which is the filesystem layout or the process model, not the prompt. This is [structured autonomy](./Structured%20autonomy.md) applied to writes.

A concrete case: three agents each collecting findings. Wrong: all three edit `findings.md`. Right: `findings/debts.md`, `findings/gaps.md`, `findings/disciplines.md`, and the lead concatenates when the three return.

_Usage:_

"Two of the agents both wrote to progress.json and one overwrote the other. I'll add a lock."

"Do they need the same file? Give each its own state file and merge when you read. Separate before serializing."
