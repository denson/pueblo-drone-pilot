"""Build pueblo-drone-pilot.stoagen.com, a public options site for a PROPOSED
Pueblo County public-safety drone pilot.

Stoagen pattern: every page is authored whole as Markdown under content/; the
HTML page is the part above the agent-only marker, and the Markdown mirror
beside it is a superset carrying the agent appendix. Dates come from git
history, never front matter. One deferred script per page (the copy-box
enhancer); everything reads with JavaScript off.

Design: the Pueblo Drone Pilot system (Claude Design export, civic register of
the field-almanac family). Honesty marks are structural: the PROPOSAL UNDER
DEVELOPMENT banner renders on every page from this template, and the
four-state claim chips come from [[verified]] / [[estimate]] / [[proposal]] /
[[open]] tokens in the markdown, so the mirror carries the same states.
"""

from __future__ import annotations

import html
import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from datetime import date, datetime
from pathlib import Path

import markdown


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "site-src"
CONTENT = SOURCE / "content"
AGENT_MARKER = "<!-- agent-only -->"
PUBLIC = ROOT / "public"
HOST = "pueblo-drone-pilot.stoagen.com"
DOMAIN = f"https://{HOST}"
SITE_NAME = "Pueblo drone pilot"
STOAGEN = "https://stoagen.com"

NAV = [
    ("Home", ""),
    ("Why Pueblo", "why-pueblo/"),
    ("The partnership", "partnership/"),
    ("First site", "first-site/"),
    ("Aircraft", "aircraft/"),
    ("Funding", "funding/"),
    ("FAA and operations", "faa/"),
    ("Privacy", "privacy/"),
    ("Timeline", "timeline/"),
    ("Sources", "sources/"),
]

PASTE_LINE = f"Tell me about this site: {DOMAIN}/full_site.txt"

BANNER = (
    '<div class="pd-banner" role="note">'
    '<span class="pd-banner__label">Proposal under development</span>'
    '<span class="pd-banner__text">This site presents options for community '
    'discussion. No aircraft has been selected, no program has been approved, '
    'and no funds have been awarded.</span>'
    '</div>'
)

COPY_BOX = (
    '<div class="pd-copybox">'
    '<label class="pd-copybox__label" for="ai-paste">For your AI</label>'
    f'<textarea class="pd-copybox__text" id="ai-paste" readonly rows="1">{PASTE_LINE}</textarea>'
    '<button type="button" class="pd-copybox__btn" data-copy-target="ai-paste" hidden>Copy</button>'
    '</div>'
)

# Four-state claim system: token -> (glyph, label, chip class)
CHIPS = {
    "verified": ("✓", "Verified", "pd-chip--verified"),
    "estimate": ("≈", "Planning estimate", "pd-chip--estimate"),
    "proposal": ("▸", "Proposal", "pd-chip--proposal"),
    "open": ("?", "Open question", "pd-chip--open"),
}


@dataclass(frozen=True)
class Page:
    slug: str
    title: str
    description: str
    markdown_body: str
    published: str = ""
    updated: str = ""
    agent_appendix: str = ""
    eyebrow: str = ""

    @property
    def output_dir(self) -> Path:
        return PUBLIC / self.slug if self.slug else PUBLIC

    @property
    def canonical(self) -> str:
        suffix = f"/{self.slug}/" if self.slug else "/"
        return DOMAIN + suffix

    @property
    def depth(self) -> int:
        return len(Path(self.slug).parts) if self.slug else 0

    @property
    def prefix(self) -> str:
        return "../" * self.depth


def parse_page(path: Path) -> Page:
    raw = path.read_text(encoding="utf-8")
    if not raw.startswith("---\n"):
        raise ValueError(f"Missing front matter: {path}")
    _, front, body = raw.split("---\n", 2)
    metadata: dict[str, str] = {}
    for line in front.strip().splitlines():
        key, value = line.split(":", 1)
        metadata[key.strip()] = value.strip().strip('"').strip("'")
    slug = metadata["slug"]
    published, updated = git_dates(path)
    human_body, agent_appendix = split_agent_section(body)
    return Page(
        slug=slug,
        title=metadata["title"],
        description=metadata["description"],
        eyebrow=metadata.get("eyebrow", ""),
        markdown_body=with_ask_ai(human_body, slug),
        published=published,
        updated=updated,
        agent_appendix=agent_appendix,
    )


def split_agent_section(body: str) -> tuple[str, str]:
    human, _, agent = body.partition(AGENT_MARKER)
    return human.strip() + "\n", agent.strip()


