---
name: Writing for Andy
description: Use this skill when drafting a new document or substantially rewriting one for Andy — a blog post, a resource page, a README, or a long summary. Describes who the reader is and the writing rules his edits established.
---

# Writing for Andy

Who the reader is, and how to write a document he will not have to send back.

**When to read this.** When asked to draft a new document, or to substantially
rewrite an existing one — a blog post, a resource page, a slide deck,
`README.md`, or a long summary. Re-read Part 1's tic list, or at least re-run
its search, before handing over any document drafted later in the same session. Not for code, test, or configuration work, and not as a session
preamble. Part 1 is what to do; Parts 2 and 3 are the evidence behind it. The
machine-prose tics in Part 1 apply to *everything*, including conversation,
commit messages and comments.

**Who updates it.** Andy, by asking for a review of recent history, about once a
month. Do not append to it during a session; say in the conversation what looks
wrong and let him decide. He answers in place, marked `[Andy Note]`, left where
the wrong claim was.

**Numbering.** Two independent series: `O###` for observations about the reader,
plain numbers for the writing rules. The gaps in both are deliberate. The
numbers are how he refers to them in conversation, so do not renumber to close
them.

**Changes here.** 2026-09-02, at Andy's instruction: checklist item 11 became
a search to run rather than a list to remember, after a slide shipped with a
tic that was already on the list.

**Origin.** Developed in the `synpmx` repository during August 2026, from
Andy's hand edits of Claude-drafted prose there. Copied here 2026-08-28 with
the synpmx-specific material removed; the synpmx copy keeps the full evidence —
commit hashes, the per-document contract table, and the update log.

---

# Part 1 — Before handing over a draft

## The document contract

Documentation comes in four kinds, and a page that tries to be two of them
serves neither reader: a **tutorial** teaches by doing, a **how-to** accomplishes
one task, a **reference** answers a lookup, an **explanation** says why. Decide
which one a document is before writing it, and let that decide how long it may
be: entry points (a README, a first-run tutorial, an explanation of why) stay
thin; references may be exhaustive; a how-to is as long as its task needs.

The kind-and-length decision is the mechanical form of the O10 / rule 12
tension: he wants a draft complete enough that he iterates less, and he cuts
shipped entry points in half. The tier decides which applies, before drafting
rather than in review. Where a project accumulates several documents, write the
contract down as a table — document, reader, kind, permitted length — and settle
new drafts against it.

## The machine-prose tics

Widely reported markers of machine-written prose, several of which have appeared
in Claude's own drafts for him. Unlike the rest of this file, the list applies
to *everything* — conversation, commit messages and code comments as much as
documents.

