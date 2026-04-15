#!/usr/bin/env python3
"""Check for broken links in link checker output and report them."""

import argparse
import json
import sys
from pathlib import Path


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="Check for broken links in link checker output."
    )
    parser.add_argument(
        "input_file", type=Path, help="Path to the link checker output JSON file"
    )
    return parser.parse_args()


def load_link_check_results(file_path: Path) -> list[dict]:
    """Load and parse link checker results from NDJSON file."""
    results = []
    with open(file_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                results.append(json.loads(line))
    return results


def is_rate_limited(result: dict) -> bool:
    """Check if a result represents a rate-limiting error.

    Rate limiting errors (HTTP 429) are indicated in the info field.
    """
    info = result.get("info", "")
    return "429" in info


def is_broken_link(result: dict) -> bool:
    """Check if a result represents a broken link (excluding rate-limited errors)."""
    return result.get("status") == "broken" and not is_rate_limited(result)


def format_broken_link(result: dict) -> str:
    """Format a broken link result for display."""
    filename = result.get("filename", "unknown")
    lineno = result.get("lineno", "?")
    uri = result.get("uri", "unknown")
    code = result.get("code", "unknown")
    info = result.get("info", "")

    output = f"{filename}:{lineno}: {uri}"
    if code:
        output += f" [HTTP {code}]"
    if info:
        output += f"\n  Error: {info}"

    return output


def main() -> int:
    """Main entry point."""
    args = parse_arguments()

    if not args.input_file.exists():
        print(f"Error: Input file '{args.input_file}' does not exist", file=sys.stderr)
        return 1

    print(f"Loading link check results from {args.input_file}...")
    all_results = load_link_check_results(args.input_file)

    broken_links = [r for r in all_results if is_broken_link(r)]
    rate_limited = [
        r for r in all_results if r.get("status") == "broken" and is_rate_limited(r)
    ]

    if rate_limited:
        print(f"\nℹ  {len(rate_limited)} URL(s) encountered rate limiting (ignored):")
        for result in rate_limited:
            print(f"  - {result.get('uri', 'unknown')}")

    if broken_links:
        print(f"\n❌ Found {len(broken_links)} broken link(s):\n")
        for result in broken_links:
            print(format_broken_link(result))
            print()
        return 1
    else:
        print("\n✅ No broken links found!")
        return 0


if __name__ == "__main__":
    sys.exit(main())
