---
description: A document one session writes for another to read; the carry for state the stateless model would otherwise lose.
origin: borrowed
---

A document one session writes so that another can pick up its work. Plans, specs, tickets, and progress notes are all handoff artifacts. The term comes from Matt Pocock's [Dictionary of AI Coding](https://github.com/mattpocock/dictionary-of-ai-coding).

Each session begins empty. Whatever the previous session decided, ruled out, or left half-done exists only in its context, and the context ends with the session. The filesystem outlives it. Writing the state to a file moves it across the boundary. Compaction is the in-memory alternative; the file is the version you can read and correct before anything depends on it, and the version five parallel sessions can share.

A good one holds absolute paths, decisions with their reasons, what is done, what remains, and what was tried and rejected. It is written for a reader with nothing in context, and it says so at the top.

Our practice adds two rules.

The artifact records what the writing session believed. The reading session treats those beliefs as claims and verifies them against the code before building on them; [prove it works](./Prove%20it%20works.md) applies to inherited state as much as to fresh work. "Tests pass" in a plan file means tests passed for a session that may have run a subset, on a tree that has since changed. Run them. "Auth refactor complete" means the writer stopped; read the diff to learn where.

Durable decisions leave the artifact. A plan file is scoped to a task and goes stale when the task ends; a decision about how the project handles migrations does not. Promote those into [Lore](./Lore.md), where the next session's resume finds them, rather than leaving them in a plan file nobody reopens. The artifact carries state across one boundary. Lore carries it across all of them.

_Usage:_

"The plan says the auth refactor is finished, so I'll start on the API."

"The plan says the previous session believed it was finished. Run the suite and read the diff before you build on it."

"Where does the decision about the retry policy go? It's in the plan."

"Out of the plan and into Lore. The plan dies with the task; the decision doesn't."
