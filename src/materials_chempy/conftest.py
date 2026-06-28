"""
Created on 2026-06-28 18:34:14.

@author: eduardotc
@email: eduardotcampos@hotmail.com
@contributors: lu4vic

Pytest personal python utils configuration and analysis module.
"""

import ast
import os
import shutil
import sys
from pathlib import Path
from typing import TYPE_CHECKING

import pytest
from pytest import Session

from .logger import LOGGER

if TYPE_CHECKING:
    from pandas import DataFrame

FILES_TO_CHECK = [
    "src/materials_chempy/spectrophotometry/utils.py",
    "src/materials_chempy/logger.py",
    "src/materials_chempy/utils.py",
    "src/materials_chempy/mass_spectrometry/treat.py",
    "src/materials_chempy/var_handler.py",
    "src/materials_chempy/test_utils.py",
    "src/materials_chempy/test_cli.py",
]


def count_functions_with_and_without_docstrings(file: str) -> (int, int):
    """
    Count the number of functions with and without docstrings in a Python file.

    Parameters
    ----------
    file : str
        File name

    Returns
    -------
    functions_with_docstrings : int
        Number of documented functions in the file
    functions_without_docstrings : int
        Number of undocumented functions in the file

    Notes
    -----
    This function adds the complete path to the current dir, that should be the repo root, and the
    path to the python module folder (/src/materials_chempy) to the passed file name
    """
    repo_path = Path.cwd()
    repo_file = repo_path / file
    if repo_file.is_file():
        tree = ast.parse(repo_file.read_text(encoding="utf-8"))

    functions_with_docstrings = 0
    functions_without_docstrings = 0

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef | ast.ClassDef):
            if ast.get_docstring(node) is not None:
                functions_with_docstrings += 1
            elif ast.get_docstring(node) is None:
                functions_without_docstrings += 1

    return functions_with_docstrings, functions_without_docstrings


def supports_ansi_colors() -> bool:
    """

    Check terminal ansi code escaping support.

    Used for the remove of custom defined colored printing outputs in pytest, if the terminal don't
    support such colors.

    Returns
    -------
    bool
        True if the current run is in a tty terminal and the terminal supports ansi colors, False
        in the contrary.
    """
    if sys.stdout.isatty():
        term = os.getenv("TERM", "")
        return "xterm" in term or "color" in term
    return False

    # @pytest.fixture(autouse=True)
    # def config_pandas():
    """Config pandas options in pytest."""
    # pd.set_option("display.max_rows", 10)
    # pd.set_option("display.max_columns", 6)


def insert_word_in_middle(word: str) -> str:
    """Insert a word in the middle of a line string element with the width of the terminal."""
    terminal_width = shutil.get_terminal_size().columns
    dash_count = terminal_width - len(word)
    if dash_count <= 0:
        return word[:terminal_width]

    left_dashes = dash_count // 2
    right_dashes = dash_count - left_dashes

    return "=" * left_dashes + word + "=" * right_dashes


def count_and_pretty_print_docstr(docstr_df: "DataFrame"):
    """

    Pretty prints to terminal the infos about total of documented docstrings functions in files.

    Parameters
    ----------
    docstr_df : pandas.DataFrame
        Dataframe with the columns:
        - File : str
        - Documented : int
        = Not Documented : int
        - Percentage : float

    """
    LOGGER.print_color_dataframe(
        docstr_df, percent_columns=["Percentage"], percent_thresholds=(50.0, 75.0),
    )


@pytest.hookimpl(tryfirst=True)
def pytest_sessionstart(session: Session):
    """Get and print docstring coverage from the defined files."""
    assert isinstance(session, Session)
    import pandas as pd
    cov_df = pd.DataFrame({"File": FILES_TO_CHECK})
    cov_df[["Documented", "Not Documented"]] = cov_df["File"].apply(
        lambda file: pd.Series(count_functions_with_and_without_docstrings(file)),
    )
    cov_df["Percentage"] = round(
        (cov_df["Documented"] / (cov_df["Documented"] + cov_df["Not Documented"])) * 100,
        2,
    )
    count_and_pretty_print_docstr(cov_df)

