import materials_chempy.database_analysis.dban_functions as dban
def main():
    tstdf = dban.pubmedfetcher('Singlet Oxygen', 2017, 2017, save_path='/home/eduardotc')
    print(tstdf)
    tst = dban.clean_df(tstdf)
    # csv_test = dban.read_pubmed_csv('/home/eduardotc/Documents/Plasmonic_pubmed.csv')
    # csv_stat = csv_test.groupby(csv_test['date'].dt.year)['articles'].agg(['sum', 'mean', 'max'])
    # print(csv_stat)
    print(tst)
    # ttt = dban.csv_statistics('/home/eduardotc/Programação/my_gits/materials_chempy/example_data/Upconversion_pubmed.csv')
    # print(ttt)
if __name__ == "__main__":
    main()
