#!/usr/bin/env python3
"""
Tests for add_descriptions.py

Run with:
    python3 -m pytest scripts/test_descriptions.py -v
    # or
    make test-descriptions

Tests are grouped into three suites:
  Unit    – pure logic (extract_description, find_docs, validate_file)
  Files   – verify every discovered file already has a valid description
            (only meaningful *after* running ``make descriptions``)
  HTML    – verify the Sphinx build exposes <meta name="description"> tags
            (only meaningful *after* running ``make html``; marked slow)
"""
from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import pytest

# ---------------------------------------------------------------------------
# Locate the module under test
# ---------------------------------------------------------------------------
SCRIPTS_DIR = Path(__file__).parent
REPO_ROOT   = SCRIPTS_DIR.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from add_descriptions import (  # noqa: E402
    DESC_HARD_MIN,
    DESC_MAX,
    DESC_MIN,
    EXCLUDED_PATHS,
    _clean_markdown,
    _get_existing_description,
    _parse_frontmatter,
    extract_description,
    find_docs,
    validate_file,
)


# ===========================================================================
# Unit tests – pure logic
# ===========================================================================

class TestCleanMarkdown:
    def test_strips_links(self):
        assert _clean_markdown("[foo](https://example.com)") == "foo"

    def test_strips_bold(self):
        assert _clean_markdown("**important**") == "important"

    def test_strips_italic(self):
        assert _clean_markdown("*italic*") == "italic"

    def test_strips_inline_code(self):
        assert _clean_markdown("use `amc launch`") == "use"

    def test_strips_myst_role(self):
        assert _clean_markdown("{ref}`some-target`") == ""

    def test_normalises_whitespace(self):
        assert _clean_markdown("  a   b  ") == "a b"


class TestExtractDescription:
    # ------------------------------------------------------------------
    # Length invariants
    # ------------------------------------------------------------------
    def test_length_within_range_for_normal_page(self):
        content = """\
(some-label)=
# My Page Title

This is the opening paragraph of the page. It explains what the page is about
in enough detail that a reader knows whether they want to continue reading it.

More content follows here, but we only care about the first paragraph or two.
"""
        desc = extract_description(content)
        assert desc, "description must not be empty"
        assert len(desc) <= DESC_MAX, f"too long ({len(desc)}): {desc!r}"

    def test_length_at_least_hard_min_for_any_content(self):
        # A title + one paragraph that is genuinely long must hit DESC_HARD_MIN.
        content = "# Title\n\n" + ("Word " * 30) + "\n"
        desc = extract_description(content)
        assert len(desc) >= DESC_HARD_MIN, f"too short ({len(desc)}): {desc!r}"
        assert len(desc) <= DESC_MAX, f"too long ({len(desc)}): {desc!r}"

    def test_long_content_is_trimmed_at_most_to_max(self):
        # When content is very long the description must be ≤ DESC_MAX.
        long_para = "This is a fairly long sentence that keeps going and going. " * 10
        content = f"# Title\n\n{long_para}\n"
        desc = extract_description(content)
        assert len(desc) <= DESC_MAX, f"too long ({len(desc)}): {desc!r}"

    def test_short_page_does_not_exceed_max(self):
        content = "# Short\n\nBrief content.\n"
        desc = extract_description(content)
        assert len(desc) <= DESC_MAX

    # ------------------------------------------------------------------
    # Content quality
    # ------------------------------------------------------------------
    def test_no_markdown_links_in_output(self):
        content = "# Title\n\nSee [the guide](https://example.com) for more.\n"
        desc = extract_description(content)
        assert "](http" not in desc
        assert "[the guide]" not in desc

    def test_no_inline_code_in_output(self):
        content = "# Title\n\nUse `amc launch` to start an instance.\n"
        desc = extract_description(content)
        assert "`" not in desc

    def test_no_myst_role_in_output(self):
        content = "# Title\n\nSee {ref}`some-target` for details.\n"
        desc = extract_description(content)
        assert "{ref}" not in desc

    def test_ends_with_punctuation(self):
        content = "# Title\n\n" + "Word " * 40 + "\n"
        desc = extract_description(content)
        assert desc[-1] in ".!?"

    def test_skips_frontmatter(self):
        content = "---\norphan: true\n---\n# Title\n\nReal content here.\n"
        desc = extract_description(content)
        assert "orphan" not in desc

    def test_skips_code_blocks(self):
        content = "# Title\n\n```bash\namc launch myapp\n```\n\nProse follows here.\n"
        desc = extract_description(content)
        assert "amc launch" not in desc

    def test_skips_admonition_fences(self):
        content = "# Title\n\n:::{note}\nDo not rely on this.\n:::\n\nActual prose.\n"
        desc = extract_description(content)
        assert "Do not rely" not in desc

    def test_includes_title(self):
        content = "# Android Automotive OS\n\nContent about AAOS.\n"
        desc = extract_description(content)
        assert "Android Automotive OS" in desc

    def test_empty_file_returns_empty_string(self):
        assert extract_description("") == ""

    def test_heading_only_returns_something(self):
        desc = extract_description("# Just A Title\n")
        # Title alone is very short so we get at most the title + period
        assert "Just A Title" in desc


