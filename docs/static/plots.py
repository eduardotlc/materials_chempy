import materials_chempy.utils as mcpyut
import materials_chempy.database_analysis.dban_functions as mcpydban
import materials_chempy.cli as mcpycli
import metapub
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


.. plot::

   import matplotlib.pyplot as plt
   plt.plot([1, 2, 3], [4, 5, 6])
   plt.title("A plotting exammple")


.. plot:: static/plots.py
   mpl_test()
   :include-source:


.. plot:: static/plots.py
   pubmed_barplot_pdt()
   :include-source:
def pubmed_barplot_pdt():
    """

    Bar plot a fetched pubmed number of articles per year, with the
    keyword 'PDT'
    """
    mcpyut.matplotlib_config()
    dfbarpubmed = mcpydban.pubmedfetcher('PDT', 2008, 2023, save_path=None)
    dfbarpubmed = mcpydban.df_statistics(dfbarpubmed)
    mcpydban.bar_plot_df(dfbarpubmed, save_path=None, title='PDT')


# def  test_df():
    # testdf = pd.read_csv('/home/eduardotc/Programação/my_gits/materials_chempy/example_data/MOF_pubmed.csv', index_col=0)
    # testdf = mcpydban.df_statistics(testdf)
    # testdf = testdf.data.iris()
    # testdf.head()

def mpl_test():
    x = np.random.randn(1000)
    plt.hist( x, 20)
    plt.grid()
    plt.title(r'Normal: $\mu=%.2f, \sigma=%.2f$'%(x.mean(), x.std()))
    plt.show()
# def main():
    # # pubmed_barplot_pdt()
    # mpl_test()


# if __name__ == '__main__':
    # main()
