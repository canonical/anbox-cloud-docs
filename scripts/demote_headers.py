#!/usr/bin/env python3
"""Demote markdown headers by one level (e.g., ## becomes #, ### becomes ##).

Return codes:
    0: Success - files were modified
    1: Error - invalid input or file system error
    2: Success - no files needed modification
"""

import argparse
import difflib
import logging
import re
import sys
from pathlib import Path


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Demote markdown headers by one level (e.g., ## becomes #, ### becomes ##)",
    )
    parser.add_argument(
        "paths",
        nargs="+",
        type=Path,
        help="Markdown files or directories to process",
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


def demote_headers(content: str) -> str:
    """Demote markdown headers by one level using regex.

    Lines starting with ## or more have one leading # removed.
    Level-1 headers (#) are left unchanged."""
    return re.sub(
        r"^(#{2,})([ \t]|$)",
        lambda m: m.group(1)[1:] + m.group(2),
        content,
        flags=re.MULTILINE,
    )


def process_file(file_path: Path, *, dry_run: bool = False) -> bool:
    """Process a single markdown file.

    Returns True if the file was modified (or would be modified in dry-run mode).
    """
    try:
        with file_path.open(encoding="utf-8") as f:
            original_content = f.read()
    except OSError as e:
        logging.error("Failed to read %s: %s", file_path, e)
        return False

    new_content = demote_headers(original_content)

    if new_content != original_content:
        if dry_run:
            # Generate unified diff
            original_lines = original_content.splitlines(keepends=True)
            new_lines = new_content.splitlines(keepends=True)

            diff = difflib.unified_diff(
                original_lines,
                new_lines,
                fromfile=f"a/{file_path}",
                tofile=f"b/{file_path}",
            )

            sys.stdout.writelines(diff)
            # print("\n".join(diff))
        else:
            try:
                with file_path.open("w", encoding="utf-8") as f:
                    f.write(new_content)
                logging.debug("Modified %s", file_path)
            except OSError as e:
                logging.error("Failed to write %s: %s", file_path, e)
                return False

        return True

    return False


def process_paths(paths: list[Path], *, dry_run: bool = False) -> int:
    """Process one or more files or directories.

    Returns the number of files modified.
    """
    modified_count = 0
    files_to_process = []

    for path in paths:
        if not path.exists():
            logging.warning("Path does not exist: %s", path)
            continue

        if path.is_file():
            if path.suffix == ".md":
                files_to_process.append(path)
            else:
                logging.warning("Skipping non-markdown file: %s", path)

        elif path.is_dir():
            files_to_process.extend(path.rglob("*.md"))

    logging.info("Found %d markdown file(s) to process", len(files_to_process))

    for md_file in files_to_process:
        if process_file(md_file, dry_run=dry_run):
            modified_count += 1
            if not dry_run:
                logging.info("Modified %s", md_file)

    return modified_count


def main() -> int:
    """Main entry point."""
    args = parse_arguments()

    logging.basicConfig(
        level=getattr(logging, args.log_level),
        format="%(levelname)s: %(message)s",
        stream=sys.stderr,
    )

    if args.dry_run:
        print("\nDRY RUN - No files will be modified\n")

    modified_count = process_paths(args.paths, dry_run=args.dry_run)

    if args.dry_run:
        print(f"\nWould modify {modified_count} file(s)")
        return 0
    else:
        if modified_count > 0:
            logging.info("Modified %d file(s)", modified_count)
            return 0
        else:
            logging.info("No files needed modification")
            return 2


if __name__ == "__main__":
    sys.exit(main())
