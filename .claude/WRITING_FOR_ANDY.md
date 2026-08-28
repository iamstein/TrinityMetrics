# Writing for Andy

Who the reader is, and how to write a document he will not have to send back.

**When to read this.** When asked to draft a new document, or to substantially
rewrite an existing one — a vignette, an article, `README.md`, or a long
summary. Not for code, test, or registry work, and not as a session preamble.
Part 1 is what to do; Parts 2 and 3 are the evidence behind it. The
machine-prose tics in Part 1 apply to *everything*, including conversation,
commit messages and comments.

**Who updates it.** Andy, by asking for a review of recent history, about once a
month. Do not append to it during a session; say in the conversation what looks
wrong and let him decide. He answers in place, marked `[Andy Note]`, left where
the wrong claim was — three are live, on O14 and on two of the open questions in
Part 5.

**Numbering.** Two independent series: `O###` for observations about the reader,
plain numbers for the writing rules. The gaps in `O###` are deliberate. The
numbers are how he refers to them in conversation and O1 is cited from
`learning/EFFECTIVE_LEARNING.md`, so do not renumber to close them.

**Update log.**

- 2026-08-05 — first observations, from the session of 08-04/05.
- 2026-08-14 — merged from `WRITING_STYLE.md` and `_THEORY_OF_MIND.md`; the tics
  list and its search step restored at Andy's request.
- 2026-08-14, second pass — reordered actionable-first. Rules 14 to 16 and O17
  added from his own edits of 08-13 and 08-14; the contract table added; O14 and
  two open questions closed; the proposals section retired. 546 lines to 574:
  about 85 lines of new material against 57 cut from the old.
- 2026-08-15 — at his instruction, rule 14 and checklist items 7 and 9 split
  dataset-specific numbers from algorithmic ones, from the `avatar-algorithm.Rmd`
  revision. Nothing else changed.
- 2026-08-26 — at his instruction, file names only. The contract table takes the
  `avatar-` prefix, `synpmx-4-methods.Rmd` loses its count, and the two PCA
  documents get rows beside their AVATAR counterparts. Two names in the Part 3
  standing caveat and in rule O17 renamed with them. No rule, observation or
  judgement changed.

---

# Part 1 — Before handing over a draft

## The document contract

Documentation comes in four kinds, and a page that tries to be two of them
serves neither reader: a **tutorial** teaches by doing, a **how-to** accomplishes
one task, a **reference** answers a lookup, an **explanation** says why. Decide
which one a document is before writing it, and let that decide how long it may
be.

| Document | Reader | Kind | Length |
|---|---|---|---|
| `README.md` | Deciding whether to try it | how-to | thin |
| `avatar-demo.Rmd` | First run, AVATAR | tutorial | thin |
| `pca-demo.Rmd` | First run, PCA | tutorial | thin |
| `avatar-scorecard.Rmd` | Judging one run | how-to | as long as the checks need |
| `avatar-public-data-examples.Rmd` | Finding a dataset like theirs | reference | one fixed shape per dataset |
| `avatar-algorithm.Rmd` | Auditing the mechanism, AVATAR | reference | exhaustive |
| `pca-algorithm.Rmd` | Auditing the mechanism, PCA | reference | exhaustive |
| `synpmx-methods.Rmd` | Choosing a method | explanation | thin |
| `articles/*-review.Rmd` | Learning the field | tutorial | as long as it needs |
| `design/` | Claude, and him later | reference | exhaustive |

The table is the mechanical form of the O10 / rule 12 tension: he wants a draft
complete enough that he iterates less, and he cuts shipped entry points in half.
The tier decides which applies, before drafting rather than in review.

## The machine-prose tics

Widely reported markers of machine-written prose, several of which appear in
this repo's own drafts. Unlike the rest of this file, the list applies to
*everything* — conversation, commit messages and code comments as much as
documents.

- **Contrastive antithesis.** "It is not X, it is Y", "not a bug, a feature". He
  deletes these by hand: "dropped *rather than quietly copied out of a real
  patient*" became "dropped" in `c972373`.
- **The rule of three** applied to everything: three adjectives, three-clause
  sentences, three-item lists where two items exist.
- **Significance announcements.** "crucial", "pivotal", "key insight",
  "fundamental", "underscores", "highlights", "testament to".
- **Hedge-then-assert.** "It is worth noting that", "It is important to
  understand", "arguably", "in many ways".
- **Vocabulary.** delve, leverage, robust, seamless, landscape, realm, tapestry,
  navigate the complexities, deep dive, at its core, in essence, that said.
