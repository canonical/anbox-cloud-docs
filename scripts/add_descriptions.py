#!/usr/bin/env python3
"""
Add HTML meta descriptions to Anbox Cloud documentation source files.

Each page gets a 120-160 character plain-text summary injected into its
MyST YAML frontmatter under the ``html_meta.description`` key, which
Sphinx renders as ``<meta name="description" content="...">``.

Usage
-----
    # List discovered docs files (bash one-liner equivalent)
    python3 scripts/add_descriptions.py --list

    # Dry-run: print what would change without writing files
    python3 scripts/add_descriptions.py --dry-run

    # Write descriptions to files that do not yet have one
    python3 scripts/add_descriptions.py --write

    # Overwrite existing descriptions too
    python3 scripts/add_descriptions.py --write --overwrite

    # Check that every file has a valid description (use in CI)
    python3 scripts/add_descriptions.py --check

    # Process a single file
    python3 scripts/add_descriptions.py --write --file explanation/aaos.md

Makefile shortcut: ``make descriptions`` / ``make check-descriptions``
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

REPO_ROOT = Path(__file__).parent.parent

# Directories (relative to REPO_ROOT) excluded from processing.
# - reference/cmd-ref  → auto-generated; would be clobbered on next run
# - reference/release-notes → factual records, not conceptual content pages
EXCLUDED_PATHS: list[str] = [
    ".sphinx",
    "_build",
    "_static",
    "_templates",
    "scripts",
    "reuse",
    ".github",
    "images",
    ".pytest_cache",
    # Auto-generated from tool source code; descriptions would be overwritten.
    "reference/cmd-ref",
    # Template file only — not a published page.
    "reference/release-notes/release-notes-template.md",
]

# Target character range for descriptions.
# DESC_MIN is a soft lower bound: genuinely sparse pages (stubs, index pages)
# that cannot reach DESC_MIN are still accepted if they are >= DESC_HARD_MIN.
DESC_HARD_MIN = 60   # absolute floor – below this is always an error
DESC_MIN      = 120  # desired lower bound
DESC_MAX      = 160  # hard upper bound


# ---------------------------------------------------------------------------
# File discovery
# ---------------------------------------------------------------------------

def find_docs(root: Path = REPO_ROOT) -> list[Path]:
    """Return a sorted list of all manually-maintained .md documentation files."""
    excluded = [root / p for p in EXCLUDED_PATHS]
    results: list[Path] = []
    for f in root.rglob("*.md"):
        if any(
            # handles both directory prefixes and exact file matches
            (ex.is_dir() and f.is_relative_to(ex)) or f == ex
            for ex in excluded
        ):
            continue
        results.append(f)
    return sorted(results)


# ---------------------------------------------------------------------------
# Description extraction
# ---------------------------------------------------------------------------

# Markdown/MyST patterns to strip from prose
_RE_MYST_ROLE   = re.compile(r"\{[a-z_-]+\}`[^`]*`")
_RE_LINK        = re.compile(r"\[([^\]]+)\]\([^)]+\)")
_RE_REF_LINK    = re.compile(r"\[([^\]]+)\]\[[^\]]*\]")
_RE_BOLD        = re.compile(r"\*\*([^*]+)\*\*")
_RE_ITALIC      = re.compile(r"\*([^*]+)\*")
_RE_BOLD_US     = re.compile(r"__([^_]+)__")
_RE_ITALIC_US   = re.compile(r"_([^_]+)_")
_RE_CODE        = re.compile(r"`[^`]+`")
_RE_HTML_TAG    = re.compile(r"<[^>]+>")


def _clean_markdown(text: str) -> str:
    """Return *text* with all Markdown/MyST syntax stripped, as plain prose."""
    text = _RE_MYST_ROLE.sub("", text)
    # Strip standalone MyST directive markers left after unwrapping: {note}, {term}…
    text = re.sub(r"\{[a-z][a-z_-]*\}", "", text)
    text = _RE_LINK.sub(r"\1", text)
    text = _RE_REF_LINK.sub(r"\1", text)
    text = _RE_BOLD.sub(r"\1", text)
    text = _RE_ITALIC.sub(r"\1", text)
    text = _RE_BOLD_US.sub(r"\1", text)
    text = _RE_ITALIC_US.sub(r"\1", text)
    text = _RE_CODE.sub("", text)
    text = _RE_HTML_TAG.sub("", text)
    return " ".join(text.split()).strip()


# Directive names whose content is prose and should be kept during extraction.
# All other directive fences (toctree, code-block, raw, etc.) are stripped entirely.
_PROSE_DIRECTIVES = (
    "note", "warning", "tip", "important", "caution",
    "hint", "attention", "glossary", "seealso",
)
_PROSE_DIR_PATTERN = "|".join(_PROSE_DIRECTIVES)


def extract_description(content: str) -> str:
    """
    Extract a 120-160 character plain-text description from *content*.

    Strategy:
    1. Strip frontmatter, code blocks, directives, and HTML comments.
    2. Locate the page title (first ``#`` heading).
    3. Collect the first substantial prose paragraph(s) that follow.
    4. Clean all Markdown/MyST syntax from the result.
    5. Trim to DESC_MAX at a word boundary, keeping >= DESC_MIN where possible.
    """
    # --- 1. Strip non-prose regions ---
    body = re.sub(r"^---\n.*?\n---\n", "", content, flags=re.DOTALL)

    # Unwrap prose directives (keep their content; only strip the markers)
    body = re.sub(
        rf"```{{(?:{_PROSE_DIR_PATTERN})}}[^\n]*\n(.*?)```",
        r"\1", body, flags=re.DOTALL,
    )
    # Strip all remaining directive fences entirely (toctree, code-block, raw…)
    body = re.sub(r"```\{[^}]+\}[^\n]*\n.*?```", " ", body, flags=re.DOTALL)
    # Strip plain fenced code blocks (```lang … ```)
    body = re.sub(r"```[^\n]*\n.*?```", " ", body, flags=re.DOTALL)
    body = re.sub(r"~~~.*?~~~", " ", body, flags=re.DOTALL)
    # Strip colon-fence admonitions (:::)
    body = re.sub(r":::.*?:::", " ", body, flags=re.DOTALL)
    # Strip HTML comments
    body = re.sub(r"<!--.*?-->", " ", body, flags=re.DOTALL)
    # MyST % comment lines
    body = re.sub(r"^%.*$", "", body, flags=re.MULTILINE)
    # Target labels like (label)=
    body = re.sub(r"^\([^)]+\)=\s*$", "", body, flags=re.MULTILINE)

    # --- 2 & 3. Walk lines, collect title and paragraphs ---
    title = ""
    paragraphs: list[str] = []
    current: list[str] = []

    for raw_line in body.splitlines():
        line = raw_line.strip()

        # Skip indented code blocks (4+ spaces or tab at start of raw line)
        if raw_line and raw_line[0] in (" ", "\t") and len(raw_line) - len(raw_line.lstrip()) >= 4:
            continue

        # Paragraph boundary
        if not line:
            if current:
                para = " ".join(current)
                if len(para) > 5:
                    paragraphs.append(para)
                current = []
            continue

        # Headings → grab title once, then reset current paragraph
        if line.startswith("#"):
            if current:
                para = " ".join(current)
                if len(para) > 5:
                    paragraphs.append(para)
                current = []
            if not title:
                heading = re.sub(r"^#+\s*", "", line)
                title = _clean_markdown(heading)
            continue

        # Skip table rows, directive delimiters, and horizontal rules
        if re.match(r"^(\||-{3,}|={3,}|\*{3,}|:{3,})", line):
            current = []
            continue

        # List items: include if the item text is substantial
        m = re.match(r"^[*\-+]\s+(.+)", line)
        if m:
            item = m.group(1).strip()
            if len(item) > 40:
                current.append(item)
            continue

        current.append(line)

    # Flush last paragraph
    if current:
        para = " ".join(current)
        if len(para) > 5:
            paragraphs.append(para)

    # --- 4. Build and clean candidate description ---
    parts: list[str] = []
    if title:
        parts.append(title + ".")
    # Use up to 5 paragraphs so that sparse pages (glossary, index) have
    # enough content to reach a useful length.
    parts.extend(paragraphs[:5])
    raw = _clean_markdown(" ".join(parts))

    # Remove leading punctuation artefacts
    raw = re.sub(r"^[.,;:\s]+", "", raw)

    if not raw:
        return ""

    # --- 5. Trim to target length ---
    if len(raw) <= DESC_MAX:
        desc = raw
    else:
        cut = raw.rfind(" ", DESC_MIN, DESC_MAX)
        if cut == -1:
            cut = raw.rfind(" ", 0, DESC_MAX)
        desc = raw[:cut if cut > 0 else DESC_MAX]

    desc = desc.rstrip(".,;:")
    if desc and desc[-1] not in ".!?":
        desc += "."

    # Accept descriptions that are shorter than DESC_MIN when content is sparse
    # (they are still useful even if below the target length).
    return desc


# ---------------------------------------------------------------------------
# Frontmatter handling
# ---------------------------------------------------------------------------

def _parse_frontmatter(content: str) -> tuple[dict, str]:
    """
    Split *content* into (frontmatter_dict, body_string).
    Returns ({}, content) when there is no frontmatter or YAML is unavailable.
    """
    if not HAS_YAML:
        return {}, content
    if not content.startswith("---\n"):
        return {}, content
    end = content.find("\n---\n", 4)
    if end == -1:
        return {}, content
    yaml_str = content[4:end]
    body = content[end + 5:]
    try:
        fm = yaml.safe_load(yaml_str) or {}
    except yaml.YAMLError:
        return {}, content
    return fm, body


def _render_frontmatter(fm: dict) -> str:
    """Serialise *fm* back to a YAML string (no trailing newline)."""
    return yaml.dump(fm, default_flow_style=False, allow_unicode=True,
                     sort_keys=False).rstrip("\n")


def _get_existing_description(fm: dict) -> str | None:
    """Return the existing html_meta description, or None."""
    meta = fm.get("html_meta")
    if isinstance(meta, dict):
        return meta.get("description")
    return None


def _set_description(fm: dict, desc: str) -> dict:
    """Return a copy of *fm* with html_meta.description set to *desc*."""
    fm = dict(fm)
    if not isinstance(fm.get("html_meta"), dict):
        fm["html_meta"] = {}
    fm["html_meta"] = dict(fm["html_meta"])
    fm["html_meta"]["description"] = desc
    return fm


def process_file(path: Path, overwrite: bool = False) -> tuple[str, str | None]:
    """
    Compute the new content for *path*.

    Returns
    -------
    (status, new_content) where status is one of:
        'added'    – description was newly inserted
        'updated'  – existing description was replaced (only when overwrite=True)
        'skipped'  – file already has a description and overwrite is False
        'no_yaml'  – PyYAML not available; file cannot be processed
        'error'    – description could not be extracted
    """
    if not HAS_YAML:
        return "no_yaml", None

    content = path.read_text(encoding="utf-8")
    fm, body = _parse_frontmatter(content)
    existing = _get_existing_description(fm)

    if existing is not None and not overwrite:
        return "skipped", None

    desc = extract_description(content)
    if not desc:
        return "error", None

    new_fm = _set_description(fm, desc)
    fm_block = _render_frontmatter(new_fm)
    new_content = f"---\n{fm_block}\n---\n{body}"

    status = "updated" if existing is not None else "added"
    return status, new_content


# ---------------------------------------------------------------------------
# Validation helpers (used by --check and tests)
# ---------------------------------------------------------------------------

def validate_file(path: Path) -> list[str]:
    """
    Return a list of validation error strings for *path*.
    An empty list means the file is valid.
    """
    errors: list[str] = []
    if not HAS_YAML:
        errors.append("PyYAML not installed; cannot validate")
        return errors

    content = path.read_text(encoding="utf-8")
    fm, _ = _parse_frontmatter(content)
    desc = _get_existing_description(fm)

    if desc is None:
        errors.append("missing html_meta.description")
        return errors

    if not isinstance(desc, str) or not desc.strip():
        errors.append("html_meta.description is empty")
        return errors

    if len(desc) < DESC_HARD_MIN:
        errors.append(
            f"description too short ({len(desc)} chars, minimum {DESC_HARD_MIN}): {desc!r}"
        )
    if len(desc) > DESC_MAX:
        errors.append(
            f"description too long ({len(desc)} chars, maximum {DESC_MAX}): {desc!r}"
        )

    # Check for residual markdown syntax
    md_patterns = [
        (r"\[.*?\]\(.*?\)", "contains markdown link"),
        (r"\*\*.+?\*\*",    "contains bold markup"),
        (r"`[^`]+`",        "contains inline code"),
        (r"\{[a-z_]+\}`",   "contains MyST role"),
    ]
    for pattern, label in md_patterns:
        if re.search(pattern, desc):
            errors.append(f"{label}: {desc!r}")

    return errors


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Add HTML meta descriptions to Anbox Cloud documentation pages.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--list",    action="store_true", help="List all discovered docs files")
    mode.add_argument("--dry-run", action="store_true", help="Print proposed descriptions without writing")
    mode.add_argument("--write",   action="store_true", help="Write descriptions to disk")
    mode.add_argument("--check",   action="store_true", help="Validate all files; exit 1 on failures")

    parser.add_argument("--overwrite", action="store_true",
                        help="Replace existing descriptions (used with --write or --dry-run)")
    parser.add_argument("--file", metavar="PATH",
                        help="Process a single file instead of the whole tree")
    args = parser.parse_args()

    if not HAS_YAML:
        print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
        sys.exit(1)

    # ---- Discover files ----
    if args.file:
        p = Path(args.file)
        docs = [p if p.is_absolute() else REPO_ROOT / p]
    else:
        docs = find_docs()

    # ---- --list ----
    if args.list:
        for f in docs:
            print(f.relative_to(REPO_ROOT))
        print(f"\n{len(docs)} files", file=sys.stderr)
        return

    # ---- --check ----
    if args.check:
        failures: dict[Path, list[str]] = {}
        for path in docs:
            errs = validate_file(path)
            if errs:
                failures[path] = errs

        if failures:
            for path, errs in sorted(failures.items()):
                rel = path.relative_to(REPO_ROOT)
                for err in errs:
                    print(f"  FAIL  {rel}: {err}")
            print(f"\n{len(failures)}/{len(docs)} files failed validation.", file=sys.stderr)
            sys.exit(1)
        else:
            print(f"  OK  All {len(docs)} files have valid descriptions.")
        return

    # ---- --dry-run / --write ----
    counts: dict[str, int] = {"added": 0, "updated": 0, "skipped": 0, "error": 0}
    for path in docs:
        rel = path.relative_to(REPO_ROOT)
        status, new_content = process_file(path, overwrite=args.overwrite)
        counts[status] = counts.get(status, 0) + 1

        if status in ("added", "updated"):
            # Show the proposed description
            fm, _ = _parse_frontmatter(new_content)
            desc = _get_existing_description(fm)
            verb = "WOULD ADD" if args.dry_run else status.upper()
            print(f"  {verb:8s}  {rel}")
            print(f"           {desc!r}")
            if args.write:
                path.write_text(new_content, encoding="utf-8")
        elif status == "skipped":
            pass  # silent for brevity
        elif status == "error":
            print(f"  ERROR     {rel}: could not extract description", file=sys.stderr)

    total = len(docs)
    print(
        f"\nDone: {counts.get('added',0)} added, "
        f"{counts.get('updated',0)} updated, "
        f"{counts.get('skipped',0)} skipped, "
        f"{counts.get('error',0)} errors  "
        f"({total} files total)."
    )


if __name__ == "__main__":
    main()
