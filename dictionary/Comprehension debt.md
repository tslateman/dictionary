---
description: Code that ships without anyone holding a mental model of it; the gap between what was generated and what anyone understands.
origin: borrowed
---

Code that ships without anyone holding a mental model of it. The debt is the gap between what was generated and what anyone on the team understands, and it accrues one accepted diff at a time.

Michael Bolton named the mechanism in [To the Developer: About Your Impending "Promotion"](https://developsense.com/blog/2023/11/to-the-developer-about-your-impending-promotion): the developer who adopts an LLM is promoted, without a raise, from author of their own code to reviewer and maintenance programmer for a prolific, barely competent colleague. Authorship builds a model of the code as a side effect; every line written is a line understood. Review builds no such model unless the reviewer does that work deliberately, and the volume works against them. An agent produces a thousand lines in the time a reviewer reads a hundred, and [the verification gap](./The%20verification%20gap.md) is the space between those rates. The lines that pass through unread still ship.

The symptom arrives later. A bug report lands on a module and nobody can say how the module works. The person who accepted the diff remembers accepting it and little else. The agent that wrote it holds nothing at all; the session ended. Onboarding a colleague means pointing them at code nobody can explain, and the next change is made by another agent from the same position, which is how the debt compounds: the second generation extends code the first generation understood no better, and the wake it leaves is [local-fix debt](./Local-fix%20debt.md).

Two remedies, both cheap next to the debt. A comprehension gate before commit: the author explains the change in their own words — what it does, why this shape, what it touches — and a change they cannot explain does not merge; an author who cannot is a [meat proxy](./Meat%20proxy.md) for the agent. Reading the diff, not the summary: the agent's account of its work is a [proxy](./Proxy%20signal.md) for the work, written by the party least placed to report its own gaps. [Prove it works](./Prove%20it%20works.md) applies to understanding as much as to behavior: the artifact is the code, and the summary is a report about it.

_Usage:_

"The auth module's broken, Sam's the only one who has touched it, and Sam says the agent wrote it."

"Comprehension debt. Nobody ever held a model of that module — it went from generator to merge with a skim in between. Read it now, before the next agent extends it."
