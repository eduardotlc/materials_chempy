# /home/eduardotc/mambaforge/envs/materials_chempy/bin python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 17:58:00 2023

@author: eduardotcampos@usp.br
"""

import pandas as pd
import pyopenms
import matplotlib.pyplot as plt
import os
# sys.path.insert(1, '/home/eduardotc/Programação/my_gits/materials_chempy')


def mzmldf(mzmlpath):
    """

    Gets a m/z and intensity dataframe.

    Returns a pandas dataframe, with one 'm/z' column and ond 'intensity'
    column, from a user given .mzML mass spectra file.

    Parameters
    ----------
    mzmlpath : str
           String of the path to the .mzML file.

    Returns
    -------
    df : pandas.DataFrame
           Pandas dataframe, with one 'm/z' and one 'intensity' columns.

    Examples
    --------
    >>> test = mzmldf('../example_data/anad2.mzML')
    >>> print(test)
                  mz      intensity
    0     101.596733 -145034.828125
    1     102.640442 -117682.968750
    2     102.927109 -146770.203125
    3     103.801506 -124195.812500
    4     104.562500 -154113.390625
    ...          ...            ...
    7415  294.877625 -166492.343750
    7416  303.156250 -166584.515625
    7417  314.438904 -164998.968750
    7418  336.156250 -166484.265625
    7419  348.063538 -164486.343750
    <BLANKLINE>
    [7420 rows x 2 columns]

    """
    exp = pyopenms.MSExperiment()
    pyopenms.MzMLFile().load(mzmlpath, exp)
    mz_values = []
    intensity_values = []

    # Extract the mass-to-charge ratios (m/z) and intensity values
    for spectrum in exp:
        mz_array = spectrum.get_peaks()[0]
        intensity_array = spectrum.get_peaks()[1]
        mz_values.extend(mz_array)
        intensity_values.extend(intensity_array)

    df = pd.DataFrame({'mz': mz_values,
                       'intensity': intensity_values})

    baseline = df['intensity'].mean()
    df['intensity'] = df['intensity'] - baseline
    return df


def dfpltlimits(df):
    """

    Gets plot limits based on the m/z and intensity dataframe.

    Parameters
    ----------
    df : pandas.DataFrame
        m/z and intensity columns mass spectra dataframe.

    Returns
    -------
    xlimit : list
        list of the plot x axis limits.

    ylimit : list
        list of the plot y axis limits.

    Examples
    --------
    >>> df = pd.DataFrame({
    ...     'mz': [100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150],
    ...     'intensity': [5000, 2000, 1000, 100, 7400, 3000, 2000, 1110, 400,
    ...                   900, 3225]
    ... })
    >>> test = dfpltlimits(df)
    >>> print(test)
    ([80.0, 180.0], [0, 8880.0])

    """
    ylimit = [0, (df['intensity'].max()) * 1.2]
    xlimit = [(df['mz'].min()) * 0.8, (df['mz'].max()) * 1.2]
    return xlimit, ylimit


def msmplcfg(xlimit,
             ylimit,
             mzmlpath,
             subtitle):
    """

    Configure matplotlib plot for a mass spectra.

    Parameters
    ----------
    subtitle : str
        Subtitle of the plot.

    mzmlpath : str (opt)
        String to the path of the .mzML file that will be plotted, used
        to define a subtitle based on the file name, in case a subtitle
        is not defined.

    xlimit : list
        List containing x axis limits.

    ylimit : list
        List containing y axis limits.

    Returns
    -------
    fig : matplotlib.figure.Figure
        Matplotlib figure class.

    ax : matplotlib.axes._subplots.AxesSubplot
        Axes subplot matplotlib class.

    Examples
    --------
    >>> fig, ax = msmplcfg([80.0, 180.0], [0, 8880.0], 'test', 'test')
    >>> print(fig)
    Figure(4000x2400)
    >>> print(type(fig))
    <class 'matplotlib.figure.Figure'>
    >>> print(ax)
    Axes(0.125,0.11;0.775x0.77)
    >>> print(type(ax))
    <class 'matplotlib.axes._axes.Axes'>

    """
    fig, ax = plt.subplots(figsize=(10, 6), dpi=400)
    ax.set_ylim(ylimit)
    ax.set_xlim(xlimit)
    ax.set_xlabel("m/z")
    ax.set_ylabel("Intensity")
    ax.set_title("Mass spectrum")
    if subtitle == 'default':
        subtitle = (os.path.basename(mzmlpath))[:-5]
    fig.suptitle(f"{subtitle}", fontsize=15, color='#3333b2')
    return fig, ax


def dfhighests(df,
               resolution_thrs,
               n_highest):
    """

    Sort from the m/z and intensity dataframe the n highest intensity rows,
    with the sorted values having a m/z difference between then higher than
    resolution_thrs.

    Parameters
    ----------
    df : pd.DataFrame
        m/z and intensity columns dataframe, from which will be extracte
        the interested peaks.

    resolution_thrs : float
        m/z difference between 2 peaks to have both of them plotted.

    n_highest : int
        Number of most intense peaks ('intenisty' dataframe column values)
        to be extracted and plotted.

    Returns
    -------
    result_df : pd.DataFrame
        extracted m/z, intensity and index (olds) columns dataframe, cleaned
        from too close peaks and low intensity peaks.

    Examples
    --------
    >>> df = pd.DataFrame({
    ...     'mz': [114.24, 143.22, 137.98, 114.20, 160.87, 197.77, 182.43,
    ...             160.61, 144.49],
    ...     'intensity': [10000, 4300, 250, 8700, 11350, 789, 6649, 6680, 200]
    ... })
    >>> test = dfhighests(df, 0.5, 3)
    >>> print(test)
       index      mz  intensity
    0      4  160.87    11350.0
    1      0  114.24    10000.0
    2      6  182.43     6649.0

    """

    df = df.sort_values(by='intensity', ascending=False)

    # Initialize an empty list to store the selected rows
    selected_rows = []

    # Loop through the sorted DataFrame and select rows
    for _, row in df.iterrows():
        if len(selected_rows) >= n_highest:
            break

        # Check if the current 'x' value has a difference of at least 1 from
        # previously selected 'x' values
        if all(abs(row['mz'] - prev_row['mz']) >= resolution_thrs for prev_row
               in selected_rows):
            selected_rows.append(row)

    # Create a new DataFrame from the selected rows
    result_df = pd.DataFrame(selected_rows)
    result_df = result_df.reset_index()
    return result_df


def auto_annotate(fig,
                  ax,
                  result_df,
                  n_labels):
    """

    Annotate matplotlib spectra with the given m/z highest intensity peaks.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Matplotlib figure class.

    ax : matplotlib.axes._subplots.AxesSubplot
        Axes subplot matplotlib class.

    result_df : pd.DataFrame
        m/z and intensity mzml dataframe from the plotted spectra which
        will be annotated.

    n_labels : int
        Number of spectra peaks, based on the highests intensities, the is
        desired to label.

    Returns
    -------
    None

    """
    peakannotateds = 0
    while peakannotateds < n_labels:
        # Getting a result_df row based on the number of the loop, being a pd
        # series containing a m/z and its intensity
        mzannot = result_df.loc[peakannotateds, 'mz']
        intannot = result_df.loc[peakannotateds, 'intensity']
        ax.annotate(
            (
                f'{round(mzannot, 2)}'
            ),
            xy=(mzannot, intannot),
            fontsize=10,
            fontweight='bold',
        )
        peakannotateds += 1


def manual_peak(fig,
                ax,
                result_df,
                manual_peak_df):
    """

    Annotate a user given string in a desired m/z peak.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Matplotlib figure class.

    ax : matplotlib.axes._subplots.AxesSubplot
        Axes subplot matplotlib class.

    result_df : pd.DataFrame
        m/z and intensity mzml dataframe.

    manual_peak_df : pd.DataFrame
        Pandas dataframe class consisting of one 'mz' and one 'labels'
        column.

    Returns
    -------
    None

    """
    for n in manual_peak_df['mz']:
        # Getting the row from the dataFrame that contains the closest m/z
        # Value from the one given
        mzreal = result_df.iloc[(result_df['mz'] - n).abs().
                                argsort()[:1]]
        # Getting the corresponding manual peak label list element
        # (same index from the actual loop m/z), and annotating it
        ax.annotate(
            (
                f"{(manual_peak_df.loc[manual_peak_df['mz'] == n, 'labels'])}"
                '\n'
            ),
            # Adding xy coordinates, extracting from the above defined
            # closest m/z row
            xy=(mzreal['mz'], mzreal['intensity']),
            fontsize=10,
            fontweight='bold',
        )


def mpl_labelbox(fig,
                 ax,
                 xlimit,
                 ylimit,
                 label1,
                 label2):
    """

    Create an upper right box in the plot, with 2 labels written inside it.

    Parameters
    ----------
    xlimit : list
        x axis limits.

    ylimit : list
        y axis limits.

    label1 : str
        first line written in the label box.

    label2 : str
        second line written in the label box.

    Returns
    -------
    None

    """

    label_list = [label1, label2]
    label_size = (len(max(label_list, key=len))) * 0.015
    mz_label_offset = 12.48 / (len(max(label_list, key=len)))

    # Defining a legend colored box
    ax.indicate_inset([(mz_label_offset * xlimit[1]),
                       (0.82 * ylimit[1]),
                       (label_size * (xlimit[1] - xlimit[0])),
                       (0.15 * (ylimit[1] - ylimit[0]))],
                      facecolor='#a6bcf8',
                      edgecolor='#252a2d',
                      alpha=0.35)

    # Defining the writtent content of the legend box
    ax.annotate(
        (
            f'{label1}'
            '\n'
            '\n'
            f'{label2}'
        ),
        xy=(1.03 * (mz_label_offset * xlimit[1]), 0.85 * ylimit[1]),
        fontsize=12,
        fontfamily='QTHelvet-black',
        fontweight='normal',
        color='#000000',
    )


def msplot(mzmlpath,
           resolution_thrs,
           n_highest,
           n_labels,
           subtitle,
           manual_peak_df,
           label1,
           label2):
    """

    Plot a .mzML file in matplotlib.

    Plot a .mzML file in matplotlib, as a mz traces plot, of the user defined
    (or predefined) n highest mz peaks, with the possibility of adding general
    annotated labels to the plot, to define the number of mz peaks labeled with
    their value, minimal mz difference between two peaks to have both of the
    plotted and custom manual labeling of single mz peaks (to write to wich
    molecule it belongs for example).

    Parameters
    ----------
    mzmlpath : str
        String of the path to the .mzML file.

    resolution_thrs : float
        m/z necessary difference between 2 peaks for both being plotted,
        otherwise, if the difference between the 2 peaks is lower, only one of
        them is plotted.

    n_highest : int
        Number of total mz peaks to be drawn, based on the highest intensities.

    n_labels : int
        Number of most intese peaks to be labeled with their m/z value.

    subtitle : str
        Plot subtitle, if not defined will be the parsed .mzML file name.

    manual_peak_df : pd.DataFrame
        Pandas dataframe class consisting of one 'mz' and one 'labels'
        column.

    label1 : str
        First label that appears in a box in the top right of the plot, for
        example, the mass spectrometry technique used.

    label2 : str
        Second label that appears in a box in the top right of the plot, for
        example, the injection method (like direct injection or hplc).

    Returns
    -------
    None
        Don't have return, but plot the spectrum and save it to a png.

    """
    # Defining errors
    if mzmlpath == 'default':
        raise Exception("A path to a .mzml file should be given")

    # Load the spectra from the mzML file
    df = mzmldf(mzmlpath)

    # Getting the plot limits
    xlimit, ylimit = dfpltlimits(df)

    # Configuring plot properties
    fig, ax = msmplcfg(xlimit, ylimit, mzmlpath, subtitle)

    # Filtering dataframe based on difference of the m/z between peaks and
    # highest intensities
    result_df = dfhighests(df, resolution_thrs, n_highest)

    # Automatic n highest intensity annotation with the m/z value
    auto_annotate(fig, ax, result_df, n_labels)

    # Manual peak annotation
    if len(manual_peak_df) != 0:
        manual_peak(fig, ax, result_df, manual_peak_df)

    # Drawing and labeling a box in the plot
    mpl_labelbox(fig, ax, xlimit, ylimit, label1, label2)

    # Plotting the spectrum as line peaks
    ax.stem(result_df['mz'], result_df['intensity'], markerfmt="none")
    ax.plot
    plt.show

    # Saving the image
    plt.savefig(os.path.splitext(mzmlpath)[0])
