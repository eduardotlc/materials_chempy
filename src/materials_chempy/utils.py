"""
Created on 2026-06-28 12:49:24.

@author: eduardotc
@email: eduardotcampos@hotmail.com

materials_chempy module general utils functions, to be used by other scripts/functions from the
app, not directly by client commands executions.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Literal


def assert_pathlib(
    path: any | None,
    type: str = "dir",
    check_exist: bool = False,
    fallback: str | None = None,
    print_error: bool | None = True,
) -> Path | None:
    """
    Assert given path is a pathlib path.

    Parameters
    ----------
    path : any, Optional
    type : str, Default "dir"
        Given path type, only influences if check_exist is `True`.
        may be "file" or "dir".
    check_exist : bool, Default False
        Wheter to raise error if given path don't exists
    fallback : str, Optional
        Fallback if path is not given, accepts special values like "cwd" that returns current dir.

    Returns
    -------
    Path, Optional

    Examples
    --------
    >>> from os import chdir, getcwd
    >>> curr_dir = getcwd()  # type: string
    >>> tst_p = assert_pathlib(curr_dir)
    >>> print(type(tst_p))
    <class 'pathlib.PosixPath'>

    >>> tst_miss_dir = assert_pathlib("./non_existing", fallback="cwd")
    >>> print(tst_miss_dir)
    non_existing

    >>> d_check = assert_pathlib("./non_existing", check_exist=True, fallback="cwd")
    >>> assert str(d_check) == curr_dir
    """
    try:
        if path is None:
            if fallback:
                path = Path.cwd() if fallback == "cwd" else fallback

            else:
                if check_exist:
                    print("\033[31mNot given any path to assert_pathlib function!\033[0m")
                    sys.exit(1)
                else:
                    return None

        elif isinstance(path, (str, bytes)):
            path = Path(path)

        if check_exist:
            if type == "file":
                if not path.is_file():
                    if fallback:
                        path = fallback
                    else:
                        print(f"\033[31mgiven file path {path} asserting failed!\033[0m")
                        return None
            elif type == "dir" and not path.is_dir():
                if fallback:
                    path = Path.cwd() if fallback == "cwd" else fallback
                else:
                    print(f"\033[31mgiven dir path {path} asserting failed!\033[0m")
                    return None

    except ValueError:
        if print_error:
            print(f"\033[31mGiven {path} could not be asserted as pathlib\033[0m")
        return None

    return path


def check_ansi_complete_color_code(arg: any) -> re.Match | Literal["repeat"]:
    r"""
    Check if given arg matches an ansi escaped color code with foreground and background colors.

    Parameters
    ----------
    arg : Any

    Returns
    -------
    re.Match or "repeat"
        An re Match class if the arg is an escaped color code, being Re.Match.group(1) the bg color
        and Re.Match.group(2) the fg color.

    Examples
    --------
    >>> ansi_test = "\x1b[48;5;002m\x1b[38;5;003m"
    >>> arg = check_ansi_complete_color_code(ansi_test)
    >>> print(arg.group(1))
    002
    >>> print(arg.group(2))
    003
    """
    pattern = r"\x1b\[48;5;(\d{3})m\x1b\[38;5;(\d{3})m"
    match = re.search(pattern, arg)
    return match if match is not None else "repeat"


def check_ansi_color_code(arg: any) -> re.Match | Literal["repeat"]:
    r"""
    Check if given arg matches an ansi escaped color code with foreground and background colors.

    Parameters
    ----------
    arg : Any

    Returns
    -------
    re.Match or "repeat"
        An re Match class if the arg is an escaped color code, being Re.Match.group(1) the bg color
        and Re.Match.group(2) the fg color.

    Examples
    --------
    >>> ansi_test = "\x1b[48;5;004m\x1b[38;5;010mtest_b\x1b[0m"
    >>> arg = check_ansi_color_code(ansi_test)

    >>> print(arg[0])
    (48, 4)

    >>> print(arg[1])
    (38, 10)
    """
    pattern = r"\x1b\[(38|48);5;(\d{2,3})m"
    match = re.findall(pattern, arg)
    result = [tuple(map(int, tup)) for tup in match] if match is not None else "repeat"

    return result
