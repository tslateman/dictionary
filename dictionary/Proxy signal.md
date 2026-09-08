---
description: A signal that stands in for the artifact it is meant to prove: a green check, a fresh mtime, an exit code, an agent's summary.
origin: coined
---

A signal that stands in for the artifact it is meant to prove. A build that compiles, a fresh mtime, a green check, a cached view, an agent's own summary: each reports on the work at one remove, and each can be right about everything except whether the work works.

The symptom: the summary says "tests pass", and the test command never ran — or ran in the wrong directory, or collected zero tests and exited 0. The proxy held; the artifact did not.

| Proxy                  | Artifact it stands for                       |
| ---------------------- | -------------------------------------------- |
| Agent's summary        | The diff                                     |
| Fresh mtime            | The file contents                            |
| Exit code 0            | The observed behavior                        |
| "Tests pass"           | The test output                              |
| Green check            | The requirement the check was meant to cover |
| Cached or derived view | The live value                               |

Proxies are cheap to read, which is why they get read. The artifact costs a Read, a run, or a diff, and finds the class of failure proxies hide: the work happened, and was wrong.

Delegated work is the sharpest case. An agent reports what it intended, and the report tracks the plan rather than the result; a reviewer that accepts the summary lets the agent grade its own homework. An agent that described an edit in prose instead of emitting the tool call reports the edit as done; an agent whose test run hit a permission prompt reports the tests as green. Inspect the output artifact, not the report.

The remedy is to [prove it works](./Prove%20it%20works.md): run the feature, read the value, inspect the diff. When a check fails, suspect the observation before the system — a proxy misreports in either direction. Script the check when it will run more than once; a script a reviewer can re-run beats a claim they have to trust. At the scale of tooling the same failure is [the verification gap](./The%20verification%20gap.md): orchestrators emit process-health proxies where requirement status is what was wanted.

_Usage:_

"The agent says all three migrations applied and the tests are green."

"That's its summary — a proxy signal. Show me the test output and `git diff` on the migrations folder."

"Diff shows two migration files. It wrote the third one in the transcript and never saved it."
