from metapub import PubMedFetcher
from time import sleep
import numpy as np
import pandas as pd
from pybliometrics.scopus import ScopusSearch
import matplotlib.pyplot as plt
import httpx


def pubmedfetcher(keyword, year_1, year_2, save_path):
    """

    Queryes from the PubMed database the number of articles containing a
    specific keyword, in an specified year range, returning a pandas dataframe
    and saving the results to a csv if save_path argument is given.

    Parameters
    ----------
    keyword : str
        Keyword to search articles tha contains it.
        Required.

    year_1 : int
        Starting year to search for articles. Remember that pubmed was created
        in january 1996.
        Required.

    year_2 : int
        Ending year to search for articles.
        Required.

    save_path : str
        Path to save the dataframe into a csv file.
        Optional.

    Returns
    -------
    pubmed_df : DataFrame
        Pandas dataframe with every selected year months in a column named
        "date", and the corresponding number of published articles in that
        month containing the given keyword in other column named "articles".

    Examples
    --------
    Getting the articles published in 2010 and 2011 containing the keyword

    >>> test = pubmedfetcher('Plasmonic', 2010, 2011, None)
    2010-1:  2
    ...
    ...
    2011-12:  4
    >>> print(test)
        Month  Year  Articles
    0       1  2010         2
    1       2  2010         2
    ...
    ...
    22     11  2011         0
    23     12  2011         4

    """

    # Defining optional argument save_path

    # Fetching the PubMed database
    fetch = PubMedFetcher()

    # Creating empty pandas dataframe with 'date' and 'articles' columns
    pubmed_df = pd.DataFrame({"Date": [], "Articles": []})

    # Creating a list containing the number correspondant to every year month
    month_list = np.arange(1, 13, 1)

    # Creating a pandas dataframe with every month number in one column, named
    # 'month', and in the other column 'ends', the corresponding months ending
    # day
    months_days = pd.DataFrame(
        {"month": month_list, "ends": [31, 28, 31, 30, 31, 30, 31, 31, 30, 31,
                                       30, 31]}
    )

    # Creating a list for with every year in the given range
    year_list = np.arange(year_1, year_2 + 1, 1)

    # Looping for every month in every year
    for year in year_list:
        for month in months_days["month"]:
            # Creating a variable to store the current loop month ending day
            endsin = [(months_days.loc[months_days["month"] == month, "ends"])
                      [month - 1]]

            # Fetching all articles containing the given keyword, in the date
            # ranging from the first day (1) of the current loop month, to the
            # above defined current loop month last day
            pmids = fetch.pmids_for_query(
                f"{keyword} "
                + str(year)
                + f"/{month}/1[MDAT] : "
                + str(year)
                + f"/{month}/{endsin}[MDAT]",
                retmax=100000000,
            )
            # Appending to the result dataframe, in the first available row
            # (given by the dataframe length), the current loop date in the
            # format year-month, and the number of published articles in this
            # month, given by the above articles fetch length
            pubmed_df.loc[len(pubmed_df)] = [f"{year}-{month}", len(pmids)]

            # Printing for tracking the current loop date, in the year-month
            # format, and the number of articles containing the given keyword
            # found in the Scoupus database with corresponding year-month
            # publication date
            print(f"{year}-{month}: ", len(pmids))

            # Sleeping for avoiding to many/simultaneous API requests, if any
            # error is presented during this function execution, this sleeping
            # time may be enlarged
            sleep(0.1)

    # Converting the result dataframe 'date' column to pandas date format
    # pd.to_datetime(pubmed_df.Date, format="%Y-%m")
    pubmed_df['Date'] = pd.to_datetime(pubmed_df.Date.astype(str),
                                       format="%Y-%m")
    pubmed_df['Year'] = pubmed_df['Date'].dt.year
    pubmed_df['Month'] = pubmed_df['Date'].dt.month
    pubmed_df = pubmed_df.drop(['Date'], axis=1)
    pubmed_df = pubmed_df[['Month', 'Year', 'Articles']]
    # If optional argument save_path is given, the bellow saving loop is
    # executed
    if save_path:
        pathcsv = f"{save_path}/{keyword}_pubmed.csv"
        pubmed_df.to_csv(path_or_buf=pathcsv)

    return pubmed_df


