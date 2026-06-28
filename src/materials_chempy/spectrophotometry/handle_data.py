#!/usr/bin/env python3
"""
Created on 2026-06-28 14:05:05.

@author: eduardotc
@email: eduardotcampos@hotmail.com

materials_chempy spectrophotometry data handling, treating, ploting, etc.
"""
from __future__ import annotations

import os

import matplotlib.pyplot as plt


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
