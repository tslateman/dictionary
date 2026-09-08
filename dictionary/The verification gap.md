---
description: The distance between "the agents ran" and "the work satisfies the requirement". Execution tooling is commodity; verification is not.
origin: coined
---

The distance between "the agents did work" and "the work satisfies the requirement". Every agent orchestrator of the 2025–2026 wave solved the same problem: run many agents in parallel without file conflicts. Worktrees for isolation, SQLite for messaging, tmux for processes, hooks for access control. That pattern is now a commodity. None of them confirm the agents built the right thing.

The symptom is a dashboard of twenty healthy agents, every worktree clean, every merge green, and a feature that does not do what the ticket asked. Nobody noticed, because every signal the tooling emits reports process health, and it emits no signal for requirement status.

| Dimension | Execution infrastructure          | Verification infrastructure                    |
| --------- | --------------------------------- | ---------------------------------------------- |
| Asks      | Did the agents run?               | Did the agents satisfy the requirement?        |
| Feedback  | Watchdog, heartbeat, merge status | Requirement status: passing, failing, untested |
| Detects   | Crash, timeout, conflict          | Wrong thing shipped                            |
| Maturity  | Commodity                         | Research-grade                                 |

Speed is visible and correctness is not, so execution tooling leads and verification tooling follows. Continuous deployment shipped faster before continuous testing caught up; microservices shipped before distributed tracing made them observable. Failures accumulate in the interval. A green check in that interval is a [proxy](./Proxy%20signal.md): it reports that the pipeline ran, and the pipeline checked what the developer remembered to test, not what the spec demanded. The gap is [specification debt](./Specification%20debt.md) made architectural.

The gap separates open-loop systems from closed-loop ones. An open loop writes a spec, dispatches agents, merges code, and hopes. A closed loop dispatches agents, runs verification against the spec, computes requirement status, and turns unmet requirements into new tasks. Closing it takes three things: a traceable link from each requirement to the test that proves it; status computed from the test result, with no agent judgment involved; and failing requirements becoming tasks without a human relaying them. That feedback is the third component of [structured autonomy](./Structured%20autonomy.md), and the one the orchestrators left to humans.

The merge gate then moves from "a reviewer agent approved" to "every linked test passes". Review still catches coherence and intent; the tests catch every assertion the reviewer will not re-run. Neither replaces the other. Both are how you [prove it works](./Prove%20it%20works.md) at the scale of a swarm.

_Usage:_

"All twelve agents finished green and the merge went through. Why does the login flow still reject valid tokens?"

"Green tells you the agents ran. Nothing in that pipeline checked the token requirement — you're standing in the verification gap. Link the requirement to a test and let the test decide."
