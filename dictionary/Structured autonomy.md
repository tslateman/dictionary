---
description: Controlling an agent through its environment, boundaries, tools, and feedback, then letting it decide how to do the work.
origin: coined
---

Controlling an agent by controlling its environment rather than its actions: set boundaries, provide tools, establish feedback, then let the actor decide how to do the work. Prescribe every step and each handoff compounds the specification error; prescribe nothing and the work drifts. Structured autonomy sits between the two, and it is the position that scales.

| Dimension     | Prescribed decomposition             | Structured autonomy                    |
| ------------- | ------------------------------------ | -------------------------------------- |
| Who decides   | Planner, before work starts          | Actor, during work                     |
| Failure mode  | Wrong decomposition propagates       | Wrong boundaries constrain too much    |
| Scales by     | More planning, more planners         | Better boundaries, fewer interventions |
| Feedback      | Late, after every step completes     | Continuous; actor adjusts mid-task     |
| Cost of error | Rework cascades through the pipeline | Actor self-corrects within bounds      |

Three components carry the structure. Boundaries: ownership, permissions, quality gates, scope. Tools: the actor's interface for inspecting and acting within those boundaries. Feedback: how the actor and the system learn whether the approach is working. Remove boundaries and you get chaos; remove tools, helplessness; remove feedback, drift.

The merge button is the feedback component. A reviewer with [requisite variety](./Requisite%20variety.md) catches what automated checks cannot encode, so structured autonomy concentrates human judgment at integration points instead of spreading it across every step. The pattern predates agents: Torvalds shifted from contributor to reviewer as Linux scaled, building subsystem maintainers and merge gates rather than prescribing how patches decompose. Contributors self-direct inside that structure.

The same shape appears at the inference level. Give a model a REPL and a handle to its input instead of loading everything into context, and it inspects, filters, and recurses on its own; the REPL is the boundary, the recursion is the autonomy. It appears again in the rule to [separate before serializing](./Separate%20before%20serializing.md): give each worker its own file or branch, and the boundary does the coordination a lock would otherwise have to.

_Usage:_

"I wrote a twelve-step plan for the agent. It went wrong at step four, then built eight more steps on that foundation."

"Swap the twelve steps for a boundary and a check: it owns this directory, the suite must pass, and you review the merge. Structured autonomy lets it find the decomposition itself."