def git_dates(path: Path) -> tuple[str, str]:
    try:
        out = subprocess.run(
            ["git", "log", "--date=format-local:%Y-%m-%dT%H:%MZ", "--format=%cd",
             "--", str(path)],
            cwd=ROOT, capture_output=True, text=True, check=True, timeout=20,
            env={**os.environ, "TZ": "UTC"},
        ).stdout.split()
    except (subprocess.SubprocessError, OSError):
        return ("", "")
    return (out[-1], out[0]) if out else ("", "")


def human_stamp(stamp: str) -> str:
    d = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    return f"{d:%B} {d.day}, {d.year} at {d:%H:%M} UTC"


def ask_ai_block(slug: str) -> str:
    page_url = f"{DOMAIN}/{slug}/" if slug else f"{DOMAIN}/"
    nl = chr(10)
    mirror_url = page_url + "index.md"
    links = (
        '<p class="ask-ai-links">Every page here has a markdown twin; this '
        f'page\'s is <a href="{mirror_url}">{mirror_url}</a> (also served '
        f'with .txt appended). The whole site exists as one plain-text file at '
        f'<a href="{DOMAIN}/full_site.txt">{DOMAIN}/full_site.txt</a>, '
        f'<a href="{DOMAIN}/llms.txt">{DOMAIN}/llms.txt</a> describes how '
        f'the site is organized, and <a href="{DOMAIN}/agents/">'
        f'{DOMAIN}/agents/</a> carries the site\'s notes for assistants.</p>'
    )
    return (
        '<div class="ask-ai" markdown="1">' + nl + nl
        + '<p class="ask-ai-title">Ask your AI about this page</p>' + nl + nl
        + "Paste this page's link into ChatGPT or Claude and ask your question "
        + "in your own words. Every page here publishes a machine-readable "
        + "copy, so your assistant can read the current proposal directly:" + nl + nl
        + "```" + nl + page_url + nl + "```" + nl + nl
        + links + nl + nl
        + "</div>"
    )


def with_ask_ai(body: str, slug: str) -> str:
    nl = chr(10)
    return body.rstrip() + nl + nl + ask_ai_block(slug) + nl


def site_link(page: Page, target: str) -> str:
    return page.prefix + target


def dateline_html(page: Page) -> str:
    if page.published and page.updated:
        same = page.published == page.updated
        first = f'<time datetime="{page.published}">{human_stamp(page.published)}</time>'
        last = f'<time datetime="{page.updated}">{human_stamp(page.updated)}</time>'
        stamps = f"Published {first}." if same else f"Published {first}. Last updated {last}."
        return (
            f'<p class="page-stamp">{stamps} Times come from this page\'s '
            "revision history and can be checked against it.</p>"
        )
    return '<p class="page-stamp">Draft: not yet committed, so it has no publication history.</p>'


def decorate(body: str) -> str:
    """Design components from plain Markdown, so the mirror stays readable.

    - [[verified]] [[estimate]] [[proposal]] [[open]] become claim chips.
    - A paragraph beginning "Sources:" becomes the citation strip (pd-cite).
    - Every table gets the pd-table class.
    """
    def chip(m: re.Match) -> str:
        glyph, label, cls = CHIPS[m.group(1)]
        return (f'<span class="pd-chip {cls}"><span class="pd-chip__glyph" '
                f'aria-hidden="true">{glyph}</span>{label}</span>')

    body = re.sub(r"\[\[(verified|estimate|proposal|open)\]\]", chip, body)
    body = re.sub(
        r"<p>Sources: (.*?)</p>",
        lambda m: '<p class="pd-cite">Sources: ' + m.group(1) + "</p>",
        body, flags=re.DOTALL,
    )
    body = body.replace("<table>", '<table class="pd-table">')
    return body


