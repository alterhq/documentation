#!/usr/bin/env python3
"""Validate markdown links and asset references."""

from __future__ import annotations

import argparse
import re
import sys
import urllib.error
import urllib.request
from pathlib import Path

LINK_RE = re.compile(r"(!)?\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
ASSET_DOC_PREFIX = "https://alterhq.com/assets-doc/"
MEDIA_EXTENSIONS = (
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".svg",
    ".mp4",
    ".mov",
    ".webm",
)
SKIP_MARKDOWN_FILES = {
    "temp-docs.md",
    "references/temp-docs-source.md",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check markdown links")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument(
        "--check-external",
        action="store_true",
        help="Check HTTP status for external links",
    )
    parser.add_argument(
        "--check-external-media",
        action="store_true",
        help="Check HTTP status for external media links only",
    )
    parser.add_argument("--timeout", type=int, default=10, help="HTTP timeout")
    return parser.parse_args()


def iter_markdown_files(root: Path) -> list[Path]:
    files = []
    for path in root.rglob("*.md"):
        if ".git" in path.parts:
            continue
        rel = path.relative_to(root).as_posix()
        if rel in SKIP_MARKDOWN_FILES:
            continue
        files.append(path)
    return sorted(files)


def extract_links(path: Path) -> list[tuple[str, bool]]:
    text = path.read_text(encoding="utf-8")
    links: list[tuple[str, bool]] = []
    in_code_block = False
    for line in text.splitlines():
        if line.strip().startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        for match in LINK_RE.finditer(line):
            is_image = bool(match.group(1))
            link = match.group(2).strip().strip("<>")
            links.append((link, is_image))
    return links


def is_media_link(url: str, is_image: bool) -> bool:
    if is_image:
        return True
    normalized = url.lower().split("#", 1)[0].split("?", 1)[0]
    return normalized.endswith(MEDIA_EXTENSIONS)


def check_external(url: str, timeout: int) -> bool:
    req = urllib.request.Request(
        url, method="HEAD", headers={"User-Agent": "alter-docs-skill/1.0"}
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return 200 <= resp.status < 400
    except Exception:
        req = urllib.request.Request(
            url, method="GET", headers={"User-Agent": "alter-docs-skill/1.0"}
        )
        try:
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return 200 <= resp.status < 400
        except (urllib.error.URLError, TimeoutError):
            return False


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    issues: list[str] = []

    for md_path in iter_markdown_files(root):
        for link, is_image in extract_links(md_path):
            if link.startswith(("#", "mailto:", "tel:")):
                continue

            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", link):
                if not link.startswith(("http://", "https://")):
                    continue

            if link.startswith(("http://", "https://")):
                if link.startswith(ASSET_DOC_PREFIX):
                    rel = link[len(ASSET_DOC_PREFIX) :].lstrip("/")
                    local_path = root / "assets" / rel
                    if not local_path.exists():
                        issues.append(
                            f"{md_path.relative_to(root)}: missing asset for {link} -> {local_path.relative_to(root)}"
                        )
                elif args.check_external_media and is_media_link(link, is_image):
                    if not check_external(link, args.timeout):
                        issues.append(
                            f"{md_path.relative_to(root)}: broken external media link {link}"
                        )
                elif args.check_external and not check_external(link, args.timeout):
                    issues.append(
                        f"{md_path.relative_to(root)}: broken external link {link}"
                    )
                continue

            if link.startswith("/"):
                if args.check_external:
                    full_url = f"https://alterhq.com{link}"
                    if not check_external(full_url, args.timeout):
                        issues.append(
                            f"{md_path.relative_to(root)}: broken root-relative link {link}"
                        )
                continue

            target = link.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            if target.startswith("assets/"):
                resolved = (root / target).resolve()
            else:
                resolved = (md_path.parent / target).resolve()
            if not resolved.exists():
                issues.append(
                    f"{md_path.relative_to(root)}: missing local link target {link}"
                )

    if issues:
        print("Link check failed:\n")
        for issue in issues:
            print(f"- {issue}")
        print(f"\nTotal issues: {len(issues)}")
        return 1

    print("Link check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
