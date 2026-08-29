# Case study: Claude Code as a scoping and execution partner

Talk prep. One worked example, told from the commit record, for a 15-minute
slot.

The example is the TCE-IPDE working document: from a prompt to a published
specification, a figure, a corrected error, a ranked reading list, and a
reading method, in nine commits between 19:18 and 22:06 on 2026-08-28.

**What the talk claims.** Claude Code is useful for the part of the work that
happens before any code is written: turning a half-formed strategy into a
specification detailed enough to argue with, finding the prior art that says
the idea already has a name, and then narrowing the work when that prior art
turns out to shrink it.

**What the talk does not claim.** That any of it is verified. The
specification is a hypothesis and the reference list was assembled from
abstracts. The last hour of the arc is the part where that starts to be
checked, and the first paper checked did not say what the model said it said.
That is a slide, not a footnote — see "The honest slide" below.

---

## The timeline

The first ten commits are authored `Claude` and the last two are Andy's. The
direction is in the prompts, which are not in the repository, so the commit
record shows what was built and not what was asked. Bring the terminal
history.

| Time | Commit | What changed | Lines |
|:--|:--|:--|:--|
| 19:18 | `068a307` | The scoping document exists: 27 numbered sections, PK and PD models, endpoints, three designs to compare, operating characteristics. | +1695 |
| 19:31 | `95b7cc0` | Prior art, priming argument, pre-screening, population, decision criterion. | +190 |
| 19:42 | `a0bbe67` | Markdown to Quarto, so it renders. | +49 −26 |
| 20:53 | `fd1f14d` | Published: a Projects section, and the document moves out of `blog/drafts/`. | +187 −262 |
| 21:23 | `3b6f5c9` | The writing guide and `CLAUDE.md` arrive; the MCLA-117 escalation example and its figure. | +1145 −123 |
| 21:25 | `743eac2` | The escalation interval is held at one week for v1. | +17 −3 |
| 21:26 | `d858775` | A worked example that depicted a patient at a flat dose is corrected. | +10 −5 |
| 21:46 | `980ec51` | PD-guided escalation, and the reading list is rewritten. Simon 1997 drops from first to fifth. | +207 −55 |
| 21:53 | `2af4e1b` | The references move onto their own page, every entry carrying a status marker for whether it has been checked. | +208 −155 |
| 22:06 | `304b174` | A Guides section, and a method for reading the five papers. | +182 |
| 22:10 | `add612c` | **Andy's.** Two entries read and marked, with what they actually said. | +7 −14 |
| 22:11 | `aec5101` | **Andy's.** A third entry's status corrected. | +1 −1 |

The 262 deletions at 20:53 are the interesting number in that column:
publishing the document cut it. The two commits at the end are the other one,
because they are the first in the sequence a human wrote.

---

## Beat 1 — The scoping document, from one prompt

**Show:** the prompt, then the table of contents of `068a307`.

> [PASTE THE INITIAL PROMPT HERE — it is the first slide and the record does
> not contain it.]

The output is not prose about intrapatient dose escalation. It is a
specification with numbered sections that a colleague can disagree with
section by section: a central hypothesis stated as a ratio, a primary endpoint
defined on observables only, three named designs, a PK model, a PD model, and
a list of the operating characteristics the simulation would report.

**The point for the audience.** The value is not that it wrote 1,695 lines. It
is that the lines are *addressable*. Section 13 is where the dose escalation
factor lives, so "I disagree with Section 13" is a sentence someone can say.

---

## Beat 2 — It found the prior art without being asked

**Show:** the `### Prior art` section, and the sentence "the catch-up design is
that mechanism".

Two of the three designs under study turned out to be published in 1997, as
accelerated titration designs. The document now says so before a reviewer
would, and reclassifies one of its own anticipated conclusions as a
replication of a known result rather than a new claim.

**The point.** This is the highest-value thing in the transcript and it took
minutes. Locating prior art is a deliverable, not a courtesy. A specification
that says "the thing you already do is called X" is worth more than one that
does not, and it is cheaper to hear it from a model than from a reviewer.

---

## Beat 3 — Publishing it made it shorter

**Show:** the `fd1f14d` diffstat, +187 −262.

Moving the document from `blog/drafts/` to a published Projects page cut more
than it added. The same session added `CLAUDE.md` and a writing guide that
says what a document of each kind may cost the reader in length.

**The point.** Length is where these tools fail by default, and the fix is
mechanical rather than stylistic: decide what kind of document it is and how
long that kind is allowed to be, write that down, and let the constraint do
the cutting.

---

## Beat 4 — Two errors, both caught in the same loop

This is the beat to spend time on. Both errors are Claude's.

**The flat-dose example (`d858775`).** A worked example of the catch-up design
read $0.3 \rightarrow 0.3 \rightarrow 0.3\ldots$, where the arrows are
escalation steps and none of them escalate. It depicted flat dosing as one of
the designs under study, which it is not. The corrected version is a patient's
actual regimen, and it adds the sentence the original needed: each arrow is one
weekly administration.

**The demoted reference (`980ec51`).** Four commits earlier, the document
carried a section headed **"Read Simon 1997 before building anything"**. Two
hours later that heading is "What to read before building", the section holds
five papers in a deliberate order, and Simon 1997 is fifth:

