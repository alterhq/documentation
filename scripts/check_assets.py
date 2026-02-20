#!/usr/bin/env python3
"""Validate assets-doc URL mapping and orphaned bundled assets."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
ASSET_DOC_PREFIX = "https://alterhq.com/assets-doc/"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check assets referenced by markdown")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument(
        "--fail-on-orphans",
        action="store_true",
        help="Fail if files in assets/ are not referenced",
    )
    return parser.parse_args()


def markdown_files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if ".git" not in p.parts)


def collect_asset_refs(root: Path) -> set[str]:
    refs: set[str] = set()
    for md in markdown_files(root):
        text = md.read_text(encoding="utf-8")
        for link in LINK_RE.findall(text):
            normalized = link.strip().strip("<>")
            if normalized.startswith(ASSET_DOC_PREFIX):
                rel = normalized[len(ASSET_DOC_PREFIX) :].lstrip("/")
                if rel:
                    refs.add(rel)
    return refs


def collect_assets(root: Path) -> set[str]:
    assets_root = root / "assets"
    if not assets_root.exists():
        return set()
    refs = set()
    valid_ext = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".mp4"}
    for p in assets_root.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(assets_root).as_posix()
        if rel == "manifest.csv":
            continue
        if p.suffix.lower() not in valid_ext:
            continue
        refs.add(rel)
    return refs


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()

    referenced = collect_asset_refs(root)
    bundled = collect_assets(root)

    missing = sorted(
        rel for rel in referenced if (root / "assets" / rel).exists() is False
    )
    orphaned = sorted(rel for rel in bundled if rel not in referenced)

    failed = False

    if missing:
        failed = True
        print("Missing local files for referenced /assets-doc/ URLs:\n")
        for rel in missing:
            print(f"- assets/{rel}")
        print()

    if orphaned:
        print("Orphaned bundled assets (not referenced by markdown):\n")
        for rel in orphaned:
            print(f"- assets/{rel}")
        print()
        if args.fail_on_orphans:
            failed = True

    if failed:
        return 1

    print("Asset check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
