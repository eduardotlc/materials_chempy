#!/usr/bin/env python3
"""
Created on 2026-06-28 14:05:05.

@author: eduardotc
@contributors: lu4vic
@email: eduardotcampos@hotmail.com

Matplotlib, pandas, numpy and other maths/plots utils.

Notes
-----
Matplotlib configs types and valid values:

  Font Sizes:

    - Validated by `matplotlib.rcsetup.validate_fontsize(s)`

    - Choices: xx-small, x-small, small, medium, large, x-large, xx-large, smaller, larger
"""
#TODO: Check usage and defs of default paths, like ~/.fonts

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any
from materials_chempy.utils import assert_pathlib

if TYPE_CHECKING:
    from argparse import ArgumentGroup, ArgumentParser, Namespace

    from matplotlib.axes._axes import Axes
    from matplotlib.figure import Figure
    from pandas import Series


@dataclass
class BenchLayout:  # noqa: D101
    box_width: float = 2.0
    gap_size: float = 2.0

    def bench_width(self, num_inputs: int) -> float:  # noqa: D102
        return self.box_width * num_inputs + self.gap_size

    def col_center(self, col_idx1: int, num_inputs: int) -> float:  # noqa: D102
        return col_idx1 * self.bench_width(num_inputs) + (num_inputs - 1) * self.box_width / 2.0

    def file_offset(self, input_idx0: int) -> float:  # noqa: D102
        return input_idx0 * self.box_width

    def separator_at(self, col_idx1: int, num_inputs: int) -> float:  # noqa: D102
        return col_idx1 * self.bench_width(num_inputs) - self.box_width / 2.0 - self.gap_size / 2.0


