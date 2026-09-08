---
description: Guards for states the contract already rules out; they convert bugs into silent wrong answers and read as safety.
origin: coined
---

Defensive code that guards against states the contract already rules out: a null check on a value the caller guarantees, a blanket `try/except` around a call whose failures the handler cannot fix, a fallback default for a key that must be present, a cast that coerces a wrong type into a plausible one. Each converts a bug into a silent wrong answer. The exception that would have named the fault at the line it occurred is caught, and the program continues with a value nobody chose.

The symptom is the run that finished clean and is wrong. A missing config key became an empty string, became a request to the wrong host, became a 404 the except block logged at debug level. Four layers of defense, and the failure surfaced two days later in a dashboard, far from any line that caused it.

| Form                        | What it hides                        |
| --------------------------- | ------------------------------------ |
| Guard for an excluded state | A caller violating the contract      |
| Blanket try/except          | Every failure the handler cannot fix |
| Fallback default            | A missing or malformed input         |
| Lazy cast                   | A type mismatch upstream             |

Agents produce this by default. A guard never fails a test; a raised exception might. Asked to make the suite green, the model wraps the call, returns `None`, and the suite is green. The test now passes over a swallowed exception, and the green run is a [proxy](./Proxy%20signal.md): the signal says done and the work is undone. [Prove it works](./Prove%20it%20works.md) by reading the output the run produced, not the color of the run.

The practice: let exceptions raise. The caller that can handle the error sits higher in the stack, and a guard at the wrong level denies it the chance. Fail loud and early. Where a guard seems necessary, ask what the contract says. If the contract already excludes the state, the guard is dead; delete it. If the contract does not exclude the state, tighten the contract or handle the case with a branch that does something, not a default that hides it.

_Usage:_

"The pipeline finished green but half the rows are blank."

"Find the try/except that swallowed the parse error. That's dead defensiveness: it turned a crash into a wrong answer."
