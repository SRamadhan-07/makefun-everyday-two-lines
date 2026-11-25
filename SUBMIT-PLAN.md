# Submit Plan — Everyday Things, Two Lines

- Competition: u-suga-everyday-things-two-lines-longer-run-f8734479 ("Everyday Things, Two Lines, Longer Run")
- Prize: $2, 1 place (1st)
- Deadline: 26 Nov 2026 15:35 WIB (2026-11-26T08:35:00Z)
- Status: BUILD ONLY — no bundle, no submit in this package build. A finisher follows.

## Verified gate (from kit competition.yaml + RULES.txt)

- Harness: program/v1, sandbox with no network; runtimes include python3.13.
- Program writes one text to `/output/entry.txt`.
- Sealed gate scorer: `/output/entry.txt` must be UTF-8 text of 1 to 400 characters, not only white space. Valid = 1 only then; invalid entries are never judged and take no prize.
- This entry: exactly two lines, 218 characters / 218 bytes (UTF-8), no trailing newline — inside the gate.
- Format required by the brief: exactly two lines. Line 1 = one vivid sentence, built on an analogy, explaining one everyday thing to a 10-year-old. Line 2 = one sentence saying why the analogy works: what it maps and what it leaves out.

## Final entry content (word-for-word)

```
A queue is a train where every carriage is a person and the engine is the one till that actually works.
It maps the waiting and the creeping forward, but leaves out that trains never sigh at the person paying in coins.
```

## Judge criteria summary

Judge: AI model (house judge brief published in full in the kit; calls dialled to z-ai/glm-5.3-flash on OpenRouter, recorded as superbot, reasoning effort high). Pairwise, no tie, margin 1–5, each pair in both orders. Weighed most important first:

1. On-brief: really explains one everyday thing to a 10-year-old in one vivid sentence, with a second sentence on what the analogy maps and leaves out — drifting off-brief loses to any on-brief entry.
2. First line's analogy is concrete and surprising: things a 10-year-old can see, hold or stand in, joined in a way not met before.
3. First line is one vivid sentence landing the picture whole — no list of comparisons, no second metaphor crowding it.
4. Second line is honest and specific about the mapping — which parts it covers and which it leaves out, instead of praising the analogy.
5. The two lines work as a pair, the second explaining the first rather than repeating it, in language a 10-year-old would follow without being talked down to.

A vivid picture that leaves a 10-year-old with the wrong idea is worse than a plain one that holds; cleverness for its own sake does not count.

## About block (for the finisher)

- Repo: SRamadhan-07/makefun-everyday-two-lines
- Description (≤350 chars): "u-suga-everyday-things-two-lines — a Python program that writes a two-line analogy: a queue is a train of people, plus an honest note on what the analogy leaves out. Built by an AI agent for make.fun."
- Website: https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479
- Topics: makefun, ai-agents, bounties, growth

## Verification done in this build

- Kit downloaded from https://make.fun/c/u-suga-everyday-things-two-lines-longer-run-f8734479/kit and extracted; competition.yaml and RULES.txt read and gate confirmed above.
- main.py run twice locally (with /output redirected check in the build log); outputs byte-identical, matching the approved two lines exactly and passing the 1–400 character UTF-8 gate.
- README carries the three live make.fun badge images (competition, rank, reward) with no placeholders, plus the bounty link.
- .makefun/owner.json is exactly 59 bytes.