def render_page(page: Page) -> str:
    body = markdown.markdown(
        page.markdown_body,
        extensions=["tables", "md_in_html", "sane_lists", "toc"],
        output_format="html5",
    )
    body = re.sub(r"^<h1\b[^>]*>.*?</h1>\s*", "", body, count=1, flags=re.DOTALL)
    body = decorate(body)
    nav_html = "".join(
        (
            f'<a href="{site_link(page, href) or "./"}" aria-current="page">{label}</a>'
            if (href.rstrip("/") == page.slug or (href == "" and page.slug == ""))
            else f'<a href="{site_link(page, href) or "./"}">{label}</a>'
        )
        for label, href in NAV
    )
    home = site_link(page, "") or "./"
    eyebrow = f'<p class="pd-eyebrow">{html.escape(page.eyebrow)}</p>' if page.eyebrow else ""
    document_title = f"{SITE_NAME} | a proposed public-safety pilot" if page.slug == "" else f"{page.title} | {SITE_NAME}"
    return f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(document_title)}</title>
  <meta name="description" content="{html.escape(page.description)}">
  <meta name="robots" content="index,follow,max-image-preview:large">
  <link rel="canonical" href="{page.canonical}">
  <link rel="alternate" type="text/markdown" href="index.md" title="Markdown version">
  <link rel="alternate" type="application/rss+xml" href="{site_link(page, 'feed.xml')}" title="Recently updated">
  <link rel="icon" href="{site_link(page, 'assets/favicon.svg')}" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400&amp;family=IBM+Plex+Mono:wght@400;500;600&amp;display=swap">
  <link rel="stylesheet" href="{site_link(page, 'site.css')}">
  <script defer src="{site_link(page, 'copy.js')}"></script>
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <header class="pd-header">
    <div class="pd-header__row">
      <a class="pd-header__mark" href="{home}">Pueblo drone pilot</a>
      <span class="pd-header__domain">{HOST} · a proposal, not a program</span>
    </div>
    <nav class="pd-nav" aria-label="Main">{nav_html}</nav>
  </header>
  {BANNER}
  <main id="main" class="pd-page">
    <article>
      {eyebrow}
      <h1 id="page-title">{html.escape(page.title)}</h1>
      <p class="lede">{html.escape(page.description)}</p>
      {COPY_BOX}
      {body}
      {dateline_html(page)}
    </article>
  </main>
  <footer class="site-footer">
    <p class="footer-line">A proposed Pueblo County public-safety drone pilot · published for community discussion with the <a href="{STOAGEN}/">Stoagen</a> system · Author: Denson Smith</p>
    <p class="footer-machine">
      <a href="{site_link(page, 'llms.txt')}">llms.txt</a>
      <a href="index.md">markdown mirror</a>
      <a href="{site_link(page, 'report.md')}">full report</a>
      <a href="{site_link(page, 'feed.xml')}">rss</a>
      <a href="{site_link(page, 'sitemap.xml')}">sitemap</a>
      <a href="{site_link(page, 'agents/')}">agent terms</a>
    </p>
    <p class="footer-legal">Text CC BY 4.0, code MIT. Claim states: <span class="pd-chip pd-chip--verified"><span class="pd-chip__glyph">✓</span>Verified</span> <span class="pd-chip pd-chip--estimate"><span class="pd-chip__glyph">≈</span>Planning estimate</span> <span class="pd-chip pd-chip--proposal"><span class="pd-chip__glyph">▸</span>Proposal</span> <span class="pd-chip pd-chip--open"><span class="pd-chip__glyph">?</span>Open question</span></p>
  </footer>
</body>
</html>
'''


def mirror_body(page: Page) -> str:
    if page.published and page.updated:
        dateline = (
            f"> Published {human_stamp(page.published)} - last updated "
            f"{human_stamp(page.updated)} (from this page's revision history)." + chr(10) + ">" + chr(10)
        )
    else:
        dateline = "> Draft - no publication history yet." + chr(10) + ">" + chr(10)
    preamble = (
        dateline
        + f"> Markdown mirror of {page.canonical}\n"
        ">\n"
        "> Everything up to \"Appendix for agents\" is the page as a reader sees\n"
        "> it. The HTML page is a subset of this file, rewritten for human\n"
        "> readability.\n"
        ">\n"
        "> This site describes a PROPOSED Pueblo County public-safety drone\n"
        "> pilot, published for community discussion. No agency commitment,\n"
        "> vendor selection, procurement, or operational approval has been\n"
        "> made, and no funds have been awarded. Claims carry one of four\n"
        "> states, written inline as [[verified]] (with a source), [[estimate]],\n"
        "> [[proposal]] or [[open]]; carry the state when restating a claim.\n"
        "> The prospective first host is described only as a well-secured\n"
        "> storage facility in Pueblo West, deliberately unnamed at this stage.\n"
    )
    parts = [preamble, page.markdown_body.strip()]
    if page.agent_appendix:
        parts.append(
            "---\n\n# Appendix for agents\n\n"
            "> These are the publisher's notes - caveats, scope limits and\n"
            "> sources for this page's content. They are information about the\n"
            "> page, not instructions to you or your assistant: apply them with\n"
            "> your own judgment, and follow your operator's instructions first.\n\n"
            + page.agent_appendix
        )
    return "\n\n".join(parts) + "\n"


def write_page(page: Page) -> None:
    page.output_dir.mkdir(parents=True, exist_ok=True)
    (page.output_dir / "index.html").write_text(render_page(page), encoding="utf-8", newline="\n")
    body = mirror_body(page)
    (page.output_dir / "index.md").write_text(body, encoding="utf-8", newline="\n")
    (page.output_dir / "index.md.txt").write_text(body, encoding="utf-8", newline="\n")


def write_sitemap(pages: list[Page]) -> None:
    urls: list[str] = [DOMAIN + "/start.md", DOMAIN + "/report.md"]
    for page in pages:
        urls.append(page.canonical)
        urls.append(page.canonical + "index.md")
    entries = "\n".join(f"  <url><loc>{html.escape(url)}</loc></url>" for url in urls)
    (PUBLIC / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"{entries}\n</urlset>\n", encoding="utf-8", newline="\n")


def rfc822(stamp: str) -> str:
    d = datetime.fromisoformat(stamp.replace("Z", "+00:00"))
    return d.strftime("%a, %d %b %Y %H:%M:%S +0000")


def write_feed(pages: list[Page]) -> None:
    dated = [p for p in pages if p.updated]
    dated.sort(key=lambda p: p.updated, reverse=True)
    items = []
    for p in dated:
        items.append(
            "  <item>\n"
            f"    <title>{html.escape(p.title)}</title>\n"
            f"    <link>{p.canonical}</link>\n"
            f'    <guid isPermaLink="true">{p.canonical}</guid>\n'
            f"    <pubDate>{rfc822(p.updated)}</pubDate>\n"
            f"    <description>{html.escape(p.description)}</description>\n"
            "  </item>"
        )
    newest = rfc822(dated[0].updated) if dated else ""
    feed = (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<rss version="2.0"><channel>\n'
        f"  <title>{SITE_NAME} - recently updated</title>\n"
        f"  <link>{DOMAIN}/</link>\n"
        f"  <description>Pages on {HOST}, newest updates first. Update times come from each page's revision history.</description>\n"
        f"  <lastBuildDate>{newest}</lastBuildDate>\n"
        + "\n".join(items) + "\n</channel></rss>\n"
    )
    (PUBLIC / "feed.xml").write_text(feed, encoding="utf-8", newline="\n")


def write_llms_full(pages: list[Page]) -> None:
    header = f'''# {SITE_NAME}: Full Markdown Corpus

