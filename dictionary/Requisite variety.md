---
description: Ashby's law. A controller needs at least as much variety as what it controls, or the system finds states it cannot handle.
origin: borrowed
---

A controller needs at least as much variety as the system it controls; fall short and the system finds states the controller cannot handle. W. Ross Ashby stated the law in [An Introduction to Cybernetics](http://pespmc1.vub.ac.be/books/IntroCyb.pdf) (1956): only variety can absorb variety. A thermostat regulates a room because its two states, on and off, match the room's two conditions, too cold and warm enough. A system with more states than its regulator will reach an unregulated state.

| System variety | Controller variety | Outcome                                    |
| -------------- | ------------------ | ------------------------------------------ |
| Low            | Low                | Simple control works                       |
| High           | Low                | Controller overwhelmed; unregulated states |
| High           | High               | Effective regulation                       |

Applied to agents: the agent's output space has enormous variety. A reviewer, harness, or test suite with less variety than that space will pass states it cannot evaluate. An automated check has exactly the variety that was encoded: lint rules, type checks, test assertions. A codebase has far more: edge cases, architectural invariants, undocumented assumptions, user expectations. The gap between encoded variety and actual variety is where the bugs the checks passed live. This is why the merge button stays with a person who understands the system, and why [structured autonomy](./Structured%20autonomy.md) places that person at the integration point.

Ashby wrote the law as a prescription, and it is usually quoted as a caution. The most-cited PDF drops the "only," and the first clause gets severed, leaving "variety can destroy variety" to read as a warning that complexity begets complexity. Restored, the point is directional: build up the regulator. The reviewer, the harness, and the suite are the things to invest variety in, and the fix for a check that passes bad states is more variety in the check, never less variety in the agent.

Two more consequences. A planner decomposing work before implementation holds only an abstraction's variety, while the implementer accumulates the problem's actual variety through contact; [premature decomposition](./Premature%20decomposition.md) is low-variety planning applied to a high-variety problem. And variety is domain-specific, so a model's variety in one domain says little about the adjacent one; [the jagged frontier](./The%20jagged%20frontier.md) is Ashby applied to capability.

_Usage:_

"CI is green on every agent PR, and production keeps breaking in ways the tests never mention."

"The suite has less variety than the agent's output, so it passes what it can't see. Add the invariants it's missing, and keep a reviewer with requisite variety on the merge."
