"""
Created on 2026-06-28 17:28:24.

@author: eduardotc
@email: eduardotcampos@hotmail.com
@contributors: lu4vic

Smoke-test materials_chempy CLI commands via real subprocess calls.

These tests exercise the installed module entry point (`materials_chempy`) rather than importing
its internals. They are suitable for local runs (kitty, Wayland) and CI. For commands that need
a D-Bus session, run tests under `dbus-run-session -- pytest -q`.
"""

from __future__ import annotations

import os
import subprocess
import sys
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from pytest_benchmark.fixture import BenchmarkFixture


def _base_env(overrides: dict[str, str] | None = None) -> dict[str, str]:
    """
    Build a deterministic environment for subprocess calls.

    Returns
    -------
    dict
        A copy of os.environ with stability tweaks (e.g., no colors, fixed width).
    """
    env = os.environ.copy()
    # Tame output formatting / encoding differences.
    env.setdefault("PYTHONUTF8", "1")
    env.setdefault("PYTHONIOENCODING", "utf-8")
    env.setdefault("LC_ALL", "C.UTF-8")
    env.setdefault("LANG", "C.UTF-8")
    # env.setdefault("NO_COLOR", "0")
    env.setdefault("SHELL", "/usr/bin/zsh")
    # Some CLIs branch on TERM; pick something vanilla.
    env.setdefault("TERM", "xterm-kitty")
    if overrides:
        env.update(overrides)
    return env


def _cmd(argv: list[str]) -> None:
    subprocess.run(
        [sys.executable, "-m", "materials_chempy", *argv],
        capture_output=True,
        env=_base_env(),
        text=True,
        check=False,
    )


def test_help_benchmark(benchmark: BenchmarkFixture) -> None:
    """Benchmark `materials_chempy --help` with pytest-benchmark."""
    benchmark(_cmd, ["--help"])
