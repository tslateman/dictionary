---
description: The written record of why: decisions, rejected alternatives, and patterns kept outside any session so the next one inherits them.
origin: project
---

The written record of why: the decisions a project made, the alternatives it rejected, and the patterns it learned, kept outside any one session so the next session inherits them. A changelog records what changed; lore records the judgment behind the change, structured so an agent can read it at the start of work without a person re-explaining it.

Three records answer three questions:

| Record      | Question it answers                 | Who reads it well                |
| ----------- | ----------------------------------- | -------------------------------- |
| Changelog   | What shipped, in which version?     | Users, release managers          |
| Git history | What changed, when, by whom?        | A person tracing a regression    |
| Lore        | Why this, and what did we rule out? | The next session, human or agent |

The first two are byproducts of the work. Lore is a deliberate act: someone decides an outcome is worth carrying forward and writes it down with its reasoning. "We tried Jaccard dedup and it worked." "Don't mock the database; here is why." A commit message can hold that, but an agent cannot extract judgment from four thousand commits at session start. Lore pre-structures it for machine consumption — [information architecture](./Information%20architecture.md) with an agent for a reader. For a solo developer with good commit hygiene and a `decisions/` folder, lore adds little; for parallel agents that need pre-structured judgment, it earns its keep.

One writer, curated. Capture is cheap and judgment is scarce, so the record grows through a single curation pass, never through parallel agents each appending what they think mattered. Reads are safe and fail silent; writes need a librarian.

A record nobody reads at decision time is [write-only memory](./Write-only%20memory.md). Count the read paths against the write paths, and make sure something fires when the next session begins, which is [just-in-time information retrieval](./Just-in-time%20information%20retrieval%20%28JITIR%29.md).

Our implementation is the `lore` tool: `lore resume` loads the record into a session, `lore capture` records a decision or pattern, `lore handoff` snapshots state for the next session. A failure that recurs three times surfaces as a pattern, and the pattern reaches every session that follows.

_Usage:_

"The agent rewrote the dedup to use embeddings. We tried that in March and it was slower."

"That decision lives in a Slack thread. Put it in lore with the benchmark, and the next session starts knowing it."