def big_pubmedfetcher(keyword, year_1, year_2, save_path):
    """

    The same as above pubmedfethcer function, but this functions make the
    number of articles to be fetched per day in the given data range. Usefull
    if the month fetching aproach is trespassing the free api limit of 9999
    api calls per command.

    Parameters
    ----------
    keyword : str
        String with the kewyord argument, that will be used to fetch the pubmed
        data containing this keyword in the given year range

    year_1 : int
        Starting year to search for articles. Remember that pubmed was created
        in january 1996.
        Required.

    year_2 : int
        Ending year to search for articles.
        Required.

    save_path : str
        Path to save the dataframe into a csv file.
        Optional.

    Returns
    -------
    pubmed_df : DataFrame
        Pandas dataframe with every selected year months in a column named
        'date', and the corresponding number of published articles in that
        day, containing the given keyword in other column named 'articles'

    Examples
    --------
    Fetching and printing, day by day, the number of articles in the
    PubMed database, presenting the 'xrd' keyword, in the year of 2012
    >>> test_daily = big_pubmedfetcher('xrd', 2012, 2012, None)
    2012-1-1:  0
    2012-1-2:  2
    2012-1-3:  1
    2012-1-4:  0
    ...
    2012-12-26:  4
    2012-12-27:  0
    2012-12-28:  0
    2012-12-29:  0
    2012-12-30:  0
    2012-12-31:  0
    """
    # Fetching the PubMed database
    fetch = PubMedFetcher()

    # Creating empty pandas dataframe with 'date' and 'articles' columns
    pubmed_df = pd.DataFrame({"Date": [], "Articles": []})

    # Creating a list containing the number correspondant to every year month
    month_list = np.arange(1, 13, 1)

    # Creating a pandas dataframe with every month number in one column, named
    # 'month', and in the other column 'ends', the corresponding months ending
    # day
    months_days = pd.DataFrame({"month": month_list,
                                "ends": [31, 28, 31, 30, 31, 30, 31, 31, 30,
                                         31, 30, 31]})

    # Creating a list for with every year in the given range
    year_list = np.arange(year_1, year_2 + 1, 1)

    # Looping for every month in every year
    for year in year_list:
        for month in months_days['month']:
            sleep(1)
            # Creating a variable to store the current loop month ending day
            endsin = (
                (months_days.loc[months_days["month"] == month, "ends"]
                 )[month - 1])
            days_list = np.arange(1, endsin + 1, 1)
            # Fetching all articles containing the given keyword, in the date
            # ranging from the first day (1) of the current loop month, to the
            # above defined current loop month last day
            for days in days_list:
                pmids = fetch.pmids_for_query(
                    f"{keyword} " + str(year) + f"/{month}/{days}[MDAT]",
                    retmax=100000000,
                )
                # Appending to the result dataframe, in the first available row
                # (given by the dataframe length), the current loop date in the
                # format year-month, and the number of published articles in
                # month, given by the above articles fetch length
                pubmed_df.loc[len(pubmed_df)] = [f"{year}-{month}-{days}",
                                                 len(pmids)]

            # Printing for tracking the current loop date, in the
            # year-month format, and the number of articles containing
            # the given keyword found in the Scoupus database with
            # corresponding year-month publication date
                print(f"{year}-{month}-{days}: ", len(pmids))

            # Sleeping for avoiding to many/simultaneous API requests, if
            # any error is presented during this function execution, this
            # sleeping time may be enlarged
                sleep(0.1)

    # Converting the result dataframe 'date' column to pandas date format
    pubmed_df['Date'] = pd.to_datetime(pubmed_df.Date.astype(str),
                                       format="%Y-%m-%d")
    pubmed_df['Year'] = pubmed_df['Date'].dt.year
    pubmed_df['Month'] = pubmed_df['Date'].dt.month
    pubmed_df = [pubmed_df.groupby(['Month', 'Year']).agg
                 ({'Articles': 'sum'}).reset_index()]
    # If optional argument save_path is given, the bellow saving loop is
    # executed
    if save_path:
        pathcsv = f"{save_path}/{keyword}_daily_pubmed.csv"
        pubmed_df.to_csv(path_or_buf=pathcsv)

    return pubmed_df


