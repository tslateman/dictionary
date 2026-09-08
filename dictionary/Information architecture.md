---
description: The structure of the written record — names, places, indexes, pointers — arranged so the reader who needs a fact finds it.
origin: borrowed
---

The structure of the written record: what gets a file, what the file is named, where it sits, and what points to it. The term is [Richard Saul Wurman's](https://en.wikipedia.org/wiki/Information_architecture), and Rosenfeld and Morville built the discipline for the web, where the reader was a person with a browser. The discipline transfers; the reader changed. An agent starts each session blank, finds files by name and grep rather than by browsing, reads one file at a time, and pays for every token it loads — structure is a budget question as much as a findability one ([guard the context window](./Guard%20the%20context%20window.md)).

The symptom: the fact was written down, and the agent re-derived it anyway. The note existed; nothing on the agent's path pointed to it. Recorded knowledge that no read path surfaces is [write-only memory](./Write-only%20memory.md), and more writing does not fix it — the failure sits in the architecture, not the archive.

Four rules cover most of the practice:

| Rule      | For the agent reader                                                                                                                                   |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Placement | Put the fact where the work happens, so it loads when it matters — [just-in-time retrieval](./Just-in-time%20information%20retrieval%20%28JITIR%29.md) |
| Authority | One file owns each fact; the rest point to it. Copies drift; pointers hold                                                                             |
| Indexes   | A small always-read file — a CLAUDE.md, an [llms.txt](https://llmstxt.org/) — earns its tokens by routing to files read sometimes                      |
| Names     | The filename is the query interface: name the file what a reader would grep for                                                                        |

[Lore](./Lore.md) is what the record holds; information architecture is why the next session finds it. The test is the same for both: start an agent cold and count how long before it stands where the last session stood.

_Usage:_

"I documented that decision three weeks ago, and the agent just re-litigated it from scratch."

"The note exists and nothing routes to it — an information architecture problem, not a documentation one. Move it to the seam, or into the index the session always reads."
