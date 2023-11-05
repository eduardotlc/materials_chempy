import pandas as pd
import materials_chempy
import os


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
        df : pandas.DataFrame
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
        -M    --msplot     Run default matplotlib configure.
        -S    --subtitle   Define the plot subtitle.
        -t    --title      Define the plot title.
    <BLANKLINE>
        Mass Spectrometry
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
        -f    --flem       Plot fluorescence emission
        -b    --baseline  [Args]    Args = simple       Add baseline to \
spectra.
    <BLANKLINE>
        Articles Database Querying
        --pubmed [args]    Args = keyword Year_1 Year_2 save_path=str(opt)    \
Query articles in PubMed database containing the keyword, starting from Year_1\ 
ending in Year_2, save_path can be used to save the result to a csv
        --scopus [args]    Args = keyword Year_1 Year_2    Query articles in \
Scopus database containing the keyword, starting from Year_1 ending in Year_2
        --dailypubmed [args]    Args = keyword Year_1 Year_2 save_path    Like the\
--pubmed above command, but fetches the number of articles daily, usefull for \
fetching high ocurring keywords in case of only having the free api.
    <BLANKLINE>
    """
    help_msg = """
    -h    --help,      Print this help message.
    -i    --input      Input file path.
    -o    --output     Output file path.

    General Matplotlib plotting
    -M    --msplot     Run default matplotlib configure.
    -S    --subtitle   Define the plot subtitle.
    -t    --title      Define the plot title.

    Mass Spectrometry
    -m    --msplot     Plot .mzml file in matplotlib.

    --resolution       minimum m/z difference between two plotted peaks.
    -n                 Number of peaks to be plotted, based on intensity.
    -N                 Number of most intense peaks to be labeled with m/z.
    --manual_peak      m/z manual peak labeling, argument in form m/z1 \
label1 m/z2 label2...
    --label1           Top right box first annotation
    --label2           Top right box second annotation

    Spectrophotometry
    -f    --flem       Plot fluorescence emission
    -b    --baseline  [Args]    Args = simple       Add baseline to spectra.

    Articles Database Querying
    --pubmed [args]    Args = keyword Year_1 Year_2 save_path=str(opt)    \
Query articles in PubMed database containing the keyword, starting from Year_1\ 
ending in Year_2, save_path can be used to save the result to a csv
    --scopus [args]    Args = keyword Year_1 Year_2    Query articles in \
Scopus database containing the keyword, starting from Year_1 ending in Year_2
    --dailypubmed [args]    Args = keyword Year_1 Year_2 save_path    Like the\
--pubmed above command, but fetches the number of articles daily, usefull for \
fetching high ocurring keywords in case of only having the free api.

               """
    print(help_msg)


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
            "axes.edgecolor": "#bcbcbc",
            "axes.facecolor": "#eeeeee",
            "axes.linewidth": 1.0,
        }
    )

    plt.rcParams.update(
        {
            "grid.alpha": 1.0,
            "grid.color": "#b2b2b2",
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
                    "#348ABD",
                    "#988ED5",
                    "#777777",
                    "#FBC15E",
                    "#8EBA42",
                    "#FFB5B8",
                ],
            )
        }
    )


def absolute_path(file_path):
    """

    Concatenate the package main folder absolute path to a given string,
    permmiting to use paths as relatives, with this function converting to
    absolute.

    parameters
    ----------
    file_path : str
        str of a relative (with relation of package main folder) file path

    returns
    -------
    absol_path : str
        str of absolute path.

    examples
    --------
    >>> test = absolute_path(file_path = 'example_data/anad2.mzml')
    >>> print(test)
    /home/eduardotc/Programação/my_gits/materials_chempy/example_data/anad2.mzml
    """
    path = os.path.dirname(materials_chempy.__file__)
    absol_path = path + "/" + file_path
    return absol_path


def remove_duplicates(strings_list):
    """

    Removes repeated string elements from a list.

    Parameters
    ----------
    strings_list : list
        List containing strings, will be cleaned removing duplicates

    Returns
    -------
    unique_strings : list
        Cleaned list

    Examples
    --------

    >>> a = ['2012', '2012', '2014', '2019', '2012']
    >>> no_duplicates = remove_duplicates(a)
    >>> print(no_duplicates)
    ['2012', '2014', '2019']
    """
    unique_strings = []
    for string in strings_list:
        if string not in unique_strings:
            unique_strings.append(string)
    return unique_strings
