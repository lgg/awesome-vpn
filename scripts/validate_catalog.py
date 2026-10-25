#!/usr/bin/env python3
"""Offline catalog integrity checks for Awesome VPN (stdlib only)."""
from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent.parent
MARKDOWN = ["README.md", "COMPATIBILITY.md", "CLIENTS.md", "TROUBLESHOOTING.md", "CONTRIBUTING.md", "MAINTENANCE.md", "RESEARCH-2026.md", "CLIENT-RESEARCH-2026.md", "ECOSYSTEM-RESEARCH-2026.md", "TRANSPORT-RESEARCH-2026.md", "DPI-RESEARCH-2026.md", "DPI-RESEARCH-ROUND2-2026.md"]
LINK = re.compile(r"(?<!!)\[[^\]]+\]\(([^\s)]+)(?:\s+[^)]*)?\)")
HEADING = re.compile(r"^#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)
SECTION = re.compile(r"^##\s+(.+)$", re.MULTILINE)
GITHUB_ENTRY = re.compile(r"^\s*- \*\*\[[^\]]+\]\((https://github\.com/[^)]+)\)\*\*", re.MULTILINE)


def github_slug(value: str) -> str:
    text = re.sub(r"<[^>]+>", "", value)
    text = re.sub(r"\[[^\]]+\]\([^)]+\)", "", text)
    text = text.lower().strip().replace(" ", "-")
    return re.sub(r"[^\w\-]", "", text)


def validate() -> int:
    problems = []
    warnings = []
    total_links = 0
    entry_count = 0

    for filename in MARKDOWN:
        path = ROOT / filename
        if not path.is_file():
            problems.append(f"Missing required file: {filename}")
            continue
        contents = path.read_text(encoding="utf-8")
        headings = Counter(github_slug(m.group(1)) for m in HEADING.finditer(contents))
        repeated = sorted(k for k, n in headings.items() if n > 1)
        if repeated:
            warnings.append(f"{filename}: repeated heading slugs: {', '.join(repeated)}")

        for hit in LINK.finditer(contents):
            dest = hit.group(1)
            total_links += 1
            uri = urlparse(dest)
            if uri.scheme in {"http", "https"}:
                if uri.scheme != "https":
                    warnings.append(f"{filename}: non-HTTPS URL: {dest}")
                if not uri.netloc:
                    problems.append(f"{filename}: invalid external URL: {dest}")
                if uri.netloc.lower() in {"github.com", "www.github.com"}:
                    if any(s in dest for s in (" ", "\\", "\n")):
                        problems.append(f"{filename}: invalid GitHub URL: {dest}")
                continue
            if uri.scheme:
                continue
            target = unquote(uri.path) or filename
            target_path = path.parent / target
            if not target_path.is_file():
                problems.append(f"{filename}: missing local target: {dest}")
                continue
            if uri.fragment and target_path.suffix.lower() == ".md":
                slug = unquote(uri.fragment)
                target_content = target_path.read_text(encoding="utf-8")
                target_headings = {github_slug(m.group(1)) for m in HEADING.finditer(target_content)}
                if slug not in target_headings:
                    problems.append(f"{filename}: missing heading anchor: {dest}")

    readme_path = ROOT / "README.md"
    if readme_path.exists():
        readme = readme_path.read_text(encoding="utf-8")
        if not readme.startswith("# Awesome VPN\n"):
            problems.append("README.md: expected top-level title")
        section = ""
        entries = []
        for line in readme.splitlines():
            if line.startswith("## "):
                section = line[3:]
            found = GITHUB_ENTRY.match(line)
            if found:
                entries.append((section, found.group(1).split("#")[0].rstrip("/").lower()))
        entry_count = len(entries)
        count = Counter(entries)
        dup = [f"{sect}: {url}" for (sect, url), n in count.items() if n > 1]
        if dup:
            problems.extend(f"Duplicate GitHub entry in same section: {x}" for x in dup)
        cross = Counter(url for _, url in entries)
        repeated_across = [url for url, n in cross.items() if n > 1]
        if repeated_across:
            warnings.append(f"{len(repeated_across)} projects intentionally appear in multiple topical sections")

    # Check that platform matrix entries remain valid Markdown table rows.
    clients_path = ROOT / "CLIENTS.md"
    if clients_path.is_file():
        client_rows = 0
        for line_no, line in enumerate(clients_path.read_text(encoding="utf-8").splitlines(), 1):
            if line.startswith("| **"):
                client_rows += 1
                if len(line.split("|")) != 6:
                    problems.append(f"CLIENTS.md:{line_no}: expected four table columns")
                if "](" not in line:
                    problems.append(f"CLIENTS.md:{line_no}: missing project link")
        if client_rows < 10:
            problems.append(f"CLIENTS.md: suspiciously short directory ({client_rows} rows)")
    else:
        problems.append("CLIENTS.md: required client catalog missing")

    print(f"Catalog check: {len(MARKDOWN)} Markdown files; {total_links} Markdown links; {entry_count} GitHub list entries")
    for notice in warnings:
        print(f"[WARN] {notice}")
    for problem in problems:
        print(f"[FAIL] {problem}")
    if problems:
        print(f"FAIL: {len(problems)} catalog integrity error(s)")
        return 1
    print("PASS: local links, fragment anchors and per-section duplicate checks")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
