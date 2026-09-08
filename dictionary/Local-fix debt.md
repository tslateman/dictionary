---
description: The minimal edit that silences the checker without fixing the design.
origin: coined
---

The minimal edit that silences the checker without fixing the design. An agent hits a borrow-checker error. It can restructure the ownership, or it can add `.clone()`. Both make the error disappear; one addresses why the error existed. The agent optimizes for the signal it can see, and a green build is satisfied by either edit, so it takes the cheaper one, every time, in every file. This is the [tactical tornado](./Tactical%20tornado.md) working one diff at a time.

Every language offers its own spelling:

| Language   | The silencer                               | What it hides                           |
| ---------- | ------------------------------------------ | --------------------------------------- |
| Rust       | `.clone()` to satisfy the borrow checker   | Ownership fighting the data flow        |
| Python     | `try/except: pass`, `# type: ignore`       | The error, and where it came from       |
| Go         | `_ = err`, `strings.Contains(err.Error())` | A package with no error contract        |
| TypeScript | `as any`, `!`, `@ts-ignore`                | The runtime value the type lied about   |
| Shell      | `2>/dev/null`, `\|\| true`                 | Whether the script ran at all           |
| Tests      | Assert on whatever came out                | That the suite can still detect a break |

Each silencer is a one-line edit, needs no understanding of the surrounding module, and turns the build green. The restructure needs the whole module held in mind. An agent patching locally has no reason to prefer the expensive fix and no way to see that it is needed.

The debt is invisible to the tools that catch bad code. The compiler passes, by definition. Linters flag a fraction — a redundant clone, a discarded error — and cannot judge whether a suppression was warranted, because that judgment needs the specific failure that was expected. Review catches it only when the reviewer reads for design rather than diff, and a reviewer facing thousands of generated lines reads for diff. Green is a [proxy](./Proxy%20signal.md) for design; each edit looks correct on its own, and the drift is [compounding error](./Compounding%20error.md) at the scale of a line.

Remedy: read the suppression, not the error it hides. The checker passing is the floor of review, never its verdict. Every suppression names the failure it suppresses — `except KeyError` is engineering, `except Exception` is a wish, and a failure nobody can name is a finding. Repeated silencers are one design finding: five clones of the same field point at one struct's ownership, twelve mocks of one collaborator at one untestable seam. [Dead defensiveness](./Dead%20defensiveness.md) is the same debt in the shape of a guard.

_Usage:_

"Clippy is clean and the tests pass. What's the objection?"

"Fourteen clones of the same config struct. That's local-fix debt — one ownership problem paid off fourteen times, and the build never noticed."
