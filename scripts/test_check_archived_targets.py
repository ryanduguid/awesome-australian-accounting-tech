"""Deterministic tests for the archived-target check; no network."""

from __future__ import annotations

import unittest
import urllib.error
from unittest import mock

import check_archived_targets as check


README = """
- **[Ozzit](https://github.com/ryanduguid/Ozzit)** - LAMBDAs.
- **[Payday](https://github.com/ryanduguid/payday-super-checker)** - archived.
- **[Payday again](https://GitHub.com/RyanDuguid/Payday-Super-Checker/releases)** - archived, case variant.
- **[xero-python](https://github.com/XeroAPI/xero-python)** - not ours.
"""


class ArchivedTargetTests(unittest.TestCase):
    def test_counts_links_per_own_repository(self) -> None:
        self.assertEqual(
            check.linked_repositories(README),
            {"ozzit": 1, "payday-super-checker": 2},
        )

    def test_archived_repository_fails_once_with_its_link_count(self) -> None:
        verdicts = {"ozzit": False, "payday-super-checker": True}

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

    def test_lookup_retries_server_errors_then_reads_the_flag(self) -> None:
        class ApiResponse:
            def __enter__(self) -> "ApiResponse":
                return self

            def __exit__(self, *args: object) -> None:
                return None

            def read(self) -> bytes:
                return b'{"archived": true}'

        attempts = 0

        def opener(request: object, timeout: int) -> ApiResponse:
            nonlocal attempts
            attempts += 1
            if attempts == 1:
                raise urllib.error.HTTPError("https://api.github.com/x", 502, "Bad Gateway", {}, None)
            return ApiResponse()

        self.assertTrue(check.repository_is_archived("hardhat-ledger", opener=opener))
        self.assertEqual(attempts, 2)

    def test_lookup_does_not_retry_client_errors(self) -> None:
        attempts = 0

        def opener(request: object, timeout: int) -> None:
            nonlocal attempts
            attempts += 1
            raise urllib.error.HTTPError("https://api.github.com/x", 404, "Not Found", {}, None)

        with self.assertRaises(urllib.error.HTTPError):
            check.repository_is_archived("missing", opener=opener)
        self.assertEqual(attempts, 1)

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
