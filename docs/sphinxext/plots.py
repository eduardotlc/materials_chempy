import materials_chempy.utils as mcpyut
import materials_chempy.database_analysis.dban_functions as mcpydban
import materials_chempy.cli as mcpycli
import metapub


def pubmed_barplot_pdt():
    """

    Bar plot a fetched pubmed number of articles per year, with the
    keyword 'PDT'
    """
    mcpyut.matplotlib_config()
    dfbarpubmed = mcpydban.pubmedfetcher('PDT', 2008, 2023, save_path=None)
    dfbarpubmed = mcpydban.df_statistics(dfbarpubmed)
    mcpydban.bar_plot_df(dfbarpubmed, save_path=None, title='PDT')


def main():
    pubmed_barplot_pdt()


if __name__ == '__main__':
    main()
