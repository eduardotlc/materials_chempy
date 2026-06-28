"""
Created on 2026-06-29 15:44:09.

@author: eduardotc
@contributors: lu4vic
@email: eduardotcampos@hotmail.com

Pytest utils, focused on docstrings examples tests, runned by `--doctest-modules` pytest flag.
"""

from collections.abc import Callable
from pathlib import Path
from typing import TYPE_CHECKING

from .logger import LOGGER

if TYPE_CHECKING:
    from argparse import ArgumentParser, Namespace, _ArgumentGroup

FILES_TO_CHECK = [
    "src/materials_chempy/spectrophotometry/utils.py",
    "src/materials_chempy/logger.py",
    "src/materials_chempy/utils.py",
    "src/materials_chempy/mass_spectrometry/treat.py",
    "src/materials_chempy/var_handler.py",
    "src/materials_chempy/test_utils.py",
]

HTML_CONTENT = [
    "<h1>Title</h1>",
    "\tcontent",
    "<h2>List</h2>",
    " - item 1",
    " - item 2",
]


def check_fn_with_input(toexec_fn: Callable, str_input: str, args_list: tuple) -> any:
    """
    Run given `fn` function, including given string `str_input`.

    Parameters
    ----------
    toexec_fn : Callable
    str_input : str
    args_list : list

    Returns
    -------
    any
        The return of `fn` function

    Examples
    --------
    >>> def check_fn(test_param):
    ...     print_tst = input()
    ...     print(print_tst)
    ...     return test_param

    >>> tst = check_fn_with_input(check_fn, "test_inp", ["test_param"])
    test_inp

    >>> print(tst)
    test_param
    """
    from unittest.mock import patch

    with patch("builtins.input", return_value=str_input):
        test_return = toexec_fn(*args_list)
    if test_return:
        return test_return


def create_dummy_img(file_path: Path | str):
    """
    Create a dummy image.

    Parameters
    ----------
    file_path : str or Path
    """
    from PIL import Image

    img = Image.new("RGB", (1024, 768), (144, 142, 24))
    img.save(file_path)


def create_dummy_file(file_path: Path | str):
    """
    Create a dummy file based on file extension.

    Parameters
    ----------
    file_path : str or Path
    """
    from .utils import assert_pathlib
    dummy_content = {
        ".md": ["# Markdown Title"],
        ".png": create_dummy_img,
        ".jpg": create_dummy_img,
        ".jpeg": create_dummy_img,
        ".html": HTML_CONTENT,
        ".mp4": ["dummy video data"],
    }

    file_path = assert_pathlib(path=file_path, type="file", check_exist=False)

    file_ext = file_path.suffix

    if isinstance(dummy_content[file_ext], list):
        file_path.write_text("\n".join(dummy_content[file_ext]), encoding="utf-8")

    elif callable(dummy_content[file_ext]):
        dummy_content[file_ext](file_path)


# -TODO: Check necessity or allow deprecation
def create_tmp_dir_with_files(files_list: list[Path | str]) -> str:
    """
    Create a tmp dir withe given `files_list` dummy files.

    The tmp dir is created using module `tempfile`, and the temp files with names obtained from
    the list `files_list` are created on this dir, with each file content being a dummy content
    based on the file name extension.

    All files from given list should contain the full file name including extension, the possible
    extensions are:

        - md

        - png

        - dir

    Parameters
    ----------
    files_list : list

    Returns
    -------
    test_dir : str
        The full path to created temporary dir
    files_list : list
        List with complete file path of created files
    """
    from tempfile import mkdtemp

    from .utils import assert_pathlib

    if not isinstance(files_list, list):
        files_list = [files_list]

    files_list = [
        assert_pathlib(path=f, check_exist=False, type="file", fallback=f) for f in files_list
    ]

    test_dir = Path(mkdtemp())

    files_list = [test_dir / f for f in files_list]

    for file in files_list:
        create_dummy_file(file)

    return test_dir, files_list


def create_tmp_file_with_content(
    file_content: list,
    file_suffix: str = "",
    file_name: str | None = None,
    create_dir: str | None = None,
    override_dir: bool = False,
    override_file: bool = False,
) -> str:
    """
    Create temp file of given name, and write to it each element of `file_content` as a line.

    Parameters
    ----------
    file_content : list
        List of lines to be written to the file, each string element is a line.
    file_suffix : str, optional
        Optional suffix file extension to add to the file
    file_name : str, optional
        Name of the file to be created (without the complete path)
    create_dir : str, optional
        Complete path to the dir to create the file in (Only dir path, without file name)
    override_dir : bool, default False
        If the given `create_dir` already exists, deletes it
    override_file : bool, default False
        If given `file_name` in given `create_dir` already exists, force override the file

    Returns
    -------
    file_path : str

    Examples
    --------
    >>> file_cont = ["line a", "line b"]
    >>> tmp_file = create_tmp_file_with_content(file_cont, file_name="materials_chempy_test.ini")
    >>> with open(tmp_file, "r") as f:
    ...     lines = f.readlines()
    >>> assert len(lines) == 2

    >>> tmp_new = create_tmp_file_with_content(
    ...     file_cont,
    ...     file_name="materials_chempy_test_utils.ini",
    ...     create_dir="/tmp/tmpdir_materials_chempy",
    ...     override_dir=True,
    ... )
    >>> with open(tmp_new, "r") as f:
    ...     lines_new = f.readlines()
    >>> print(lines_new[-1])
    line b
    """
    from shutil import rmtree
    from tempfile import mkdtemp, mkstemp

    from .utils import assert_pathlib

    tmpdir = Path(create_dir or mkdtemp())

    file_name = assert_pathlib(path=file_name, type="file", check_exist=False)

    if file_name is None:
        _, tmp_file = mkstemp(suffix=file_suffix, dir=tmpdir)

    tmp_file = tmpdir / file_name

    if tmpdir.is_dir():
        if override_dir:
            rmtree(tmpdir)
            tmpdir.mkdir()
        elif tmp_file.is_file() and override_file:
            tmp_file.unlink()
    else:
        tmpdir.mkdir()

    file_content = [
        a + "\n" for a in file_content[0 : len(file_content) - 1] if not a.endswith("\n")
    ] + [file_content[-1]]
    tmp_file.write_text("".join(file_content), encoding="utf-8")

    return tmp_file