- **The closing summary.** "In conclusion", "Ultimately", "The takeaway is". If
  the section needs a summary, it is too long.
- **Bold as emphasis spray.** Bold marks a term being defined or a verdict;
  three bolded phrases in one paragraph mark none of them.
- **Symmetric sentence pairs.** "X does A. Y does B." for rhythm, not content.
- **Second-person coaching.** "Let us break this down", "Think of it like",
  "Here is the thing".
- **Invented framing.** A coined metaphor ("the manifest of what survives") in
  place of a literal description. Deleted in `f8c22f1`; rule 12 says it again.
- **The aphoristic section opener.** "The tier that is easy to skip and
  embarrassing to fail." "Two public datasets, and the second one is the point."
  Both deleted in `d333313`. A section starts at its content.
- **Sycophancy.** No "great question", no praising the request, no announcing
  that something is a strong idea before doing it.

## The checklist

1. The document's kind and length are settled against the contract table above.
2. Every heading names a subject (rule 2).
3. Each paragraph's first sentence stands alone with the topic explicit (rule 4).
4. Every acronym expanded at first use, and every method from outside
   pharmacometrics explained from zero (O8), answering *what is calculated, from
   what inputs, and what does a good number look like* (O1).
5. Verdicts lead; nuance follows, and a hedge is a legitimate verdict (rule 10).
6. Out-of-scope stated explicitly and bluntly, once, at the top (rule 11).
7. Numbers where a claim is measurable, computed by a chunk that runs rather
   than written into the prose; no adjective standing in for one (rule 9, O12).
8. Comparable items climb the ladder sentence → list → table → figure and stop
   at the rung that answers the question (rule 15).
9. No number measured on a named dataset is written into prose; an algorithm
   number such as a default or a property of the formula stays (rule 14).
10. A survey ends with a ranked entry path (O9), and repeated things hold the
    same shape in the same order (O17).
11. The tics above are *searched for*, not read for: crucial, key, worth,
    honestly, honest, delve, leverage, robust, seamless, "not just", "it is worth
    noting", "here is why", "the point is", matters, "the difference matters".

---

# Part 2 — The rules

Every rule below is derived from an edit he actually made. The cited commits and
diffs are the evidence, and when a rule and the evidence disagree, the evidence
wins.

## 1. Do not describe the document inside the document

Cut on 2026-08-11 from `synthetic-data-checking-review.Rmd`: "is separate from
the literature on generating it, has its own vocabulary, and is easy to reinvent
badly if you have not read it" / "written as a tutorial rather than a survey" /
"and says where `synpmx` fits among them" / "Current as of August 2026".

What survived: "This article is a tutorial on these methods and at each step it
states which measures `synpmx` implements, which it does not, and why." One
sentence, describing content rather than the author's intentions. A reader who
is reading the document does not need to be sold on it.

## 2. A heading names its subject

| Deleted | Replaced with |
|---|---|
| The fix, and it is the same fix everywhere | Training vs Control Set |
| What it costs in pharmacometrics, honestly | Applications of control set to pharmacometrics datasets |
| Why this is hard: population facts versus patient facts | Introduction |
| How synthetic data is made | Algorithms for Generating Synthetic Data |
| Running it on your own study | Generating Synthetic Data with AVATAR algorithm |
| The checks to run, most of which do not exist yet | B5b. The source-side census |

No stance words (`honestly`, `worth having`), no narrative beats (`The fix`,
`Now the part that needs the holdout`), no colon-plus-restatement. A reader
scanning the table of contents should find a topic, not follow a plot. He writes
headings in title case, and where a document is organized around numbered items
the heading carries the number.

## 3. Cut transitional stage directions

Deleted: "Here is why the separation is hard." / "Now make it a measurement
problem." / "If that feels familiar, it should:" / "Here is the part that closes
the loop." These announce a move instead of making it. Delete the sentence and
start the paragraph at its content.

## 4. Repeat the noun; do not lean on a pronoun

He *adds* words for this, while deleting words everywhere else.

- "**You cannot tell from the synthetic data alone.**" became "**You cannot tell
  from the synthetic data alone if a leak of individual information occurred.**"
- "...only person who could have qualified for it, it is." became "...only person
  who could have qualified for it, then it is a leak."

A sentence that depends on the previous sentence for its subject fails when the
reader arrives from the table of contents, and this reader does arrive from the
table of contents. He also splits appositives rather than nesting them: "AVATAR,
called by `synpmx_avatar()` needs two things" became "AVATAR is called by
`synpmx_avatar()`. It needs two things." (`c972373`).