def scopusfetcher(keyword, year_1, year_2, save_path):
    """

    Queryes from the Scopus database the number of articles containing a
    specific keyword, in an specified year range, returning a pandas dataframe
    with one column named 'date' containing the year month in format year-month
    and one column named 'articles', with the number of published articles
    containing the given keyword in that corresponding month.If the argument
    csv_path is given, the function saves the results to a csv file.

    Parameters
    ----------
    keyword : str
        Keyword to search articles tha contains it.
        Required.

    year_1 : int
        Starting year to search for articles. Remember that pubmed was created
        in january 1996.
        Required.

    year_2 : int
        Ending year to search for articles.
        Required.

    save_path : str
        Path to save the dataframe into a csv file.
        Optional.

    Returns
    -------
    scopus_df : DataFrame
        Pandas dataframe with every selected year months in a column named
        "date", and the corresponding number of published articles in that
        month containing the given keyword in other column named "articles".

    Examples
    --------
    Printing number of articles in scopus database containing the keyword
    laser, in each month, from the year 2017 to 2019
    >>> test_scopus = scopusfetcher('laser', 2017, 2019, save_path=None)
    2017-january:  3161
    2017-february:  2321
    ...
    2019-november:  3391
    2019-december:  4353
    """

    # Defining optional argument save_path

    # Creating a list with every month in the year
    months_list = [
        "january",
        "february",
        "march",
        "april",
        "june",
        "july",
        "august",
        "september",
        "october",
        "november",
        "december",
    ]

    # Creating an empty dataframe with one column named 'date' and one column
    # named 'articles'
    scopus_df = pd.DataFrame({"Date": [], "Articles": []})

    # Creating a list containing every year in the given range
    years_list = np.arange(year_1, year_2 + 1, 1)

    # Looping for every month in every year
    for year in years_list:
        for month in months_list:
            # Searching articles containing the given keyword, in the specific
            # month and year, in the scopus database. subscriber=False refers
            # to be using a free API key.
            s = ScopusSearch(
                f"KEY {keyword}, PUBDATETXT({month} {year})", subscriber=False
            )

            # Prints the year-month and number of published articles (size of
            # the search result)
            print(f"{year}-{month}: ", s.get_results_size())

            # Appending to previously created empty list, always in the first
            # available row (given by the length of the list), the date in the
            # format year-month of current loop, and the number of published
            # articles containing the keyword in this month
            scopus_df.loc[len(scopus_df)] = [f"{year}-{month}",
                                             s.get_results_size()]

            # Some errors have being ocurring while querying the database, to
            # try to minimize it, i setted a relatvielly large sleep time, may
            # be lowered to test your specific case results.
            sleep(1)

    # Converting the 'date' column to pandas datetime format
    scopus_df["Date"] = pd.to_datetime(scopus_df.Date.astype(str),
                                       format="%Y-%B")
    scopus_df['Year'] = scopus_df['Date'].dt.year
    scopus_df['Month'] = scopus_df['Date'].dt.month
    scopus_df = scopus_df.drop(columns=['Date'])
    scopus_df = scopus_df[['Month', 'Year', 'Articles']]
    # If optional argument save_path is given, the saving loop bellow is
    # executed
    if save_path:
        pathcsv = f"{save_path}/{keyword}_scopus.csv"
        scopus_df.to_csv(path_or_buf=pathcsv)

    return scopus_df


def df_statistics(df):
    """

    Given a dataframe with one column 'Year' and one column 'Articles', makes
    basic statistics of the 'Articles' numbers column, returning a dataframe
    with the sum per year of 'Articles' value, their mean, an their max.

    Parameters
    ----------
    df : DataFrame
        Pandas DataFrame, with one column named 'Year', in datetime format,
        and one Articles column, with integer values correlating to
        the date column.

    Returns
    -------
    df_stat : DataFrame
        Pandas dataframe with the results, one column named 'sum', one named
        'mean' and one named 'max', all the columns refers to the values
        calculated from the original dataframe 'date' column values.

    Examples
    --------
    Defining an example dataframe, formated similar to articles databases
    functions present in this file.

    >>> x = ['2015-01-01', '2015-02-01', '2015-03-01', '2015-04-01',
    ...      '2015-06-01', '2015-07-01', '2015-08-01', '2015-09-01',
    ...      '2015-10-01', '2015-11-01', '2015-12-01']
    >>> y = [136, 126, 122, 135, 154, 178, 187, 149, 125, 120, 120]
    >>> df_test = pd.DataFrame({'Date': x,
    ...                         'Articles': y})
    >>> df_test["Date"] = pd.to_datetime(df_test.Date.astype(str),
    ...                                  format="%Y-%m-%d")
    >>> df_test['Year'] = df_test['Date'].dt.year
    >>> df_test['Month'] = df_test['Date'].dt.month
    >>> df_test = df_test.drop(columns=['Date'])
    >>> df_test = df_test[['Month', 'Year', 'Articles']]
    >>> stat_test_df = df_statistics(df_test)
    >>> print(stat_test_df)
       Year   sum        mean  max
    0  2015  1552  141.090909  187
    """
    if type(df['Year'][0]) == str:
        df['Year'] = pd.to_datetime(df.Year.astype(str),
                                    format="%Y")
        df['Year'] = df['Year'].dt.year
    df_stat = df.groupby(df["Year"])["Articles"].agg(
        ["sum", "mean", "max"]
    )
    df_stat.reset_index(inplace=True)
    return df_stat


