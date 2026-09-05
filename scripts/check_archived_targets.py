"""Fail when README.md links a ryanduguid repository that GitHub has archived.

lychee resolves every link, but an archived repository still answers 200, so a
link to a repository whose code moved into a monorepo passes the resolver and
sends a reader to a read-only archive. This check extracts every
github.com/ryanduguid/<repo> link from README.md, asks the GitHub REST API once
per repository whether it is archived, and fails on any archived target. A
lookup that cannot complete is a failure, not a pass. GITHUB_TOKEN, when set,
lifts the unauthenticated rate limit.

ARCHIVED_TARGET_ALLOWLIST lists files that may cite an archived repository as
provenance. The index has none today: every entry is a maintained home.

Stdlib only. Exit 0 clean, 1 on any failure.
"""

from __future__ import annotations

import json
import os
import re
import sys
import urllib.error
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FILES = ("README.md",)
ARCHIVED_TARGET_ALLOWLIST: frozenset[str] = frozenset()
# GitHub owner and repository names are case-insensitive, so match and
# count them that way.
OWN_REPO = re.compile(r"https://github\.com/ryanduguid/([A-Za-z0-9._-]+)", re.I)
MAX_ATTEMPTS = 5
GITHUB_API = "https://api.github.com/repos/ryanduguid/"
USER_AGENT = "awesome-australian-accounting-tech-archived-check"


def repository_is_archived(
    name: str, *, opener: object = urllib.request.urlopen
) -> bool:
    headers = {"User-Agent": USER_AGENT, "Accept": "application/vnd.github+json"}
    token = os.environ.get("GITHUB_TOKEN")
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(GITHUB_API + name, headers=headers)
    for attempt in range(1, MAX_ATTEMPTS + 1):
        try:
            with opener(req, timeout=30) as resp:  # type: ignore[operator]
                payload = json.loads(resp.read().decode("utf-8"))
            break
        except urllib.error.HTTPError as exc:
            # 4xx is definitive; 5xx and transport errors get a bounded retry.
            if not 500 <= exc.code < 600 or attempt == MAX_ATTEMPTS:
                raise
            print(f"retry {attempt}/{MAX_ATTEMPTS - 1} {name}: HTTP {exc.code}")
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt == MAX_ATTEMPTS:
                raise
            print(f"retry {attempt}/{MAX_ATTEMPTS - 1} {name}: {exc}")
    archived = payload.get("archived")
    if not isinstance(archived, bool):
        raise ValueError(f"GitHub API returned no archived flag for {name}")
    return archived


def linked_repositories(text: str) -> dict[str, int]:
    """Map each linked ryanduguid repository name to its link count."""
    return dict(Counter(name.lower() for name in OWN_REPO.findall(text)))


def archived_target_failures(
    rel: str, text: str, *, lookup=repository_is_archived
) -> list[str]:
    if rel in ARCHIVED_TARGET_ALLOWLIST:
        return []
    failures: list[str] = []
    for name, count in sorted(linked_repositories(text).items()):
        try:
            archived = lookup(name)
        except Exception as exc:  # noqa: BLE001 - report every failure mode
            failures.append(f"{rel}: ryanduguid/{name} -> archived lookup failed: {exc}")
            continue
        if archived:
            failures.append(
                f"{rel}: {count} link(s) to ryanduguid/{name}, which is archived "
                "(repoint to the maintained repository)"
            )
        else:
            print(f"ok {rel}: ryanduguid/{name} is maintained ({count} link(s))")
    return failures


def main() -> int:
    failures: list[str] = []
    for rel in FILES:
        text = (ROOT / rel).read_text(encoding="utf-8")
        failures.extend(archived_target_failures(rel, text))
    if failures:
        print(f"\n{len(failures)} failure(s):")
        for failure in failures:
            print(f"  FAIL {failure}")
        return 1
    print("\nall clear: no archived repository targets")
    return 0


if __name__ == "__main__":
    sys.exit(main())
