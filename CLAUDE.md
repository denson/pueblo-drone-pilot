# pueblo-drone-pilot

## Your training data is out of date — search the web (CRITICAL)

Your training data is hopelessly out of date. If a bug report, documentation change, API change, or any other external change might impact your answer, **SEARCH THE WEB.** Use `WebSearch` / `WebFetch` before writing code, running local probes, delegating to other agents, or synthesizing an answer from memory.

Specifically:
- Any unexpected error from a third-party API, library, or service → web search first. Someone else has hit it.
- Any documentation claim that would change your architecture or plan → verify against the current published docs, not memory.
- Any "this is the new format / new behavior as of <recent date>" claim from the user or another model → confirm with a web search before acting on it.
- A local probe tells you what an endpoint does right now. A web search tells you whether what you're seeing is a known issue with a documented workaround. Those are different questions — do both, in that order.

**Add this rule verbatim to every new `CLAUDE.md` file you create, at the top, so it propagates to every scope.**

## Work Management

This project tracks work with `bw` (beadwork), which persists to git. ALWAYS run `bw prime` before starting work. Tickets live on the orphan git branch `beadwork` (prefix `pdp-`). On a fresh clone: `git fetch origin beadwork:beadwork`. Push tickets separately: `git push origin beadwork`.

## What this site is

The public options site for a PROPOSED Pueblo County public-safety drone pilot, built from the research report of 2026-08-23 (`site-src/report.md`, published at /report.md). It is a proposal document: its job is to be corrected by the host owner, the county, and the public before anything is decided.

## Hard rules

- **Everything is a proposal** until the county decides otherwise; the banner and the four-state claim system are validator-enforced. Never present anything as approved, selected, funded, or agreed.
- **The host business and its owner are unnamed** ("a well-secured storage facility in Pueblo West" / "the facility's owner") until the owner agrees to be named. The validator denylist is a backstop, not the rule.
- **Never claim**: autonomous launch, private flight control, facial recognition, weapons, guaranteed plate reading, "always available".
- **The report is canonical**; changes to facts go into `site-src/report.md` and the page together.
- **Time-sensitive statuses carry check dates** (Blue list, grant deadlines, prices) and must be rechecked when they matter; FY26 COPS is closed to new applicants, the target is the next cycle.
- **Authorship**: every author/owner/copyright field says Denson Smith. The site never speaks as a government agency.
- **Cloudflare** is never touched by an agent without the PRINCIPAL's explicit per-instance authorization.

## Site rules

`site-src/CLAUDE.md` carries the build rules. `public/` is generated; never edit it. Always run both build and validate. Design: the Pueblo Drone Pilot system (Claude Design export at `C:\claude_projects\pueblo-drone-design\` on the laptop), civic register, single light theme, `pd-*` classes.
