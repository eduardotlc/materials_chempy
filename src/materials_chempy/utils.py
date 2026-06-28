#!/usr/bin/env python3
"""
Created on 2026-06-28 12:49:24.

@author: eduardotc
@email: eduardotcampos@hotmail.com

materials_chempy module general utils functions, to be used by other scripts/functions from the
app, not directly by client commands executions.
"""
from __future__ import annotations

import sys
from pathlib import Path

import pandas as pd


# def manual_peaks_sepparation(manual_peak: list) -> pd.DataFrame:
    # """
    # Format manual peaks list like [m/z1, label1, m/z2, label2] to pandas daraframe.

    # Parameters
    # ----------
    # manual_peak : list
        # manual peaks in a mass spectra plot, formatted like [m/z1, label1,
        # m/z2, label2], with m/z being a float and label being strings.

    # Returns
    # -------
    # df : DataFrame
        # Dataframe with a 'm/z' column and a 'label' column.

    # Examples
    # --------
    # >>> df = manual_peaks_sepparation([100.27, 'Label1', 210.34, 'Label2'])
    # >>> print(df)
          # m/z  labels
    # 0  100.27  Label1
    # 1  210.34  Label2

    # """
    # if len(manual_peak) % 2 != 0:
        # raise ValueError("Input list length must be even")

    # data = {
        # 'm/z': manual_peak[::2],  # Select odd-indexed elements
        # 'labels': manual_peak[1::2]     # Select even-indexed elements
    # }

    # df = pd.DataFrame(data)
    # return df


# def general_print():
    # general_message = """
    # -h    --help,      Print this help message.
    # -i    --input      Input file path.
    # -o    --output     Output file path.
    # """
    # print(general_message)


# def mpl_print():
    # mpl_message = """\
    # General Matplotlib plotting
    # ---------------------------
    # -M    --msplot     Run default matplotlib configure.
    # -S    --subtitle   Define the plot subtitle.
    # -t    --title      Define the plot title.
    # """
    # print(mpl_message)


# def ms_print():
    # ms_message = """\
    # Mass Spectrometry
    # -----------------
    # -m    --msplot     Plot .mzml file in matplotlib.

    # --resolution       minimum m/z difference between two plotted peaks.
    # -n                 Number of peaks to be plotted, based on intensity.
    # -N                 Number of most intense peaks to be labeled with m/z.
    # --manual_peak      m/z manual peak labeling, argument in form m/z1 \
# label1 m/z2 label2...
    # --label1           Top right box first annotation
    # --label2           Top right box second annotation
    # """
    # print(ms_message)


# def spc_print():
    # spc_message = """\
    # Spectrophotometry
    # -----------------
    # -f    --flem       Plot fluorescence emission
    # -b    --baseline  [Args]    Args = simple       Add baseline to spectra.
    # """
    # print(spc_message)


# def dban_print():
    # dban_message = """\
    # Articles Database Querying
    # --------------------------
    # save_path to a csv file can be given as last flag argument, or \
# separetelly, as the --output value.

    # --pubmed [args]    Args = keyword Year_1 Year_2 save_path=str(opt)    \
# Query articles in PubMed database containing the keyword, starting from Year_1\
 # ending in Year_2, save_path can be used to save the result to a csv
    # --scopus [args]    Args = keyword Year_1 Year_2    Query articles in \
# Scopus database containing the keyword in the given year range
    # --dailypubmed [args]    Args = keyword Year_1 Year_2 save_path    Like the\
 # --pubmed above command, but fetches the number of articles daily, usefull \
# for fetching high ocurring keywords in case of having the free api.
    # --springer [args]   Args = keyword year_1 year_2 save_path    Query \
# articles in springer database containing the keyword in this time range
    # --barplot [args]    Args = csv_path or plotted_year_range    Bar plot a \
# csv given as argument or in --input, or plot if together with one of above \
# commands.
    # --inbarplot    Saves a bar plot image of the queryied database, needing \
# to be used with one of the above flags. Saves to the same output given to the \
# above functions, or --output flag
    # """
    # print(dban_message)


# def client_help():
    # """

    # Prints materials chempy client flags and arguments help.

    # Parameters
    # ----------
        # None

    # Returns
    # -------
        # None

    # Examples
    # --------
    # >>> client_help()
    # <BLANKLINE>
        # -h    --help,      Print this help message.
        # -i    --input      Input file path.
        # -o    --output     Output file path.
    # <BLANKLINE>
        # General Matplotlib plotting
        # ---------------------------
        # -M    --msplot     Run default matplotlib configure.
        # -S    --subtitle   Define the plot subtitle.
        # -t    --title      Define the plot title.
    # <BLANKLINE>
        # Mass Spectrometry
        # -----------------
        # -m    --msplot     Plot .mzml file in matplotlib.
    # <BLANKLINE>
        # --resolution       minimum m/z difference between two plotted peaks.
        # -n                 Number of peaks to be plotted, based on intensity.
        # -N                 Number of most intense peaks to be labeled with m/z.
        # --manual_peak      m/z manual peak labeling, argument in form m/z1 \