## 6. State a recommendation as an instruction

"**Hold some patients out.** Split the real cohort in two: a *training* set the
generator is allowed to use, and a *control* set it never sees." became "**To
assess a synthetic data generating algorithm, split real cohort into a training
and control (holdout) set.**" The bolded clause carries the action and the
definitions ride along inside it. See rule 10: the verdict comes first, the
nuance second.

Where the reader has more than one action available, give both. He edited "the
right answer is to leave it undeclared, which is what the run above does" into
"leave it undeclared or to correct the censoring variable."

## 8. Punctuation

- Em dashes are for a genuine parenthesis, not for a rhetorical pause. Most of
  his edits replace one with a period or a comma. The one measured target comes
  from `42d6d02`, which took an 846-line vignette from 71 em dashes to 19, about
  one per forty lines.

## 9. Numbers survive; adjectives do not

"a *median local cloaking of 11*", "253 patients", "`k` = 5 donors" all survive
review untouched. "considerably", "genuinely", "wildly", "close to meaningless",
"the elegant part" are what gets cut. Prefer the measurement to the
characterization of the measurement.

## 10. A verdict leads, and the verdict may be a hedge

The four use-case lines in `README.md` each open with a marker and a verdict in
parentheses: **✅ Develop code**, **✅ Teaching tool (Yes)**, **⚠️ Send data past
a trust boundary (Use Caution)**, **❌ Answer scientific questions (No)**. The
nuance follows within the same line — "the formal privacy-protecting methods
provided with this package are illustrative, but not audited" is still there,
after the verdict rather than softening it.

**An earlier version of this rule said he converts hedged verdicts into binary
ones. He rejected it in writing and reverted the example.** The trust-boundary
row was Claude's "Only with care", became his "No", and is now "⚠️ Use Caution".
What the evidence supports is the *marker* first so the line is scannable. Do not
flatten a real "it depends" into a "No" to satisfy this rule.

The marker generalizes past prose: `synpmx_scorecard_datatable()` (`9633859`)
colours `FAIL` red and `review` orange, because five verdicts among thirty-odd
rows were being found by reading all of them. Mark a verdict that sits inside a
body of output.

## 11. State the out-of-scope, and state it bluntly, once

"Maybe I want to be explicit about this is not about scientific discovery." His
own `README.md` rewrite replaced a four-row table of hedged verdicts with four
bolded lines carrying ✅ / ⚠️ / ❌ markers. Every explanatory document should
carry an explicit out-of-scope statement, unqualified. The "why almost none of
this is `synpmx`'s problem" subsection in
`vignettes/articles/synthetic-data-checking-review.Rmd` exists because of this.

It belongs at the document level, not in each section. He deleted "It does not
assess scientific validity, and it is not a privacy check." from underneath
`validate_pmx()`, where it was a third statement of a scope already declared.

## 12. Thin at the entry point; literal over coined

`f8c22f1` cut a fully annotated 13-argument `synpmx_avatar()` call down to four
arguments and removed the multi-line hanging comments explaining `dvid` and
`dose_covariate`. The same commit deleted the coinage "The declaration is also
the **manifest of what survives**" in favour of "The function drops every column
that is not described."

`c972373` is the same edit a week later: the paragraph arguing why `remotes` is
the right installer, and the paragraph on pinning a branch and building
vignettes, both cut from `README.md`. Show the minimum that works; detail
belongs one document deeper. Prefer literal description to coined framing — the
metaphors reached for to make something memorable are what he deletes first. The
contract table in Part 1 says where this applies and where O10 overrides it.

## 14. The document names the questions; the output carries the answers

`d333313`, his own edit. The scorecard vignette led with an eighteen-row table
of `# | Question | What to run | Reads | Pass`, restating in static prose what
`synpmx_scorecard()` prints on a real run. He cut it to `# | Question` and
replaced the other three columns with five bullets saying what the function's
own output contains.

A number written into prose beside a function that computes it will go stale,
and the reader cannot tell which is current. Name the question in the document,
run the function, let the output answer. The cross-document contract in
`AGENTS.md` now has this shape: every row the function emits has a section under
the same identifier, stating the criterion the function actually scores.

