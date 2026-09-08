---
description: Ousterhout's prolific programmer who ships features fast and leaves a wake of complexity for others to clean up.
origin: borrowed
---

The prolific programmer who ships features fast and leaves a wake of complexity for others to clean up. John Ousterhout names the figure in [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php). The tactical tornado works in tactical mode, every decision made to finish the current task soonest, and management sees a hero, because features appear at a rate nobody else matches. The engineers who inherit the code keep the other ledger. Each shortcut cost the tornado nothing and costs the next person hours, and the sum of those hours exceeds the time the tornado saved.

Ousterhout's contrast is strategic programming: investing a fraction of each task in the design, on the expectation that the codebase will be edited many more times than it is written. The tactical programmer optimizes the edit in front of them; the strategic programmer optimizes the edits to come.

An agent optimizing for the green check in front of it is a tactical tornado by construction. The harness rewards a passing build, a clean lint run, a closed task, and each of those is satisfied by the shortcut as readily as by the restructure. The agent holds no memory of the last time the shortcut cost someone; that session ended. It holds no picture of the module as a whole unless the picture is in context. So it takes the shortcut, and the wake it leaves is [local-fix debt](./Local-fix%20debt.md): the clone, the suppression, the swallowed error, each a one-line edit that makes the complaint stop. Facundo Olano [drew the line](https://olano.dev/blog/tactical-tornado/) from Ousterhout's figure to coding agents directly: they work diff by diff and never hold the system in view.

The symptom is a project that felt fast for a month and then stalled, every change now touching code nobody wants to touch.

Remedy: make the strategic cost visible where the agent and the reviewer can see it. Review reads for design rather than diff. The harness adds checks the shortcut fails: a strict lint set that flags the suppression, a review pass that buckets each hit as fine, mechanical fix, or design restructure, with the third bucket reserved for a human. Standing instructions rule out the dialect of shortcut the language offers. Without those, green is a [proxy](./Proxy%20signal.md) for done, and the tornado is the rational response to it.

_Usage:_

"Forty commits this week from the agent branch, and velocity has never looked better."

"Read one of them. It's a tactical tornado — every commit ships, and every commit leaves a clone or a swallowed error for the next commit to work around."
