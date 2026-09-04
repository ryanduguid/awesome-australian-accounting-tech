"""Deterministic tests for the archived-target check; no network."""

from __future__ import annotations

import unittest
from unittest import mock

import check_archived_targets as check


README = """
- **[Ozzit](https://github.com/ryanduguid/Ozzit)** - LAMBDAs.
- **[Payday](https://github.com/ryanduguid/payday-super-checker)** - archived.
- **[Payday again](https://github.com/ryanduguid/payday-super-checker/releases)** - archived.
- **[xero-python](https://github.com/XeroAPI/xero-python)** - not ours.
"""


class ArchivedTargetTests(unittest.TestCase):
    def test_counts_links_per_own_repository(self) -> None:
        self.assertEqual(
            check.linked_repositories(README),
            {"Ozzit": 1, "payday-super-checker": 2},
        )

    def test_archived_repository_fails_once_with_its_link_count(self) -> None:
        verdicts = {"Ozzit": False, "payday-super-checker": True}

        failures = check.archived_target_failures(
            "README.md", README, lookup=verdicts.__getitem__
        )

        self.assertEqual(len(failures), 1)
        self.assertIn("2 link(s) to ryanduguid/payday-super-checker", failures[0])

    def test_lookup_failure_is_a_failure(self) -> None:
        def lookup(name: str) -> bool:
            raise OSError("rate limited")

        failures = check.archived_target_failures("README.md", README, lookup=lookup)

        self.assertEqual(len(failures), 2)
        self.assertTrue(all("archived lookup failed" in f for f in failures))

    def test_allowlisted_file_is_skipped(self) -> None:
        with mock.patch.object(
            check, "ARCHIVED_TARGET_ALLOWLIST", frozenset({"HISTORY.md"})
        ):
            failures = check.archived_target_failures(
                "HISTORY.md", README, lookup=lambda name: True
            )

        self.assertEqual(failures, [])


if __name__ == "__main__":
    unittest.main()