# label1 m/z2 label2...
        # --label1           Top right box first annotation
        # --label2           Top right box second annotation
    # <BLANKLINE>
        # Spectrophotometry
        # -----------------
        # -f    --flem       Plot fluorescence emission
        # -b    --baseline  [Args]    Args = simple       Add baseline to \
# spectra.
    # <BLANKLINE>
        # Articles Database Querying
        # --------------------------
        # save_path to a csv file can be given as last flag argument, or \
# separetelly, as the --output value.
    # <BLANKLINE>
        # --pubmed [args]    Args = keyword Year_1 Year_2 save_path=str(opt)    \
# Query articles in PubMed database containing the keyword, starting from Year_1\
 # ending in Year_2, save_path can be used to save the result to a csv
        # --scopus [args]    Args = keyword Year_1 Year_2    Query articles \
# in Scopus database containing the keyword in the given year range
        # --dailypubmed [args]    Args = keyword Year_1 Year_2 save_path    \
# Like the --pubmed above command, but fetches the number of articles daily, \
# usefull for fetching high ocurring keywords in case of having the free api.
        # --springer [args]   Args = keyword year_1 year_2 save_path    Query \
# articles in springer database containing the keyword in this time range
        # --barplot [args]    Args = csv_path or plotted_year_range    Bar plot \
# a csv given as argument or in --input, or plot if together with one of above \
# commands.
        # --inbarplot    Saves a bar plot image of the queryied database, \
# needing to be used with one of the above flags. Saves to the same output \
# given to the above functions, or --output flag
    # <BLANKLINE>
    # """
    # general_print()
    # mpl_print()
    # ms_print()
    # spc_print()
    # dban_print()
    # # exit()


def matplotlib_config():
    """

    Configure matplotlib plots.

    Parameters
    ----------
        None

    Returns
    -------
        None

    Examples
    --------
    >>> import matplotlib.pyplot as plt
    >>> matplotlib_config()
    >>> test = plt.rcParams["font.family"]
    >>> print(test)
    ['QTHelvet-Black']

    """
    import matplotlib.pyplot as plt
    from cycler import cycler

    plt.rcParams["pdf.use14corefonts"] = True
    plt.rcParams["ps.useafm"] = True
    plt.rcParams.update(
        {
            "figure.dpi": 400,
            "font.size": 16,
            "figure.facecolor": "white",
            "figure.figsize": [10, 6],
            "figure.frameon": True,
            "figure.titlesize": "large",
            "figure.titleweight": "bold",
            "figure.labelsize": "medium",
            "figure.labelweight": "normal",
            "figure.edgecolor": "#000000",
        }
    )

    plt.rcParams.update(
        {
            "font.style": "normal",
            "font.weight": "bold",
            "font.family": "QTHelvet-Black",
            "font.sans-serif": "QTHelvet-Black",
        }
    )

    plt.rcParams.update(
        {
            "axes.grid": True,
            "axes.grid.axis": "both",
            "axes.grid.which": "major",
            "axes.labelcolor": "#172038",
            "axes.edgecolor": "#d1d1d1",
            "axes.facecolor": "#efefef",
            "axes.linewidth": 1.0,
        }
    )

    plt.rcParams.update(
        {
            "grid.alpha": 1.0,
            "grid.color": "#c8c8c8",
            "grid.linestyle": "--",
            "grid.linewidth": 0.5,
        }
    )

    plt.rcParams.update(
        {
            "xtick.labelsize": "small",
            "xtick.major.pad": 3.5,
            "xtick.major.size": 3.5,
            "xtick.alignment": "center",
            "xtick.color": "#000000",
            "ytick.labelsize": "x-small",
            "ytick.major.pad": 3.5,
            "ytick.major.size": 3.5,
            "ytick.alignment": "center_baseline",
            "ytick.color": "#000000",
        }
    )
    plt.rcParams.update(
        {
            "axes.prop_cycle": cycler(
                "color",
                [
                    "#7499ff",
                    "#4f7dc4",
                    "#78a1d9",
                    "#99b5e3",
                    "#bacced",
                    "#6e80c7",
                    "#214599",
                ],
            )
        }
    )


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
    >>> curr_dir = getcwd() # type: string
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
