#!/usr/bin/env python3
"""Measure an OpenClaw AGENTS.md file without modifying it."""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path


def utf16_code_units(text: str) -> int:
    """Match JavaScript String.length, used by OpenClaw character limits."""
    return len(text.encode("utf-16-le")) // 2


def analyze(path: Path, target_min: int, target_max: int, limit: int) -> dict:
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    lines = text.splitlines()
    headings = [line.strip() for line in lines if line.lstrip().startswith("#")]
    duplicate_headings = sorted(
        heading for heading, count in Counter(headings).items() if count > 1
    )
    characters = utf16_code_units(text)
    if characters > limit:
        status = "over-live-limit"
    elif characters > target_max:
        status = "above-recommended"
    elif characters < target_min:
        status = "below-target-review-for-completeness"
    else:
        status = "within-recommended-range"

    nonempty = [line.strip() for line in lines if line.strip()]
    return {
        "path": str(path.resolve()),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "openclaw_characters": characters,
        "unicode_code_points": len(text),
        "lines": len(lines),
        "target_min": target_min,
        "target_max": target_max,
        "live_limit": limit,
        "status": status,
        "remaining_characters_before_limit": limit - characters,
        "duplicate_headings": duplicate_headings,
        "last_nonempty_line": nonempty[-1] if nonempty else "",
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Report AGENTS.md size, hash, duplicate headings, and limit status."
    )
    parser.add_argument("path", type=Path, help="Path to the AGENTS.md file")
    parser.add_argument("--target-min", type=int, default=10000)
    parser.add_argument("--target-max", type=int, default=14000)
    parser.add_argument("--limit", type=int, default=20000)
    parser.add_argument(
        "--format", choices=("json", "text"), default="json", dest="output_format"
    )
    parser.add_argument(
        "--fail-over-limit",
        action="store_true",
        help="Return exit code 3 when the file exceeds --limit.",
    )
    args = parser.parse_args()

    if args.target_min < 0 or args.target_max < args.target_min:
        parser.error("target range must be non-negative and ordered")
    if args.limit <= 0:
        parser.error("limit must be greater than zero")
    if not args.path.is_file():
        parser.error(f"file not found: {args.path}")

    try:
        result = analyze(args.path, args.target_min, args.target_max, args.limit)
    except UnicodeDecodeError as exc:
        parser.error(f"file is not valid UTF-8: {exc}")

    if args.output_format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        for key, value in result.items():
            print(f"{key}: {value}")
    if args.fail_over_limit and result["status"] == "over-live-limit":
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
