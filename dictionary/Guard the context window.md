---
description: Every token entering a session must earn its place, because context is finite and, within a session, unrecoverable.
origin: coined
---

The rule that every token entering a session must earn its place. Context is finite and, within a session, unrecoverable: a file dumped into the thread at turn three is still there at turn forty, crowding the instruction it was meant to serve, and no later turn can take it back.

The symptom is an agent sharp for the first task and sloppy by the third. Nothing changed in the model or the prompt. The window filled with output nobody re-read, and the attention that should hold the current instruction is spread across a build log, two whole-file reads, and a screenshot. A related shape: the agent asked to fix one function reads the whole module, then forgets which function. The instruction was in context. It was outnumbered.

Four practices follow.

Route bulk to subagents. Verbose command output, long files, and screenshots belong in an agent's context; the main thread keeps the summary. The subagent's window is spent and discarded, and the main thread pays only for the conclusion.

Read selectively. A file you will not use costs the same as one you will. Read the function, not the module; the failing test, not the suite.

Size phases and cap fan-out before launching. Five parallel agents each returning two thousand words is ten thousand words in the thread. Decide the return budget before the fan-out, and ask each agent for a conclusion, not a transcript.

Put content used on every invocation inline. A rule read on every turn belongs where it is read once, not in a separate file that costs a read each time.

When a task outgrows one window, stop rather than push through. Write a [handoff artifact](./Handoff%20artifact.md) at a natural boundary and let a fresh session take the next phase with the sharpest part of its window.

_Usage:_

"It nailed the first refactor and by the third it was inventing function names."

"Look at what's in the thread. Three whole-file reads and a full test log. Guard the context window: send those to a subagent and keep the summary."
