#!/usr/bin/env python3
"""Update URLs in files based on permanent redirects from link checker.

Return codes:
    0: Success - files were modified
    1: Error - invalid input or file system error
    2: Success - no files needed modification
"""

import argparse
import json
import logging
import sys
from pathlib import Path
from urllib.parse import urlparse, urlunparse

# Directories to ignore when updating redirects
IGNORED_DIRECTORIES = [
    "reference/cmd-ref/amc/",
    "reference/cmd-ref/appliance/",
]

IGNORED_URLS = [
    # Wants to redirect to localized versions (e.g.
    # https://azure.microsoft.com/en-us), but we want to keep the original URL
    # to let it redirect to the correct localized version based on user location
    "https://azure.microsoft.com/",
]


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Update URLs in markdown files based on permanent redirect information.",
    )
    parser.add_argument(
        "input_file",
        type=Path,
        help="Path to the link checker output JSON file",
    )
    parser.add_argument(
        "--base-dir",
        type=Path,
        default=Path.cwd(),
        help="Base directory for resolving relative file paths (default: current directory)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would be changed without modifying files",
    )
    parser.add_argument(
        "--log-level",
        default="INFO",
        choices=["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"],
        help="Set the logging level (default: INFO)",
    )
    return parser.parse_args()


def load_link_check_results(file_path: Path) -> list[dict]:
    """Load and parse link checker results from NDJSON file."""
    results = []
    with file_path.open(encoding="utf-8") as f:
        for line in f:
            sline = line.strip()
            if sline:
                results.append(json.loads(sline))
    return results


def is_permanent_redirect(result: dict) -> bool:
    """Check if a result represents a permanent HTTP redirect.

    HTTP 301 (Moved Permanently) and 308 (Permanent Redirect) are considered permanent.
    """
    return result.get("status") == "redirected" and result.get("code") in (301, 308)


def should_ignore_file(filename: str) -> bool:
    """Check if a file should be ignored based on IGNORED_DIRECTORIES."""
    return any(filename.startswith(ignored_dir) for ignored_dir in IGNORED_DIRECTORIES)


def should_ignore_url(url: str) -> bool:
    """Check if a URL should be ignored based on IGNORED_URLS (exact match)."""
    return url in IGNORED_URLS


def preserve_url_fragment(old_uri: str, new_uri: str) -> str:
    """Preserve URL fragment from old URI if new URI doesn't have one.

    If the old URI has a fragment (#...) and the new URI doesn't,
    append the fragment to the new URI.
    """
    old_parsed = urlparse(old_uri)
    new_parsed = urlparse(new_uri)

    # If old URI has a fragment and new URI doesn't, preserve the fragment
    if old_parsed.fragment and not new_parsed.fragment:
        return urlunparse(
            (
                new_parsed.scheme,
                new_parsed.netloc,
                new_parsed.path,
                new_parsed.params,
                new_parsed.query,
                old_parsed.fragment,
            ),
        )

    return new_uri


def update_file_redirects(
    file_path: Path,
    redirects: list[dict],
    *,
    dry_run: bool = False,
) -> int:
    """Update redirects in a single file.

    Returns the number of lines modified.
    """
    with file_path.open(encoding="utf-8") as f:
        lines = f.readlines()

    modified_count = 0

    # Sort redirects by URI length (longest first) to handle substring issues
    sorted_redirects = sorted(redirects, key=lambda r: len(r["uri"]), reverse=True)

    for redirect in sorted_redirects:
        lineno = redirect["lineno"]
        old_uri = redirect["uri"]
        new_uri = redirect["info"]

        # Convert to 0-based index
        line_idx = lineno - 1

        # Check if line is in range
        if line_idx < 0 or line_idx >= len(lines):
            logging.warning(
                "Line %d out of range in %s for URI '%s'",
                lineno,
                file_path,
                old_uri,
            )
            continue

        original_line = lines[line_idx]

        # Check if URI is actually on this line
        if old_uri not in original_line:
            logging.warning(
                "URI '%s' not found on line %d in %s",
                old_uri,
                lineno,
                file_path,
            )
            continue

        # Preserve URL fragment if present in old URI but not in new URI
        new_uri = preserve_url_fragment(old_uri, new_uri)

        # Apply the replacement
        updated_line = original_line.replace(old_uri, new_uri)

        if updated_line != original_line:
            if dry_run:
                print(f"{file_path}:{lineno}")
                print(f"  - {original_line.rstrip()}")
                print(f"  + {updated_line.rstrip()}")
            else:
                lines[line_idx] = updated_line
            modified_count += 1

    if not dry_run and modified_count > 0:
        with file_path.open("w", encoding="utf-8") as f:
            f.writelines(lines)

    return modified_count


def group_redirects_by_file(redirects: list[dict]) -> dict[str, list[dict]]:
    """Group redirects by filename for efficient processing."""
    files = {}
    for redirect in redirects:
        filename = redirect["filename"]
        if filename not in files:
            files[filename] = []
        files[filename].append(redirect)
    return files


def main() -> int:
    """Main entry point."""
    args = parse_arguments()

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(levelname)s: %(message)s",
        stream=sys.stderr,
    )

    if not args.input_file.exists():
        logging.error("Input file '%s' does not exist", args.input_file)
        return 1

    # Load and filter results
    logging.info("Loading results from %s...", args.input_file)
    all_results = load_link_check_results(args.input_file)
    redirects = [
        r
        for r in all_results
        if is_permanent_redirect(r)
        and not should_ignore_file(r["filename"])
        and not should_ignore_url(r["uri"])
    ]

    # Log ignored redirects if any
    ignored_file_count = sum(
        1
        for r in all_results
        if is_permanent_redirect(r) and should_ignore_file(r["filename"])
    )
    ignored_url_count = sum(
        1
        for r in all_results
        if is_permanent_redirect(r) and should_ignore_url(r["uri"])
    )
    if ignored_file_count > 0:
        logging.info(
            "Ignored %d redirect(s) in excluded directories", ignored_file_count
        )
    if ignored_url_count > 0:
        logging.info("Ignored %d redirect(s) for excluded URLs", ignored_url_count)

    if not redirects:
        logging.info("No permanent redirects found.")
        return 0

    logging.info("Found %d permanent redirect(s)", len(redirects))

    if args.dry_run:
        print("\nDRY RUN - No files will be modified\n")

    # Group redirects by file
    files_to_update = group_redirects_by_file(redirects)

    # Process each file
    total_modified = 0
    for filename, file_redirects in files_to_update.items():
        file_path = args.base_dir / filename

        if not file_path.exists():
            logging.warning("File '%s' does not exist", file_path)
            continue

        modified = update_file_redirects(
            file_path,
            file_redirects,
            dry_run=args.dry_run,
        )
        total_modified += modified

    # Summary
    if args.dry_run:
        print(
            "Would modify %d line(s) in %d file(s)",
            total_modified,
            len(files_to_update),
        )
        return 0
    else:
        if total_modified > 0:
            logging.info(
                "Modified %d line(s) in %d file(s)",
                total_modified,
                len(files_to_update),
            )
            return 0
        else:
            logging.info("No files needed modification")
            return 2


if __name__ == "__main__":
    sys.exit(main())
