# Site source — rules that hold regardless of the task

This directory builds `pueblo-drone-pilot.stoagen.com`, the public options
site for a PROPOSED Pueblo County public-safety drone pilot. `public/` is
generated output; never edit it. Edit `site-src/` and run the build.

Voice: a well-made county ballot information booklet. Plain, exact, local
and civic, never military, never a drone dealer. Conditional mood for
anything not decided. No emoji, no exclamation points, no em-dashes in
reader-facing prose. Sentence case everywhere.

## Pages are Markdown; the page is a subset of them

Write the whole document — prose, sources, cautions — in one file under
`content/`. Everything after `<!-- agent-only -->` goes to the Markdown
mirror and never to the page. The HTML page is the part above the marker,
rewritten for human readability.

The mirror is a **superset**: it may carry more than the page, it may never
carry less, and the two may never contradict each other.

## Dates are derived, never typed

Published and last-updated come from the file's commit history, UTC to the
minute. There is no date field in front matter. CI needs `fetch-depth: 0`.

## Hard constraints

- **Everything is a proposal.** The PROPOSAL UNDER DEVELOPMENT banner is
  rendered by the template on every page; the validator enforces it. Never
  present anything as approved, selected, funded, or agreed.
- **Four-state claims.** Assertions carry `[[verified]]` (only with a
  source and check date), `[[estimate]]`, `[[proposal]]`, or `[[open]]`
  inline in the markdown; the build renders them as chips and the mirror
  keeps the tokens. A fact without a source is an open question, never an
  invention.
- **The host is unnamed.** "A well-secured storage facility in Pueblo West"
  and "the facility's owner" only. The validator's denylist is a backstop.
- **Never claim**: autonomous launch, private flight control, facial
  recognition, weapons, guaranteed plate reading, "always available".
- **The report is canonical.** Every figure traces to `site-src/report.md`
  (published at /report.md), which carries the source register. Update the
  report and the page together or not at all.
- **No images** until rights and attribution are cleared; the aircraft-card
  placeholder text is intentional. One script per page (the copy-box
  enhancer); readable with JavaScript off; prints cleanly.
- **robots.txt is allow-all with the all-yes Content-Signal.** A decision,
  not an oversight.
- Components from Markdown: `[[state]]` tokens; `Sources:` paragraphs
  become the citation strip; tables get `pd-table` (wrap budget tables in
  `<div class="budget" markdown="1">`); steppers, launch sequences,
  aircraft cards and panels are HTML blocks with `pd-*` classes per
  `site.css`.

## Always run both

```
python site-src/build_site.py
python site-src/validate_site.py
```

CI runs both on every pull request and only `main` deploys.
