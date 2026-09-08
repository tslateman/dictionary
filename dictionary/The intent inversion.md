---
description: Implementation used to be the expensive half of software and intent the cheap half. AI swapped them, and most budgets have not caught up.
origin: coined
---

The swap AI made in the cost of software: implementation, once the expensive half, is now cheap, and intent, once cheap, is now the scarce input. For decades a product manager wrote a ticket in ten minutes and an engineer spent two weeks building it, so the industry optimized the build — agile, CI/CD, microservices, DevOps. A developer with an agent now builds in hours what took weeks. Nothing made ambiguous requirements clear, surfaced the invariants the ticket omitted, or learned what "right" looks like in a given system. That work costs what it always did, and most organizations still plan as if the build were the expensive part.

The symptom is review under water. More PRs arrive faster, from the same vague specs and the same implicit assumptions. Speeding review up processes the same ambiguity faster. Reducing the load on it — clearer specification, tighter ownership so the reviewer knows the invariants of the code they review — is the fix. A model can generate the wrong thing perfectly: flawless code from an ambiguous ticket is still the wrong feature, delivered sooner and with fewer syntax errors. "Models will improve" is true and beside the point, because better generation does nothing for [specification debt](./Specification%20debt.md).

Two kinds of verification get conflated, and the confusion is expensive:

| Kind      | Question                                                     | Scales with                          |
| --------- | ------------------------------------------------------------ | ------------------------------------ |
| Component | Does this unit work?                                         | Automation: tests, types, lint, CI   |
| System    | Does this change, with everything else, keep the invariants? | A person who holds the whole picture |

Component verification is largely solved and models keep getting better at it. System verification resists automation because the variety of the system exceeds what any predefined check encodes — [requisite variety](./Requisite%20variety.md) applied to integration. No check catches a semantic merge conflict, architectural drift, or ten individually correct changes that add up to an incoherent whole. The tooling shape of this is [the verification gap](./The%20verification%20gap.md).

The bet follows. Models will keep improving, so bet on what stays hard when generation is perfect: knowing what to build, and knowing whether what was built is right. Speed is table stakes. Judgment scales through structure — ownership, specification, feedback loops, the components of [structured autonomy](./Structured%20autonomy.md) — and not through heroics.

_Usage:_

"We doubled PR throughput this quarter and review is drowning. Should we put an agent on review too?"

"That's the intent inversion — building got cheap, deciding what to build didn't. A faster reviewer processes the same vague tickets faster. Fix the tickets."
