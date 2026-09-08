---
description: The accumulated cost of never saying what right looks like.
origin: coined
---

The accumulated cost of never saying what right looks like. Technical debt is "we built it wrong"; specification debt is "we never defined what right means." Both compound. Specification debt compounds faster, because every downstream decision inherits the ambiguity, and the code that results looks finished.

| Dimension        | Technical debt            | Specification debt              |
| ---------------- | ------------------------- | ------------------------------- |
| What is missing  | Quality in implementation | Clarity in intent               |
| Who pays         | The next developer        | Everyone who touches the system |
| Visible when     | Review, bugs, slowdown    | Wrong feature, rework, argument |
| Agent multiplier | Ships bad code faster     | Ships the wrong thing faster    |

The debt accrues from four sources. "The code is the spec": the codebase becomes the only record of intent, so a newcomer or an agent can see what the system does and not what it should do. Verbal agreements: requirements settled in a meeting and remembered differently by each participant. Implicit standards: "we all know how this works," until the person who knew leaves or an agent generates the next module. Spec-free tickets: "add pagination to the API" — which endpoint, what page size, cursor or offset? Whoever implements it decides, and the decision becomes the spec by default.

Agents make the debt expensive. Execution is cheap now; ten features ship in the time one used to. When the specification was wrong, ten wrong features ship instead of one. The symptom is a team arguing after the merge about what the feature was supposed to do, with working code on both sides of the argument. [The intent inversion](./The%20intent%20inversion.md) moved the cost from building to deciding what to build; specification debt is that cost, unpaid. [The verification gap](./The%20verification%20gap.md) is the same debt made architectural: nothing can check the work against a requirement nobody wrote down.

Remedy: treat specification as a skill rather than overhead. Write what right looks like before dispatching the work, in a form a test can check, and gate implementation on it. A written specification is a boundary, and boundaries are what make [structured autonomy](./Structured%20autonomy.md) possible: the agent moves freely inside them because the edges exist. The structural cousin is [premature decomposition](./Premature%20decomposition.md), where the boundaries are drawn before the intent is clear.

_Usage:_

"It built exactly what the ticket said and product rejected it."

"The ticket said 'add pagination'. Cursor or offset, page size, ordering — none of it was written down, so the agent chose. Specification debt: it built the ticket, and nobody had written the feature."
