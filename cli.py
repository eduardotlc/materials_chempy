import argparse
import materials_chempy.utils as mcpyut
import materials_chempy.mass_spectrometry.ms_functions as msmcpy
import materials_chempy.spectrophotometry.spec_functions as spcmcpy
import materials_chempy.database_analysis.dban_functions as dbanmcpy
import pandas as pd

# Predefined msplot parameters
# mzmlpath = mcpyut.absolute_path("example_data/anad2.mzML")
# output_path = './example_data/'

resolution_thrs = 0.3
n_highest = 15
n_labels = 5
subtitle = 'default'
manual_peak_df = pd.DataFrame({})
label1 = 'Ion Trap ESI-MS'
label2 = 'Direct injection'
title = None
year_1 = 1996
year_2 = 2023

def add_arguments():
    """

    Adds argparse arguments.

    """
    parser = argparse.ArgumentParser(description="Materials chempy package\
                                     main fucntion, parsing specific submodule\
                                     functions by user parsed flags.",
                                     add_help=False)

    # Add flags
    parser.add_argument("-h", "--help", action="store_true")
    parser.add_argument("-m", "--msplot", action="store_true", help="Plot\
                        .mzML file in matplotlib.")
    parser.add_argument("-i", "--input", type=str)
    parser.add_argument("-o", "--output", type=str)
    parser.add_argument("--resolution", type=float)
    parser.add_argument("-N", type=int)
    parser.add_argument("-n", type=int)
    parser.add_argument("-S", "--subtitle", type=str)
    parser.add_argument("--manual_peak", nargs='+')
    parser.add_argument("--label1", type=str)
    parser.add_argument("--label2", type=str)
    parser.add_argument("-M", "--mplcfg", action="store_true")
    parser.add_argument("-f", "--flem", action="store_true")
    parser.add_argument("-t", "--title", type=str)
    parser.add_argument("-b", "--baseline", type=str)
    parser.add_argument("--pubmed", nargs="+")
    parser.add_argument("--scopus", nargs="+")
    parser.add_argument("--dailypubmed", nargs="+")
    parser.add_argument("--springer", nargs="+")

    return parser


def main():
    """

    Materials chempy package main fucntion, parsing specific submodule
    functions by user parsed flags.

    Returns
    -------
        None

    """
    parser = add_arguments()
    args = parser.parse_args()
    if args.help:
        mcpyut.client_help()
    if args.mplcfg:
        mcpyut.matplotlib_config()
    if args.input:
        input_path = args.input
    if args.output:
        output_path = args.output
    if args.title:
        title = args.title
    if args.resolution:
        resolution_thrs = args.resolution
    if args.n:
        n_highest = args.n
    if args.N:
        n_labels = args.N
    if args.subtitle:
        subtitle = args.subtitle
    if args.manual_peak:
        manual_peak_df = mcpyut.manual_peaks_sepparation(args.manual_peak)
    if args.label1:
        label1 = args.label1
    if args.label2:
        label2 = args.label2
    if args.msplot:
        msmcpy.msplot(input_path, resolution_thrs, n_highest,
                      n_labels, subtitle, manual_peak_df, label1, label2)
    if args.flem:
        df = spcmcpy.file_extract(input_path)
        if args.baseline == 'simple':
            df = spcmcpy.mean_baseline(df)
        spcmcpy.spc_plot(df, input_path, title)

    if args.dailypubmed or args.pubmed or args.springer:
        for n in [args.pubmed, args.dailypubmed, args.springer]:
            if n:
                if len(n) == 1:
                    n.append(year_1)
                    n.append(year_2)
                if len(n) == 2:
                    n.append(year_2)
                if args.output:
                    n.append(output_path)
                else:
                    n.append(None)
                if args.pubmed:
                    pubdf = dbanmcpy.pubmedfetcher(n[0], int(n[1]), int(n[2]), save_path=n[3])
                elif args.dailypubmed:
                    pubdf = dbanmcpy.big_pubmedfetcher(n[0], int(n[1]), int(n[2]), save_path=n[3])
                else:
                    pubdf = dbanmcpy.fetch_springer(n[0], int(n[1]), int(n[2]), save_path=n[3])

    return ()


if __name__ == "__main__":
    main()

# TODO

# Remove the necessity on parsing the mzmlpath file path to the main
# mass spectra function

# Add title variable as parameter to msplot function

# Plot multiple spectrophotometry spectras together

# Spectrophotometry plot baseline

# Make a type variable for using as functions parameter, for knowing which
# kind of plot/analysis is being made (like fl em or uv vis), this way
# permmiting to use only one function for more then one technique