**Which numbers this applies to: the dataset-specific ones.** A figure measured
on a named study — 63 of 120 `mavoglurant` avatars flagged, 29 of 59 `pheno_sd`
infants truncated, `theo_md`'s between-subject variability by cap setting — goes
stale on the next default change, is about a dataset that is not the reader's,
and is what a function already prints on a run. It comes out. A number that is a
property of the algorithm — `k` = 5, `max_donor_weight` = 0.50, the 15-point
grid, the uncapped weight formula putting a median 58% of an avatar into one
donor — holds whatever study is loaded, and stays. His instruction on 2026-08-15,
revising `avatar-algorithm.Rmd`: "I'd prefer to remove references to specific
numbers on datasets. I don't think they're needed." Where the per-dataset number
is the point, name the dataset qualitatively and let the run report the figure.

This does not weaken rule 9. Rule 9 governs the choice between a number and an
adjective, and a number still wins every time; the survivals cited there —
"253 patients", "a median local cloaking of 11" — were in documents working that
dataset in front of the reader, which is not the same as a measurement asserted
about a study the page never runs.

## 15. Past a table, draw it

`cb036bc`: `compare_pmx_distributions()` printed nine columns per endpoint and
per covariate, "which is not how anyone judges whether two distributions agree",
and now draws source against synthetic by default.

The full ladder is sentence → list → table → figure. A table answers *what is
the value*; a figure answers *what is the shape*, and no table of moments does —
one mode and two modes with the same mean and spread give identical rows. Where
the question is about a distribution, a trajectory or a schedule, draw it and
let the table be the supporting detail.

## 16. Fix the wreckage of his edits, and restore nothing

He edits fast and leaves debris: `ollowing`, `hat data`, `teh` and `placae`
across two commits, a dangling "either." where a sentence was cut in half, and
"It is the shaped like a real study report" where "only public dataset" came out
of the middle of a clause. Repair the broken sentence and the mistyped word on
the next pass over that file, silently. Never reinstate what he removed, never
reflow the paragraph around it (rule 8), and do not read the debris as license
to rewrite the passage he has just rewritten.

---

# Part 3 — The reader

## The original charter, in his words

> *Written 2026-08-05. Kept verbatim; the document names have since changed.*
>
> I often ask Claude to create good explanatory documents: Readme, literature
> reviews, etc., as in the vignettes for this project.
>
> Usually, the first few drafts, I do not fully understand, I have a lot of
> questions. There may be technical material I don't know. Or just definitions.
> And it requires a lot of back and forth with Claude to get something that
> answers my question.
>
> I'd like the AI here to start developing a theory of mind for me around how to
> provide good explanations in vignettes and articles that will be accessible by
> humans. To do that, start by using this document. Keep a structured set of
> observations based on the questions I ask and the documents I create.

## Where the evidence comes from

Three sources, in decreasing order of reliability.

1. **His own commits editing Claude's prose.** `f8c22f1 "simplify readme"`
   (−123/+31), the README rewrite in `0edffdc`, `c972373 "update readme"`
   (−21/+16), and `d333313 "updating scorecard and its vignette"`. These are
   revealed preference and outrank anything he says about his preferences, and
   they are recognizable by their commit messages: lower case, a few words,
   typos left in.
2. **The verbatim questions in the 2026-08-04/05 session.** A dense list of
   "I don't know X" / "I'm not sure I get Y" / "I don't care about Z".
3. **Rules he has written into `AGENTS.md`** — especially the acronym rule and
   the README-ownership rule. Each of those is a scar from earlier friction.

**Standing caveat.** As of 2026-08-14 he has read and hand-edited `README.md`
and the front of `avatar-scorecard.Rmd`, and has **not** read the
two literature-review articles or `avatar-algorithm.Rmd`, both queued in
`design/_TODO_owner.md`. Anything citing those is evidence about *what he asked
for*, not that the result worked. Mark what turns out to be wrong.

## O1 — He asks for the mechanism, not the citation

**Evidence.** "I don't know the measures by Raab/Nowok/Dibben in 2024 that
shipped in synthpop. I don't know what Linability is. Or the WP criterion."
"I'm not sure what pMSE is." "What is authenticity?" In every one of those
cases the draft had already given the name, the authors, the year, and a
one-sentence gloss. That was not enough.

**What to do.** A named method is not explained until the reader could either
compute it or recognize a bad value. The working test: *what is calculated, from
what inputs, and what does a good number look like?* The pMSE passage that
survived is four numbered mechanical steps; the version that failed was
"the standard measure is pMSE (Snoke et al. 2018)".

## O2 — Implementing a method is not understanding it

