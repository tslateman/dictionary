---
description: A task is done when the real artifact has been exercised; a build, a fresh mtime, or an agent's summary does not count.
origin: coined
---

The rule that a task is done when the real artifact has been checked, never when a [proxy](./Proxy%20signal.md) for it has reported success. Run the feature and walk the path a user would walk. Read the value the code holds rather than a cached or derived copy of it. Inspect the diff. A build that compiles, a fresh mtime, and an agent's own summary each stand in for the check, and each can be right about everything except whether the work works.

The failure it prevents is [the verification gap](./The%20verification%20gap.md): the stretch between "the agent said it passed" and "I watched it pass", where a wrong answer sits undetected. Delegated work is the sharpest case. An agent reports what it intended, and the report is the most fluent thing it produces; the code underneath may not match. Inspect the output artifact, not the account of it. A migration agent that reports "all 14 tables migrated" has produced a sentence. The proof is `\dt` against the target and a row count per table.

Two corollaries follow.

When a check fails, suspect the observation method before the system. A test that greps the wrong log, a curl against a stale port, a screenshot of the previous build: the code that watches is code too, and it breaks more often than the code it watches. Fix the eyes, then read the result again. Reverting a correct change because the check was wrong costs more than the check did.

Script the check when it will run more than once. A shell line a reviewer can re-run beats a claim they have to trust, and the second run is free. The script also outlives the session: the next agent inherits a command instead of a memory of what passed, and the [handoff artifact](./Handoff%20artifact.md) can point at it instead of asserting the result.

_Usage:_

"The agent says the endpoint returns 200 now."

"Curl it. Its summary is a proxy; the response is the artifact."

"I re-ran the check and it went red, so the fix must have regressed."

"Look at what the check observes first. Last time it was reading the old container."