# ===========================================================================
# Frontmatter handling
# ===========================================================================

class TestFrontmatterRoundtrip:
    def test_parses_orphan(self):
        content = "---\norphan: true\n---\n# Title\n"
        fm, body = _parse_frontmatter(content)
        assert fm.get("orphan") is True
        assert body == "# Title\n"

    def test_no_frontmatter(self):
        content = "# Title\n\nParagraph.\n"
        fm, body = _parse_frontmatter(content)
        assert fm == {}
        assert body == content

    def test_get_existing_description(self):
        fm = {"html_meta": {"description": "Hello world"}}
        assert _get_existing_description(fm) == "Hello world"

    def test_get_description_missing(self):
        assert _get_existing_description({}) is None
        assert _get_existing_description({"orphan": True}) is None


# ===========================================================================
# File-level tests – run after ``make descriptions``
# ===========================================================================

class TestFileDiscovery:
    def test_find_docs_returns_list(self):
        docs = find_docs()
        assert isinstance(docs, list)
        assert len(docs) > 0

    def test_excluded_paths_are_absent(self):
        docs = find_docs()
        for path in docs:
            rel = str(path.relative_to(REPO_ROOT))
            for excluded in EXCLUDED_PATHS:
                assert not rel.startswith(excluded), \
                    f"{rel} is inside excluded path {excluded!r}"

    def test_only_markdown_files(self):
        docs = find_docs()
        for path in docs:
            assert path.suffix == ".md", f"Unexpected extension: {path}"

    def test_sorted_output(self):
        docs = find_docs()
        assert docs == sorted(docs)


@pytest.mark.skipif(
    not any(
        (REPO_ROOT / f).exists()
        and (lambda fm, _: _get_existing_description(fm))(
            *_parse_frontmatter((REPO_ROOT / f).read_text(encoding="utf-8"))
        ) is not None
        for f in ["explanation/aaos.md"]
    ),
    reason="Run 'make descriptions' first to add descriptions to files",
)
class TestFileDescriptions:
    """Validate that every discovered file has a correctly-formed description."""

    @pytest.fixture(scope="class")
    def docs(self):
        return find_docs()

    @pytest.fixture(scope="class")
    def validation_results(self, docs):
        return {path: validate_file(path) for path in docs}

    def test_all_files_have_description(self, docs, validation_results):
        missing = [
            str(p.relative_to(REPO_ROOT))
            for p, errs in validation_results.items()
            if any("missing" in e for e in errs)
        ]
        assert not missing, (
            f"{len(missing)} file(s) missing html_meta.description:\n"
            + "\n".join(f"  {f}" for f in missing)
        )

    def test_description_length(self, docs, validation_results):
        bad = {
            str(p.relative_to(REPO_ROOT)): errs
            for p, errs in validation_results.items()
            if any("too short" in e or "too long" in e for e in errs)
        }
        assert not bad, (
            f"{len(bad)} file(s) have out-of-range description length:\n"
            + "\n".join(f"  {f}: {e}" for f, errs in bad.items() for e in errs)
        )

    def test_no_markdown_in_descriptions(self, docs, validation_results):
        bad = {
            str(p.relative_to(REPO_ROOT)): errs
            for p, errs in validation_results.items()
            if any("contains" in e for e in errs)
        }
        assert not bad, (
            f"{len(bad)} file(s) have markdown syntax in their description:\n"
            + "\n".join(f"  {f}: {e}" for f, errs in bad.items() for e in errs)
        )

    def test_no_validation_errors_overall(self, docs, validation_results):
        """Aggregate assertion: every file passes all checks."""
        all_failures = {
            str(p.relative_to(REPO_ROOT)): errs
            for p, errs in validation_results.items()
            if errs
        }
        assert not all_failures, (
            f"{len(all_failures)} file(s) failed validation:\n"
            + "\n".join(
                f"  {f}: {'; '.join(errs)}"
                for f, errs in all_failures.items()
            )
        )


