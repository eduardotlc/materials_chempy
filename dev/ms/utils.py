#/home/eduardotc/mambaforge/envs/materials_chempy/bin python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 7 23:25:50 2023

@author: eduardotcampos@usp.br
"""

import sys
sys.path.insert(1, '/home/eduardotc/application/app/folder')


def msplot(mzmlpath="/home/eduardotc/Programação/my_gits/materials_chempy/example_data/anad2.mzML", n_highest=20, n_labels=8, manual_peak=False, manual_peak_value, manual_peak_label, label1='Ion Trap ESI-MS', label2='Direct injection' ):
    import matplotlib.pyplot as plt
    import pandas as pd
    import numpy as np
    import pyopenms
    import os

    # Customizable variables
    fname = os.path.basename(mzmlpath)
    fname = os.path.splitext(mzmlpath)[0]
    resolution_thrs=0.3
    # Load the spectra from the mzML file
    exp = pyopenms.MSExperiment()
    pyopenms.MzMLFile().load(mzmlpath, exp)

    # Extract the mass-to-charge ratios (m/z) and intensity values
    mz_values = []
    intensity_values = []
    for spectrum in exp:
        mz_array = spectrum.get_peaks()[0]
        intensity_array = spectrum.get_peaks()[1]
        mz_values.extend(mz_array)
        intensity_values.extend(intensity_array)

        mz_max = max(mz_values)
        int_max = max(intensity_values)
        ymax = int_max*1.2
        ylimit = [0, ymax]

    # Calculate the baseline (simple mean in this example)
    baseline = np.mean(intensity_values)

    # Subtract the baseline from the intensity values
    intensity_values = np.array(intensity_values) - baseline


    # Initiate conditional variable counters
    total_indices = []
    total_indices.append(0)
    ncycle = 1
    diffms = True
    npeaks=0

    # Define the size and dpi of the image
    (
        fig,
        ax,
    ) = plt.subplots(figsize=(10, 6), dpi=200)

    # Defining the plot design
    ax.set_ylim(ylimit)
    ax.set_xlabel("m/z")
    ax.set_ylabel("Intensidade")
    fig.suptitle("$AnAd_2$", fontsize=15, color='#3333b2')

    # Determine the number of highest intensity peaks to label (user-defined)
    ax.set_title("Espectro de Massas")
    high_ind = np.array([])
    high_mz = np.array([])
    high_int = np.array([])

    # Conditional loop to plot the defined number of peaks
    while len(total_indices) <= n_highest:
        intaddind = np.argpartition(intensity_values, -ncycle)[-ncycle]
        mz = mz_values[intaddind]
        for i in total_indices:
            if abs(mz - i) < resolution_thrs:
                diffms = False
        if diffms:
            high_int = np.append(high_int, intensity_values[intaddind])
            high_mz = np.append(high_mz, mz_values[intaddind])

            # Conditional to automatic label the desired number of peaks
            if npeaks < n_labels:
                ax.annotate(
                    round(mz, 2), xy=(mz, intensity_values[intaddind]), fontsize=10
                )
                npeaks=npeaks+1
            total_indices.append(mz)
        ncycle = ncycle + 1
        diffms = True

    # Manual peak annotation
    if manual_peak:
        ax.annotate(
            (
                f'{manual_peak_label}'
                '\n'
            ),
            xy=(236.74, 3.20e+6),
            fontsize=10,
            fontweight='bold',
        )

    # Defining a legend colored box
    axin2=ax.indicate_inset([(0.85*mz_max), (int_max), (0.2*mz_max), (0.18*int_max)], facecolor='#a6bcf8', edgecolor='#252a2d', alpha=0.35)

    # Defining the writtent content of the legend box
    ax.annotate(
        (
            f'{label1}'
            '\n'
            '\n'
            f'{label2}'
        ),
        xy=(0.9*mz_max, 1.03*int_max),
        fontsize=12,
        fontfamily='QTHelvet-black',
        fontweight='normal',
        color='#000000',
    )

    # Plotting the spectrum as line peaks
    ax.stem(high_mz, high_int, markerfmt="none")
    ax.plot
    plt.show

    # Saving the image


    plt.savefig(fname)
