from metapub import PubMedFetcher
from time import sleep
import numpy as np
import pandas as pd
fetch = PubMedFetcher()
keyword = 'singlet oxygen'
save_path = f'/home/eduardotc/Programação/csv/{keyword}_pubmed_tmp.csv'
ystart = 2005
yend = 2023
df = pd.DataFrame({'date': [],
       'articles': []})
month_list = np.arange(1, 13, 1)
months_days = pd.DataFrame({'month': month_list,
                            'ends': [31, 28, 31, 30, 31, 30, 31, 31, 30, 31,
                                     30, 31]})
year_list = np.arange(ystart, yend+1, 1)
for year in year_list:
    for month in months_days['month']:
        endsin = (months_days.loc[months_days['month'] == month, 'ends'])[month-1]
        pmids = fetch.pmids_for_query(f'{keyword} '+str(year)+f'/{month}/01[MDAT] : '+str(year)+f'/{month}/{endsin}[MDAT]',retmax=100000000)
        df.loc[len(df)] = [f'{year}-{month}', len(pmids)]
        print(f"{year}-{month}: ", len(pmids))
        sleep(0.5)
pd.to_datetime(df.date, format="%Y-%m")
df
save_inp = str(input("Should save the dataframe to a csv? (y/n) "))
if save_inp == 'y':
    df.to_csv(path_or_buf=save_path)
