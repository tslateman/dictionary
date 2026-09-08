<!--
  GENERATED FILE — DO NOT EDIT.
  Source: dictionary/*.md, internal/Curriculum.md, internal/README.template.md
  Regenerate: make generate
-->

# Dictionary

The vocabulary of running agents on real codebases, one term per entry.

[Matt Pocock's AI Coding Dictionary](https://github.com/mattpocock/dictionary-of-ai-coding) covers the primitives: tokens, context windows, tool calls, handoffs. This dictionary starts where that one stops. Its terms name what accumulates when agents write most of the code, where their output diverges from intent, the rules that keep it honest, and the written record that carries knowledge between sessions.

Each entry defines the term, names the symptom you have probably already hit, and says what to do. Entries link on first mention.

---

## Table of contents

<details>
<summary>Section 1 — Debts</summary>

- [Local-fix debt](#local-fix-debt)
- [Tactical tornado](#tactical-tornado)
- [Specification debt](#specification-debt)
- [Comprehension debt](#comprehension-debt)
- [Write-only memory](#write-only-memory)

</details>

<details>
<summary>Section 2 — Gaps</summary>

- [The verification gap](#the-verification-gap)
- [The intent inversion](#the-intent-inversion)
- [The jagged frontier](#the-jagged-frontier)
- [Compounding error](#compounding-error)
- [Proxy signal](#proxy-signal)
- [Meat proxy](#meat-proxy)

</details>

<details>
<summary>Section 3 — Disciplines</summary>

- [Prove it works](#prove-it-works)
- [Guard the context window](#guard-the-context-window)
- [Separate before serializing](#separate-before-serializing)
- [Dead defensiveness](#dead-defensiveness)

</details>

<details>
<summary>Section 4 — The Written Record</summary>

- [Lore](#lore)
- [Information architecture](#information-architecture)
- [Just-in-time information retrieval (JITIR)](#just-in-time-information-retrieval-jitir)
- [Handoff artifact](#handoff-artifact)

</details>

<details>
<summary>Section 5 — Teams of Agents</summary>

- [Structured autonomy](#structured-autonomy)
- [Premature decomposition](#premature-decomposition)
- [Requisite variety](#requisite-variety)

</details>

<details>
<summary>Coined here (12)</summary>

- [Compounding error](#compounding-error)
- [Dead defensiveness](#dead-defensiveness)
- [Guard the context window](#guard-the-context-window)
- [Local-fix debt](#local-fix-debt)
- [Premature decomposition](#premature-decomposition)
- [Prove it works](#prove-it-works)
- [Proxy signal](#proxy-signal)
- [Separate before serializing](#separate-before-serializing)
- [Specification debt](#specification-debt)
- [Structured autonomy](#structured-autonomy)
- [The intent inversion](#the-intent-inversion)
- [The verification gap](#the-verification-gap)

</details>

<details>
<summary>Project terms — named tools of ours (1)</summary>

- [Lore](#lore)

</details>

<details>
<summary>Borrowed — attributed in the entry (9)</summary>

- [Comprehension debt](#comprehension-debt)
- [Handoff artifact](#handoff-artifact)
- [Information architecture](#information-architecture)
- [Just-in-time information retrieval (JITIR)](#just-in-time-information-retrieval-jitir)
- [Meat proxy](#meat-proxy)
- [Requisite variety](#requisite-variety)
- [Tactical tornado](#tactical-tornado)
- [The jagged frontier](#the-jagged-frontier)
- [Write-only memory](#write-only-memory)

</details>

## Section 1 — Debts

### Local-fix debt

The minimal edit that silences the checker without fixing the design. An agent hits a borrow-checker error. It can restructure the ownership, or it can add `.clone()`. Both make the error disappear; one addresses why the error existed. The agent optimizes for the signal it can see, and a green build is satisfied by either edit, so it takes the cheaper one, every time, in every file. This is the [tactical tornado](#tactical-tornado) working one diff at a time.

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

The debt is invisible to the tools that catch bad code. The compiler passes, by definition. Linters flag a fraction — a redundant clone, a discarded error — and cannot judge whether a suppression was warranted, because that judgment needs the specific failure that was expected. Review catches it only when the reviewer reads for design rather than diff, and a reviewer facing thousands of generated lines reads for diff. Green is a [proxy](#proxy-signal) for design; each edit looks correct on its own, and the drift is [compounding error](#compounding-error) at the scale of a line.

Remedy: read the suppression, not the error it hides. The checker passing is the floor of review, never its verdict. Every suppression names the failure it suppresses — `except KeyError` is engineering, `except Exception` is a wish, and a failure nobody can name is a finding. Repeated silencers are one design finding: five clones of the same field point at one struct's ownership, twelve mocks of one collaborator at one untestable seam. [Dead defensiveness](#dead-defensiveness) is the same debt in the shape of a guard.

_Usage:_

"Clippy is clean and the tests pass. What's the objection?"

"Fourteen clones of the same config struct. That's local-fix debt — one ownership problem paid off fourteen times, and the build never noticed."

### Tactical tornado

The prolific programmer who ships features fast and leaves a wake of complexity for others to clean up. John Ousterhout names the figure in [A Philosophy of Software Design](https://web.stanford.edu/~ouster/cgi-bin/book.php). The tactical tornado works in tactical mode, every decision made to finish the current task soonest, and management sees a hero, because features appear at a rate nobody else matches. The engineers who inherit the code keep the other ledger. Each shortcut cost the tornado nothing and costs the next person hours, and the sum of those hours exceeds the time the tornado saved.

Ousterhout's contrast is strategic programming: investing a fraction of each task in the design, on the expectation that the codebase will be edited many more times than it is written. The tactical programmer optimizes the edit in front of them; the strategic programmer optimizes the edits to come.

An agent optimizing for the green check in front of it is a tactical tornado by construction. The harness rewards a passing build, a clean lint run, a closed task, and each of those is satisfied by the shortcut as readily as by the restructure. The agent holds no memory of the last time the shortcut cost someone; that session ended. It holds no picture of the module as a whole unless the picture is in context. So it takes the shortcut, and the wake it leaves is [local-fix debt](#local-fix-debt): the clone, the suppression, the swallowed error, each a one-line edit that makes the complaint stop. Facundo Olano [drew the line](https://olano.dev/blog/tactical-tornado/) from Ousterhout's figure to coding agents directly: they work diff by diff and never hold the system in view.

The symptom is a project that felt fast for a month and then stalled, every change now touching code nobody wants to touch.

Remedy: make the strategic cost visible where the agent and the reviewer can see it. Review reads for design rather than diff. The harness adds checks the shortcut fails: a strict lint set that flags the suppression, a review pass that buckets each hit as fine, mechanical fix, or design restructure, with the third bucket reserved for a human. Standing instructions rule out the dialect of shortcut the language offers. Without those, green is a [proxy](#proxy-signal) for done, and the tornado is the rational response to it.

_Usage:_

"Forty commits this week from the agent branch, and velocity has never looked better."

"Read one of them. It's a tactical tornado — every commit ships, and every commit leaves a clone or a swallowed error for the next commit to work around."

### Specification debt

The accumulated cost of never saying what right looks like. Technical debt is "we built it wrong"; specification debt is "we never defined what right means." Both compound. Specification debt compounds faster, because every downstream decision inherits the ambiguity, and the code that results looks finished.

| Dimension        | Technical debt            | Specification debt              |
| ---------------- | ------------------------- | ------------------------------- |
| What is missing  | Quality in implementation | Clarity in intent               |
| Who pays         | The next developer        | Everyone who touches the system |
| Visible when     | Review, bugs, slowdown    | Wrong feature, rework, argument |
| Agent multiplier | Ships bad code faster     | Ships the wrong thing faster    |

The debt accrues from four sources. "The code is the spec": the codebase becomes the only record of intent, so a newcomer or an agent can see what the system does and not what it should do. Verbal agreements: requirements settled in a meeting and remembered differently by each participant. Implicit standards: "we all know how this works," until the person who knew leaves or an agent generates the next module. Spec-free tickets: "add pagination to the API" — which endpoint, what page size, cursor or offset? Whoever implements it decides, and the decision becomes the spec by default.

Agents make the debt expensive. Execution is cheap now; ten features ship in the time one used to. When the specification was wrong, ten wrong features ship instead of one. The symptom is a team arguing after the merge about what the feature was supposed to do, with working code on both sides of the argument. [The intent inversion](#the-intent-inversion) moved the cost from building to deciding what to build; specification debt is that cost, unpaid. [The verification gap](#the-verification-gap) is the same debt made architectural: nothing can check the work against a requirement nobody wrote down.

Remedy: treat specification as a skill rather than overhead. Write what right looks like before dispatching the work, in a form a test can check, and gate implementation on it. A written specification is a boundary, and boundaries are what make [structured autonomy](#structured-autonomy) possible: the agent moves freely inside them because the edges exist. The structural cousin is [premature decomposition](#premature-decomposition), where the boundaries are drawn before the intent is clear.

_Usage:_

"It built exactly what the ticket said and product rejected it."

"The ticket said 'add pagination'. Cursor or offset, page size, ordering — none of it was written down, so the agent chose. Specification debt: it built the ticket, and nobody had written the feature."

### Comprehension debt

Code that ships without anyone holding a mental model of it. The debt is the gap between what was generated and what anyone on the team understands, and it accrues one accepted diff at a time.

Michael Bolton named the mechanism in [To the Developer: About Your Impending "Promotion"](https://developsense.com/blog/2023/11/to-the-developer-about-your-impending-promotion): the developer who adopts an LLM is promoted, without a raise, from author of their own code to reviewer and maintenance programmer for a prolific, barely competent colleague. Authorship builds a model of the code as a side effect; every line written is a line understood. Review builds no such model unless the reviewer does that work deliberately, and the volume works against them. An agent produces a thousand lines in the time a reviewer reads a hundred, and [the verification gap](#the-verification-gap) is the space between those rates. The lines that pass through unread still ship.

The symptom arrives later. A bug report lands on a module and nobody can say how the module works. The person who accepted the diff remembers accepting it and little else. The agent that wrote it holds nothing at all; the session ended. Onboarding a colleague means pointing them at code nobody can explain, and the next change is made by another agent from the same position, which is how the debt compounds: the second generation extends code the first generation understood no better, and the wake it leaves is [local-fix debt](#local-fix-debt).

Two remedies, both cheap next to the debt. A comprehension gate before commit: the author explains the change in their own words — what it does, why this shape, what it touches — and a change they cannot explain does not merge; an author who cannot is a [meat proxy](#meat-proxy) for the agent. Reading the diff, not the summary: the agent's account of its work is a [proxy](#proxy-signal) for the work, written by the party least placed to report its own gaps. [Prove it works](#prove-it-works) applies to understanding as much as to behavior: the artifact is the code, and the summary is a report about it.

_Usage:_

"The auth module's broken, Sam's the only one who has touched it, and Sam says the agent wrote it."

"Comprehension debt. Nobody ever held a model of that module — it went from generator to merge with a skim in between. Read it now, before the next agent extends it."

### Write-only memory

A system with rich write paths and no read paths. More `record_*` functions than `query_*`; schemas nothing consults at decision time; logs nobody opens; memory nobody recalls. The name is the old hardware joke — a [write-only memory](https://en.wikipedia.org/wiki/Write-only_memory_%28joke%29) is a part you can store to and never read, absurd by construction — applied to systems where the absurdity shipped. The writes run on every event, the reads were never wired, so the store grows and the decisions it exists to inform are made without it.

The symptom: the team keeps recording, and the recorded facts never change a decision. A hook stores every session's outcome; the next session starts from scratch. A registry holds every project's interfaces; the plan that needed them was written from memory. Metrics ship to a dashboard nobody opens between incidents, and during the incident the dashboard lacks the one series that mattered. Each write felt like progress when it was added, because writing is visible work with a visible artifact. Reading happens later, in someone else's session, under time pressure, when the store is the last place anyone thinks to look.

Diagnostic: count writers versus readers. List the functions, hooks, and jobs that put facts into the store, then the code paths that pull facts out at a moment of choice. If the read side is unwired, the writes are ceremony, and the richness of the schema measures effort spent on the wrong half. A second test: name the last decision the store changed. If the answer is a date, the system reads. If the answer is a hope, it does not.

Remedy: build the read side first, or to the same standard as the write side. Decide which decision the store serves and wire that consumer before adding the next writer. [Just-in-time information retrieval](#just-in-time-information-retrieval-jitir) is the shape of a wired read: the lookup happens at the boundary where the decision is made, not in a report someone might open later. [Lore](#lore) is resumed at session start for this reason; a written record no session reads is a write-only store with good prose. [Guard the context window](#guard-the-context-window) governs the read side too: a read path that dumps the whole store into context is the same failure reversed — everything loaded, nothing used.

_Usage:_

"We've got three months of session telemetry in that table."

"And which decision did it change? Count the readers. If it's zero, that's write-only memory — record everything, query nothing."

## Section 2 — Gaps

### The verification gap

The distance between "the agents did work" and "the work satisfies the requirement". Every agent orchestrator of the 2025–2026 wave solved the same problem: run many agents in parallel without file conflicts. Worktrees for isolation, SQLite for messaging, tmux for processes, hooks for access control. That pattern is now a commodity. None of them confirm the agents built the right thing.

The symptom is a dashboard of twenty healthy agents, every worktree clean, every merge green, and a feature that does not do what the ticket asked. Nobody noticed, because every signal the tooling emits reports process health, and it emits no signal for requirement status.

| Dimension | Execution infrastructure          | Verification infrastructure                    |
| --------- | --------------------------------- | ---------------------------------------------- |
| Asks      | Did the agents run?               | Did the agents satisfy the requirement?        |
| Feedback  | Watchdog, heartbeat, merge status | Requirement status: passing, failing, untested |
| Detects   | Crash, timeout, conflict          | Wrong thing shipped                            |
| Maturity  | Commodity                         | Research-grade                                 |

Speed is visible and correctness is not, so execution tooling leads and verification tooling follows. Continuous deployment shipped faster before continuous testing caught up; microservices shipped before distributed tracing made them observable. Failures accumulate in the interval. A green check in that interval is a [proxy](#proxy-signal): it reports that the pipeline ran, and the pipeline checked what the developer remembered to test, not what the spec demanded. The gap is [specification debt](#specification-debt) made architectural.

The gap separates open-loop systems from closed-loop ones. An open loop writes a spec, dispatches agents, merges code, and hopes. A closed loop dispatches agents, runs verification against the spec, computes requirement status, and turns unmet requirements into new tasks. Closing it takes three things: a traceable link from each requirement to the test that proves it; status computed from the test result, with no agent judgment involved; and failing requirements becoming tasks without a human relaying them. That feedback is the third component of [structured autonomy](#structured-autonomy), and the one the orchestrators left to humans.

The merge gate then moves from "a reviewer agent approved" to "every linked test passes". Review still catches coherence and intent; the tests catch every assertion the reviewer will not re-run. Neither replaces the other. Both are how you [prove it works](#prove-it-works) at the scale of a swarm.

_Usage:_

"All twelve agents finished green and the merge went through. Why does the login flow still reject valid tokens?"

"Green tells you the agents ran. Nothing in that pipeline checked the token requirement — you're standing in the verification gap. Link the requirement to a test and let the test decide."

### The intent inversion

The swap AI made in the cost of software: implementation, once the expensive half, is now cheap, and intent, once cheap, is now the scarce input. For decades a product manager wrote a ticket in ten minutes and an engineer spent two weeks building it, so the industry optimized the build — agile, CI/CD, microservices, DevOps. A developer with an agent now builds in hours what took weeks. Nothing made ambiguous requirements clear, surfaced the invariants the ticket omitted, or learned what "right" looks like in a given system. That work costs what it always did, and most organizations still plan as if the build were the expensive part.

The symptom is review under water. More PRs arrive faster, from the same vague specs and the same implicit assumptions. Speeding review up processes the same ambiguity faster. Reducing the load on it — clearer specification, tighter ownership so the reviewer knows the invariants of the code they review — is the fix. A model can generate the wrong thing perfectly: flawless code from an ambiguous ticket is still the wrong feature, delivered sooner and with fewer syntax errors. "Models will improve" is true and beside the point, because better generation does nothing for [specification debt](#specification-debt).

Two kinds of verification get conflated, and the confusion is expensive:

| Kind      | Question                                                     | Scales with                          |
| --------- | ------------------------------------------------------------ | ------------------------------------ |
| Component | Does this unit work?                                         | Automation: tests, types, lint, CI   |
| System    | Does this change, with everything else, keep the invariants? | A person who holds the whole picture |

Component verification is largely solved and models keep getting better at it. System verification resists automation because the variety of the system exceeds what any predefined check encodes — [requisite variety](#requisite-variety) applied to integration. No check catches a semantic merge conflict, architectural drift, or ten individually correct changes that add up to an incoherent whole. The tooling shape of this is [the verification gap](#the-verification-gap).

The bet follows. Models will keep improving, so bet on what stays hard when generation is perfect: knowing what to build, and knowing whether what was built is right. Speed is table stakes. Judgment scales through structure — ownership, specification, feedback loops, the components of [structured autonomy](#structured-autonomy) — and not through heroics.

_Usage:_

"We doubled PR throughput this quarter and review is drowning. Should we put an agent on review too?"

"That's the intent inversion — building got cheap, deciding what to build didn't. A faster reviewer processes the same vague tickets faster. Fix the tickets."

### The jagged frontier

The uneven boundary of AI capability: models handle some tasks well and fail at adjacent ones, and no clean line separates the two. The term comes from the 2023 Harvard Business School / BCG working paper [Navigating the Jagged Technological Frontier](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4573321) (Dell'Acqua et al.), which measured consultants on tasks just inside and just outside the boundary; [Ethan Mollick](https://www.oneusefulthing.org/p/centaurs-and-cyborgs-on-the-jagged) popularized it. The frontier runs differently through every domain, and every model release moves it.

The symptom: the agent that refactored an auth module without a slip hallucinates a database migration, or the one that solved the hard algorithmic problem botches a config file. The failure surprises because difficulty predicted the wrong place.

| Assumption                     | Reality                                                             |
| ------------------------------ | ------------------------------------------------------------------- |
| AI handles the routine tasks   | Some routine tasks fail; some complex tasks succeed                 |
| Difficulty predicts capability | Easy tasks fail and hard tasks work, with no line between           |
| Capability improves uniformly  | Each model version shifts the frontier somewhere new                |
| One evaluation generalises     | Benchmark performance does not predict performance on your codebase |

Two strategies fail against it. "Let the agent handle everything below this line" assumes the line exists; delegation by perceived difficulty produces failures at random. "We tested it and it works" assumes the frontier holds still; it shifts between model versions, prompting strategies, and codebases, so evaluation is continuous rather than one-time.

The remedy is empirical boundaries. Map your own frontier — which tasks succeed in this codebase, which fail — because benchmarks and other teams answer a different question. Design boundaries for adjustment rather than as permanent capability lines; [structured autonomy](#structured-autonomy) depends on redrawing them as the frontier moves. Spend review at the edge: failures cluster at the frontier, not deep in either territory, and when agents chain outputs a jagged failure becomes [compounding error](#compounding-error).

Delegate where a failure is cheap and reviewable; keep control where a failure is expensive to reverse. Developers who lean on agents for generation and keep deployment by hand are reading the frontier correctly.

_Usage:_

"It rewrote the whole auth module without a mistake, then wrote a cron expression that fires every minute instead of every day."

"Jagged frontier. Difficulty doesn't tell you where it fails — the boundary is wherever it is. Add cron expressions to the list of things you check by hand."

### Compounding error

Semantic drift across a chain of handoffs, where each step is locally correct and the aggregate misses the intent. No single actor fails; the failure lives between actors. It differs from two failures existing tooling already catches:

| Type              | Mechanism                         | Concerns     | Detection          |
| ----------------- | --------------------------------- | ------------ | ------------------ |
| Cascading failure | A dependency chain breaks         | Availability | Monitoring, alerts |
| Error propagation | Bad data flows through a pipeline | Data         | Validation         |
| Compounding error | Meaning drifts at each handoff    | Meaning      | Integration review |

The arithmetic understates it. Three agents at a 5% individual error rate give a 14.3% aggregate failure probability (1 − 0.95³), and that model assumes independent failures. Agents fail dependently: each accepts flawed peer output as valid input and builds on it, so errors reinforce rather than accumulate.

The symptom: a swarm merges cleanly and the codebase now has three date-parsing utilities, two naming schemes, and a disagreement about which layer owns retries. Every output passed its local checks. Semantic merge conflicts are worse than textual ones because no tool flags them. [DORA's 2025 report](https://dora.dev/research/2025/dora-report/) found AI adoption correlating with higher throughput and lower stability: each change passes CI alone, and the interactions introduce bugs no single test covers. Maintainers see the same shape in AI-generated pull requests — each plausible in isolation, the aggregate eroding coherence, evaluation cost transferred to whoever still understands the invariants. Organizations had it first: requirements pass from PM to designer to engineer to QA, each translation reasonable, the product wrong.

[Premature decomposition](#premature-decomposition) sets it up: work split before the invariants were named leaves each worker to invent their own. Compounding error is autonomy without feedback, and [structured autonomy](#structured-autonomy) is the antidote. Three mechanisms reduce it:

1. Integration checkpoints. Review the aggregate, not only the parts. The merge button exists because someone has to hold the whole picture.
2. Shared invariants. Actors that reference one specification have a correction signal for drift. Without one, each actor invents its own.
3. Early feedback. CI catches textual conflicts and review catches semantic ones; the sooner drift is seen, the less it compounds.

_Usage:_

"Every one of the six PRs reviewed fine. Merged together, the checkout flow charges tax twice."

"Compounding error. Nothing in any one PR was wrong — two agents each added tax because neither saw the other's. Review the merged whole, not six diffs."

### Proxy signal

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

The remedy is to [prove it works](#prove-it-works): run the feature, read the value, inspect the diff. When a check fails, suspect the observation before the system — a proxy misreports in either direction. Script the check when it will run more than once; a script a reviewer can re-run beats a claim they have to trust. At the scale of tooling the same failure is [the verification gap](#the-verification-gap): orchestrators emit process-health proxies where requirement status is what was wanted.

_Usage:_

"The agent says all three migrations applied and the tests are green."

"That's its summary — a proxy signal. Show me the test output and `git diff` on the migrations folder."

"Diff shows two migration files. It wrote the third one in the transcript and never saved it."

### Meat proxy

A human who forwards questions to an AI and forwards the answers back, adding no judgment on the way through. The term is satire — [meatproxy.me](https://meatproxy.me/) defines the role as adding "nothing but latency" — and the satire names a real seat on a real team: the reviewer who pastes the ticket into a session and pastes the session's answer into the PR, the lead who relays an agent's summary to a stakeholder unread.

The symptom: asked a follow-up, the meat proxy has to go ask the model, because nothing about the answer lives in their head. The forwarding worked; the understanding never happened — [comprehension debt](#comprehension-debt) accruing at conversational speed.

The forwarding is not the failure; pipelines forward. The failure is that the human occupies the one seat where judgment was supposed to be added. An agent's answer arrives as a [proxy signal](#proxy-signal) — fluent, confident, unverified — and the meat proxy passes it along with a human signature attached. The reader downstream trusts it more because a person sent it, and the person added exactly nothing. That misplaced signature is the cost: [the verification gap](#the-verification-gap) crossed on borrowed credibility.

The remedy is the comprehension gate's test, applied at forwarding time: explain the answer in your own words before you send it, or [prove it works](#prove-it-works) before you sign it. A human who can do neither should step out of the path; the reader loses nothing but latency.

_Usage:_

"I asked him how the migration handles the legacy rows, and he said he'd check with the agent and get back to me."

"Then you're not talking to a reviewer, you're talking to a meat proxy. Ask the session yourself — it's faster by one hop."

## Section 3 — Disciplines

### Prove it works

The rule that a task is done when the real artifact has been checked, never when a [proxy](#proxy-signal) for it has reported success. Run the feature and walk the path a user would walk. Read the value the code holds rather than a cached or derived copy of it. Inspect the diff. A build that compiles, a fresh mtime, and an agent's own summary each stand in for the check, and each can be right about everything except whether the work works.

The failure it prevents is [the verification gap](#the-verification-gap): the stretch between "the agent said it passed" and "I watched it pass", where a wrong answer sits undetected. Delegated work is the sharpest case. An agent reports what it intended, and the report is the most fluent thing it produces; the code underneath may not match. Inspect the output artifact, not the account of it. A migration agent that reports "all 14 tables migrated" has produced a sentence. The proof is `\dt` against the target and a row count per table.

Two corollaries follow.

When a check fails, suspect the observation method before the system. A test that greps the wrong log, a curl against a stale port, a screenshot of the previous build: the code that watches is code too, and it breaks more often than the code it watches. Fix the eyes, then read the result again. Reverting a correct change because the check was wrong costs more than the check did.

Script the check when it will run more than once. A shell line a reviewer can re-run beats a claim they have to trust, and the second run is free. The script also outlives the session: the next agent inherits a command instead of a memory of what passed, and the [handoff artifact](#handoff-artifact) can point at it instead of asserting the result.

_Usage:_

"The agent says the endpoint returns 200 now."

"Curl it. Its summary is a proxy; the response is the artifact."

"I re-ran the check and it went red, so the fix must have regressed."

"Look at what the check observes first. Last time it was reading the old container."

### Guard the context window

The rule that every token entering a session must earn its place. Context is finite and, within a session, unrecoverable: a file dumped into the thread at turn three is still there at turn forty, crowding the instruction it was meant to serve, and no later turn can take it back.

The symptom is an agent sharp for the first task and sloppy by the third. Nothing changed in the model or the prompt. The window filled with output nobody re-read, and the attention that should hold the current instruction is spread across a build log, two whole-file reads, and a screenshot. A related shape: the agent asked to fix one function reads the whole module, then forgets which function. The instruction was in context. It was outnumbered.

Four practices follow.

Route bulk to subagents. Verbose command output, long files, and screenshots belong in an agent's context; the main thread keeps the summary. The subagent's window is spent and discarded, and the main thread pays only for the conclusion.

Read selectively. A file you will not use costs the same as one you will. Read the function, not the module; the failing test, not the suite.

Size phases and cap fan-out before launching. Five parallel agents each returning two thousand words is ten thousand words in the thread. Decide the return budget before the fan-out, and ask each agent for a conclusion, not a transcript.

Put content used on every invocation inline. A rule read on every turn belongs where it is read once, not in a separate file that costs a read each time.

When a task outgrows one window, stop rather than push through. Write a [handoff artifact](#handoff-artifact) at a natural boundary and let a fresh session take the next phase with the sharpest part of its window.

_Usage:_

"It nailed the first refactor and by the third it was inventing function names."

"Look at what's in the thread. Three whole-file reads and a full test log. Guard the context window: send those to a subagent and keep the summary."

### Separate before serializing

The rule that, when concurrent actors might write the same file, branch, key, or object, the first question is whether they need the same mutable thing at all. Usually they are publishing independent facts, and the remedy is to give each its own target and merge at the read boundary. Two workers writing their own field into one `state.json` still share mutable state; `indexer-state.json` beside `metrics-state.json` does not.

The failure it prevents arrives in two forms. Two agents append to a shared notes file and the second write erases the first. Or a lock is added, works, and now every writer waits on the slowest, and the run that took four minutes in parallel takes eleven. The lock treated a design problem as a scheduling problem.

| Option                          | When it fits                                                     |
| ------------------------------- | ---------------------------------------------------------------- |
| Separate targets, merge on read | Writers publish independent facts. The default.                  |
| Sequential phases               | Later writes depend on earlier ones; order them structurally.    |
| Single-writer actor             | One shared target is a real invariant; funnel writes through it. |
| Lockfile or compare-and-swap    | The target must be shared and the writers must run concurrently. |

Serialize only when one shared write target is a real invariant, and then serialize structurally. Treat "we need a lock" as a design smell worth checking before accepting.

Instructions are not concurrency control. Telling agents to take turns does not make them take turns. An agent told to "wait until the other agent finishes" has no way to observe the other agent and proceeds when its own reasoning says the time has come. The constraint has to live where the agent cannot reason past it, which is the filesystem layout or the process model, not the prompt. This is [structured autonomy](#structured-autonomy) applied to writes.

A concrete case: three agents each collecting findings. Wrong: all three edit `findings.md`. Right: `findings/debts.md`, `findings/gaps.md`, `findings/disciplines.md`, and the lead concatenates when the three return.

_Usage:_

"Two of the agents both wrote to progress.json and one overwrote the other. I'll add a lock."

"Do they need the same file? Give each its own state file and merge when you read. Separate before serializing."

### Dead defensiveness

Defensive code that guards against states the contract already rules out: a null check on a value the caller guarantees, a blanket `try/except` around a call whose failures the handler cannot fix, a fallback default for a key that must be present, a cast that coerces a wrong type into a plausible one. Each converts a bug into a silent wrong answer. The exception that would have named the fault at the line it occurred is caught, and the program continues with a value nobody chose.

The symptom is the run that finished clean and is wrong. A missing config key became an empty string, became a request to the wrong host, became a 404 the except block logged at debug level. Four layers of defense, and the failure surfaced two days later in a dashboard, far from any line that caused it.

| Form                        | What it hides                        |
| --------------------------- | ------------------------------------ |
| Guard for an excluded state | A caller violating the contract      |
| Blanket try/except          | Every failure the handler cannot fix |
| Fallback default            | A missing or malformed input         |
| Lazy cast                   | A type mismatch upstream             |

Agents produce this by default. A guard never fails a test; a raised exception might. Asked to make the suite green, the model wraps the call, returns `None`, and the suite is green. The test now passes over a swallowed exception, and the green run is a [proxy](#proxy-signal): the signal says done and the work is undone. [Prove it works](#prove-it-works) by reading the output the run produced, not the color of the run.

The practice: let exceptions raise. The caller that can handle the error sits higher in the stack, and a guard at the wrong level denies it the chance. Fail loud and early. Where a guard seems necessary, ask what the contract says. If the contract already excludes the state, the guard is dead; delete it. If the contract does not exclude the state, tighten the contract or handle the case with a branch that does something, not a default that hides it.

_Usage:_

"The pipeline finished green but half the rows are blank."

"Find the try/except that swallowed the parse error. That's dead defensiveness: it turned a crash into a wrong answer."

## Section 4 — The Written Record

### Lore

The written record of why: the decisions a project made, the alternatives it rejected, and the patterns it learned, kept outside any one session so the next session inherits them. A changelog records what changed; lore records the judgment behind the change, structured so an agent can read it at the start of work without a person re-explaining it.

Three records answer three questions:

| Record      | Question it answers                 | Who reads it well                |
| ----------- | ----------------------------------- | -------------------------------- |
| Changelog   | What shipped, in which version?     | Users, release managers          |
| Git history | What changed, when, by whom?        | A person tracing a regression    |
| Lore        | Why this, and what did we rule out? | The next session, human or agent |

The first two are byproducts of the work. Lore is a deliberate act: someone decides an outcome is worth carrying forward and writes it down with its reasoning. "We tried Jaccard dedup and it worked." "Don't mock the database; here is why." A commit message can hold that, but an agent cannot extract judgment from four thousand commits at session start. Lore pre-structures it for machine consumption — [information architecture](#information-architecture) with an agent for a reader. For a solo developer with good commit hygiene and a `decisions/` folder, lore adds little; for parallel agents that need pre-structured judgment, it earns its keep.

One writer, curated. Capture is cheap and judgment is scarce, so the record grows through a single curation pass, never through parallel agents each appending what they think mattered. Reads are safe and fail silent; writes need a librarian.

A record nobody reads at decision time is [write-only memory](#write-only-memory). Count the read paths against the write paths, and make sure something fires when the next session begins, which is [just-in-time information retrieval](#just-in-time-information-retrieval-jitir).

Our implementation is the `lore` tool: `lore resume` loads the record into a session, `lore capture` records a decision or pattern, `lore handoff` snapshots state for the next session. A failure that recurs three times surfaces as a pattern, and the pattern reaches every session that follows.

_Usage:_

"The agent rewrote the dedup to use embeddings. We tried that in March and it was slower."

"That decision lives in a Slack thread. Put it in lore with the benchmark, and the next session starts knowing it."

### Information architecture

The structure of the written record: what gets a file, what the file is named, where it sits, and what points to it. The term is [Richard Saul Wurman's](https://en.wikipedia.org/wiki/Information_architecture), and Rosenfeld and Morville built the discipline for the web, where the reader was a person with a browser. The discipline transfers; the reader changed. An agent starts each session blank, finds files by name and grep rather than by browsing, reads one file at a time, and pays for every token it loads — structure is a budget question as much as a findability one ([guard the context window](#guard-the-context-window)).

The symptom: the fact was written down, and the agent re-derived it anyway. The note existed; nothing on the agent's path pointed to it. Recorded knowledge that no read path surfaces is [write-only memory](#write-only-memory), and more writing does not fix it — the failure sits in the architecture, not the archive.

Four rules cover most of the practice:

| Rule      | For the agent reader                                                                                                                   |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| Placement | Put the fact where the work happens, so it loads when it matters — [just-in-time retrieval](#just-in-time-information-retrieval-jitir) |
| Authority | One file owns each fact; the rest point to it. Copies drift; pointers hold                                                             |
| Indexes   | A small always-read file — a CLAUDE.md, an [llms.txt](https://llmstxt.org/) — earns its tokens by routing to files read sometimes      |
| Names     | The filename is the query interface: name the file what a reader would grep for                                                        |

[Lore](#lore) is what the record holds; information architecture is why the next session finds it. The test is the same for both: start an agent cold and count how long before it stands where the last session stood.

_Usage:_

"I documented that decision three weeks ago, and the agent just re-litigated it from scratch."

"The note exists and nothing routes to it — an information architecture problem, not a documentation one. Move it to the seam, or into the index the session always reads."

### Just-in-time information retrieval (JITIR)

Retrieval that fires at the moment of decision, without anyone remembering the record exists. The term is [Bradley Rhodes's](https://www.bradleyrhodes.com/Papers/rhodes-phd-JITIR.pdf): his Remembrance Agent watched the document under edit and pushed related notes unasked, no query issued. The seam is the point where the mistake gets made: the edit, the commit, the prompt submission. A record that surfaces there counts; a record that waits to be searched for counts only for the reader who already knows it is there.

Classify retrieval by what triggers it, not by the technology underneath:

| Mode         | Mechanism                                                                               | Recall required                     |
| ------------ | --------------------------------------------------------------------------------------- | ----------------------------------- |
| Push at seam | Failing check, pre-commit hook, PR template question, context injected on prompt submit | None                                |
| Proximity    | ADR beside the code, docstring over wiki, comment at the confusing line                 | None; the reader is already looking |
| Query        | Someone searches                                                                        | Must know it exists                 |
| Ambient      | Session-start resume, weekly review, scheduled audit                                    | None, but untargeted                |

The ranking is steep. Push and proximity work because they ask nothing of memory. Query fails silently: the person who most needs a record is the one who does not know it was written, and the archive looks healthy while nothing gets read.

Three constraints shape the push mode. Injection has a budget: three to five items, ranked. Inject everything and the reader skims, and you are back to no retrieval with worse latency. The seam must be where the mistake happens, not where it is discovered: a check at merge time beats a wiki page, and a check at edit time beats a check at merge. And the best retrieval is none: a lesson that became a default, a lint rule, or a type needs no finding.

The diagnostic for a knowledge system: count read paths against write paths. More capture verbs than query verbs means [write-only memory](#write-only-memory), a diary with good intentions. Ask what fires at decision time, how many items it injects, and whether the record sits beside the work or in a separate system someone must choose to enter. [Lore](#lore) exists to be injected at session start; a [handoff artifact](#handoff-artifact) is retrieval at the seam between two sessions.

_Usage:_

"We documented that migration gotcha six months ago. Nobody read it before they hit it again."

"Nobody was going to search for it. Put the check where the mistake happens, a pre-commit hook on the migrations directory, and just-in-time retrieval does the remembering."

### Handoff artifact

A document one session writes so that another can pick up its work. Plans, specs, tickets, and progress notes are all handoff artifacts. The term comes from Matt Pocock's [Dictionary of AI Coding](https://github.com/mattpocock/dictionary-of-ai-coding).

Each session begins empty. Whatever the previous session decided, ruled out, or left half-done exists only in its context, and the context ends with the session. The filesystem outlives it. Writing the state to a file moves it across the boundary. Compaction is the in-memory alternative; the file is the version you can read and correct before anything depends on it, and the version five parallel sessions can share.

A good one holds absolute paths, decisions with their reasons, what is done, what remains, and what was tried and rejected. It is written for a reader with nothing in context, and it says so at the top.

Our practice adds two rules.

The artifact records what the writing session believed. The reading session treats those beliefs as claims and verifies them against the code before building on them; [prove it works](#prove-it-works) applies to inherited state as much as to fresh work. "Tests pass" in a plan file means tests passed for a session that may have run a subset, on a tree that has since changed. Run them. "Auth refactor complete" means the writer stopped; read the diff to learn where.

Durable decisions leave the artifact. A plan file is scoped to a task and goes stale when the task ends; a decision about how the project handles migrations does not. Promote those into [Lore](#lore), where the next session's resume finds them, rather than leaving them in a plan file nobody reopens. The artifact carries state across one boundary. Lore carries it across all of them.

_Usage:_

"The plan says the auth refactor is finished, so I'll start on the API."

"The plan says the previous session believed it was finished. Run the suite and read the diff before you build on it."

"Where does the decision about the retry policy go? It's in the plan."

"Out of the plan and into Lore. The plan dies with the task; the decision doesn't."

## Section 5 — Teams of Agents

### Structured autonomy

Controlling an agent by controlling its environment rather than its actions: set boundaries, provide tools, establish feedback, then let the actor decide how to do the work. Prescribe every step and each handoff compounds the specification error; prescribe nothing and the work drifts. Structured autonomy sits between the two, and it is the position that scales.

| Dimension     | Prescribed decomposition             | Structured autonomy                    |
| ------------- | ------------------------------------ | -------------------------------------- |
| Who decides   | Planner, before work starts          | Actor, during work                     |
| Failure mode  | Wrong decomposition propagates       | Wrong boundaries constrain too much    |
| Scales by     | More planning, more planners         | Better boundaries, fewer interventions |
| Feedback      | Late, after every step completes     | Continuous; actor adjusts mid-task     |
| Cost of error | Rework cascades through the pipeline | Actor self-corrects within bounds      |

Three components carry the structure. Boundaries: ownership, permissions, quality gates, scope. Tools: the actor's interface for inspecting and acting within those boundaries. Feedback: how the actor and the system learn whether the approach is working. Remove boundaries and you get chaos; remove tools, helplessness; remove feedback, drift.

The merge button is the feedback component. A reviewer with [requisite variety](#requisite-variety) catches what automated checks cannot encode, so structured autonomy concentrates human judgment at integration points instead of spreading it across every step. The pattern predates agents: Torvalds shifted from contributor to reviewer as Linux scaled, building subsystem maintainers and merge gates rather than prescribing how patches decompose. Contributors self-direct inside that structure.

The same shape appears at the inference level. Give a model a REPL and a handle to its input instead of loading everything into context, and it inspects, filters, and recurses on its own; the REPL is the boundary, the recursion is the autonomy. It appears again in the rule to [separate before serializing](#separate-before-serializing): give each worker its own file or branch, and the boundary does the coordination a lock would otherwise have to.

_Usage:_

"I wrote a twelve-step plan for the agent. It went wrong at step four, then built eight more steps on that foundation."

"Swap the twelve steps for a boundary and a check: it owns this directory, the suite must pass, and you review the merge. Structured autonomy lets it find the decomposition itself."

### Premature decomposition

Splitting work into parts before understanding how the parts relate. Each part is then wrong in a different way, and nobody sees it, because each piece looks fine in isolation. The symptom arrives at integration: four agents report success, and the merged result does not work.

The scout-spec-build pipeline assumes exploration and implementation separate cleanly. They do not. The right shape emerges during implementation, and boundaries drawn before that point lock in the wrong ones.

| Stage         | What goes wrong                                   |
| ------------- | ------------------------------------------------- |
| Decomposition | Boundaries drawn without knowing the connections  |
| Specification | Each part specified apart from the others         |
| Execution     | Each executor discovers its spec was wrong        |
| Integration   | Locally correct pieces, globally incoherent whole |

Each handoff multiplies the error. Agent A passes flawed output to Agent B, who treats it as valid and builds on it; the failure lives between agents, and debugging it means forensic reconstruction across fragmented histories. This is the mechanism of [compounding error](#compounding-error), and decomposition is what switches it on. Overstory's author [documented](https://github.com/jayminwest/overstory/blob/main/STEELMAN.md) a 20-agent swarm spending $60 on work a single sequential agent finished for $9: one data point, not a law, written by the tool's own author before deployment.

Planning stays. The argument is against committing to boundaries you have not earned. [Specification debt](#specification-debt) looks like the opposite advice, since it says specify more, but the two concern different things. Specification debt is about intent: you never said what right looks like. Premature decomposition is about structure: you divided the work before you understood it. Specify intent thoroughly and leave the decomposition flexible.

The pattern recurs wherever work is divided before it is understood. Microservices before domain boundaries produce a distributed monolith. Org charts redrawn before workflow mapping produce structure that fights the work. Sprints estimated before a spike produce scope surprises that cascade.

The alternative is [structured autonomy](#structured-autonomy): set boundaries, provide tools, establish feedback, and let the actor decompose based on what it finds. The decomposition emerges from the work.

_Usage:_

"I split the feature across five agents by layer. Every one passed its tests and the feature doesn't work."

"You decomposed by layer before anyone knew how the layers talk. That is premature decomposition. One agent should have built the tracer bullet first; then you split what it found."

### Requisite variety

A controller needs at least as much variety as the system it controls; fall short and the system finds states the controller cannot handle. W. Ross Ashby stated the law in [An Introduction to Cybernetics](http://pespmc1.vub.ac.be/books/IntroCyb.pdf) (1956): only variety can absorb variety. A thermostat regulates a room because its two states, on and off, match the room's two conditions, too cold and warm enough. A system with more states than its regulator will reach an unregulated state.

| System variety | Controller variety | Outcome                                    |
| -------------- | ------------------ | ------------------------------------------ |
| Low            | Low                | Simple control works                       |
| High           | Low                | Controller overwhelmed; unregulated states |
| High           | High               | Effective regulation                       |

Applied to agents: the agent's output space has enormous variety. A reviewer, harness, or test suite with less variety than that space will pass states it cannot evaluate. An automated check has exactly the variety that was encoded: lint rules, type checks, test assertions. A codebase has far more: edge cases, architectural invariants, undocumented assumptions, user expectations. The gap between encoded variety and actual variety is where the bugs the checks passed live. This is why the merge button stays with a person who understands the system, and why [structured autonomy](#structured-autonomy) places that person at the integration point.

Ashby wrote the law as a prescription, and it is usually quoted as a caution. The most-cited PDF drops the "only," and the first clause gets severed, leaving "variety can destroy variety" to read as a warning that complexity begets complexity. Restored, the point is directional: build up the regulator. The reviewer, the harness, and the suite are the things to invest variety in, and the fix for a check that passes bad states is more variety in the check, never less variety in the agent.

Two more consequences. A planner decomposing work before implementation holds only an abstraction's variety, while the implementer accumulates the problem's actual variety through contact; [premature decomposition](#premature-decomposition) is low-variety planning applied to a high-variety problem. And variety is domain-specific, so a model's variety in one domain says little about the adjacent one; [the jagged frontier](#the-jagged-frontier) is Ashby applied to capability.

_Usage:_

"CI is green on every agent PR, and production keeps breaking in ways the tests never mention."

"The suite has less variety than the agent's output, so it passes what it can't see. Add the invariants it's missing, and keep a reviewer with requisite variety on the merge."
