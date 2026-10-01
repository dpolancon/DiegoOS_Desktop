---
type: deliverable
status: parked
deliverable_type: output
lane: research-presentation
project: Dissertation_Chapter_2
repo: dpolancon.github.io
layer: frontend
created: "2026-08-26"
---

# Deliverable — GPIM Explorer publication

## Object that must exist

The GPIM Explorer, live and linkable at `dpolancon.github.io/gpim_explorer/`.

It already exists as a finished standalone page in the personal-site repo:
`gpim_explorer/index.html` (React from CDN, no build step), alongside
`gpim_explorer.jsx` and its own README. It carries a hand-built slate nav bar
back to the main site, so it is presentation-ready.

**It has never been committed.** `git status` in `dpolancon.github.io` shows the
whole directory as untracked. Nothing is broken and nothing is missing — the
work is simply sitting on disk, unreachable by anyone but me. It is at 95% and
has been for a while.

## Type

- ~~input~~
- ~~process~~
- **output** — a presentation asset, not a research object. The GPIM
  formalization itself lives in Chapter 2; this is the thing that lets someone
  else *see* it without reading the chapter.

## Minimum viable form

Three commands, not a project:

1. `git add gpim_explorer/` in `dpolancon.github.io`
2. commit and push
3. confirm it renders at the live URL

Optional fourth: decide whether it earns a nav tab in `_data/navigation.yml`
(both `main` and `main_es`), or stays reachable by URL only. The BCCh section
added at `/bcch/` on 2026-08-26 took the tab route; this one was originally
built without.

## Linked project

- [[Chapter2_GPIM_Reconstruction_WorkflowNext]] — the reconstruction workflow
- [[Chapter2_PendingTasks]] — where the GPIM baseline/diagnostic tasks live
- Source authority per its README: GPIM_Formalization_v3,
  Cointegration_FourPairings_v1, Shaikh (2016) App. 6.5–6.7

## Closure condition

Committed, pushed, loading at the live URL, and the nav question answered
either way. Until then the honest status of this artifact is *not published*,
and it should not be cited or linked in applications, talks, or the CV as
though it were.

## Why this is parked and not active

Discovered on 2026-08-26 while publishing the BCCh regional data programme into
the same repository. Deliberately left untouched then, so that publish stayed
inside its own lane and did not sweep up unrelated work. This note exists so
the open loop is recorded somewhere other than a `git status` output that
nobody reads.