**Evidence.** "I haven't really learned about adversarial accuracy yet (even
though you implemented it)." `compare_pmx_proximity()` had been in the package,
documented and tested, for weeks.

**What to do.** Never assume the package's own statistics are understood because
the package computes them. Explain in-house methods with the same care as
external ones. The parenthetical also reads as slightly self-deprecating, so
explain without any framing that implies he should have known already.

## O3 — Telling him he has reinvented something is welcome, not a criticism

**Evidence.** "I see I'm inventing something rather than learning from what's
been done before." This was his reaction to being shown that his hand-derived B5
checks were most of `synthpop`'s RepU/DiSCO. The tone is relief, and the
follow-up was to ask for *more* prior art, not less.

**What to do.** When a home-grown idea has a published name, say so early and
plainly: "the thing you already do is called X." Treat locating prior art as a
deliverable in its own right, not as a politeness. This is probably the single
highest-value thing Claude can do for him on a literature document.

## O4 — "I don't care about X" and "I don't get X" arrive in one sentence and need opposite responses

**Evidence.** One message contained "I honestly don't care that much about the
distributions" (a **scope** decision), "I'm not sure what pMSE is" (an
**explanation** request), and "Regarding coverage, I'm not sure I get what
you're talking about. On did we lose the tails, is the idea we want to?"
(**both** — explain the concept, then rule on whether it matters).

**What to do.** Separate the two explicitly. A scope statement changes what the
document *claims*; an explanation request changes what it *teaches*. Conflating
them cuts a section he did not understand but did want, or explains at length
something he had already ruled out.

## O8 — He is an expert in one half of every document and a novice in the other

**Evidence.** He needed no explanation of PK, PD, BLOQ, trough samples, mg/kg
dosing, arms, or dropout. He needed full definitions of linkability, WP29, pMSE,
authenticity, local cloaking, and adversarial accuracy. The line falls exactly at
the pharmacometrics / statistical-disclosure-control boundary.

**What to do.** Make that boundary conscious rather than accidental. The
pharmacometric side can be terse to the point of shorthand and the
privacy/statistics side must be taught from zero: **expand every acronym, and
fully explain every named method that comes from outside pharmacometrics.**
Uniform explanation depth is wrong in both directions at once — the expertise
reversal effect, in Part 4.

## O9 — "Where do I start?" is a literal request

**Evidence.** "I don't know these different methods you described. I'm not sure
where to start."

**What to do.** Any survey should end with a ranked entry path: read these N
things, in this order, and one clause on why each. The four-item list closing the
literature review exists for this reason. A flat alphabetical reference list does
not answer the question he actually asked.

## O10 — He optimizes for fewer review rounds, which fights the thinness rule

**Evidence.** "I'd first like to make them more complete so that I iterate less."
He will accept a longer first draft if it reduces the number of passes.

**Resolution of the conflict.** The tolerance for length is a function of the
document *tier*, not of his mood, and the contract table in Part 1 is where the
tier is written down. Getting it backwards produced the README he cut in half.

## O11 — A mangled term is a reliable signal that the concept has not landed

**Evidence.** "local cleaking", "Linability", "the WP criterion",
"synpmx_validate" (the function is `validate_pmx()`).

**What to do.** Do not silently correct and move on. A term he has half-absorbed
is one he met once and has not yet used. Also note the `synpmx_validate` slip: he
holds the *concept* ("is the dataset even validated") and reconstructs the name
from it. So documents should lead with what a function does and let the name
follow, not the other way round.

## O12 — He reviews by running things and by looking at output

**Evidence.** `_TODO_owner.md`: "Try out on real data and apply checks (pit,
eci), see if I can follow all steps." The render-and-open-in-browser loop he set
up for `avatar-algorithm.Rmd`. And the entire thesis of the checks vignette —
every defect was found by looking at output, not by reasoning about the
algorithm.

**What to do.** Prefer a document that *computes* its claims on a real dataset
over one that asserts them. `42d6d02` is the shape that stuck: run
`synpmx_scorecard()` on both datasets immediately after reading them, so the
reader meets two filled-in cards before any explanation of what a check asks.

## O14 — Essay-shaped sections do not earn their length

