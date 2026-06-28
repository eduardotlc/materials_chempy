"""
Created on 2026-06-28 19:49:24.

@author: eduardotc
@contributors: lu4vic
@email: eduardotcampos@hotmail.com

mass spectrometry utils, for hadnling analysys data results, treatments, etc.
"""
from __future__ import annotations

import pandas as pd


def manual_peaks_sepparation(manual_peak: list) -> pd.DataFrame:
    """
    Format manual peaks list like [m/z1, label1, m/z2, label2] to pandas daraframe.

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

