"""
Created on 2026-06-28 14:00:17.

@author: eduardotc
@contributors: lu4vic
@email: eduardotcampos@hotmail.com

matertials_chempy spectrophotometry module utils.
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd


def file_extract(spec_file: str | Path = "example_data/aunu_fl.txtx"):
    """
    Extract from a given txt file the 2 axis from the spectra.

    Parameters
    ----------
    spec_file : str | Path
        Path to the txt spectra file.

    Returns
    -------
    df : pd.DataFrame
        Dataframe with one x 'wavelength' column and onde y 'CPS' column.

    Examples
    --------
    Reading the fluorescence emission txt example file, storing the axis in
    the dataframe
    >>> data_file = Path("example_data") / "aunu_fl.txt"
    >>> test_extract = file_extract(data_file)

    >>> pd.testing.assert_index_equal(test_extract.columns, pd.Index(["wavelength", "cps"]))
    >>> assert test_extract.size == 402
    >>> assert test_extract["cps"][100] == 1178.0

    >>> print(test_extract.iloc[40].wavelength)
    1240.0
    >>> print(test_extract["cps"][100])
    1178.0
    """
    spec_file = Path(spec_file) if isinstance(spec_file, str) else spec_file

    data = []

    # Open the text file for reading
    with spec_file.open("r") as file:
        for line in file:
            # Split each line into two elements, assuming space as the separator
            elements = line.split()
            # Check if the first element is a string (you can modify this condition)
            if not elements[0].isalpha():
                # Append the first element to 'axis' and the second element to 'cps'
                data.append([elements[0], elements[1]])

    # Create a Pandas DataFrame from the collected data
    df = pd.DataFrame(data, columns=["wavelength", "cps"])
    df["cps"] = df["cps"].astype("float")
    df["wavelength"] = df["wavelength"].astype("float")
    df.round({"wavelength": 0})

    return df
