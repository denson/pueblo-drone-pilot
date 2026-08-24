# pueblo-drone-pilot

Source for **pueblo-drone-pilot.stoagen.com**: a public options website for
a PROPOSED Pueblo County public-safety drone pilot, in which local
businesses would host secure launch sites and county public-safety
personnel would operate a long-endurance thermal drone from them. Nothing
is approved: no agency commitment, no vendor selected, no funds awarded.

Published with the [Stoagen](https://stoagen.com/) pattern. Every claim
carries one of four states (verified fact, planning estimate, proposal,
open question); the PROPOSAL UNDER DEVELOPMENT banner is on every page;
the prospective host business is deliberately unnamed; and the research
report behind the site is published at /report.md with its source register.

## Build

```
python site-src/build_site.py
python site-src/validate_site.py
```

Output lands in `public/` (gitignored). CI runs both on every pull request;
only `main` deploys to GitHub Pages. See `site-src/CLAUDE.md` for the rules.

Text CC BY 4.0 (`LICENSE`), code MIT (`LICENSE-CODE`). Author: Denson Smith.
Not published by or endorsed by any government agency.
