---
description: Knowledge that fires at the moment of decision, without anyone remembering to look for it.
origin: borrowed
---

Retrieval that fires at the moment of decision, without anyone remembering the record exists. The term is [Bradley Rhodes's](https://www.bradleyrhodes.com/Papers/rhodes-phd-JITIR.pdf): his Remembrance Agent watched the document under edit and pushed related notes unasked, no query issued. The seam is the point where the mistake gets made: the edit, the commit, the prompt submission. A record that surfaces there counts; a record that waits to be searched for counts only for the reader who already knows it is there.

Classify retrieval by what triggers it, not by the technology underneath:

| Mode         | Mechanism                                                                               | Recall required                     |
| ------------ | --------------------------------------------------------------------------------------- | ----------------------------------- |
| Push at seam | Failing check, pre-commit hook, PR template question, context injected on prompt submit | None                                |
| Proximity    | ADR beside the code, docstring over wiki, comment at the confusing line                 | None; the reader is already looking |
| Query        | Someone searches                                                                        | Must know it exists                 |
| Ambient      | Session-start resume, weekly review, scheduled audit                                    | None, but untargeted                |

The ranking is steep. Push and proximity work because they ask nothing of memory. Query fails silently: the person who most needs a record is the one who does not know it was written, and the archive looks healthy while nothing gets read.

Three constraints shape the push mode. Injection has a budget: three to five items, ranked. Inject everything and the reader skims, and you are back to no retrieval with worse latency. The seam must be where the mistake happens, not where it is discovered: a check at merge time beats a wiki page, and a check at edit time beats a check at merge. And the best retrieval is none: a lesson that became a default, a lint rule, or a type needs no finding.

The diagnostic for a knowledge system: count read paths against write paths. More capture verbs than query verbs means [write-only memory](./Write-only%20memory.md), a diary with good intentions. Ask what fires at decision time, how many items it injects, and whether the record sits beside the work or in a separate system someone must choose to enter. [Lore](./Lore.md) exists to be injected at session start; a [handoff artifact](./Handoff%20artifact.md) is retrieval at the seam between two sessions.

_Usage:_

"We documented that migration gotcha six months ago. Nobody read it before they hit it again."

"Nobody was going to search for it. Put the check where the mistake happens, a pre-commit hook on the migrations directory, and just-in-time retrieval does the remembering."
