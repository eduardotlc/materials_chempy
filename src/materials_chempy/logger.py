"""
Created on 2026-06-28 15:49:15.

@author: eduardotc
@contributors: lu4vic
@email: eduardotcampos@hotmail.com

Logger module function, defined on a separate file, since it is a core utillity.

Define the following TypeAlias

- LoggerColorsNames
    Used for the possible colors names, defined by the class dict of ansi colors

- LoggerColors
    Define the possible colors formats to be passed to the class to use

- LoggerLineStyle
    Define the strigs binded to lines styles when printing lines

- LoggerArgs
    Define the optional args strings that may be passed to some of the class functions
"""

from __future__ import annotations

import re
import sys
from collections.abc import Iterable
from dataclasses import asdict, is_dataclass
from json import dumps as jdumps
from os import system
from pathlib import Path
from re import match
from typing import (
    TYPE_CHECKING,
    Any,
    Literal,
    TextIO,
)

from .var_handler import VARHANDLE

if TYPE_CHECKING:
    from blessed import Terminal
    from pandas import DataFrame

type LoggerColorsNames = Literal[
    "RED",
    "GRN",
    "YLW",
    "BLUE",
    "MGN",
    "CYAN",
    "PRP",
    "PNK",
    "RST",
    "BLD",
    "TXT",
    "BLCK",
    "WHT",
    "blue",
    "yellow",
    "red",
    "green",
    "magenta",
    "purple",
    "pink",
    "reset",
    "white",
    "black",
    "cyan",
    "text",
    "foreground",
    "bold",
    "aqua",
    "orange",
    "dark_gray",
    "gray",
    "light_gray",
    "light_red",
]

type LoggerColors = LoggerColorsNames | list[LoggerColorsNames] | tuple[LoggerColorsNames]

type LoggerLineStyle = Literal["single", "simple", "double"]

type LoggerArgs = LoggerLineStyle | Literal["print_next_line"]