> Simon 1997 is the design ancestry but it is not the most useful thing to
> read first, and it is not the most recent treatment of intra-patient
> escalation.

Above it are a 2024 review that covers this project's actual problem and a
2025 paper flagged **"Read this second because it can change the premise"**,
because it attacks the same gap by raising the starting dose rather than by
crossing the gap faster. If that result is general, it shrinks the value of
the strategy the whole document specifies.

**The point.** The first recommendation was confident, specific, and wrong
about priority. What corrected it was another pass over the same document with
a different question asked. Neither error was found by the model noticing on
its own, and neither was found by reading the prose carefully — one was found
by looking at a figure-shaped thing and one by asking "is this actually the
first thing to read".

---

## Beat 5 — The reading method, and the first paper that was actually read

**Show:** `projects/tce-ipde/references.qmd`, then `guides/reading-papers.qmd`,
then Andy's two entries.

Reading the paper that had just been demoted raised an ordinary question — how
should I read this, and for how long — and the answer had three parts. The
reusable part became a site page summarizing Keshav's three-pass method and
Pain's Science Careers piece. The project-specific part is on the references
page: an hour on Simon, aimed at the two questions it can answer, with the
outcome to watch for written down in advance.

The third part is the status marker. Every reference now carries ❌ not
checked, ⚠️ transcribed but unverified, or ✅ checked, and the page opens by
saying that nothing on it has been checked against its source.

Then the first two papers were read, and the top of the queue did not survive
contact. Elmeliegy 2024 had been characterized, from its abstract, as "the
closest published treatment of this project's actual problem". The note on the
entry now reads:

> Talks about using small cohorts (n=1), large steps (3x), and starting around
> MABEL dosing but didn't actually talk about intrapatient escalation.

Zhou 2025, the paper flagged as the one that could change the premise, was
closed with a decision not to read it: a different topic, complementary rather
than competing.

**The point.** The status markers earned their keep within twenty minutes of
existing. A characterization written from an abstract is a prediction about a
paper, and the first one checked was wrong. A reading queue with no marker on
each entry would have carried that claim into the specification, where it
would have looked like a finding.

## The honest slide

Put this in the middle of the talk, not at the end.

1. **The reference list is unchecked, and it says so on every entry.** The
   references page opens with "Nothing on this page has been read and checked
   against its source", and each entry carries ❌, ⚠️ or ✅. The two entries
   that have since been checked are the evidence that this is not decoration:
   one of them did not say what the model said it said.
2. **The document declines to model what it cannot.** Section 16 is titled
   "ICANS: critical limitation, not a fabricated model", and it states that no
   established exposure-to-ICANS relationship was found and that the
   simulation will not invent one. The limitation belongs to the strategy, not
   only to the simulation.
3. **The kill criterion is prespecified.** Section 26b sets the minimum time
   saving below which the strategy is not worth an unquantified
   delayed-toxicity risk, with a starting value of 8 weeks and an instruction
   to replace it with the program's real number. It is written down before any
   results exist, so the threshold is not negotiated against results already
   seen.
4. **Ten of the twelve commits are authored by Claude.** The judgement was
   exercised through prompts and through what got rejected, and none of that
   is visible in the repository. The two human-authored commits are the ones
   that record a paper having been read, which is the division of labour the
   talk is arguing for.

This is the accountability argument the site already makes, with an artifact
attached: see the post "AI can assist, humans must own decisions".

---

## Fifteen-minute run sheet

| Minutes | Section | On screen |
|:--|:--|:--|
| 0–2 | The problem: a strategy in your head, and no specification. | The prompt. |
| 2–4 | Beat 1, the scoping document. | Table of contents, then Section 13. |
| 4–6 | Beat 2, prior art. | The Prior art section. |
| 6–7 | Beat 3, publishing cut it. | The `fd1f14d` diffstat. |
| 7–11 | Beat 4, the two errors. | The flat-dose diff, then the two headings side by side. |
| 11–13 | Beat 5, the reading method and the first check. | The references page with its markers, then Elmeliegy's entry before and after. |
| 13–15 | The honest slide, and questions. | The four numbered points. |

Beat 4 is the one to protect if the talk runs long. Cut Beat 3 first, then
Beat 5.

---

## Materials to have open

- The published document: `projects/tce-ipde/specification.qmd`, which was
  `projects/tce-ipde/index.qmd` until the folder gained an index.
- `git log --format='%h %ad %s' --date=format:'%H:%M' --stat` for the timeline
  slide.
- `git show d858775` for the flat-dose correction, which reads well as a diff.
- `git show 980ec51 -- projects/tce-ipde/index.qmd` for the demotion, which
  needs the old heading and the new one on one slide rather than a raw diff.
- `guides/reading-papers.qmd`.
- `projects/tce-ipde/references.qmd`, and `git show add612c` for the two
  entries that were checked.

## Before the talk

- Paste the initial prompt into Beat 1. Everything else is reconstructable
  from the repository; that is not.
- Decide whether the audience sees the terminal live or screenshots. A live
  terminal makes the point about speed and risks making the point about
  scrolling.
- Check the two citations on the Guides page, which were written from memory
  in the session that created it.
- Rehearse Beat 4 against the clock. It is four minutes of material and it is
  the reason to give the talk.
