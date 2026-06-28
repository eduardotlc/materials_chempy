import materials_chempy.utils as mcpyut
import pandas as pd
import materials_chempy.database_analysis.dban_functions as dbanmcpy
import os

def gen_args(args):
    """

    Parameters
    ----------
    args : argparse.Namespace
        argparse aroguments

    Returns
    -------
    input_path : str or None

    output_path : str or None
    """
    input_path = None
    output_path = None
    if args.help:
        mcpyut.client_help()
    if args.mplcfg:
        mcpyut.matplotlib_config()
    if args.input:
        input_path = args.input
    if args.output:
        output_path = args.output
    return input_path, output_path


def ms_args(args):
    """

    Parameters
    ----------
    args : argparse.Namespac
        argparse arguments

    Returns
    -------
    resolution_thrs : float, default 0.3
        minimum m/z difference between two plotted peaks

    n_highest : int, default 15
        Number of peaks to be plotted, based on intensity

    n_labels : int, default 5
       Number of most intense peaks to be labeled with m/z

    manual_peak_df : DataFrame
        labeling argument in form m/z1 label1 m/z2 label2

    label1 : str, default 'Ion Trap ESI-MS'
        Top right box first annotation

    label2 : strm, default 'Direct injection'
        Top right box second annotation
    """
    resolution_thrs = 0.3
    n_highest = 15
    n_labels = 5
    manual_peak_df = pd.DataFrame({})
    label1 = 'Ion Trap ESI-MS'
    label2 = 'Direct injection'
    if args.resolution:
        resolution_thrs = args.resolution
    if args.n:
        n_highest = args.n
    if args.N:
        n_labels = args.N
    if args.manual_peak:
        manual_peak_df = mcpyut.manual_peaks_sepparation(args.manual_peak)
    if args.label1:
        label1 = args.label1
    if args.label2:
        label2 = args.label2
    return resolution_thrs, n_highest, n_labels, manual_peak_df, label1, label2


def mpl_args(args):
    """

    Parameters
    ----------
    args : argparse.Namespace
        argparse arguments

    Returns
    -------
    subtitle : str
        Define the plot subtitle

    title : str
        Define the plot title
    """
    title = None
    subtitle = "default"
    if args.title:
        title = args.title
    if args.subtitle:
        subtitle = args.subtitle
    return title, subtitle


def dban_args(args, output_path):
    """
    Parameters
    ----------
    args : argparse.Namespace
        argparse arguments

    output_path : str
        String of the path to save a csv queryied

    Returns
    -------
    pubdf : DataFrame
        Pandas dataframe with number of published articles per date columns
    """
    year_1 = 1996
    year_2 = 2023
    pubdf = None
    if args.dailypubmed or args.pubmed or args.springer or args.scopus:
        for n in [args.pubmed, args.dailypubmed, args.springer, args.scopus]:
            if n:
                if len(n) == 1:
                    keyword = n[0]
                if len(n) == 2:
                    keyword = n[0]
                    output_path = n[1]
                elif len(n) == 3:
                    keyword = n[0]
                    year_1 = int(n[1])
                    year_2 = int(n[2])
                elif len(n) == 4:
                    keyword = n[0]
                    year_1 = int(n[1])
                    year_2 = int(n[2])
                    output_path = n[3]
                if args.pubmed:
                    pubdf = dbanmcpy.pubmedfetcher(keyword, year_1, year_2,
                                                   save_path=output_path)
                elif args.dailypubmed:
                    pubdf = dbanmcpy.big_pubmedfetcher(keyword, year_1,
                                                       year_2,
                                                       save_path=output_path)
                elif args.springer:
                    pubdf = dbanmcpy.fetch_springer(keyword, year_1, year_2,
                                                    save_path=output_path)
                elif args.scopus:
                    pubdf = dbanmcpy.scopusfetcher(keyword, year_1, year_2,
                                                   save_path=output_path)
    return pubdf, output_path


def barplot_args(input_path, output_path, title, pubdf, args):
    if args.barplot:
        if len(args.barplot) == 1:
            if args.barplot[0].lower().endswith('.csv'):
                pubdf = pd.read_csv(args.barplot, index_col=0)
                pubdf = dbanmcpy.df_statistics(pubdf)
        elif len(args.barplot) == 2:
            if args.barplot[0].lower().endswith('.csv'):
                pubdf = pd.read_csv(args.barplot[0], index_col=0)
                pubdf = dbanmcpy.df_statistics(pubdf)
                output_path = args.barplot[1]
        dbanmcpy.bar_plot_df(save_path=output_path, df=pubdf,
                             title=title)
    return pubdf


def inbarplot_args(pubdf, output_path, title, args):
    if args.inbarplot:
        pubdf = dbanmcpy.df_statistics(pubdf)
        dbanmcpy.bar_plot_df(save_path=output_path, df=pubdf,
                             title=title)


