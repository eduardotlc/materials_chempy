import pandas as pd


def manual_peaks_sepparation(manual_peak):
    """

    Formats manual peaks list like [m/z1, label1, m/z2, label2] to pandas
    daraframe.

    Parameters
    ----------
        manual_peak : list
            manual peaks in a mass spectra plot, formatted like [m/z1, label1,
            m/z2, label2], with m/z being a float and label being strings.

    Returns
    -------
        df : DataFrame
            Dataframe with a 'm/z' column and a 'label' column.

    Examples
    --------
    >>> df = manual_peaks_sepparation([100.27, 'Label1', 210.34, 'Label2'])
    >>> print(df)
          m/z  labels
    0  100.27  Label1
    1  210.34  Label2

    """
    if len(manual_peak) % 2 != 0:
        raise ValueError("Input list length must be even")

    data = {
        'm/z': manual_peak[::2],  # Select odd-indexed elements
        'labels': manual_peak[1::2]     # Select even-indexed elements
    }

    df = pd.DataFrame(data)
    return df


def general_print():
    general_message = """
    -h    --help,      Print this help message.
    -i    --input      Input file path.
    -o    --output     Output file path.
    """
    print(general_message)


def mpl_print():
    mpl_message = """\
    General Matplotlib plotting
    ---------------------------
    -M    --msplot     Run default matplotlib configure.
    -S    --subtitle   Define the plot subtitle.
    -t    --title      Define the plot title.
    """
    print(mpl_message)


def ms_print():
    ms_message = """\
    Mass Spectrometry
    -----------------
    -m    --msplot     Plot .mzml file in matplotlib.

    --resolution       minimum m/z difference between two plotted peaks.
    -n                 Number of peaks to be plotted, based on intensity.
    -N                 Number of most intense peaks to be labeled with m/z.
    --manual_peak      m/z manual peak labeling, argument in form m/z1 \
label1 m/z2 label2...
    --label1           Top right box first annotation
    --label2           Top right box second annotation
    """
    print(ms_message)


def spc_print():
    spc_message = """\
    Spectrophotometry
    -----------------
    -f    --flem       Plot fluorescence emission
    -b    --baseline  [Args]    Args = simple       Add baseline to spectra.
    """
    print(spc_message)


def dban_print():
    dban_message = """\
    Articles Database Querying
    --------------------------
    save_path to a csv file can be given as last flag argument, or \
separetelly, as the --output value.

    --pubmed [args]    Args = keyword Year_1 Year_2 save_path=str(opt)    \
Query articles in PubMed database containing the keyword, starting from Year_1\
 ending in Year_2, save_path can be used to save the result to a csv
    --scopus [args]    Args = keyword Year_1 Year_2    Query articles in \
Scopus database containing the keyword in the given year range
    --dailypubmed [args]    Args = keyword Year_1 Year_2 save_path    Like the\
 --pubmed above command, but fetches the number of articles daily, usefull \
for fetching high ocurring keywords in case of having the free api.
    --springer [args]   Args = keyword year_1 year_2 save_path    Query \
articles in springer database containing the keyword in this time range
    --barplot [args]    Args = csv_path or plotted_year_range    Bar plot a \
csv given as argument or in --input, or plot if together with one of above \
commands.
    --inbarplot    Saves a bar plot image of the queryied database, needing \
to be used with one of the above flags. Saves to the same output given to the \
above functions, or --output flag
    """
    print(dban_message)


def client_help():
    """

    Prints materials chempy client flags and arguments help.

    Parameters
    ----------
        None

    Returns
    -------
        None

    Examples
    --------
    >>> client_help()
    <BLANKLINE>
        -h    --help,      Print this help message.
        -i    --input      Input file path.
        -o    --output     Output file path.
    <BLANKLINE>
        General Matplotlib plotting
        ---------------------------
        -M    --msplot     Run default matplotlib configure.
        -S    --subtitle   Define the plot subtitle.
        -t    --title      Define the plot title.
    <BLANKLINE>
        Mass Spectrometry
        -----------------
        -m    --msplot     Plot .mzml file in matplotlib.
    <BLANKLINE>
        --resolution       minimum m/z difference between two plotted peaks.
        -n                 Number of peaks to be plotted, based on intensity.
        -N                 Number of most intense peaks to be labeled with m/z.
        --manual_peak      m/z manual peak labeling, argument in form m/z1 \
label1 m/z2 label2...
        --label1           Top right box first annotation
        --label2           Top right box second annotation
    <BLANKLINE>
        Spectrophotometry
        -----------------
        -f    --flem       Plot fluorescence emission
        -b    --baseline  [Args]    Args = simple       Add baseline to \
spectra.
    <BLANKLINE>
        Articles Database Querying
        --------------------------
        save_path to a csv file can be given as last flag argument, or \
separetelly, as the --output value.
    <BLANKLINE>
        --pubmed [args]    Args = keyword Year_1 Year_2 save_path=str(opt)    \
Query articles in PubMed database containing the keyword, starting from Year_1\
 ending in Year_2, save_path can be used to save the result to a csv
        --scopus [args]    Args = keyword Year_1 Year_2    Query articles \
in Scopus database containing the keyword in the given year range
        --dailypubmed [args]    Args = keyword Year_1 Year_2 save_path    \
Like the --pubmed above command, but fetches the number of articles daily, \
usefull for fetching high ocurring keywords in case of having the free api.
        --springer [args]   Args = keyword year_1 year_2 save_path    Query \
articles in springer database containing the keyword in this time range
        --barplot [args]    Args = csv_path or plotted_year_range    Bar plot \
a csv given as argument or in --input, or plot if together with one of above \
commands.
        --inbarplot    Saves a bar plot image of the queryied database, \
needing to be used with one of the above flags. Saves to the same output \
given to the above functions, or --output flag
    <BLANKLINE>
    """
    general_print()
    mpl_print()
    ms_print()
    spc_print()
    dban_print()
    # exit()


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
            "grid.alpha": 1.0,
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
