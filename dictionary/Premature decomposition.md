---
description: Splitting work into parts before understanding how the parts relate. Each part passes alone; together they are wrong.
origin: coined
---

Splitting work into parts before understanding how the parts relate. Each part is then wrong in a different way, and nobody sees it, because each piece looks fine in isolation. The symptom arrives at integration: four agents report success, and the merged result does not work.

The scout-spec-build pipeline assumes exploration and implementation separate cleanly. They do not. The right shape emerges during implementation, and boundaries drawn before that point lock in the wrong ones.

| Stage         | What goes wrong                                   |
| ------------- | ------------------------------------------------- |
| Decomposition | Boundaries drawn without knowing the connections  |
| Specification | Each part specified apart from the others         |
| Execution     | Each executor discovers its spec was wrong        |
| Integration   | Locally correct pieces, globally incoherent whole |

Each handoff multiplies the error. Agent A passes flawed output to Agent B, who treats it as valid and builds on it; the failure lives between agents, and debugging it means forensic reconstruction across fragmented histories. This is the mechanism of [compounding error](./Compounding%20error.md), and decomposition is what switches it on. Overstory's author [documented](https://github.com/jayminwest/overstory/blob/main/STEELMAN.md) a 20-agent swarm spending $60 on work a single sequential agent finished for $9: one data point, not a law, written by the tool's own author before deployment.

Planning stays. The argument is against committing to boundaries you have not earned. [Specification debt](./Specification%20debt.md) looks like the opposite advice, since it says specify more, but the two concern different things. Specification debt is about intent: you never said what right looks like. Premature decomposition is about structure: you divided the work before you understood it. Specify intent thoroughly and leave the decomposition flexible.

The pattern recurs wherever work is divided before it is understood. Microservices before domain boundaries produce a distributed monolith. Org charts redrawn before workflow mapping produce structure that fights the work. Sprints estimated before a spike produce scope surprises that cascade.

The alternative is [structured autonomy](./Structured%20autonomy.md): set boundaries, provide tools, establish feedback, and let the actor decompose based on what it finds. The decomposition emerges from the work.

_Usage:_

"I split the feature across five agents by layer. Every one passed its tests and the feature doesn't work."

"You decomposed by layer before anyone knew how the layers talk. That is premature decomposition. One agent should have built the tracer bullet first; then you split what it found."