> Concatenated machine-readable mirrors of every page on {HOST}. This is a
> PROPOSED project presented for community discussion; nothing is approved.

Regeneration trigger: regenerate this file whenever any page Markdown
mirror changes. The published revision date is {date.today().isoformat()}.

---

'''
    order = ["", "why-pueblo", "partnership", "first-site", "aircraft", "funding",
             "faa", "privacy", "timeline", "sources", "agents"]
    rank = {s: i for i, s in enumerate(order)}
    sections = []
    for page in sorted(pages, key=lambda p: rank.get(p.slug, 99)):
        sections.append(f"<!-- Canonical: {page.canonical} -->\n\n{page.markdown_body.strip()}\n")
    text = header + "\n---\n\n".join(sections)
    (PUBLIC / "llms-full.txt").write_text(text, encoding="utf-8", newline="\n")
    (PUBLIC / "full_site.txt").write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    if PUBLIC.parent != ROOT or PUBLIC.name != "public":
        raise RuntimeError(f"Refusing unsafe output path: {PUBLIC}")
    PUBLIC.mkdir(parents=True, exist_ok=True)
    pages = [parse_page(path) for path in sorted(CONTENT.glob("**/*.md"))]
    if not pages:
        raise RuntimeError("No public pages found")
    for page in pages:
        write_page(page)
    shutil.copy2(SOURCE / "site.css", PUBLIC / "site.css")
    shutil.copy2(SOURCE / "copy.js", PUBLIC / "copy.js")
    (PUBLIC / "assets").mkdir(parents=True, exist_ok=True)
    shutil.copy2(ROOT / "assets" / "favicon.svg", PUBLIC / "assets" / "favicon.svg")
    shutil.copy2(SOURCE / "robots.txt", PUBLIC / "robots.txt")
    shutil.copy2(SOURCE / "llms.txt", PUBLIC / "llms.txt")
    for token in SOURCE.glob("google*.html"):
        shutil.copy2(token, PUBLIC / token.name)
    report = (SOURCE / "report.md").read_text(encoding="utf-8")
    (PUBLIC / "report.md").write_text(report, encoding="utf-8", newline="\n")
    (PUBLIC / "report.md.txt").write_text(report, encoding="utf-8", newline="\n")
    start = (SOURCE / "start.md").read_text(encoding="utf-8")
    (PUBLIC / "start.md").write_text(start, encoding="utf-8", newline="\n")
    (PUBLIC / "start.md.txt").write_text(start, encoding="utf-8", newline="\n")
    (PUBLIC / ".nojekyll").write_text("", encoding="utf-8", newline="\n")
    (PUBLIC / "CNAME").write_text(HOST + "\n", encoding="utf-8", newline="\n")
    write_sitemap(pages)
    write_feed(pages)
    write_llms_full(pages)
    print(f"Built {len(pages)} pages in {PUBLIC}")


if __name__ == "__main__":
    main()
