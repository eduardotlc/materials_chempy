import pandas as pd
import matplotlib.pyplot as plt
import os


def file_extract(spec_file):
    """

    Extracts from a given txt file the 2 axis from the spectra.

    Parameters
    ----------
    spec_file : str
        Path to the txt spectra file.

    Returns
    -------
    df : pd.DataFrame
        Dataframe with one x 'wavelength' column and onde y 'CPS' column.

    Examples
    --------
    Reading the fluorescence emission txt example file, storing the axis in
    the dataframe

    >>> file_extract('../example_data/aunu_fl.txt')
         Wavelenght (nm)     CPS
    0             1200.0  1031.0
    1             1201.0  1034.0
    2             1202.0  1098.0
    3             1203.0  1122.0
    4             1204.0  1079.0
    ..               ...     ...
    196           1396.0   937.0
    197           1397.0   898.0
    198           1398.0   912.0
    199           1399.0   844.0
    200           1400.0   953.0
    <BLANKLINE>
    [201 rows x 2 columns]

    """
    data = []

    # Open the text file for reading
    with open(spec_file, 'r') as file:
        for line in file:
            # Split each line into two elements, assuming space as the
            # separator
            elements = line.split()

            # Check if the first element is a string (you can modify
            # this condition)
            if not elements[0].isalpha():
                # Append the first element to 'axis' and the second
                # element to 'cps'
                data.append([elements[0], elements[1]])

    # Create a Pandas DataFrame from the collected data
    df = pd.DataFrame(data, columns=['Wavelenght (nm)', 'CPS'])
    df['CPS'] = df['CPS'].astype('float')
    df['Wavelenght (nm)'] = df['Wavelenght (nm)'].astype('float')
    df.round({'Wavelenght (nm)': 0})
    return df


def spc_plot(df, input_path, title=None):
    """

    Plots a matplotlib spectra from a given dataframe extracted from a txt.

    Parameters
    ----------
    df : pd.Dataframe
        Dataframe extracted from a spectrum in .txt format
    input_path : str
        String of the path from the parsed input txt file
    title : str
        Plot title

    Returns
    -------
    None

    """
    df_names = df.columns.values.tolist()
    col1 = df_names[0]
    col2 = df_names[1]
    fig, ax = plt.subplots()
    ax.grid(True)
    plt.xlabel(col1)
    plt.ylabel(col2)
    if title is None:
        plt.title((os.path.basename(input_path))[:-4])
    else:
        plt.title(title)
    ax.plot(df[col1], df[col2])
    plt.savefig(os.path.splitext(input_path)[0])


def mean_baseline(df):
    """

    Makes a simple mean baseline normalization.

    Parameters
    ----------
    df : pd.Dataframe
        Original spectra dataframe

    Returns
    -------
    df : pd.Dataframe
        Simple mean baseline subtracted spectra dataframe

    Examples
    --------
    >>> import pandas as pd
    >>> import numpy as np
    >>> from scipy.stats import norm
    >>> wavenumbers = np.arange(-10, 10, 0.02)
    >>> value = norm.pdf(wavenumbers,0,1)
    >>> df = pd.DataFrame({'wavenumber': wavenumbers,
    ...                    'CPS': value})
    >>> tt = mean_baseline(df)
    >>> print(tt.max())
    wavenumber    9.980000
    CPS           0.348942
    dtype: float64

    """
    baseline = df['CPS'].mean()
    df['CPS'] = df['CPS'] - baseline
    df['CPS'] = df['CPS'].clip(lower=0)
    return df