**Evidence.** He asked nothing at all about sections E ("what these checks cannot
tell you") and F ("check the output, not the algorithm") of the checks vignette,
the two most essay-like parts of the corpus. This file recorded that as
ambiguous — they worked, or he skipped them — and asked him.

[Andy Note] These sections were not good and were significantly changed.  F removed altogether.

**What to do.** Silence on a narrative section is not approval. Section F was
deleted outright in `c17f23e` and section E lost its label; what replaced them is
a numbered subsection per check, each opening with what it asks and what counts
as passing (`58fe067`). Where a document is organized around a list of items,
give every item its own numbered subsection and let the argument live inside it.
Prose that has to stand alone should be short, under a heading that names a
subject rather than a stance.

## O16 — He asks for the design tradeoff to be argued, not just implemented

**Evidence.** 2026-08-13, on the discrete-endpoint defect: *"Implement a check
and a fix for when LIDV is binary or ordinal or categorical. And actually, give
a thought of whether it's reasonable for this to be determined from the data or
whether it should be specified in the pmxroles somehow."* The instruction to
build came first and was unambiguous; the second sentence reopened the interface
question the first had already implied an answer to. He wanted the alternative
weighed before the code existed. Note also that he named the symptom in his own
terms rather than the ID of the issue just filed, and asked for **a check and a
fix** in one sentence — per O12, a fix he cannot see fire is half a delivery.

**What to do.** When a task has an inference-versus-declaration fork — or any
comparable interface choice — state the fork and the answer in the reply, with
the reason, in a few sentences. Do not present it as an open question to be
resolved before starting, and do not bury it in a code comment. The answer that
fit here was *both*: infer by default where the data answers the question
outright, and offer the declaration as the override, which is `dose_covariate`
one step further along. Cite the existing precedent when there is one; it is the
strongest argument available and it keeps the API consistent.

## O17 — He reads by comparing, so repeated things must hold their shape

**Evidence.** `27da2d9` and `58fe067`, both his: every scorecard now emits all
its rows even where the roles gave a check nothing to ask, because "two cards
that hold different rows cannot be compared, and the absence reads as a check
that passed when it means the question was never asked". `c5c8348` is the same
instinct at document scale — the two `xgxr` study-shaped datasets moved from last
to first in `avatar-public-data-examples.Rmd`, so the six sparser sets after them are
read against something familiar.

**What to do.** Anything appearing more than once — a card, a dataset section, a
worked example — holds the same shape in the same order, and says explicitly
when a slot is empty rather than omitting it. Order a sequence so the first item
teaches the ones after it, rather than by taxonomy or by date written.

---

# Part 4 — Where these came from

Browsed 2026-08-05. Four sources, each already applied above.

- [Diátaxis](https://diataxis.fr/) — the four documentation kinds in Part 1, and
  the claim that a page serving two of them serves neither reader. It diagnoses
  O9: the literature review was **explanation** and he needed **tutorial**.
- [Expertise reversal effect](https://en.wikipedia.org/wiki/Expertise_reversal_effect)
  — O8 with an evidence base. Support that measurably helps a low-knowledge
  reader measurably *hurts* a high-knowledge one, competing for working memory.
- [Curse of knowledge](https://earthly.dev/blog/curse-of-knowledge/) — attributed
  to *fluency misattribution*, the writer misreading his own ease of retrieval as
  the reader's. The drafts that failed here were carefully written.
- [Hedging, verbosity and over-elaboration](https://passo.uno/whats-wrong-ai-generated-docs/)
  — the catalogued LLM pathologies, which match his edits closely enough to be a
  default to correct rather than a preference to accommodate.

---

# Part 5 — Open questions

Things that cannot be inferred from the evidence available, in order of how much
they would change future drafts. Two earlier questions are closed: O14 resolved
itself against the narrative sections, and the ✅/⚠️/❌ marker style did
generalize, as colour on the scorecard (rule 10).

1. **Is the mathematics helpful or is it noise?** The literature review carries
   the adversarial-accuracy formula in display math. It could as easily be three
   sentences of English. [Andy Note - The Math is helpful]
2. **Inline definitions or a glossary?** Every term is defined inline at first
   use, which is why that section is long. `learning/GLOSSARY.md` is yours and
   Claude does not write to it, so a shipped glossary would be a third place a
   definition lives. [Andy Note - Inline definitions]
3. **What is the length ceiling for a shipped vignette?** The contract table says
   `avatar-algorithm.Rmd` may be exhaustive, and it is 2,114 lines. Whether that
   is fine because nobody reads reference material end to end is not answerable
   until you have read it.

**One convention still to adopt.** Record what was tried and rejected. A way of
explaining something that fails review is more informative than the version that
passed, and it is currently lost; two lines per rejection is enough. The one
that survives is the reverted verdict in rule 10.
