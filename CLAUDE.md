# Dictionary

README.md is generated. Edit `dictionary/*.md`, `internal/Curriculum.md`, or `internal/README.template.md`, then run `make generate`. Never edit README.md by hand.

`make page` builds the interactive graph-explorer page (`internal/dictionary_page.html`, gitignored) from `internal/page.template.html` and the same entries; it is published as a Claude artifact.

## Adding an entry

1. Create `dictionary/<Term>.md`. The filename is the term, in sentence case.
2. Add the term to a section in `internal/Curriculum.md`. The generator fails on orphans.
3. Search the other entries for places the new term can replace a longer explanation.

## Entry format

```markdown
---
description: One sentence, under 140 characters, stating what the term names.
origin: coined | project | borrowed. Borrowed means the term came from outside — industry, a paper, another dictionary — and its body attributes the source with a link. Project means it names a tool of ours (Lore, and eventually Council, Sweep). Coined means it is our phrase for a concept.
---

Body. First sentence defines the term flatly. Links to other entries use
`[text](./Other%20term.md)`, spaces percent-encoded, on the first occurrence only.

_Usage:_

"A line the reader has said or heard."

"The reply that uses the term correctly."
```

Rules the generator enforces: `description` present and under 140 characters; `origin` present, `coined` or `borrowed`, and a borrowed entry carries at least one external attribution link; body plus Usage at least 200 words; every link target exists; each target linked at most once per entry; every entry appears in the Curriculum.

## Voice

- Define the term in the first sentence. Mechanism, symptom, remedy follow, in that order, as the term earns them.
- Where the term names a felt failure, weave the symptom into the prose near the definition so the reader recognizes their own incident. Building-block terms get no manufactured symptom.
- Reach 200 words with substance, never padding.
- Prefer a table for stepped or comparative material: lifecycles, ladders of options, contrasts between three terms.
- Plain register. State what happens and what to do. No superlatives, no dramatized moments, no emphasis words ("core", "real power", "the whole point").
- American spelling.
- Strunk throughout: positive form, active voice, definite and concrete, needless words omitted.
- Constructions in `~/.claude/rules/banned-phrasing.md` are barred: no "X was never the bottleneck", no matched sections closing on aphorisms.
- Attribute borrowed terms in the body with a link to the source. Our own coinages carry no attribution.
- The Usage dialogue is two or three lines: a symptom the reader has said, and a reply that names the term. The reply demonstrates the term; it does not lecture.