def bar_plot_df(df, save_path, title):
    """

    Creates a bar plot from a pandas DataFrame or saved csv, being obrigatory
    to give one of these two parameters.

    Parameters
    ----------
    df : DataFrame
        Dataframe to be plotted

    csv_path : str
        Path to csv file to be readed and plotted
        Optional

    save_path : str
        Path to save the plot image
        Optional

    time_grouping : str
        String to inform desired grouping of the date axis, accepts the values:
        'year', 'month'.
        Optional

    title : str
        Title of the plot, in case of plotting a dataframe, it should be given,
        while if plotting a csv, the title defaults to be extracted from the
        file name if not given
        Optional

    """
    fig, ax = plt.subplots(dpi=100)
    plt.xlabel("Year", fontsize=14)
    plt.ylabel("Published Articles", fontsize=14)
    plt.xlim(df.Year.min() - 1, df.Year.max() + 1)
    if title:
        ax.set_title(title, fontsize=18)
    else:
        title = 'Database'
    ax.bar(df['Year'], df["sum"], label=df["sum"])
    for index, value in enumerate(df['sum']):
        plt.text(df['Year'][index], value + 0.15, str(value), ha='center',
                 va='bottom', fontsize=8)
    plt.xticks(df.Year[df.index % 2 == 0], fontsize=10)
    # ytickstmp = (np.arange(df['sum'].min, df['sum'].max, 6)
    plt.yticks(fontsize=10)
    if save_path:
        plt.savefig(f"{save_path}/{title}.png")
    plt.show()


def fetch_springer(keyword, year_1, year_2, save_path):
    """

    Fetches number of specific keyword containing articles, published
    in each year from a range.

    Parameters
    ----------
    keyword : str
        keyword that the fetched articles have to present

    year_1 : int
        First year to search the database for

    year_2 : int
        Last year to search the database for

    save_path : str
        Path to save the results to a csv.
        Optional

    Returns
    -------
    df : DataFrame
        Results dataframe, with one column containing each year, and the other
        column containing the number of published articles that contains
        the keyword

    Examples
    --------
    >>> springer_test = fetch_springer('Plasmonic', 2010, 2022, save_path=None)
    2010:  536
    2011:  845
    ...
    ...
    2021:  4059
    2022:  4723
    >>> print(springer_test)
        Year  Articles
    0   2010       536
    1   2011       845
    ...
    ...
    11  2021      4059
    12  2022      4723
    """
    springer_api_key = "56580f5684a4934af904f1edf8f07706"
    base_url_springer = 'http://api.springer.com/metadata/json'
    date_list = np.arange(year_1, year_2 + 1, 1)
    url_params_springer = {}
    url_params_springer["api_key"] = springer_api_key
    url_params_springer["p"] = 200
    springer_df = pd.DataFrame({'Year': [],
                                'Articles': []})

    with httpx.Client(params=url_params_springer) as client:
        for date_int in date_list:
            springer_keyword = ("?q=(" + "%22" + keyword.replace(" ", "%20") +
                                "%22" + "%20AND%20year:" + str(date_int) + ")")

    # Building the Springer Metadata API parameters dictionary
            d_springer = client.get(base_url_springer + springer_keyword)
            d_springer = d_springer.json()
            articles = pd.DataFrame([d_springer])
            articles = articles.result
            articles = articles[0]
            articles = pd.DataFrame(articles)
            articles = int(articles.total[0])
            print(f'{date_int}:  {articles}')
            springer_df.loc[len(springer_df)] = [date_int, articles]

    springer_df['Year'] = pd.to_datetime(springer_df.Year.astype(str),
                                         format="%Y")
    springer_df['Year'] = springer_df['Year'].dt.year
    if save_path:
        pathcsv = f"{save_path}/{keyword}_springer.csv"
        springer_df.to_csv(path_or_buf=pathcsv)

    return springer_df

# TODO:
# - Adds table with arguments and functioning of client to the
# documentation
# - Separate docstrings doctests in high time required tests, using them only
# in complete tests, and other functions for more usual tests.