class ScriptLogger:
    """
    Handle script messages with optional ANSI colors and stderr redirection.

    This class provides methods for formatting messages in different categories, such as info,
    warning, error, success, and debug. ANSI colors can be enabled or disabled, and error/warning
    messages can optionally be redirected to stderr.

    Parameters
    ----------
    use_colors : bool, optional
        Whether to use ANSI colors in the output (default is True).

    Attributes
    ----------
    ansi_dicts : dict
        `VARHANDLE.ansi_dicts` dictionary, that associates ansi colors names to their escaped codes.

    messages : dict
        Associates the log message types ("error", "info" etc...) to a list containing the prefix
        ([LOG_NAME]) color on the message, and the main text color from the message.
        For example, a list of "warning": ["WHITE", "PURPLE"], would print [WARNING] in white, and
        the message after it on purple.

        Message type can be:
            - info
            - warning
            - error
            - success
            - debug
            - reset

    style_elements : dict
        Dict with style elements names associated to its char, like "double" (from double line) has
        the value "=".

        has the keys:
            - "simple"/"single"
            - "double"
            - "blank"

    use_colors : bool
        Stores whether ANSI colors should be used in the output.

    console : rich.console.Console
        Rich console class instance, initiated with `VARHANDLE.markdown_theme` personal theme

    ignore_list : list
        List of log message types ("warning", "info", etc...) that should not be printed to terminal
        (sends it to /dev/null)

    alt_stdout_file : str, Default "/tmp/materials_chempy/alt_stdout"

    alternative_stdout : bool, Default False
        Instead of printing to default terminal output, redirect it to `alt_stdout_file` attribute.
        Can be setted through `set_use_alt_stdout` method.

    alt_stderr_file : str, Default "/tmp/materials_chempy/alt_stderr"

    alternative_stderr : bool, Default False
        Instead of printing stderr to terminal output, redirect it to `alt_stderr_file` attribute.
        Can be setted through `set_use_alt_stderr` method.

    pipe_stderr_to_stdout : bool, Default False
        Redirect stderr outputs to stdout

    printed_checking_error : bool, Default False
        Stores whether a checking error from `argtypes` argparse args handling has already been
        raised.

    input_string : str, Default ""
        Stores user inputs in terminal in `terminal_handle_input`.

    _ansi_re
    """
    #TODO(lu4vic): `Check printed_checking_error` param

    def __init__(
        self,
        use_colors: bool = True,
    ):
        """
        Init logger class, to prompt messages and log infos to terminal.

        Parameters
        ----------
        use_colors : bool
            Wheter the printing should use ansi colors or not
        """
        self.messages = {
            "info": [VARHANDLE("BLUE"), VARHANDLE("BLD")],
            "warning": [VARHANDLE("YLW"), VARHANDLE("BLD")],
            "error": [VARHANDLE("RED"), VARHANDLE("LRED")],
            "success": [VARHANDLE("GRN"), VARHANDLE("AQUA")],
            "debug": [VARHANDLE("MGN"), VARHANDLE("BLD")],
            "reset": VARHANDLE("RST"),
        }
        self.style_elements = {
            "simple": "-",
            "single": "-",
            "double": "=",
            "blank": " ",
        }
        self.use_colors = use_colors
        self.ignore_list = []
        self.alt_stdout_file = "/tmp/materials_chempy/alt_stdout"
        self.alternative_stdout = False
        self.alt_stderr_file = "/tmp/materials_chempy/alt_stderr"
        self.alternative_stderr = False
        self.pipe_stderr_to_stdout = False
        self.printed_checking_error = False
        self.input_string = ""
        self._ansi_re = re.compile(r"\x1b\[[0-9;]*m")

    def get_line_el(self, name: str = "double") -> str:
        """
        Return line element char.

        Parameters
        ----------
        name : str, Default "double"

        Returns
        -------
        str

        Examples
        --------
        >>> logger = ScriptLogger()
        >>> print(logger.get_line_el("double"))
        =
        """
        return self.style_elements.get(name, "=")

    def toggle_ignore_print(self, msg_type: str):
        """
        Add or remove given message type to `ignore_list` list.

        Add `msg_type` to `ignore_list` if not already on it, and if already on it, remove it.

        Parameters
        ----------
        msg_type : str
            Log type from the message, should be one from:

                - info

                - warning

                - error

                - success

                - debug

        Examples
        --------
        >>> logger = ScriptLogger()

        >>> print(logger.ignore_list)
        []

        >>> logger.toggle_ignore_print("info")
        >>> print(logger.ignore_list)
        ['info']

        >>> logger.toggle_ignore_print("info")
        >>> print(logger.ignore_list)
        []
        """

        if msg_type in self.messages:
            if msg_type in self.ignore_list:
                self.ignore_list.remove(msg_type)
            else:
                self.ignore_list.append(msg_type)

    def _format_message(self, msg_type: str, message: str) -> str:
        """
        Format the message with optional ANSI color.

        Private function, to be used by message type functions like `error`, `warning` etc...

        Parameters
        ----------
        msg_type : str
            The type of message, can be:
                - info
                - warning
                - error
                - success
                - debug
                - reset
        message : str
            The message text to be displayed.

        Returns
        -------
        str
            The formatted message string.

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)

        >>> message = logger._format_message("info", "test")
        >>> print(message)
        [INFO] test
        """
        reset = [self.messages["reset"], self.messages["reset"]] if self.use_colors else ["", ""]
        colors = self.messages.get(msg_type, ["", ""])
        prefix = f"[{msg_type.upper()}]"
        return (
            f"{colors[0]}{prefix}{reset[0]} {colors[1]}{message}{reset[1]}"
            if self.use_colors
            else f"{prefix} {message}"
        )

    def _get_output_stream(self, msg_type: str) -> TextIO:
        """
        Return the appropriate output stream based on the message type and settings.

        Output stream is defined by an up-to-bottom order from the following checks:

            - `os.devnul` if `msg_type` is in `ignore_list` (added by `toggle_ignore_print`

            - `alt_stdout_file` if `alternative_stdout` and `msg_type` in `stdout_list`

            - `alt_stderr_file` if `alternative_stderr` and `msg_type` in `stderr_list`

            - `sys.stderr` if `msg_type` in `stderr_list` and not `pipe_stderr_to_stdout`

            - `sys.stdout` (All other cases)

        Parameters
        ----------
        msg_type : str
            Logging level of the message, like error or warning, can be:
                - info
                - warning
                - error
                - success
                - debug
                - input
                - reset

        Returns
        -------
        TextIO
            Either sys.stdout or sys.stderr.

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)

        >>> info_stream = logger._get_output_stream("info")
        >>> print(type(info_stream))
        <class 'doctest._SpoofOut'>

        >>> error_stream = logger._get_output_stream("error")
        >>> print(type(error_stream))
        <class '_pytest.capture.EncodedFile'>

        >>> logger.toggle_ignore_print("info")
        >>> info_stream = logger._get_output_stream("info")
        >>> print(type(info_stream))
        <class '_io.TextIOWrapper'>

        >>> logger.toggle_ignore_print("info")
        """
        stdout_list = ["success", "info", "debug", "input", "plain", "warning", "test"]
        stderr_list = ["error"]

        if msg_type in self.ignore_list:
            return Path("/dev/null").open(mode="w", encoding="utf-8")

        elif self.alternative_stdout and msg_type in stdout_list:
            return Path(self.alt_stdout_file).open(mode="a", encoding="utf-8")

        elif self.alternative_stderr and msg_type in stderr_list:
            return Path(self.alt_stderr_file).open(mode="a", encoding="utf-8")

        elif msg_type in stderr_list and not self.pipe_stderr_to_stdout:
            return sys.stderr

        return sys.stdout

    def set_use_alt_stdout(self, enable: bool, reset_clean: bool = False):
        r"""
        Set `alternative_stdout` attribute.

        When `alternative_stdout` is True, toggle pipe redirection of stdout messages appending them
        to the `/tmp/materials_chempy_alt_stdout` file.

        Parameters
        ----------
        enable : bool

        Examples
        --------
        >>> import shutil
        >>> logger = ScriptLogger()
        >>> lines = ["line a\n", "line b\n", "line c\n"]
        >>> with open(logger.alt_stdout_file, "w") as f:
        ...     _ = f.writelines(lines)

        >>> print(logger.alternative_stdout)
        False

        >>> logger.set_use_alt_stdout(True)
        >>> print(logger.alternative_stdout)
        True

        >>> with open(logger.alt_stdout_file, "r") as f:
        ...     len_lines = len(f.readlines())
        >>> print(len_lines)
        3

        >>> logger.set_use_alt_stdout(False, reset_clean=True)
        >>> with open(logger.alt_stdout_file, "r") as f:
        ...     try:
        ...         len_lines = len(f.readlines())
        ...     except FileNotFoundError:
        ...         len_lines = 0
        >>> print(len_lines)
        0
        """
        if reset_clean:
            with Path(self.alt_stdout_file).open(encoding="utf-8", mode="w") as _file:
                pass
        if enable:
            self.alternative_stdout = True
        else:
            self.alternative_stdout = False

    def get_alt_stdout(self, total_lines: int = 1) -> list:
        """
        Get alternative stdout file `total_lines` last appended lines.

        Alternative stdout file is defined by `alt_stdout_file`, and the stdout is redirected to it
        instead of default stdout based on `alternative_stdout`.

        To reset the file `set_use_alt_stdout` can be called with `reset_clean` True.

        Parameters
        ----------
        total_lines : int (default 1)
            number of lines to get, from the last to the first.

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)
        >>> logger.set_use_alt_stdout(True, reset_clean=True)

        >>> logger.info("line a")
        >>> logger.info("line b")
        >>> logger.info("line c")
        >>> logger.info("line d")

        >>> lines = logger.get_alt_stdout(3)

        >>> print(lines)
        ['[INFO] line b', '[INFO] line c', '[INFO] line d']

        >>> logger.set_use_alt_stdout(False, reset_clean=True)
        """
        with Path(self.alt_stdout_file).open(encoding="utf-8") as f:
            lines = f.readlines()

        lines = [re.sub(r"\n", "", line) for line in lines]
        total_lines = len(lines) if total_lines == -1 else total_lines
        # return lines
        return lines[len(lines) - total_lines : len(lines)]

    def set_use_alt_stderr(self, enable: bool, reset_clean: bool = False):
        r"""
        Set `alternative_stderr` attribute.

        When `alternative_stderr` is True, toggle pipe redirection of stderr messages appending them
        to the `/tmp/materials_chempy_alt_stderr` file.

        Parameters
        ----------
        enable : bool

        Examples
        --------
        >>> import shutil
        >>> logger = ScriptLogger()
        >>> lines = ["line a\n", "line b\n", "line c\n"]
        >>> with open(logger.alt_stderr_file, "w") as f:
        ...     _ = f.writelines(lines)

        >>> print(logger.alternative_stderr)
        False

        >>> logger.set_use_alt_stderr(True)
        >>> print(logger.alternative_stderr)
        True

        >>> with open(logger.alt_stderr_file, "r") as f:
        ...     len_lines = len(f.readlines())
        >>> print(len_lines)
        3

        >>> logger.set_use_alt_stderr(False, reset_clean=True)
        >>> with open(logger.alt_stderr_file, "r") as f:
        ...     len_lines = len(f.readlines())
        >>> print(len_lines)
        0
        """
        if reset_clean:
            with Path(self.alt_stderr_file).open(encoding="utf-8", mode="w") as _file:
                pass
        if enable:
            self.alternative_stderr = True
        else:
            self.alternative_stderr = False

    def get_alt_stderr(self, total_lines: int = 1) -> list:
        """
        Get alternative stderr file `total_lines` last appended lines.

        Alternative stderr file is defined by `alt_stderr_file`, and the stderr is redirected to it
        instead of default stderr based on `alternative_stderr`.

        To reset the file `set_use_alt_stderr` can be called with `reset_clean` True.

        Parameters
        ----------
        total_lines : int (default 1)
            number of lines to get, from the last to the first.

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)
        >>> logger.set_use_alt_stderr(True, reset_clean=True)

        >>> logger.error("line a")
        >>> logger.error("line b")
        >>> logger.error("line c")
        >>> logger.error("line d")

        >>> lines = logger.get_alt_stderr(3)

        >>> print(lines)
        ['[ERROR] line b', '[ERROR] line c', '[ERROR] line d']

        >>> logger.set_use_alt_stderr(False, reset_clean=True)
        """
        with Path(self.alt_stderr_file).open(encoding="utf-8") as f:
            lines = f.readlines()

        lines = [re.sub(r"\n", "", line) for line in lines]

        return lines[len(lines) - total_lines : len(lines)]

    def info(self, message: str, exit_bool: bool | None = False) -> None:
        """
        Print an info message.

        Parameters
        ----------
        message : str
        exit_bool : bool (Default False)
            Whether to exit running script after the error

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)
        >>> logger.info("test")
        [INFO] test
        """
        print(self._format_message("info", message), file=self._get_output_stream("info"))
        if exit_bool:
            sys.exit(1)

    def warning(self, message: str) -> None:
        """
        Print a warning message.

        Parameters
        ----------
        message : str

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)
        >>> logger.pipe_stderr_to_stdout = True

        >>> logger.warning("test")
        [WARNING] test
        """
        print(self._format_message("warning", message), file=self._get_output_stream("warning"))

    def error(self, message: str, exit_bool: bool | None = False) -> None:
        """
        Print an error message.

        Parameters
        ----------
        message : str
        exit_bool : bool (Default False)
            Whether to exit running script after the error

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)
        >>> logger.pipe_stderr_to_stdout = True

        >>> logger.error("test")
        [ERROR] test
        """
        print(self._format_message("error", message), file=self._get_output_stream("error"))
        if exit_bool:
            sys.exit()

    def success(self, message: str) -> None:
        """
        Print a success message.

        Parameters
        ----------
        message : str

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)
        >>> logger.success("test")
        [SUCCESS] test
        """
        print(self._format_message("success", message), file=self._get_output_stream("success"))

    def debug(self, message: str) -> None:
        """
        Print a debug message.

        Parameters
        ----------
        message : str

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)
        >>> logger.debug("test")
        [DEBUG] test
        """
        print(self._format_message("debug", message), file=self._get_output_stream("debug"))

    def plain(self, message: str) -> None:
        """
        Print a plain message without any type prefix or color.

        Parameters
        ----------
        message : str

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)
        >>> logger.plain("test")
        test
        """
        print(message, file=self._get_output_stream("plain"))

    def set_use_colors(self, enable: bool) -> None:
        """
        Enable or disable ANSI colors in the output.

        Parameters
        ----------
        enable : bool
            If True, enable ANSI colors; otherwise, disable them.

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=True)
        >>> message = logger._format_message("info", "test")
        >>> print(message.find("[38;5"))
        1

        >>> logger.set_use_colors(False)
        >>> message = logger._format_message("info", "test")
        >>> print(message.find("[38;5"))
        -1

        >>> print(message)
        [INFO] test
        """
        self.use_colors = enable

    def _handle_text(self, text: str | tuple | list, max_line_len: int | None = None) -> str:
        """
        Handle a text to be printted, formatting accordingly.

        If the parameter `text` is a string, return it unchanged, if it is a list or tuple of
        strings, with more than one element, return the joining of the elements and if it is a
        list or tuple with one string element, return this string.

        Parameters
        ----------
        text : str | tuple | list
        max_line_len : int, Optional

        Returns
        -------
        str

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)
        >>> handled_text = logger._handle_text(["test_a", "test_b"])
        >>> print(handled_text)
        test_a test_b
        """
        if isinstance(text, (tuple, list)):
            text = " ".join(text) if len(text) > 1 else text[0]

        if max_line_len:

            if max_line_len < 1:
                self.error("max_len must be >= 1")

            from textwrap import fill

            text = fill(
                text,
                width=max_line_len,
                expand_tabs=True,
                replace_whitespace=False,
                drop_whitespace=True,
                break_long_words=False,
                break_on_hyphens=False,
            )

        return text

    def _handle_color(self, iter_color: tuple | list | str) -> str | tuple[str, str]:
        """
        Handle and sanitize a color parameter.

        Check a color given parameter, if it is either a list or tuple, with elements being strings
        between the allowed ones (color names from 'VARHANDLE').

        If the parameter is not in the correct ones cited above, the function fallbacks to retrurn
        the default text color without any background color to be used.

        If the given parameter tuple/list has two elements, it considers the first one as the color
        background color, and the second one as the color foreground.

        Parameters
        ----------
        iter_color : tuple | list

        Returns
        -------
        str
            The ansi escape color for the color, or the joinig of the multiple colors

        Examples
        --------
        >>> from .utils import check_ansi_complete_color_code
        >>> logger = ScriptLogger()
        >>> handle_test = logger._handle_color(["GRN", "YLW"])
        >>> arg = check_ansi_complete_color_code(handle_test)

        >>> print(arg.group(1))
        002

        >>> print(arg.group(2))
        003
        """
        if isinstance(iter_color, (tuple, list)):
            if len(iter_color) == 1:
                return VARHANDLE(iter_color[0])

            elif len(iter_color) == 2:
                converted_bg = VARHANDLE(iter_color[0]).replace("[38", "[48")
                return f"{converted_bg}{VARHANDLE(iter_color[1])}"

        elif isinstance(iter_color, str):
            if match(r"^\x1b\[\d{2,2}\;\d{1,1}\;\d{1,3}m$", iter_color):
                return iter_color
            else:
                return VARHANDLE(iter_color)

        return VARHANDLE("TXT")

    def format_text_cols(
        self,
        text: list | str | tuple,
        colors: list | str | tuple,
        return_ansi_colors: bool = False,
        dont_reduce_colors_len: bool = False,
    ) -> (list, list):
        """
        Format given text parameter and colors to print parameter.

        Parameters
        ----------
        text : list | str | tuple
        colors : list | str | tuple
        return_ansi_colors : bool, Default False

        Returns
        -------
        text : list
        colors : list
        """
        if isinstance(text, str):
            text = [text]
        elif text is None:
            text = [""]

        if isinstance(colors, str):
            colors = [colors]
        elif colors is None:
            colors = ["TXT"] * len(text)

        if len(colors) < len(text):
            colors.extend(["TXT"] * (len(text) - len(colors)))
        elif len(colors) > len(text) and not dont_reduce_colors_len:
            colors = colors[: len(text)]

        if return_ansi_colors:
            colors = list(map(self._handle_color, colors))

        return text, colors

    def extract_text(self, escaped_code: str) -> str:
        r"""
        Extract only text part from an ansi color escaped string.

        Parameters
        ----------
        escaped_code : str

        Returns
        -------
        str

        Examples
        --------
        >>> logger = ScriptLogger()
        >>> ansi_str = "\x1b[38;5;004mtest_b\x1b[0m"
        >>> print(logger.extract_text(ansi_str))
        test_b
        """
        # pattern = re.compile(r"\x1b[^m]*m")
        # text_only = re.sub(pattern, "", escaped_code)
        pattern = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
        text_only = pattern.sub("", escaped_code)
        return text_only

    def print_col(
        self,
        text: str,
        color: LoggerColors = None,
        left_prefix: str = "",
        right_prefix: str = "",
        max_len: int | None = None,
    ):
        """
        Print a given text, including the given colors.

        The color can be a color name string, matching any `VARHANDLE.ansi_dicts` keys color name;
        can be a iterable list or element, with values matching the same the previous keys one,
        being in case the tuple/list have just one color name, it will be the color foreground
        to te printed text, or in case it have two colors, the first one will match the background
        color and the secon one the foreground.

        If the list/tuple have more than 2 elements, or any other formatting problem, it will
        fallback tou originals foreground color to the text (white or black)

        Parameters
        ----------
        text : str
        color : list | tuple | str
            list or tuple, being each element of it being a color name, matching the names in the
            keys from  `VARHANDLE.ansi_dicts`.
            In correct formatting, in the case of 2 colors in it, one should be a foreground
            color and other a background color, otherwise, the secon color will override the
            first one.
            If a str, it should be only one color name, matching the `VARHANDLE.ansi_dicts` keys.
        right_prefix : str
        left_prefix : str
        max_len : int, Optional

        Examples
        --------
        >>> from .utils import check_ansi_color_code

        >>> logger = ScriptLogger(use_colors=False)
        >>> logger.print_col("test", ("yellow", "red"))
        test

        >>> logger.set_use_colors(True)
        >>> logger.set_use_alt_stdout(True, reset_clean=True)
        >>> logger.print_col("test_b", "BLUE")
        >>> logger.set_use_alt_stdout(False)
        >>> tst = logger.get_alt_stdout(1)
        >>> arg = check_ansi_color_code(tst[0])

        >>> print(arg[0])
        (38, 4)

        >>> print(logger.extract_text(tst[0]))
        test_b
        """
        try:
            message = (
                f"{self._handle_color(color)}{self._handle_text(text, max_len)}{VARHANDLE('RST')}"
                if self.use_colors
                else f"{self._handle_text(text)}"
            )
            message = f"{left_prefix}{message}{right_prefix}"

        except (ValueError, TypeError, OSError) as e:
            print(e, file=self._get_output_stream("error"))
            return

        print(message, file=self._get_output_stream("success"), flush=True)

    def print_line(
        self,
        size_el: str | int,
        color: LoggerColors = None,
        style: Literal["double", "single"] = "double",
    ):
        """
        Print a line, that may be the union of different chars, like "-", defined by the param.

        Parameters
        ----------
        size_el : str | int
            String element which length defines the line length, so the line should be the same size
            as this string, or integer of the line total length.
        color : str | list | tuple | None, default None
            Color element to this line
        style : | Literal["double", "single"], default "double"
            Which chars should this line be made of, "simple"/"single" would be "-", "double" would
            be "=".

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)
        >>> logger.print_line(size_el=15, color=["TXT"], style="double")
        ===============

        >>> logger.print_line(size_el="title_string", color=["TXT"], style="double")
        ============
        """
        styel = self.style_elements.get(style, self.style_elements["double"])

        total_len = (
            size_el
            if isinstance(size_el, int)
            else (len(size_el) if isinstance(size_el, str) else None)
        )
        self.print_col(styel * total_len, color=color)

    def print_section(
        self,
        text: str,
        color: LoggerColors,
        *args: LoggerArgs,
    ):
        """
        Print a section start/header, that may consist of the title, and and optional line.

        Parameters
        ----------
        text : str
            Text to print in the section title
        color : LoggerColors
        args : LoggerArgs
            extra possible parameters strings, can be:

                - "single" | "simple" | "double" (line style)

                - "print_next_line" (Toggle section line printing)

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)
        >>> logger.print_section("title", ["TXT"], "double", "print_next_line")
        title
        =====
        """
        self.print_col(text, color)
        if "print_next_line" in args:
            if isinstance(color, (tuple, list)) and len(color) >= 2:
                color = color[0]
            self.print_line(
                text,
                color,
                next((n for n in args if n in ["simple", "double"]), "simple"),
            )

    def socket(self, message: dict) -> None:
        """
        Print a socket returned message.

        Parameters
        ----------
        message : dict
        """
        cols = []
        text = []
        if "ok" in message:
            if message["ok"]:
                cols.append("GRN")
                text.append("OK")
            else:
                cols.append("LRED")
                text.append("NOT OK")

            cols.append("NONE")
            text.append("\n")

        if "request_id" in message:
            text += ["request id: ", message["request_id"], "\n"]
            cols += ["TXT", "LSTBLUE", "NONE"]

        if "queued" in message:
            text += ["queued: ", str(message["queued"]), "\n"]
            cols += ["ORANGE", "TXT", "NONE"]
        if len(text) > 0:
            self.print_same_line(text, cols)
        else:
            LOGGER.print_same_line(["No Output"], ["LRED"])

    def _wrap_color(
        self,
        texts: list | str | tuple,
        colors: list | str | tuple,
        separator: str | None = "",
    ) -> str:
        r"""
        Wrap given colors list with given texts list, adding the ansi color in init + reset at end.

        Parameters
        ----------
        texts : list
        colors : list
        separator : str, Optiona

        Returns
        -------
        str

        Examples
        --------
        >>> logger = ScriptLogger()
        >>> tst = logger._wrap_color(["test_a", "test_b"], [VARHANDLE("TXT"), VARHANDLE("BLUE")])
        >>> tst
        '\x1b[38;5;007mtest_a\x1b[0m\x1b[38;5;004mtest_b\x1b[0m'
        """
        from .utils import check_ansi_color_code

        if (
            not isinstance(texts, list)
            or not isinstance(colors, list)
            or len(texts) != len(colors)
            or any(len(check_ansi_color_code(i)) == 0 for i in colors)
        ):
            texts, colors = self.format_text_cols(texts, colors, return_ansi_colors=True)

        result_str = ""
        try:
            for i, n in enumerate(texts):
                result_str += (
                    f"{colors[i]}{n}{VARHANDLE('RST') if colors[i] else ''}{separator}"
                    if self.use_colors
                    else f"{n}"
                )
        except (AssertionError, TypeError, ValueError) as e:
            self.error(f"Error printing with logger to the same line: {e}")

        return result_str

    def print_same_line(
        self,
        text: str | tuple[str] | list[str],
        color: list[LoggerColors] | tuple[LoggerColors] | str | None = None,
        separator: str = "",
        left_prefix: str = "",
        right_prefix: str = "",
        return_print_str: bool = False,
    ) -> str | None:
        """
        Print multiple given strings, in the same line.

        Parameters
        ----------
        text : str | tuple[str] | list[str]
            Text to be printed
        color : list[LoggerColors] | tuple[LoggerColors] | str, default None
        separator : str, default None
            String to be added between every text element on the line, default ""
        left_prefix : str
        right_prefix : str

        Examples
        --------
        >>> from .utils import check_ansi_color_code

        >>> logger = ScriptLogger(use_colors=False)
        >>> logger.print_same_line(["test simple text"], ["TXT"])
        test simple text

        >>> logger.print_same_line(["test ", "simple ", "text"], ["TXT", "TXT", "TXT"])
        test simple text

        >>> logger.set_use_colors(True)
        >>> logger.set_use_alt_stdout(True, reset_clean=True)
        >>> logger.print_same_line(["test simple text"], ["BLUE"])
        >>> tst = logger.get_alt_stdout(1)
        >>> logger.set_use_alt_stdout(False, reset_clean=True)

        >>> print(logger.extract_text(tst[0]))
        test simple text
        >>> colors = check_ansi_color_code(tst[0])
        >>> print(colors)
        [(38, 4)]
        """
        text, colors = self.format_text_cols(text, color, return_ansi_colors=True)

        result_str = self._wrap_color(text, colors, separator)

        result_str = f"{left_prefix}{result_str}{right_prefix}"

        if return_print_str:
            return result_str

        print(
            result_str,
            file=self._get_output_stream("success"),
            flush=True,
        )

    def handle_input(
        self,
        text: tuple | list | str,
        colors: tuple | list | str,
        separator: str = "",
        left_prefix: str = "",
        right_prefix: str = "",
        jump_line_after: bool = False,
    ) -> str:
        """
        Handle user input prompts instances.

        Parameters
        ----------
        text : tuple | list | str
            Text to prompt for user in the input
        colors : tuple | list | str
            Colors to print the input text

        Returns
        -------
        input_cmd : str

        Examples
        --------
        >>> from unittest.mock import patch
        >>> logger = ScriptLogger(use_colors=False)

        >>> with patch("builtins.input", return_value="input test"):
        ...     test = logger.handle_input("input: ", "TXT")

        >>> print(test)
        input test
        """
        if isinstance(text, str):
            text = [text]
        if isinstance(colors, str):
            colors = [colors]

        if colors is None:
            colors = ["text"] * len(text)
        if len(colors) < len(text):
            colors.extend(["text"] * (len(text) - len(colors)))
        if len(colors) > len(text):
            colors = colors[: len(text)]

        color_list = list(map(self._handle_color, colors))
        result_str = ""

        try:
            assert len(color_list) == len(text)
            for i, n in enumerate(text):
                result_str += (
                    f"{color_list[i]}{n}{VARHANDLE('RST')}{separator}"
                    if self.use_colors
                    else f"{n}"
                )
        except (AssertionError, TypeError, ValueError) as e:
            message = f"Error printing logger handle input text message. {e}"
            self.error(message, True)

        input_cmd = input(f"{left_prefix}{result_str}{right_prefix}")

        if jump_line_after:
            print(file=self._get_output_stream("input"))

        return input_cmd

    def color_first_letter(
        self,
        text: list | str | tuple,
        colors: list | str | tuple,
        separator: str = "",
        tab_max_limit: int | None = None,
    ):
        """
        Print given strings, with only the first letter of each one colored.

        Parameters
        ----------
        text : list or str or tuple
        colors : list or str or tuple
        separator : str (Optional)
        tab_max_limit : int (Optional)

        Examples
        --------
        >>> from .utils import check_ansi_color_code

        >>> logger = ScriptLogger(use_colors=False)
        >>> logger.color_first_letter("test", "TXT")
        test

        >>> logger.set_use_colors(True)
        >>> logger.set_use_alt_stdout(True, reset_clean=True)
        >>> logger.color_first_letter("test", "PRP")
        >>> col_test = logger.get_alt_stdout(1)
        >>> logger.set_use_alt_stdout(False, reset_clean=True)
        >>> arg = check_ansi_color_code(col_test[0])
        >>> print(arg)
        [(38, 56)]

        >>> arg_text = logger.extract_text(col_test[0])
        >>> print(arg_text)
        test

        >>> arg_text_list = col_test[0].split("[0m")
        >>> new_arg = logger.extract_text(arg_text_list[0] + "[0m")
        >>> print(new_arg)
        t
        """
        text, colors = self.format_text_cols(text, colors, return_ansi_colors=True)
        result_str = ""

        try:
            for i, n in enumerate(text):
                separator = (
                    " " * (tab_max_limit - len(n))
                    if tab_max_limit is not None and not separator
                    else separator
                )
                result_str += (
                    f"{colors[i]}{n[0]}{VARHANDLE('RST')}{n[1:]}{separator}"
                    if self.use_colors
                    else f"{n}{separator}"
                )
        except (AssertionError, TypeError, ValueError) as e:
            err_str = f"Error printing with logger to the same line: {e}"
            print(err_str, file=self._get_output_stream("error"))

        print(result_str, file=self._get_output_stream("success"))

    def print_md(
        self,
        message: str,
        right_prefix: str | None = "",
        left_prefix: str | None = "",
        fzf_preview: bool | None = False,
        console_width: int | None = None,
    ):
        """
        Print markdown formatted of the given message to terminal.

        Parameters
        ----------
        message : str
        right_prefix : str (Optional)
        left_prefix : str (Optional)

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)
        >>> logger.print_md("# Title", console_width=50)
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃                     Title                      ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
        """
        from rich.console import Console
        from rich.markdown import Markdown

        if not hasattr(self, "console"):
            self.console = Console(
                theme=VARHANDLE.theme("markdown"),
                force_terminal=True,
                color_system="truecolor",
            )

        if console_width:
            self.console.width = console_width

        if not self.use_colors:
            self.console.push_theme(VARHANDLE.theme("markdown_no_color"))

        width = 70 if fzf_preview else None
        height = 40 if fzf_preview else None

        md_msg = Markdown(f"{left_prefix}{message}{right_prefix}", code_theme="dracula")
        self.console.print(md_msg, width=width, height=height, sep="")

    def handle_console_key(
        self,
        text: list | str | tuple,
        colors: list | str | tuple,
        console: Terminal(),
        separator: str = "",
        left_prefix: str = "",
        right_prefix: str = "",
        allowed_keys: list | None = None,
    ) -> str:
        """
        Handle a single key input using  blessed `Terminal()` class.

        Parameters
        ----------
        text: list | str | tuple
        colors : list | str | tuple
        console : blessed.terminal.Terminal
        separator : str (Optional)
        left_prefix : str (Optional)
        right_prefix : str (Optional)

        Returns
        -------
        inp_key : str
            User terminal inputed key
        """
        if isinstance(text, str):
            text = [text]

        if isinstance(colors, str):
            colors = [colors]

        if colors is None:
            colors = ["text"] * len(text)

        if len(colors) < len(text):
            colors.extend(["text"] * (len(text) - len(colors)))

        if len(colors) > len(text):
            colors = colors[: len(text)]

        color_list = list(map(self._handle_color, colors))
        result_str = ""

        try:
            assert len(color_list) == len(text)
            for i, n in enumerate(text):
                result_str += (
                    f"{color_list[i]}{n}{VARHANDLE('RST')}{separator}"
                    if self.use_colors
                    else f"{n}"
                )
        except (AssertionError, TypeError, ValueError) as e:
            message = f"Error printing logger handle input text message. {e}"
            self.error(message, True)

        print(f"{left_prefix}{result_str}{right_prefix}", file=self._get_output_stream("input"))

        allowed_input = False
        first_exec = True
        while not allowed_input:
            if not first_exec:
                print(f"Invalid Key!, should be one of the following: {' '.join(allowed_keys)}")
            inp_key = console.inkey(esc_delay=0.15)
            allowed_input = bool(inp_key in allowed_keys or allowed_keys is None)
            first_exec = False

        return inp_key

    # -FIX: Currently this function only checks timeout every time user inputs a key, if the user
    #  Dont send any key, it dont timeout

    def terminal_handle_input(
        self,
        text: list | str | tuple,
        colors: list | None = None,
        shortcuts_dict: dict | None = None,
        new_line_start: bool | None = False,
        new_line_end: bool | None = True,
        timeout: float | None = 200,
    ) -> str:
        """
        Handle terminal keyboard input, including keys combination shortcuts to run commands.

        Parameters
        ----------
        text : list | str | tuple
        colors : list, optional
        shortcuts_dict : dict
            Dictionary, with keys being the keyboard shortcut key, and the value the command
        new_line_start : bool, default False
        new_line_end : bool, default True
        timeout : float, default 200

        Returns
        -------
        str
        """
        from datetime import datetime

        import readchar

        local_tz = datetime.now().astimezone().tzinfo
        self.timer_input = datetime.now(tz=local_tz)
        self.input_string = ""
        args = None
        if colors is None:
            colors = ["TXT"]

        LOGGER.print_same_line(text, colors, left_prefix="\n" if new_line_start else "")

        key = readchar.readkey()
        conv_dict = {}

        if shortcuts_dict:
            for k, v in shortcuts_dict.items():
                if isinstance(v, str):
                    vfn = globals()[v]
                elif isinstance(v, list):
                    vfn = globals()[v[0]] if isinstance(v[0], str) else v[0]
                    args = v[1]
                else:
                    vfn = v

                conv_dict[getattr(readchar.key, k)] = vfn

        while key != readchar.key.ENTER:
            if self.timer_input:
                timer_exec = datetime.now(tz=local_tz).second - self.timer_input.second

                if timer_exec > timeout:
                    print(flush=True)
                    self.error(f"Logger input handler quited by timeout {timeout}secs", True)
                    break

            if key in conv_dict:
                result = conv_dict[key](args) if args else conv_dict[key]()
                if isinstance(result, str):
                    self.input_string += result
                    print(result, end="", flush=True)
                    break
            elif key == readchar.key.BACKSPACE:
                self.input_string = self.input_string[:-1]
                print("\b \b", end="", flush=True)
            else:
                self.input_string += key
                print(key, end="", flush=True)

            key = readchar.readkey()

        if new_line_end:
            print("\n", flush=True)

        return self.input_string

    def send_kitty_key(self, key: str):
        """
        Send the parameter key input to kitty terminal.

        Parameters
        ----------
        key : str
        """
        system(f"kitty @ send-key --match state:self '{key}'")

    def clear_terminal(self):
        """Clear current terminal content."""
        system("kitten @ action --match state:focused clear_terminal active")

    def scrollback(self):
        """Toggle neovim kitty terminal scrollback pager."""
        system("kitten @ action --match state:focused scroll_home")
        system("kitten @ action --match state:focused show_scrollback")

    def print_word_in_middle(
        self,
        text: list | str | tuple,
        colors: list | str | tuple,
        arr_el: str = "double",
    ) -> None:
        """
        Print given text in the middle of the terminal, wit possible line element before and after.

        Parameters
        ----------
        text : list | str | tuple
        colors : list | str | tuple
        arr_el : str, Default "double"
            can be "simple", "double" or "blank"
        """
        from shutil import get_terminal_size

        rst = []
        styel = self.get_line_el(arr_el)

        text, colors = self.format_text_cols(text, colors, dont_reduce_colors_len=True)
        terminal_width = get_terminal_size().columns

        if len(colors) == 1:
            colors = ["TXT", colors[0], "TXT"]
        elif len(colors) == 2:
            colors.append(colors[0])

        for word in text:
            dash_count = terminal_width - len(word) - 3
            if dash_count <= 0:
                return word[:terminal_width]

            left_dashes = dash_count // 2
            right_dashes = dash_count - left_dashes
            rst += [styel * left_dashes, word, styel * right_dashes]

        self.print_same_line(rst, colors, separator=" ")

    def _ansi_strip(self, s: str) -> str:
        """
        Strip ansi codes from given string.

        Parameters
        ----------
        s : str

        Returns
        -------
        str

        Notes
        -----
        depends on class attribute `_ansi_re`

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)
        >>> tst = logger._ansi_strip(f"{VARHANDLE('GOLD')}test{VARHANDLE('RST')}")
        >>> print(tst)
        test
        """
        return self._ansi_re.sub("", s)

    def _vislen(self, s: str) -> int:
        """
        Get visual length of given string.

        Parameters
        ----------
        s : str

        Returns
        -------
        int

        Examples
        --------
        >>> logger = ScriptLogger(use_colors=False)
        >>> tst = logger._vislen(f"{VARHANDLE('GOLD')}test{VARHANDLE('RST')}")
        >>> print(tst)
        4
        """
        return len(self._ansi_strip(s))

    def test_print(self, msg: Any) -> None:
        """
        Print a given message and its type in a compact, doctest-friendly format.

        One line below summary.

        Prints with `[Type] <name>` (e.g., `[Type] str`) rather than the verbose
        `<class 'str'>`. For containers, also reports contained element types.

        Parameters
        ----------
        msg : Any
            Value to print.

        Examples
        --------
        >>> LOGGER.test_print("teste")
        [Type] str
        teste
        >>> LOGGER.test_print(2)
        [Type] int
        2
        >>> LOGGER.test_print(float(2))
        [Type] float
        2.0
        >>> LOGGER.test_print([1, "a", 2.0])
        [Type] list
        [Type elements] int str float
        1, a, 2.0
        >>> LOGGER.test_print({"k": 1, 2: "v"})
        [Type] dict
        [Type keys] str int
        [Type values] int str
        k: 1
        2: v
        """

        def _typename(obj: Any) -> str:
            """Return the bare type name (e.g., 'str', 'int', 'list')."""
            return type(obj).__name__

        def _unique_in_order(it: Iterable[str]) -> list[str]:
            """Deduplicate while preserving first-seen order."""
            seen: set[str] = set()
            out: list[str] = []
            for s in it:
                if s not in seen:
                    seen.add(s)
                    out.append(s)
            return out

        out = self._get_output_stream("test")

        # None keeps your existing special string
        if msg is None:
            print("[Type] None", file=out)
            return

        # Dictionaries: report key/value type sets (order-preserving), then pretty print
        if isinstance(msg, dict):
            key_types = _unique_in_order(_typename(k) for k in msg)
            val_types = _unique_in_order(_typename(v) for v in msg.values())
            print("[Type] dict", file=out)
            if key_types:
                print(f"[Type keys] {' '.join(key_types)}", file=out)
            if val_types:
                print(f"[Type values] {' '.join(val_types)}", file=out)
            for k, v in msg.items():
                print(f"{k}: {v}", file=out)
            return

        # Lists/tuples/sets: report container type and contained element types
        if isinstance(msg, (list, tuple, set)):
            elem_types = _unique_in_order(_typename(x) for x in msg)
            print(f"[Type] {_typename(msg)}", file=out)
            if elem_types:
                print(f"[Type elements] {' '.join(elem_types)}", file=out)
            # human-readable elements line
            if isinstance(msg, set):
                # sets are unordered; show a stable order by str()
                elems = ", ".join(str(x) for x in sorted(msg, key=str))
            elif isinstance(msg, tuple):
                elems = ", ".join(str(x) for x in msg)
                # Keep Python's single-item tuple shape visually, if you like:
                if len(msg) == 1:
                    elems = f"{elems},"
                elems = f"({elems})"
                print(elems, file=out)
                return
            else:  # list
                elems = ", ".join(str(x) for x in msg)
            print(elems, file=out)
            return

        # Scalars (int/float/str/bool/etc.)
        print(f"[Type] {_typename(msg)}", file=out)
        print(str(msg), file=out)

    def dq(self, obj: Any) -> str:
        """
        Render an object with double-quoted strings, preserving Python-like shapes.

        One line below summary.

        - Strings are encoded via JSON (guaranteed double quotes and proper escaping).
        - Tuples print as `(a, b)` with the single-item trailing comma `(a,)`.
        - Lists `[...]`, dicts `{k: v}` (keys get quoted if they are strings), sets `{a, b}`.
        - Dataclasses render via `asdict()` first.
        - Everything else falls back to `repr()`.

        Parameters
        ----------
        obj : Any
            Object to render.

        Returns
        -------
        str
            Double-quote-normalized string representation.
        """
        if isinstance(obj, str):
            return jdumps(obj, ensure_ascii=False)

        if is_dataclass(obj):
            return self.dq(asdict(obj))

        if isinstance(obj, tuple):
            inner = ", ".join(self.dq(x) for x in obj)
            if len(obj) == 1:
                inner += ","
            return f"({inner})"

        if isinstance(obj, list):
            return "[" + ", ".join(self.dq(x) for x in obj) + "]"

        if isinstance(obj, dict):
            # Keep insertion order; quote string keys; do not sort.
            items = (f"{self.dq(k)}: {self.dq(v)}" for k, v in obj.items())
            return "{" + ", ".join(items) + "}"

        if isinstance(obj, set):
            # Sets are unordered; produce a stable order by their rendered form.
            parts = sorted(self.dq(x) for x in obj)
            return "{" + ", ".join(parts) + "}"

        return repr(obj)

    def printest(self, obj: Any) -> None:
        """
        Print an object for doctest output with double-quoted strings.

        One line below summary.

        This helper is intended for docstring examples where you want printed values to use double
        quotes for strings (e.g. `"text"` rather than `'text'`) while keeping familiar Python shapes
        for tuples, lists, dicts, and sets.

        Parameters
        ----------
        obj : Any
            Object to print.

        Examples
        --------
        >>> LOGGER.printest(("a", "b"))
        ("a", "b")
        >>> LOGGER.printest(("solo",))
        ("solo",)
        >>> LOGGER.printest({"k": "v"})
        {"k": "v"}
        >>> LOGGER.printest(["x", 1])
        ["x", 1]
        """
        print(self.dq(obj), flush=True)

    def atest_print(self, obj: any):
        """
        Print given variable on pytest example section.

        Parameters
        ----------
        obj : any
        """
        if isinstance(obj, tuple):
            rst_str = f"({obj[0]}"
            if len(obj) == 1:
                rst_str += ")"
            elif len(obj) == 2:
                rst_str += f", {obj[1]})"
            elif len(obj) >= 3:
                for n in obj[1 : (len(obj) - 1)]:
                    rst_str += f"{n}, "
                rst_str += f"{obj[-1]})"
            else:
                rst_str = str(obj)

        print(
            f"{rst_str}",
            flush=True,
        )

    def _align_text(self, s: str, width: int, how: str) -> str:
        """
        Align given text based on width and padding direction.

        Parameters
        ----------
        s : str
        width : int
        how : str

        Returns
        -------
        str

        Examples
        --------
        >>> logger = ScriptLogger()
        >>> tst = logger._align_text("test_word", 20, "right")
        >>> print(tst)
                   test_word
        """
        raw = self._ansi_strip(s)
        pad = width - len(raw)
        if pad <= 0:
            return s
        if how == "right":
            return " " * pad + s
        if how == "center":
            left = pad // 2
            right = pad - left
            return " " * left + s + " " * right
        return s + " " * pad  # left

    def print_color_dataframe(
        self,
        df: DataFrame,
        *,
        show_index: bool = True,
        index_name: str | None = None,
        # Colors
        column_header_colors: dict[str, str] | None = None,
        index_color: str | None = "PNK",
        line_color: str | None = "TEAL",
        value_colors: dict[str, str] | None = None,
        default_value_color: str | None = "BLD",
        header_color_default: str | None = "YLW",
        # Layout & formatting
        float_format: str = "{:.2f}",
        max_col_width: int | None = None,
        align: dict[str, str] | None = None,  # "left" | "right" | "center"
        # Row separators
        row_separators: bool = True,
        # Percentage coloring (legacy single-column)
        percent_column: str | None = None,
        percent_thresholds: tuple[float, float] = (50.0, 85.0),
        percent_colors: tuple[str, str, str] = ("RED", "YLW", "GRN"),
        percent_decimals: int = 1,
        convert_percent: bool = True,
        # NEW: Multiple percent columns
        # - Iterable[str]: all use defaults above
        # - Dict[str, Dict]: per-column overrides: {
        #     "col": {"thresholds": (50,85), "colors": ("RED","YLW","GRN"),
        #             "decimals": 1, "convert_percent": True}
        #   }
        percent_columns: Iterable[str] | dict[str, dict[str, object]] | None = None,
        # Return instead of printing
        return_str: bool = False,
        use_all_percent_columns: bool = False,
    ) -> str | None:
        """
        Print a DataFrame with ANSI colors and optional percentage-based coloring.

        Notes
        -----
        - Borders and row separators use the same `line_color`.
        - Set `row_separators=False` to disable lines between rows.

        - Different header colors are set through `column_header_colors`, like:

        .. code-block:: python3

            text, colors = self.format_text_cols(text, color, return_ansi_colors=True)

        - The same logic from previous item is used for different value colors with `value_colors`

        Examples
        --------
        >>> import pandas as pd
        >>> logger = ScriptLogger()
        >>> dfa = pd.DataFrame()
        >>> logger.set_use_colors(False)
        >>> logger.print_color_dataframe(dfa)
        (empty DataFrame)

        >>> df = pd.DataFrame(
        ...     {
        ...         "Name": ["Alpha", "Beta", "Gamma"],
        ...         "Count": [3, 42, 7],
        ...         "Percentage": ["42.3", 85.0, "91%"],
        ...     },
        ...     index=["row1", "row2", "row3"],
        ... )
        >>> logger.print_color_dataframe(df, percent_column="Percentage")
        ╒══════╕═══════╕═══════╕════════════╕
        │      │ Name  │ Count │ Percentage │
        ├──────┤───────┤───────┤────────────┤
        │ row1 │ Alpha │     3 │ 42.3%      │
        ├──────┤───────┤───────┤────────────┤
        │ row2 │ Beta  │    42 │ 85.0%      │
        ├──────┤───────┤───────┤────────────┤
        │ row3 │ Gamma │     7 │ 91.0%      │
        ╘══════╛═══════╛═══════╛════════════╛
        """
        import pandas as pd

        def _fmt_cell(_col: str, v: object) -> str:
            if pd.isna(v):
                return ""
            if isinstance(v, float):
                return float_format.format(v)
            return str(v)

        def _col_align(colname: str, is_index_col: bool) -> str:
            if is_index_col:
                return "left"
            if colname in align:
                return align[colname]
            if colname in df.columns:
                kind = getattr(df[colname].dtype, "kind", "")
                return "right" if kind in num_kinds else "left"
            return "left"

        def _maybe_truncate(s: str) -> str:
            if max_col_width is None:
                return s
            vis = self._vislen(s)
            if vis <= max_col_width:
                return s
            keep = max(0, max_col_width - 1)
            raw = self._ansi_strip(s)
            return raw[:keep] + "…"

        def _line_piece(ch: str) -> str:
            chn, linen_color = self.format_text_cols(ch, line_color)
            return self._wrap_color(chn, linen_color)

        def _hbarl(col_widths: list) -> str:
            parts = [_line_piece("╘")]
            for w in col_widths:
                parts.extend((_line_piece("═" * (w + 2)), _line_piece("╛")))
            return "".join(parts)

        def _hbarf(col_widths: list) -> str:
            parts = [_line_piece("╒")]
            for w in col_widths:
                parts.extend((_line_piece("═" * (w + 2)), _line_piece("╕")))
            return "".join(parts)

        def _hbar(col_widths: list) -> str:
            parts = [_line_piece("├")]
            for w in col_widths:
                parts.extend((_line_piece("─" * (w + 2)), _line_piece("┤")))
            return "".join(parts)

        # --- empty df -------------------------------------------------------------
        if df.empty:
            text, colors = self.format_text_cols(
                "(empty DataFrame)",
                default_value_color,
                return_ansi_colors=True,
            )
            out = self._wrap_color(text, colors)
            if return_str:
                return out
            print(out, file=self._get_output_stream("warning"), flush=True)
            return None

        # --- setup ----------------------------------------------------------------
        cols: list[str] = list(df.columns)
        headers: list[str] = cols.copy()
        rows_plain: list[list[str]] = []
        out_lines: list[str] = []

        idx_hdr = index_name if index_name is not None else (df.index.name or "")

        align = align or {}
        num_kinds = {"i", "u", "f", "c"}

        if show_index:
            headers = ["(index)" if idx_hdr else str(idx_hdr), *headers]

        # --- build percent specs for one or many columns --------------------------
        # percent_specs: col -> dict(series, thresholds, colors, decimals, convert_percent)
        percent_specs: dict[str, dict[str, object]] = {}

        def _add_percent_spec(col: str, override: dict[str, object] | None = None) -> None:
            if col not in df.columns:
                return
            ov = override or {}
            th = tuple(ov.get("thresholds", percent_thresholds))  # (low, high)
            cs = tuple(ov.get("colors", percent_colors))  # (red, yel, grn)
            dec = int(ov.get("decimals", percent_decimals))
            conv = bool(ov.get("convert_percent", convert_percent))
            series = pd.to_numeric(
                df[col].astype(str).str.strip().str.replace("%", "", regex=False),
                errors="coerce",
            )
            percent_specs[col] = {
                "series": series,
                "thresholds": th,
                "colors": cs,
                "decimals": dec,
                "convert_percent": conv,
            }

        # New multi-column path
        if percent_columns or use_all_percent_columns:
            if isinstance(percent_columns, dict):
                for c, cfg in percent_columns.items():
                    _add_percent_spec(c, cfg or {})
            else:
                if use_all_percent_columns:
                    percent_columns = df.columns.to_numpy()
                for c in percent_columns:
                    _add_percent_spec(c, None)

        # Legacy single-column path (kept for compatibility)
        if percent_column and percent_column not in percent_specs:
            _add_percent_spec(percent_column, None)

        # --- rows (build display text) -------------------------------------------
        for r in range(len(df)):
            row_vals: list[str] = []
            if show_index:
                row_vals.append(str(df.index[r]))
            for col in cols:
                spec = percent_specs.get(col)
                if spec is not None:
                    val = spec["series"].iloc[r]  # type: ignore[index]
                    if pd.notna(val):
                        dec = spec["decimals"]  # type: ignore[assignment]
                        show_pct = spec["convert_percent"]  # type: ignore[assignment]
                        pct_symbol = "%" if show_pct else ""
                        row_vals.append(f"{float(val):.{int(dec)}f}{pct_symbol}")
                    else:
                        row_vals.append(_fmt_cell(col, df.iloc[r][col]))
                else:
                    row_vals.append(_fmt_cell(col, df.iloc[r][col]))
            rows_plain.append(row_vals)

        headers = [_maybe_truncate(h) for h in headers]
        data_plain = [[_maybe_truncate(c) for c in row] for row in rows_plain]

        col_widths = [
            max(self._vislen(headers[i]), *(self._vislen(row[i]) for row in data_plain))
            for i in range(len(headers))
        ]

        vsep = _line_piece("│")
        hbar = _hbar(col_widths)
        out_lines = [hbar]
        out_lines.pop(0)
        out_lines.insert(0, _hbarf(col_widths))
        # out_lines.pop(-1)
        # out_lines.insert(-1, _hbarl(col_widths))

        # --- header row -----------------------------------------------------------
        header_cells: list[str] = []
        for i, text in enumerate(headers):
            is_index_col = show_index and i == 0
            colname = None if is_index_col else (cols[i - 1] if show_index else cols[i])
            color = (
                index_color
                if is_index_col
                else (column_header_colors or {}).get(colname, header_color_default)
            )
            align_how = "left" if is_index_col else "center"
            padded = self._align_text(text, col_widths[i], align_how)
            header_cells.append(f" {self._wrap_color(padded, color)} ")
        out_lines.append(vsep + vsep.join(header_cells) + vsep)
        out_lines.append(hbar)

        # --- body rows + optional separators -------------------------------------
        last_row_idx = len(data_plain) - 1
        for r, row in enumerate(data_plain):
            cells: list[str] = []
            for i, cell in enumerate(row):
                is_index_col = show_index and i == 0
                colname = (
                    cols[i - 1] if (show_index and i > 0) else (cols[i] if not show_index else "")
                )
                padded = self._align_text(cell, col_widths[i], _col_align(colname, is_index_col))

                if show_index and i == 0:
                    color = index_color
                else:
                    colname_v = cols[i - 1] if show_index else cols[i]
                    spec = percent_specs.get(colname_v)
                    if spec is not None:
                        low, high = spec["thresholds"]  # type: ignore[assignment]
                        red, yel, grn = spec["colors"]  # type: ignore[assignment]
                        val = spec["series"].iloc[r]  # type: ignore[index]
                        if pd.isna(val):
                            color = default_value_color
                        elif float(val) < float(low):
                            color = red
                        elif float(low) <= float(val) <= float(high):
                            color = yel
                        else:
                            color = grn
                    else:
                        color = (value_colors or {}).get(colname_v, default_value_color)

                cells.append(" " + self._wrap_color(padded, color) + " ")

            out_lines.append(vsep + vsep.join(cells) + vsep)
            if row_separators and r != last_row_idx:
                out_lines.append(hbar)

        out_lines.append(_hbarl(col_widths))

        # out_lines.append(hbar)

        rendered = "\n".join(out_lines)
        if return_str:
            return rendered

        print(rendered, file=self._get_output_stream("success"), flush=True)
        return None


LOGGER = ScriptLogger()
