import argparse
import materials_chempy.mass_spectrometry.ms_functions as msmcpy
import materials_chempy.spectrophotometry.spec_functions as spcmcpy
import materials_chempy.cli_utils as mcpycliut


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
    parser.add_argument("--barplot", nargs="+")
    parser.add_argument("--inbarplot", action="store_true")
    return parser


def main():
    """

    Materials chempy package main fucntion, parsing specific submodule
    functions by user parsed flags.

    Parameters
    ----------
        None

    Returns
    -------
        None

    """
    parser = add_arguments()
    args = parser.parse_args()
    input_path, output_path = mcpycliut.gen_args(args)
    title, subtitle = mcpycliut.mpl_args(args)
    resolution_thrs, n_highest, n_labels, manual_peak_df, label1, label2 = \
        mcpycliut.ms_args(args)
    pubdf, output_path = mcpycliut.dban_args(args, output_path)
    mcpycliut.barplot_args(input_path, output_path, title, pubdf, args)
    mcpycliut.inbarplot_args(pubdf, output_path, title, args)
    if args.msplot:
        msmcpy.msplot(input_path, resolution_thrs, n_highest,
                      n_labels, subtitle, manual_peak_df, label1, label2)
    if args.flem:
        df = spcmcpy.file_extract(input_path)
        if args.baseline == 'simple':
            df = spcmcpy.mean_baseline(df)
        spcmcpy.spc_plot(df, input_path, title)
    # mcpycliut.inbarplot_args(pubdf, output_path, title, args)

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
