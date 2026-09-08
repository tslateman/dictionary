---
description: A system with rich write paths and no read paths; records accumulate and nothing consults them at decision time.
origin: borrowed
---

A system with rich write paths and no read paths. More `record_*` functions than `query_*`; schemas nothing consults at decision time; logs nobody opens; memory nobody recalls. The name is the old hardware joke — a [write-only memory](https://en.wikipedia.org/wiki/Write-only_memory_%28joke%29) is a part you can store to and never read, absurd by construction — applied to systems where the absurdity shipped. The writes run on every event, the reads were never wired, so the store grows and the decisions it exists to inform are made without it.

The symptom: the team keeps recording, and the recorded facts never change a decision. A hook stores every session's outcome; the next session starts from scratch. A registry holds every project's interfaces; the plan that needed them was written from memory. Metrics ship to a dashboard nobody opens between incidents, and during the incident the dashboard lacks the one series that mattered. Each write felt like progress when it was added, because writing is visible work with a visible artifact. Reading happens later, in someone else's session, under time pressure, when the store is the last place anyone thinks to look.

Diagnostic: count writers versus readers. List the functions, hooks, and jobs that put facts into the store, then the code paths that pull facts out at a moment of choice. If the read side is unwired, the writes are ceremony, and the richness of the schema measures effort spent on the wrong half. A second test: name the last decision the store changed. If the answer is a date, the system reads. If the answer is a hope, it does not.

Remedy: build the read side first, or to the same standard as the write side. Decide which decision the store serves and wire that consumer before adding the next writer. [Just-in-time information retrieval](./Just-in-time%20information%20retrieval%20%28JITIR%29.md) is the shape of a wired read: the lookup happens at the boundary where the decision is made, not in a report someone might open later. [Lore](./Lore.md) is resumed at session start for this reason; a written record no session reads is a write-only store with good prose. [Guard the context window](./Guard%20the%20context%20window.md) governs the read side too: a read path that dumps the whole store into context is the same failure reversed — everything loaded, nothing used.

_Usage:_

"We've got three months of session telemetry in that table."

"And which decision did it change? Count the readers. If it's zero, that's write-only memory — record everything, query nothing."