- **Contrastive antithesis.** "It is not X, it is Y", "not a bug, a feature". He
  deletes these by hand: "dropped *rather than quietly copied out of a real
  patient*" became "dropped".
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
  place of a literal description ("the function drops every column that is not
  described"). Rule 12 says it again.
- **The aphoristic section opener.** "The tier that is easy to skip and
  embarrassing to fail." "Two public datasets, and the second one is the point."
  Both deleted by hand. A section starts at its content.
- **Sycophancy.** No "great question", no praising the request, no announcing
  that something is a strong idea before doing it.

## The checklist

1. The document's kind and length are settled against the contract above.
2. Every heading names a subject (rule 2).
3. Each paragraph's first sentence stands alone with the topic explicit (rule 4).
4. Every acronym expanded at first use, and every method from outside his field
   explained from zero (O8), answering *what is calculated, from what inputs,
   and what does a good number look like* (O1).
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
11. The tics above are *searched for*, not read for. Run the search over the
    file you changed, as the last step before handing it over. Reading the list
    once, early in a session, does not survive to the end of one.

    ```
    grep -nEi "crucial|\bkey\b|\bworth\b|honestly|honest|delve|leverage|robust|\
    seamless|not just|it is worth noting|here is why|the point is|\
    matter(s|ed|ing)?\b|the difference matters|underscore|highlight|testament|\
    pivotal|fundamental|ultimately|in conclusion|the takeaway" <file>
    ```

    Search the whole file, speaker notes and comments included. The grep catches
    single words; four tics it cannot catch are contrastive antithesis ("not a
    crash, a plot that looked fine"), the rule of three, symmetric sentence
    pairs, and the aphoristic section opener. Those are read for, on a second
    pass.

    **Evidence.** On 2026-09-02 a slide shipped reading "wrong in the way that
    mattered", and a speaker note reading "Not a crash. A plot that looked fine
    and was not." `matters` was already on the list above. The guide had been
    read that session; the search had not been run on that file.

---

# Part 2 — The rules

Every rule below is derived from an edit he actually made. When a rule and the
evidence disagree, the evidence wins.

## 1. Do not describe the document inside the document

Cut by hand from a literature-review draft: "is separate from the literature on
generating it, has its own vocabulary, and is easy to reinvent badly if you have
not read it" / "written as a tutorial rather than a survey" / "Current as of
August 2026".

What survived: one sentence describing content rather than the author's
intentions — what the article covers and what it states at each step. A reader
who is reading the document does not need to be sold on it.

## 2. A heading names its subject

| Deleted | Replaced with |
|---|---|
| The fix, and it is the same fix everywhere | Training vs Control Set |
| What it costs in pharmacometrics, honestly | Applications of control set to pharmacometrics datasets |
| Why this is hard: population facts versus patient facts | Introduction |
| How synthetic data is made | Algorithms for Generating Synthetic Data |

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
table of contents. He also splits appositives rather than nesting them: "X,
called by `f()` needs two things" became "X is called by `f()`. It needs two
things."

## 6. State a recommendation as an instruction

"**Hold some patients out.** Split the real cohort in two: a *training* set the
generator is allowed to use, and a *control* set it never sees." became "**To
assess a synthetic data generating algorithm, split real cohort into a training
and control (holdout) set.**" The bolded clause carries the action and the
definitions ride along inside it. See rule 10: the verdict comes first, the
nuance second.

Where the reader has more than one action available, give both. He edited "the
right answer is to leave it undeclared, which is what the run above does" into
an instruction naming both options.

## 8. Punctuation

- Em dashes are for a genuine parenthesis, not for a rhetorical pause. Most of
  his edits replace one with a period or a comma. The one measured target comes
  from an edit of his that took an 846-line document from 71 em dashes to 19,
  about one per forty lines.

## 9. Numbers survive; adjectives do not

"a *median local cloaking of 11*", "253 patients", "`k` = 5 donors" all survive
review untouched. "considerably", "genuinely", "wildly", "close to meaningless",
"the elegant part" are what gets cut. Prefer the measurement to the
characterization of the measurement.

## 10. A verdict leads, and the verdict may be a hedge

His README rewrite gave each use-case line a marker and a verdict in
parentheses: **✅ Develop code**, **✅ Teaching tool (Yes)**, **⚠️ Send data past
a trust boundary (Use Caution)**, **❌ Answer scientific questions (No)**. The
nuance follows within the same line, after the verdict rather than softening it.

**An earlier version of this rule said he converts hedged verdicts into binary
ones. He rejected it in writing and reverted the example.** The trust-boundary
row was Claude's "Only with care", became his "No", and is now "⚠️ Use Caution".
What the evidence supports is the *marker* first so the line is scannable. Do not
flatten a real "it depends" into a "No" to satisfy this rule.

The marker generalizes past prose: a results table he reviewed now colours
`FAIL` red and `review` orange, because five verdicts among thirty-odd rows were
being found by reading all of them. Mark a verdict that sits inside a body of
output.

## 11. State the out-of-scope, and state it bluntly, once

"Maybe I want to be explicit about this is not about scientific discovery." His
own README rewrite replaced a four-row table of hedged verdicts with four bolded
lines carrying ✅ / ⚠️ / ❌ markers. Every explanatory document should carry an
explicit out-of-scope statement, unqualified.

It belongs at the document level, not in each section. He deleted a third
statement of a scope already declared from underneath a function's
documentation.

## 12. Thin at the entry point; literal over coined

One edit of his cut a fully annotated 13-argument function call down to four
arguments and removed the multi-line hanging comments explaining the rest. The
same edit deleted the coinage "The declaration is also the **manifest of what
survives**" in favour of "The function drops every column that is not
described." A week later he made the same edit again: the paragraph arguing why
one installer is the right one, and the paragraph on pinning a branch, both cut
from a README.

Show the minimum that works; detail belongs one document deeper. Prefer literal
description to coined framing — the metaphors reached for to make something
memorable are what he deletes first. The contract in Part 1 says where this
applies and where O10 overrides it.

## 14. The document names the questions; the output carries the answers

His own edit. A document led with an eighteen-row table of
`# | Question | What to run | Reads | Pass`, restating in static prose what a
function prints on a real run. He cut it to `# | Question` and replaced the
other three columns with five bullets saying what the function's own output
contains.

A number written into prose beside a function that computes it will go stale,
and the reader cannot tell which is current. Name the question in the document,
run the function, let the output answer.

**Which numbers this applies to: the dataset-specific ones.** A figure measured
on a named study goes stale on the next default change, is about a dataset that
is not the reader's, and is what a function already prints on a run. It comes
out. A number that is a property of the algorithm — a default, a grid size, a
property of the formula — holds whatever study is loaded, and stays. His
instruction on 2026-08-15: "I'd prefer to remove references to specific numbers
on datasets. I don't think they're needed." Where the per-dataset number is the
point, name the dataset qualitatively and let the run report the figure.

This does not weaken rule 9. Rule 9 governs the choice between a number and an
adjective, and a number still wins every time; the survivals cited there were in
documents working that dataset in front of the reader, which is not the same as
a measurement asserted about a study the page never runs.

## 15. Past a table, draw it

A comparison function he reviewed printed nine columns per endpoint and per
covariate, "which is not how anyone judges whether two distributions agree", and
now draws source against synthetic by default.

The full ladder is sentence → list → table → figure. A table answers *what is
the value*; a figure answers *what is the shape*, and no table of moments does —
one mode and two modes with the same mean and spread give identical rows. Where
the question is about a distribution, a trajectory or a schedule, draw it and
let the table be the supporting detail.

## 16. Fix the wreckage of his edits, and restore nothing

He edits fast and leaves debris: `ollowing`, `hat data`, `teh` and `placae`
across two commits, a dangling "either." where a sentence was cut in half, and
"It is the shaped like a real study report" where a phrase came out of the
middle of a clause. Repair the broken sentence and the mistyped word on the next
pass over that file, silently. Never reinstate what he removed, never reflow the
paragraph around it (rule 8), and do not read the debris as license to rewrite
the passage he has just rewritten.

---

# Part 3 — The reader

## The original charter, in his words

> *Written 2026-08-05, in the synpmx repository. Kept verbatim.*
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

1. **His own commits editing Claude's prose.** These are revealed preference and
   outrank anything he says about his preferences, and they are recognizable by
   their commit messages: lower case, a few words, typos left in.
2. **His verbatim questions in session.** A dense list of "I don't know X" /
   "I'm not sure I get Y" / "I don't care about Z".
3. **Rules he has written into a repository's agent instructions.** Each of
   those is a scar from earlier friction.

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
though you implemented it)." The function computing it had been in his package,
documented and tested, for weeks.

**What to do.** Never assume a project's own statistics are understood because
the project computes them. Explain in-house methods with the same care as
external ones. The parenthetical also reads as slightly self-deprecating, so
explain without any framing that implies he should have known already.

## O3 — Telling him he has reinvented something is welcome, not a criticism

**Evidence.** "I see I'm inventing something rather than learning from what's
been done before." This was his reaction to being shown that his hand-derived
checks were most of an existing package's published measures. The tone is
relief, and the follow-up was to ask for *more* prior art, not less.

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
authenticity, local cloaking, and adversarial accuracy. The line falls exactly
at the boundary of his field: pharmacometrics and biostatistics on one side,
adjacent specialties such as statistical disclosure control on the other.

**What to do.** Make that boundary conscious rather than accidental. His own
side can be terse to the point of shorthand and the other side must be taught
from zero: **expand every acronym, and fully explain every named method that
comes from outside his field.** Uniform explanation depth is wrong in both
directions at once — the expertise reversal effect, in Part 4.

## O9 — "Where do I start?" is a literal request

**Evidence.** "I don't know these different methods you described. I'm not sure
where to start."

**What to do.** Any survey should end with a ranked entry path: read these N
things, in this order, and one clause on why each. A flat alphabetical reference
list does not answer the question he actually asked.

## O10 — He optimizes for fewer review rounds, which fights the thinness rule

**Evidence.** "I'd first like to make them more complete so that I iterate less."
He will accept a longer first draft if it reduces the number of passes.

**Resolution of the conflict.** The tolerance for length is a function of the
document *tier*, not of his mood, and the contract in Part 1 is where the tier
is written down. Getting it backwards produced a README he cut in half.

## O11 — A mangled term is a reliable signal that the concept has not landed

**Evidence.** "local cleaking", "Linability", "the WP criterion", and a function
name reconstructed from its purpose rather than recalled.

**What to do.** Do not silently correct and move on. A term he has half-absorbed
is one he met once and has not yet used. The function-name slip also shows he
holds the *concept* and reconstructs the name from it, so documents should lead
with what a function does and let the name follow, not the other way round.

## O12 — He reviews by running things and by looking at output

**Evidence.** His own to-do notes: "Try out on real data and apply checks, see
if I can follow all steps." The render-and-open-in-browser loop he set up for
reviewing long documents. And every defect in one whole document was found by
looking at output, not by reasoning about the algorithm.

**What to do.** Prefer a document that *computes* its claims on a real dataset
over one that asserts them. The shape that stuck: run the summary function on
the data immediately after reading it, so the reader meets filled-in output
before any explanation of what a check asks.

## O14 — Essay-shaped sections do not earn their length

**Evidence.** He asked nothing at all about the two most essay-like sections of
a long document ("what these checks cannot tell you" and "check the output, not
the algorithm"). This file recorded that as ambiguous — they worked, or he
skipped them — and asked him.

[Andy Note] These sections were not good and were significantly changed.  F removed altogether.

**What to do.** Silence on a narrative section is not approval. One of those
sections was deleted outright and the other lost its label; what replaced them
is a numbered subsection per item, each opening with what it asks and what
counts as passing. Where a document is organized around a list of items, give
every item its own numbered subsection and let the argument live inside it.
Prose that has to stand alone should be short, under a heading that names a
subject rather than a stance.

## O16 — He asks for the design tradeoff to be argued, not just implemented

**Evidence.** On a defect in handling discrete endpoints: *"Implement a check
and a fix for when [the endpoint] is binary or ordinal or categorical. And
actually, give a thought of whether it's reasonable for this to be determined
from the data or whether it should be specified [in the metadata] somehow."*
The instruction to build came first and was unambiguous; the second sentence
reopened the interface question the first had already implied an answer to. He
wanted the alternative weighed before the code existed. Note also that he named
the symptom in his own terms rather than the ID of the issue just filed, and
asked for **a check and a fix** in one sentence — per O12, a fix he cannot see
fire is half a delivery.

**What to do.** When a task has an inference-versus-declaration fork — or any
comparable interface choice — state the fork and the answer in the reply, with
the reason, in a few sentences. Do not present it as an open question to be
resolved before starting, and do not bury it in a code comment. The answer that
fit here was *both*: infer by default where the data answers the question
outright, and offer the declaration as the override. Cite the existing precedent
when there is one; it is the strongest argument available and it keeps the API
consistent.

## O17 — He reads by comparing, so repeated things must hold their shape

**Evidence.** Two commits of his made a summary report emit all its rows even
where the inputs gave a check nothing to ask, because "two cards that hold
different rows cannot be compared, and the absence reads as a check that passed
when it means the question was never asked". A third is the same instinct at
document scale — the two most familiar-shaped examples moved from last to first
in a reference document, so the sparser ones after them are read against
something familiar.

**What to do.** Anything appearing more than once — a card, a dataset section, a
worked example — holds the same shape in the same order, and says explicitly
when a slot is empty rather than omitting it. Order a sequence so the first item
teaches the ones after it, rather than by taxonomy or by date written.

---

# Part 4 — Where these came from

Browsed 2026-08-05. Four sources, each already applied above.

- [Diátaxis](https://diataxis.fr/) — the four documentation kinds in Part 1, and
  the claim that a page serving two of them serves neither reader. It diagnoses
  O9: a literature review he sent back was **explanation** and he needed
  **tutorial**.
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
generalize, as colour on tabular output (rule 10).

1. **Is the mathematics helpful or is it noise?** One literature review carries
   a formula in display math. It could as easily be three sentences of English.
   [Andy Note - The Math is helpful]
2. **Inline definitions or a glossary?** Every term is defined inline at first
   use, which is why sections that teach new methods run long. A shipped
   glossary would be a second place a definition lives.
   [Andy Note - Inline definitions]

**One convention still to adopt.** Record what was tried and rejected. A way of
explaining something that fails review is more informative than the version that
passed, and it is currently lost; two lines per rejection is enough. The one
that survives is the reverted verdict in rule 10.