class Plot:
    """
    Plot matplotlib utils handling class.

    Plot parameters that user desire to use other then setted default, should be passed on class
    initing or should be assigned to class attribute (`Plot.addtribute` = value).

    Colors attributes/parameters should be `str` type, and be either a matplotlib color name or
    a html hex color code.

    Attributes
    ----------
    box_color : str, Default "mediumaquamarine"
    median_color : str, Default "darksalmon"
    ytick_color : str, Default "#f1f1f1"
    xtick_color : str, Default "#e7e7e7"
    grid_color : str, Default "#c1c1c1"
    edge_color : str, Default "#e7e7e7"
    label_color : str, Default "#f1f1f1"
    face_color : str, Default "#eeeeee"
    box_alpha : float, Default 0.9
    font_size : float, Default 14
    ytick_label_size : str, Default "medium"
    xtick_label_size : str, Default "medium"
    figsize : tuple, Default (12, 7.5)
    dpi : int, Default 100
    ylabel : str, Default "Data"
    xlabel : str, Default "Values"
    xlabel_color : str, Default "white"
    ylabel_color : str, Default "white"
    title_color : str, Default "white"
    title : str, Default "Title"
    font_name : str, Default "helvetica"
    save_format : str, Default "png"
    save_file : str, Optional
    backend : str, Default "kitcat"
    mpl_style : str, Default "dark_background"
    fonts_path : str, Default "~/.fonts"

    _ax : matplotlib.axes._axes.Axes
    _fig : matplotlib.figure.Figure
    _plt : matplotlib.pyplot
    _fm : matplotlib.font_manager
    """

    _ax: Axes = field(default=None, init=False, repr=False)
    _fig: Figure = field(default=None, init=False, repr=False)
    _plt: Any = field(default=None, init=False, repr=False)
    _fm: Any = field(default=None, init=False, repr=False)

    def __init__(
        self,
        box_color: str = "mediumaquamarine",
        median_color: str = "darksalmon",
        ytick_color: str = "#f1f1f1",
        xtick_color: str = "#e7e7e7",
        grid_color: str = "#c1c1c1",
        edge_color: str = "#e7e7e7",
        label_color: str = "#f1f1f1",
        face_color: str = "#eeeeee",
        box_alpha: float = 0.9,
        font_size: float = 14,
        xtick_label_size: str = "medium",
        ytick_label_size: str = "medium",
        figsize: tuple = (12, 7.5),
        dpi: int = 100,
        ylabel: str = "Data",
        xlabel: str = "Values",
        xlabel_color: str = "white",
        ylabel_color: str = "white",
        title_color: str = "white",
        title: str = "Title",
        font_name: str = "helvetica",
        save_format: str = "png",
        save_file: str | None = None,
        backend: str = "kitcat",
        mpl_style: str = "dark_background",
        fonts_path: str = "~/.fonts",
    ):
        """
        Init boxplot class, setting given colors parameters or using defaults if not given.

        Parameters
        ----------
        box_color : str
        median_color : str
        ytick_color : str
        xtick_color : str
        grid_color : str
        edge_color : str
        label_color : str
        face_color : str
        box_alpha : float
        figsize : tuple
        ytick_label_size : str
        xtick_label_size : str
        dpi : int
        ylabel : str
        xlabel : str
        xlabel_color : str, Default "white"
        ylabel_color : str, Default "white"
        title_color : str, Default "white"
        title : str
        save_format : str
        save_file : str
        backend : str, Default "kitcat"
        mpl_style : str, Default "dark_background"
        fonts_path : str, Default "~/.fonts"
        """
        from matplotlib import (
            font_manager as fm,
        )
        from matplotlib import (
            pyplot as plt,
        )
        from matplotlib import (
            style as mplstyle,
        )
        from matplotlib import (
            use as mpluse,
        )

        self._plt = plt
        self._fm = fm

        self.box_color = box_color
        self.median_color = median_color
        self.box_alpha = box_alpha
        self.xtick_color = xtick_color
        self.ytick_color = ytick_color
        self.grid_color = grid_color
        self.label_color = label_color
        self.edge_color = edge_color
        self.face_color = face_color
        self.figsize = figsize
        self.dpi = dpi
        self.font_size = font_size
        self.xtick_label_size = xtick_label_size
        self.ytick_label_size = ytick_label_size
        self.ylabel = ylabel
        self.xlabel = xlabel
        self.title = title
        self.xlabel_color = xlabel_color
        self.ylabel_color = ylabel_color
        self.title_color = title_color
        self.layout = BenchLayout()
        self.font_name = font_name
        self.save_format = save_format
        self.save_file = save_file
        self.backend = backend
        self.mpl_style = mpl_style
        self.fonts_path = fonts_path

        mplstyle.use(self.mpl_style)
        mpluse(self.backend)

        self._plt.rcParams.update({
            "figure.dpi": self.dpi,
            "figure.figsize": self.figsize,
            "figure.frameon": True,
            "figure.titlesize": "large",
            "figure.titleweight": "normal",
            "figure.labelweight": "normal",
        })

        self._plt.rcParams.update({
            "font.size": self.font_size,
        })

        self._plt.rcParams.update({
            "axes.grid": True,
            "axes.grid.axis": "both",
            "axes.grid.which": "major",
            "axes.labelcolor": self.label_color,
            "axes.edgecolor": self.edge_color,
            "axes.facecolor": self.face_color,
            "axes.linewidth": 1.0,
        })

        self._plt.rcParams.update({
            "grid.alpha": 1.0,
            "grid.color": self.grid_color,
            "grid.linestyle": "--",
            "grid.linewidth": 0.5,
        })

        self._plt.rcParams.update({
            "xtick.color": self.xtick_color,
            "xtick.labelsize": self.xtick_label_size,
            "xtick.major.pad": 3.5,
            "xtick.major.size": 3.5,
            "ytick.color": self.ytick_color,
            "ytick.labelsize": self.ytick_label_size,
        })

        self._plt.rcParams.update({
            "savefig.format": self.save_format,
            "savefig.transparent": False,
        })
        # "savefig.directory": "/home/eduardotc/Programming/python/plots",

    def _get_font_path(self, font_name: str) -> str:
        """
        Return a font path given the parameter font name.

        Parameters
        ----------
        font_name str

        Returns
        -------
        str
            Font path of given name, or if not found, helvetica default font
        """
        fonts_dir = self.fonts_path

        fonts = {
            "fira code nerd": f"{fonts_dir}/FiraCode/FiraCodeNerdFont-Medium.ttf",
            "fira code nerd bold": f"{fonts_dir}/FiraCode/FiraCodeNerdFont-Bold.ttf",
            "fira code nerd mono": f"{fonts_dir}/FiraCode/FiraCodeNerdFontMono-Regular.ttf",
            "fira code nerd mono bold": f"{fonts_dir}/FiraCode/FiraCodeNerdFontMono-Bold.ttf",
            "helvetica": f"{fonts_dir}/Helvetica/Helvetica.ttf",
            "garuda": f"{fonts_dir}/Garuda/Garuda.otf",
        }

        font_name = font_name.replace("-", " ").replace("_", " ")
        result_chars = []
        for i, char in enumerate(font_name):
            if char.isupper() and i != 0 and font_name[i - 1] != " ":
                result_chars.append(" ")
            result_chars.append(char.lower())

        font_name = "".join(result_chars)

        if font_name not in fonts:
            msg = f"Given font '{font_name}' not found in {fonts_dir}; fallbacking to Helvetica.ttf"
            print(f"\033[31m{msg}\033[0m")
            return

        font_path = fonts.get(font_name, f"{fonts_dir}/Helvetica/Helvetica.ttf")
        return font_path

    def read_table_from_dat_file(self, path: Path | str) -> tuple[list[str], list[list[float]]]:
        """
        Read data infos from given file and return a pandas dataframe table.

        Prameters
        ---------
        path : str

        Returns
        -------
        header : List[str]
        cols : List[List[float]]
        """
        from pandas import read_csv

        path = assert_pathlib(path=path, type="file", check_exist=True, print_error=True)

        if not path.is_file():
            print("\033[31mGiven file don't exist!\033[0m", True)
            return

        if self.title == "Title":
            self.title = path.name

        header = path.read_text(encoding="utf-8").split("\n")[0].strip().split(" ")

        df = read_csv(
            path,
            delim_whitespace=True,
            skiprows=1,
            header=None,
            names=header,
            na_values=["_"],
            engine="python",
        )

        cols: list[list[float]] = [
            (df[h].dropna().astype(float)).to_numpy().tolist() for h in header
        ]
        return header, cols

    def set_box_design(self, bplot: dict) -> dict:
        """
        Set boxplot design elements.

        Parameters
        ----------
        bplot : dict
            Boxplot object created by `ax.boxplot()`

        Returns
        -------
        bplot : dict
        """
        for box in bplot["boxes"]:
            box.set_facecolor(self.box_color)
            box.set_alpha(self.box_alpha)

        for median in bplot["medians"]:
            median.set_color(self.median_color)

        return bplot

    def boxplot(self, data: list | tuple, names: list | tuple) -> dict:
        """
        Create matplotlib boxplot object dict.

        Parameters
        ----------
        data : list | tuple
            Datas of each box to be plotted
        names : list | tuple
            Legend/name of each box

        Returns
        -------
        dict
            Boxplot dict element
        """

        self._fig, self._ax = self._plt.subplots(figsize=self.figsize, dpi=self.dpi)
        self.ax_and_fig_set_design()

        positions = [
            self.layout.bench_width(1) + i * self.layout.bench_width(1) for i in range(len(names))
        ]

        bplot = self._ax.boxplot(
            data,
            positions=positions,
            widths=self.layout.box_width * 0.9,
            patch_artist=True,
            showfliers=False,
            tick_labels=names,
        )

        bplot = self.set_box_design(bplot)

        ticks = [self.layout.col_center(j + 1, 1) for j in range(len(names))]
        self._ax.set_xticks(ticks)
        self._ax.set_xticklabels(names, rotation=315, ha="left")

        for j in range(2, len(names) + 1):
            self._ax.axvline(
                x=self.layout.separator_at(j, 1),
                linestyle=":",
                linewidth=0.8,
            )

        maxv = max(max(sublist) for sublist in data if sublist)
        minv = min(min(sublist) for sublist in data if sublist)

        y_min = 0 if (maxv / minv) > 10 else minv * 0.5
        y_max = 1.5 * maxv

        self._ax.set_ylim(y_min, y_max)

        self._ax.grid(axis="y", linestyle="--", alpha=0.5, color="#c7c8f5")

        self._plt.show()

    def plt_swatch(
        self,
        colors: list,
        colors_per_row: int = 10,
        title: str | None = None,
        label_color: str | None = None,
        label_text: str | list | None = None,
        add_col_label: bool | None = False,
    ):
        """
        Plot a grid of color swatches with hex codes.

        Parameters
        ----------
        colors : list of str
            List of HTML hex color codes.
        colors_per_row : int, Optional
            Number of colors per row before wrapping (default is 10).
        title : str, Optional
            Title of the plot (default is "Color Grid").
        label_color : str, Optional
            Color name of the label
        label_text : str, Optional
            Text to write in the label instance
        add_col_label : boo, Optional
            Whether to add the color (like the html hex code) to the label text of the square

        Examples
        --------
        >>> dpl = Plot(backend="inline")
        >>> dpl.du_swatch(["#f9b6c3", "#c4c9c6"])
        Figure(1166.83x116.683)
        >>> dpl.close()

        Notes
        -----
        With kitty `font_family`: BitstromWeraNFM and `font_size`: 19, each color square has
        approximately 29.31 pt (plotting 6 color squares/row, 2560x1440 monitor fullscreen).
        At this setup, the last color square trespass a little (≈ 20%) out of the terminal screen.
        """
        import matplotlib.colors as mplcolors
        from numpy import ceil, mean

        from .du_utils import get_kitty_terminal_size

        if isinstance(label_text, str):
            label_text = [label_text]

        term_width, _ = get_kitty_terminal_size()
        colors_per_row = min(colors_per_row, term_width // 2)
        num_colors = len(colors)
        rows = int(ceil(num_colors / colors_per_row))
        square_size = (term_width / (6.5134 * colors_per_row)) * 0.95
        fig_width = colors_per_row * square_size
        fig_height = rows * square_size

        self._fig, self._ax = self._plt.subplots(figsize=(fig_width, fig_height), dpi=self.dpi)
        self.ax_and_fig_set_design()

        self._ax.set_xlim(0, colors_per_row)
        self._ax.set_ylim(0, rows)
        self._ax.set_xticks([])
        self._ax.set_yticks([])
        self._ax.set_frame_on(False)
        self._ax.set_ylabel("")
        self._ax.set_xlabel("")

        if title is not None:
            self._ax.set_title(
                title,
                fontsize=24,
                weight="bold",
                pad=5,
                color=VARHANDLE.rgb("BLURPLE"),
            )  # Increase title size

        for idx, color in enumerate(colors):
            col = idx % colors_per_row
            row = rows - (idx // colors_per_row) - 1  # Invert y-axis for top-down ordering

            if label_text:
                add_text = f"{color}\n{label_text[idx]}" if add_col_label else label_text[idx]
            else:
                add_text = mplcolors.to_hex(color) if isinstance(color, tuple) else color

            self._ax.add_patch(
                self._plt.Rectangle(
                    (col, row),
                    1,
                    1,
                    color=mplcolors.to_hex(color) if isinstance(color, tuple) else color,
                    ec="black",
                ),
            )
            self._ax.text(
                col + 0.5,
                row + 0.5,
                add_text,
                color=label_color
                if label_color is not None
                else ("white" if mean(mplcolors.to_rgb(color)) < 0.5 else "black"),
                ha="center",
                va="center",
                fontsize=24,
                weight="bold",
            )  # Increase font size
        # print("\n\n")
        self._plt.show()

    def save_fig(self, save_path: str):
        """
        Save current plotted figure to given path.

        Parameters
        ----------
        save_path : str
        """
        self._fig.savefig(save_path)

    def close(self):
        """Close current `matplotlib.pyplot` opened figure and plot."""
        if self.save_file:
            self.save_fig(self.save_file)
        self._plt.close(self._fig)

    def ax_set_design(self):
        """Set matplotlib subplots default designs elements and configs."""
        if self._ax is None:
            LOGGER.error("Matplotlib axes element not set, impossible to run ax_set_design.", True)
            return

        font_path = self._get_font_path(self.font_name)
        self._fm.fontManager.addfont(font_path)
        self.custom_font = self._fm.FontProperties(fname=font_path)
        self._plt.rcParams.update({
            "font.family": self.custom_font.get_name(),
        })

        self._ax.set_ylabel(self.ylabel, color=self.ylabel_color)
        self._ax.set_xlabel(self.xlabel, color=self.xlabel_color)
        self._ax.set_title(self.title, color=self.title_color)

        self._ax.patch.set_alpha(0)

    def fig_set_design(self):
        """Set matplotlib figure designs elements and configs."""
        if self._fig is None:
            LOGGER.error("Matplotlib figure element not set, impossible to set designs.", True)
            return

        self._fig.patch.set_alpha(0)
        self._fig.tight_layout()

    def ax_and_fig_set_design(self):
        """Run `fig_set_design` and `ax_set_design` together."""
        self.ax_set_design()
        self.fig_set_design()

    def plot_bar(
        self,
        data: list | Series,
    ):
        """
        Plot a matplotlib bar plot given a data list.

        Parameters
        ----------
        data : list or pd.core.series.Series
            Data to be ploted, list or pandas column
        """
        from pandas import DataFrame

        self._fig, self._ax = self._plt.subplots(figsize=self.figsize, dpi=self.dpi)
        self.ax_set_design()

        # if title:
        # ax.set_title(title, fontsize=18, weight="bold", pad=20, color="white")

        data = DataFrame(data) if isinstance(data, list) else data
        data.plot(kind="bar", color="#585ac2")
        for i in range(len(data)):
            if data[i] > 1000:
                self._plt.text(
                    i,
                    1.02 * data[i],
                    f"{data[i] / 1000}k",
                    ha="center",
                    color="white",
                    fontsize=8,
                )
            else:
                self._plt.text(i, 1.02 * data[i], data[i], ha="center", color="white", fontsize=8)
        self._plt.show()

    def get_available_mpl_colors(self):
        """List all available matplotlib colors names."""
        import matplotlib.colors as mcolors

        from .color_utils import check_color_format, color_to_ansi

        all_colors = {
            **mcolors.BASE_COLORS,
            **mcolors.TABLEAU_COLORS,
            **mcolors.CSS4_COLORS,
            **mcolors.XKCD_COLORS,
        }
        fonts = []
        colors = []
        for name, code in all_colors.items():
            col = check_color_format(code)
            ans, _ = color_to_ansi(col[2])
            fonts += [name, " " * (40 - len(name)), code, "\n"]
            colors += [ans, "NONE", "BLD", "NONE"]

        LOGGER.print_same_line(fonts, colors)

    def get_available_mpl_fonts(self):
        """List all available matplotlib colors names."""
        font_dict = {}
        fonts = []
        colors = []

        font_paths = self._fm.findSystemFonts(fontpaths=self.fonts_path)

        for fp in font_paths:
            font_dict[self._fm.FontProperties(fname=fp).get_name()] = fp

        font_dict = dict(sorted(font_dict.items()))
        for name, path in font_dict.items():
            fonts += [name, " " * (40 - len(name)), path, "\n"]
            colors += ["BLUE", "NONE", "YLW", "NONE"]

        fonts += ["\n", "\n", f"{len(font_dict)}", " total fonts", "\n"]
        colors += ["NON", "NONE", "AQUA", "BLD", "NONE"]

        LOGGER.print_same_line(fonts, colors)


def cli_group_plot_utils(group_plot_utils: ArgumentGroup) -> list:
    """
    Argparse client group for plotting related flags.

    Parameters
    ----------
    group_plot_utils : argparse._ArgumentGroup
        Argparse arguments group

    Returns
    -------
    list
        List containing all flags arguments from the group

    Examples
    --------
    >>> from .cli_du_utils import create_parser, cli_parse_groups

    >>> parser = create_parser()
    >>> test = cli_parse_groups(parser)
    >>> plot_group = test["Plot"]
    >>> test_router = cli_group_plot_utils(plot_group)

    >>> print(list(test_router.keys())[0])
    bplot

    """
    router = {}

    group_plot_utils.add_argument(
        "--bplot",
        action=ArgHandle,
        type=argtypes.check_existing_file,
        help="Box plot given .dat file, containing data to plot and box names.",
    )
    router["bplot"] = cli_args_plot_utils

    group_plot_utils.add_argument(
        "--mpl-fonts",
        action="store_true",
        help="Print available matplotlib fonts.",
    )
    router["mpl_fonts"] = cli_args_plot_utils

    group_plot_utils.add_argument(
        "--mpl-colors",
        action="store_true",
        help="Print available matplotlib colors.",
    )
    router["mpl_colors"] = cli_args_plot_utils

    return router


def cli_args_plot_utils(
    args: Namespace,
    _parser: ArgumentParser,
) -> Namespace:
    """
    Client handling function for plotting related utils group flags.

    Parameters
    ----------
    args : argparse.Namespace
        Argparse arguments class
    parser : argparse.ArgumentParser
        Argparse parser class

    """
    if args.bplot is not None:
        dpl = Plot(
            ylabel="miliseconds",
            save_format="svg",
            save_file=args.save[0],
            font_name="BiraCodeNerdMonoBold",
        )

        file_data = dpl.read_table_from_dat_file(args.bplot[0])
        columns = file_data[0]

        try:
            assert len(columns) == len(file_data[1])
        except AssertionError:
            LOGGER.error("Data and columns have different lengths!", True)

        dpl.boxplot(data=file_data[1], names=columns)
        dpl.close()

    if args.mpl_fonts:
        Plot().get_available_mpl_fonts()

    if args.mpl_colors:
        Plot().get_available_mpl_colors()