# ===========================================================================
# HTML integration tests – only run after ``make html``
# ===========================================================================

BUILD_DIR = REPO_ROOT / "_build"


@pytest.mark.slow
@pytest.mark.skipif(
    not BUILD_DIR.exists(),
    reason="Run 'make html' first to build the documentation",
)
class TestHtmlMetaDescription:
    """Verify that the HTML output contains <meta name='description'> tags."""

    @pytest.fixture(scope="class")
    def html_files(self):
        return list(BUILD_DIR.rglob("*.html"))

    def test_html_files_exist(self, html_files):
        assert len(html_files) > 0, "No HTML files found in _build/"

    def test_sample_pages_have_meta_description(self, html_files):
        """
        At least 80 % of HTML files should contain a meta description tag.
        Some pages (index pages, auto-generated) may legitimately lack one.
        """
        META_RE = re.compile(
            r'<meta\s+(?:[^>]*\s+)?name=["\']description["\']', re.IGNORECASE
        )
        with_meta   = sum(1 for f in html_files if META_RE.search(f.read_text(encoding="utf-8", errors="replace")))
        without_meta = len(html_files) - with_meta
        ratio = with_meta / len(html_files)
        assert ratio >= 0.80, (
            f"Only {with_meta}/{len(html_files)} HTML files "
            f"({ratio:.0%}) have a meta description. "
            f"{without_meta} files are missing it."
        )

    def test_aaos_page_has_meta_description(self):
        """Spot-check a known content page."""
        # explanation/aaos → _build/explanation/aaos/index.html (dirhtml builder)
        candidates = [
            BUILD_DIR / "explanation" / "aaos" / "index.html",
            BUILD_DIR / "explanation" / "aaos.html",
        ]
        for html_file in candidates:
            if html_file.exists():
                text = html_file.read_text(encoding="utf-8", errors="replace")
                assert re.search(
                    r'<meta\s+(?:[^>]*\s+)?name=["\']description["\']',
                    text, re.IGNORECASE
                ), f"No meta description in {html_file}"
                return
        pytest.skip("AAOS HTML file not found in build output")


# ===========================================================================
# Bash command smoke test
# ===========================================================================

class TestBashCommand:
    """The ``--list`` flag must emit one path per line (bash-friendly output)."""

    def test_list_produces_one_path_per_line(self):
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "add_descriptions.py"), "--list"],
            capture_output=True,
            text=True,
            check=True,
        )
        lines = [ln for ln in result.stdout.splitlines() if ln.strip()]
        assert len(lines) > 0
        for line in lines:
            assert not line.startswith(" "), f"unexpected indent: {line!r}"
            assert line.endswith(".md"), f"unexpected extension: {line!r}"

    def test_check_exits_nonzero_when_missing(self, tmp_path):
        """--check must exit 1 if a file lacks html_meta.description."""
        doc = tmp_path / "page.md"
        doc.write_text("# Title\n\nContent.\n", encoding="utf-8")
        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "add_descriptions.py"),
             "--check", "--file", str(doc)],  # pass absolute path
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
        )
        assert result.returncode == 1

    def test_dry_run_does_not_modify_files(self, tmp_path):
        """--dry-run must not write to disk."""
        doc = tmp_path / "nodesc.md"
        content = "# Hello World\n\n" + "Word " * 40 + "\n"
        doc.write_text(content, encoding="utf-8")
        original_mtime = doc.stat().st_mtime

        subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "add_descriptions.py"),
             "--dry-run", "--file", str(doc)],  # pass absolute path
            capture_output=True,
            text=True,
            cwd=REPO_ROOT,
        )
        # File must be untouched
        assert doc.read_text(encoding="utf-8") == content
