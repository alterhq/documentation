#!/usr/bin/env python3
"""Download remote assets into local assets/ from a CSV manifest."""

from __future__ import annotations

import argparse
import csv
import sys
import urllib.error
import urllib.request
from pathlib import Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download assets from a CSV manifest")
    parser.add_argument(
        "--manifest",
        default="assets/manifest.csv",
        help="Path to manifest CSV (default: assets/manifest.csv)",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite files that already exist",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="HTTP timeout seconds (default: 30)",
    )
    return parser.parse_args()


def normalize_target(target_path: str) -> str:
    value = target_path.strip().lstrip("/")
    if value.startswith("assets/"):
        value = value[len("assets/") :]
    return value


def download_file(url: str, destination: Path, timeout: int) -> None:
    request = urllib.request.Request(
        url, headers={"User-Agent": "alter-docs-skill/1.0"}
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        destination.write_bytes(response.read())


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent.parent
    manifest_path = (repo_root / args.manifest).resolve()

    if not manifest_path.exists():
        print(f"ERROR: manifest not found: {manifest_path}")
        return 1

    success = 0
    skipped = 0
    failed = 0

    with manifest_path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        required = {"source_url", "target_path"}
        if not required.issubset(reader.fieldnames or set()):
            print("ERROR: manifest must include source_url,target_path columns")
            return 1

        for row in reader:
            source_url = (row.get("source_url") or "").strip()
            target_path = normalize_target(row.get("target_path") or "")
            if not source_url or not target_path:
                continue

            destination = repo_root / "assets" / target_path
            destination.parent.mkdir(parents=True, exist_ok=True)

            if destination.exists() and not args.overwrite:
                print(f"SKIP  {destination.relative_to(repo_root)}")
                skipped += 1
                continue

            try:
                download_file(source_url, destination, args.timeout)
                print(f"OK    {destination.relative_to(repo_root)}")
                success += 1
            except (urllib.error.URLError, TimeoutError, OSError) as exc:
                print(
                    f"FAIL  {source_url} -> {destination.relative_to(repo_root)} ({exc})"
                )
                failed += 1

    print(f"\nDone. downloaded={success} skipped={skipped} failed={failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
