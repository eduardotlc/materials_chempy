import matplotlib.pyplot as plt
import numpy as np
import materials_chempy.database_analysis.dban_functions as mcpydban
import materials_chempy.utils as mcpyut
import pandas as pd

mcpyut.matplotlib_config()
df = pd.read_csv('MOF_pubmed.csv')
df = mcpydban.df_statistics(df)
mcpydban.bar_plot_df(df, save_path=None, title='MOF')
