from metapub import PubMedFetcher
from time import sleep
import numpy as np
import pandas as pd
from pybliometrics.scopus import ScopusSearch
import matplotlib.pyplot as plt
import re
import requests
import pytest


def pubmedfetcher(keyword, year_1, year_2, **kwargs):
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
    pubmed_df : pandas.DataFrame
        Pandas dataframe with every selected year months in a column named
        "date", and the corresponding number of published articles in that
        month containing the given keyword in other column named "articles".

    Examples
    --------
    Getting the articles published in 2010 and 2011 containing the keyword

    >>> test = pubmedfetcher('Plasmonic', 2010, 2011)
    2010-1:  29
    2010-2:  35
    2010-3:  53
    2010-4:  80
    2010-5:  54
    2010-6:  37
    2010-7:  46
    2010-8:  29
    2010-9:  55
    2010-10:  20
    2010-11:  83
    2010-12:  39
    2011-1:  55
    2011-2:  32
    2011-3:  74
    2011-4:  56
    2011-5:  51
    2011-6:  82
    2011-7:  37
    2011-8:  94
    2011-9:  53
    2011-10:  49
    2011-11:  115
    2011-12:  40
    >>> print(test)
           date  articles
    0    2010-1        29
    1    2010-2        35
    2    2010-3        53
    3    2010-4        80
    4    2010-5        54
    5    2010-6        37
    6    2010-7        46
    7    2010-8        29
    8    2010-9        55
    9   2010-10        20
    10  2010-11        83
    11  2010-12        39
    12   2011-1        55
    13   2011-2        32
    14   2011-3        74
    15   2011-4        56
    16   2011-5        51
    17   2011-6        82
    18   2011-7        37
    19   2011-8        94
    20   2011-9        53
    21  2011-10        49
    22  2011-11       115
    23  2011-12        40

    """

    # Defining optional argument save_path
    save_path = kwargs.get("save_path", None)

    # Fetching the PubMed database
    fetch = PubMedFetcher()

    # Creating empty pandas dataframe with 'date' and 'articles' columns
    pubmed_df = pd.DataFrame({"date": [], "articles": []})

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
            endsin = (months_days.loc[months_days["month"] == month, "ends"])[month - 1]

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
    pd.to_datetime(pubmed_df.date, format="%Y-%m")

    # If optional argument save_path is given, the bellow saving loop is
    # executed
    if save_path:
        pathcsv = f"{save_path}/{keyword}_pubmed.csv"
        pubmed_df.to_csv(path_or_buf=pathcsv)

    return pubmed_df


def big_pubmedfetcher(keyword, year_1, year_2, **kwargs):
    """

    The same as above pubmedfethcer function, but this functions make the
    number of articles to be fetched per day in the given data range. Usefull
    if the month fetching aproach is trespassing the free api limit of 9999
    api calls per command.

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
    pubmed_df : pandas.DataFrame
        Pandas dataframe with every selected year months in a column named
        "date", and the corresponding number of published articles in that
         day, containing the given keyword in other column named "articles".

    Examples
    --------

    """

    # Defining optional argument save_path
    save_path = kwargs.get("save_path", None)

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
            sleep(4)
            # Creating a variable to store the current loop month ending day
            endsin = (months_days.loc[months_days["month"] == month, "ends"])[month - 1]
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
    pd.to_datetime(pubmed_df.Date, format="%Y-%m-%d")

    # If optional argument save_path is given, the bellow saving loop is
    # executed
    if save_path:
        pathcsv = f"{save_path}/{keyword}_pubmed.csv"
        pubmed_df.to_csv(path_or_buf=pathcsv)

    return pubmed_df


def read_pubmed_csv(csv_path):
    """

    Read a saved pubmed queryied csv into a pandas DataFrame.

    Parameters
    ----------
    csv_path : str
        Path to the csv file to be readed
        Required

    Returns
    -------
    df : pd.DataFrame
        Pandas Dataframe with a column named 'date' containing the year-month,
        and one column named 'articles' containing the number of published
        articles in that month.

    Examples
    --------
    saving to a csv the number of "Upconversion" keyword containing articles
    in the year of 2015.

    >>> pubmedfetcher('Upconversion', 2015, 2015, save_path='./tmp')
    2015-1:  17
    2015-2:  20
    2015-3:  33
    2015-4:  22
    2015-5:  20
    2015-6:  17
    2015-7:  20
    2015-8:  31
    2015-9:  20
    2015-10:  12
    2015-11:  64
    2015-12:  17
           date  articles
    0    2015-1        17
    1    2015-2        20
    2    2015-3        33
    3    2015-4        22
    4    2015-5        20
    5    2015-6        17
    6    2015-7        20
    7    2015-8        31
    8    2015-9        20
    9   2015-10        12
    10  2015-11        64
    11  2015-12        17
    >>> csv_test = read_pubmed_csv('./tmp/Upconversion_pubmed.csv')
    >>> print(csv_test)
             date  articles
    0  2015-01-01        17
    1  2015-02-01        20
    2  2015-03-01        33
    3  2015-04-01        22
    4  2015-05-01        20
    5  2015-06-01        17
    6  2015-07-01        20
    7  2015-08-01        31
    8  2015-09-01        20
    9  2015-10-01        12
    10 2015-11-01        64
    11 2015-12-01        17

    """
    # Reading the csv file with pandas, stating that the file first column
    # corresponds to the index values (row number)
    df = pd.read_csv(csv_path, index_col=0)

    # Converting 'date' column to pandas date format
    df["date"] = pd.to_datetime(df.date, format="%Y-%m")

    return df


def csv_statistics(csv_path):
    """

    Reads a saved csv, making a per year statistic of sum, mean and max of
    published articles per month.

    Parameters
    ----------
    csv_path : str
        Path to the csv file, in the format first row containing the columns
        names 'date' and 'articles', and the sequent rows containing the row
        number, the year-month relted to this row and the number of publised
        articles in the month.
        Required.

    Returns
    -------
    csv_stat : pd.DataFrame
        Pandas dataframe with one column named 'date' containing the years, one
        column named sum corresponding to the sum of all the months articles in
        that year, one column named mean containing the 'mean' of published
        articles per month,and one column named 'max, with the number of
        published articles in the month with the highest value.

    Examples
    --------
    Printing the yearly statistic from the previous function saved csv.
    >>> csvpytest = csv_statistics('../example_data/Upconversion_pubmed.csv')
    >>> print(csvpytest)
          sum       mean  max
    date \t \t ...
    2015  293  24.416667   64

    """
    # Reading in a pandas dataframe the csv
    csv_stat = read_pubmed_csv(csv_path)

    # Getting the date column sum, mean and max
    csv_stat = csv_stat.groupby(csv_stat["date"].dt.year)["articles"].agg(
        ["sum", "mean", "max"]
    )

    return csv_stat


def scopusfetcher(keyword, year_1, year_2, **kwargs):
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
    scopus_df : pandas.DataFrame
        Pandas dataframe with every selected year months in a column named
        "date", and the corresponding number of published articles in that
        month containing the given keyword in other column named "articles".

    Examples
    --------
    Querying, per month, the number of published articles containing the
    keyword 'Upconversion', in the year of 2015, in the Scopus database.

    @pytest.mark.xfail(run=False)
    >>> scopus_df = scopusfetcher('Upconversion', 2015, 2015,
    ...                           save_path='./tmp')
    2015-january:  136
    2015-february:  126
    2015-march:  122
    2015-april:  135
    2015-june:  154
    2015-july:  178
    2015-august:  187
    2015-september:  149
    2015-october:  125
    2015-november:  120
    2015-december:  120
    >>> print(scopus_df)
             date  articles
    0  2015-01-01       136
    1  2015-02-01       126
    2  2015-03-01       122
    3  2015-04-01       135
    4  2015-06-01       154
    5  2015-07-01       178
    6  2015-08-01       187
    7  2015-09-01       149
    8  2015-10-01       125
    9  2015-11-01       120
    10 2015-12-01       120

    """
    # Defining optional argument save_path
    save_path = kwargs.get("save_path", str)

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
    scopus_df = pd.DataFrame({"date": [], "articles": []})

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
            sleep(2)

    # Converting the 'date' column to pandas datetime format
    scopus_df["date"] = pd.to_datetime(scopus_df.date.astype(str),
                                       format="%Y-%B")

    # If optional argument save_path is given, the saving loop bellow is
    # executed
    if save_path:
        pathcsv = f"{save_path}/{keyword}_scopus.csv"
        scopus_df.to_csv(path_or_buf=pathcsv)

    return scopus_df


def df_statistics(df, **kwargs):
    """

    Given a dataframe with 'date' column, in the format year-month, returns
    the sum, the mean and the max of the 'date' column, organized as well in
    a dataframe.

    Paramters
    ---------
    df : pd.DataFrame
        Pandas DataFrame, with one column named 'date', in the year-month
        format, and one column with integer values correlating to the date
        column.

    time_grouping : str
        Time range to group data, may be 'Year' or 'Month'

    Returns
    -------
    df_stat : pd.DataFrame
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
    >>> df_test = pd.DataFrame({'date': x,
    ...                         'articles': y})
    >>> stat_test_df = df_statistics(df_test)
    >>> print(stat_test_df)
           sum        mean  max
    Date ...
    2015  1552  141.090909  187
    """
    time_grouping = kwargs.get("time_grouping", str)
    df_clean = clean_df(df)
    if time_grouping == "month" or time_grouping == "Month":
        time_grouping = "month"
        df_stat = df_clean.groupby(df_clean["Date"].dt.month)["Articles"].agg(
            ["sum", "mean", "max"]
        )
    else:
        time_grouping = "year"
        df_stat = df_clean.groupby(df_clean["Date"].dt.year)["Articles"].agg(
            ["sum", "mean", "max"]
        )
    # df_clean['Date'] = pd.to_datetime(df.date.astype(str), format="%Y-%m-%B")
    return df_stat


def find_matching_positions(string1, string2):
    """

    Find the matching letters between 2 strings, and attribute the positions
    values of the matching cases to a list variable.

    Parameters
    ----------
    string1 : str
        First string to check matching letters

    string2 : str
        Second string to compare matching letters

    Returns
    -------
    matching_postions : list
        List with the positions of matching letters between the 2 strings

    Examples
    --------
    Find the matching letters between the strings 'hello' and 'hallo'

    >>> string1 = "hello"
    >>> string2 = "hallo"
    >>> positions = find_matching_positions(string1, string2)
    >>> print("Matching positions:", positions)
    Matching positions: [0, 2, 3, 4]

    Find the matching letters between '2015-02-01' and '2015-01-01'

    >>> string1 = "2015-02-01"
    >>> string2 = "2015-01-01"
    >>> positions = find_matching_positions(string1, string2)
    >>> print("Matching positions:", positions)
    Matching positions: [0, 1, 2, 3, 4, 5, 7, 8, 9]
    """
    matching_positions = []

    # Make sure both strings are of the same length
    if len(string1) != len(string2):
        raise ValueError("Both strings must have the same length")

    for i in range(len(string1)):
        if string1[i] == string2[i]:
            matching_positions.append(i)

    return matching_positions


def clean_csv(csv_path):
    """

    Reads a csv file, organizing its columns, returning a dataframe with one
    'Date' column (pandas datetime), one 'Year' column (pandas datetime), one
    'Month' column (pandas datetime), and if the csv has an articles column,
    the cleaned dataframe also has a 'Articles' column (integer).

    Parameters
    ----------
    csv_path : str
        Path to the csv file to be cleaned

    Returns
    -------
    df_clean : Pandas.DataFrame
        Pandas dataframe of cleaned and organized csv

    Examples
    --------
    Clean example_data csv

    >>> test_clean_csv = clean_csv('../example_data/Upconversion_pubmed.csv')
    >>> print(test_clean_csv)
        Year  Month       Date  Articles
    0   2015      1 2015-01-01        17
    1   2015      2 2015-02-01        20
    2   2015      3 2015-03-01        33
    3   2015      4 2015-04-01        22
    4   2015      5 2015-05-01        20
    5   2015      6 2015-06-01        17
    6   2015      7 2015-07-01        20
    7   2015      8 2015-08-01        31
    8   2015      9 2015-09-01        20
    9   2015      1 2015-01-01        12
    10  2015     11 2015-11-01        64
    11  2015     12 2015-12-01        17

    """
    month_new = []
    df = pd.read_csv(csv_path, index_col=0)

    # Creating empty dataframe in case readed csv 'date' column is shorter
    # than 7
    if (len(df.date[0])) < 7:
        df_split = pd.DataFrame({"a": [], "b": []})

    # Creating empty dataframe in case readed csv 'date' column is longer
    # than 7
    else:
        df_split = pd.DataFrame({"a": [], "b": [], "c": []})

    df_clean = pd.DataFrame({"Year": [], "Month": [], "Date": [],
                             "Articles": []})

    # Iterating for every column from inputted dataframe
    for col in df.columns:
        # If input dataframe has a column named 'articles'
        if col == "articles" or col == "Articles":
            df_clean["Articles"] = df["articles"]

        # If input dataframe has a column named 'date'
        if col == "date" or col == "Date":
            # Iterating for every value from the row 'date'
            for values in df.date:
                # Adding each date element to empty dataframe
                df_split.loc[len(df_split)] = values.split("-")

            # Iterating for every column in the new created every
            # date element df
            for cols in df_split.columns:
                # If length from every element from the first row >
                # 4 (correspond (High chances of being a year column)
                if len(df_split[cols][0]) == 4:
                    df_clean["Year"] = df_split[cols]

                # Getting total column values range (max - min)
                col_min = int(df_split[cols].min())
                col_max = int(df_split[cols].max())
                col_diff = col_max - col_min

                # Loop if the column range is between 17 and 4 (high chances of
                # being a month column
                if 17 > col_diff > 4:
                    df_clean["Month"] = df_split[cols]

    # Removing month column trailing zeroes
    for number in df_clean.Month:
        month_new.append(int(str(number).rstrip("0")))

    # Converting year month and date columns to pandas datetime
    df_clean["Year"] = pd.to_datetime(df_clean["Year"])
    df_clean["Year"] = df_clean.Year.dt.year
    df_clean["Month"] = month_new
    df_clean["Month"] = pd.to_datetime(df_clean["Month"], format="%m")
    df_clean["Month"] = df_clean.Month.dt.month
    df_clean["Date"] = pd.to_datetime(df_clean[["Year", "Month"]]
                                      .assign(Day=1))

    return df_clean


def clean_df(df):
    """

    Organize and clean a pandas DataFrame, returning a dataframe with one
    'Date' column (pandas datetime), one 'Year' column (pandas datetime), one
    'Month' column (pandas datetime), and if the csv has an articles column,
    the cleaned dataframe also has a 'Articles' column (integer).

    Parameters
    ----------
    df : pandas.DataFrame
        Pandas Dataframe to be cleaned

    Returns
    -------
    df_clean : pandas.DataFrame
        Cleaned and organized pandas DataFrame

    Examples
    --------
    Clean a fetched pubmed dataframe with the keyword 'Singlet Oxygen' in the
    year of 2017

    >>> test_df = pubmedfetcher('Singlet Oxygen', 2017, 2017)
    2017-1:  10
    2017-2:  20
    2017-3:  29
    2017-4:  8
    2017-5:  9
    2017-6:  8
    2017-7:  2
    2017-8:  11
    2017-9:  11
    2017-10:  16
    2017-11:  128
    2017-12:  27
    >>> test_clean = clean_df(test_df)
    >>> print(test_clean)
        Year  Month       Date  Articles
    0   2017      1 2017-01-01        10
    1   2017      2 2017-02-01        20
    2   2017      3 2017-03-01        29
    3   2017      4 2017-04-01         8
    4   2017      5 2017-05-01         9
    5   2017      6 2017-06-01         8
    6   2017      7 2017-07-01         2
    7   2017      8 2017-08-01        11
    8   2017      9 2017-09-01        11
    9   2017      1 2017-01-01        16
    10  2017     11 2017-11-01       128
    11  2017     12 2017-12-01        27

    """
    month_new = []

    # Creating empty dataframe in case readed csv 'date' column is shorter
    # than 7
    if 'date' in df.columns or 'Date' in df.columns:
        df.rename({"date": "Date"}, axis="columns")
    if (len(df.date[0])) < 7:
        df_split = pd.DataFrame({"a": [], "b": []})

    # Creating empty dataframe in case readed csv 'date' column is longer
    # than 7
    else:
        df_split = pd.DataFrame({"a": [], "b": [], "c": []})

    df_clean = pd.DataFrame({"Year": [], "Month": [], "Date": [],
                             "Articles": []})

    # Iterating for every column from inputted dataframe
    for col in df.columns:
        # If input dataframe has a column named 'articles'
        if col == "articles" or col == "Articles":
            df_clean["Articles"] = df["articles"]

        # If input dataframe has a column named 'date'
        if col == "date" or col == "Date":
            # Iterating for every value from the row 'date'
            for values in df.date:
                # Adding each date element to empty dataframe
                df_split.loc[len(df_split)] = values.split("-")

            # Iterating for every column in the new created every
            # date element df
            for cols in df_split.columns:
                # If length from every element from the first row >
                # 4 (correspond (High chances of being a year column)
                if len(df_split[cols][0]) == 4:
                    df_clean["Year"] = df_split[cols]

                # Getting total column values range (max - min)
                col_min = int(df_split[cols].min())
                col_max = int(df_split[cols].max())
                col_diff = col_max - col_min

                # Loop if the column range is between 17 and 4 (high chances of
                # being a month column
                if 17 > col_diff > 4:
                    df_clean["Month"] = df_split[cols]

    # Removing month column trailing zeroes
    for number in df_clean.Month:
        month_new.append(int(str(number).rstrip("0")))

    # Converting year month and date columns to pandas datetime
    df_clean["Year"] = pd.to_datetime(df_clean["Year"])
    df_clean["Year"] = df_clean.Year.dt.year
    df_clean["Month"] = month_new
    df_clean["Month"] = pd.to_datetime(df_clean["Month"], format="%m")
    df_clean["Month"] = df_clean.Month.dt.month
    df_clean["Date"] = pd.to_datetime(df_clean[["Year", "Month"]]
                                      .assign(Day=1))

    return df_clean


def bar_plot_df(**kwargs):
    """

    Creates a bar plot from a pandas DataFrame or saved csv, being obrigatory
    to give one of these two parameters.

    Parameters
    ----------
    df : pd.DataFrame
        Dataframe to be plotted
        Optional

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

    Returns
    -------

    Examples
    --------

    """
    dirty_list = [
        "pubmed",
        "PubMed",
        "Scopus",
        "scopus",
        "DataBase" "database",
        "Database",
        "csv",
    ]
    df = kwargs.get("df", pd.DataFrame)
    csv_path = kwargs.get("csv_path", str)
    save_path = kwargs.get("save_path", str)
    time_grouping = kwargs.get("time_grouping", str)
    title = kwargs.get("title", str)

    fig, ax = plt.subplots(figsize=(12, 4), dpi=400)
    if time_grouping:
        plt.xlabel(time_grouping)
    else:
        plt.xlabel("Year")
        time_grouping = "Year"
    plt.ylabel("Published Articles")
    if csv_path:
        dfclean = clean_csv(csv_path)
        title_tmp = re.split(r"_|\.|-", csv_path)
        for n in title_tmp:
            for j in dirty_list:
                if n == j:
                    title_tmp.remove(n)
    elif df:
        dfclean = clean_df(df)
    elif not df and not csv_path:
        raise Exception(
            "a pandas dataframe or path to csv file has to be\
                         inputted."
        )
    dfstat = df_statistics(dfclean, time_grouping=time_grouping)
    # plt.xlim(dfclean.Year.min - 1, dfclean.Year.max + 1)

    if title:
        ax.set_title(title)
    elif title_tmp:
        ax.set_title(title_tmp)
    else:
        raise Exception(
            "When given a dataframe, \
        --title argument is obrigatory"
        )
    # dfstat = df_statistics(dfclean, time_grouping=time_grouping)
    ax.bar(dfstat.index.values, dfstat["sum"], label=dfstat["sum"])
    if save_path:
        plt.savefig(f"{save_path}/{title}.png")
    plt.show()


def fetch_springer(keyword, year_1, year_2, **kwargs):
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
    df : pd.DataFrame
        Results dataframe, with one column containing each year, and the other
        column containing the number of published articles that contains
        the keyword

    Example
    -------
    >>> springer_test = fetch_springer('Plasmonic', 2010, 2022)
    2010:  536
    2011:  845
    2012:  1323
    2013:  2347
    2014:  2530
    2015:  2964
    2016:  3155
    2017:  3300
    2018:  3301
    2019:  3383
    2020:  3744
    2021:  4059
    2022:  4722
    >>> print(springer_test)
        Year  Articles
    0   2010       536
    1   2011       845
    2   2012      1323
    3   2013      2347
    4   2014      2530
    5   2015      2964
    6   2016      3155
    7   2017      3300
    8   2018      3301
    9   2019      3383
    10  2020      3744
    11  2021      4059
    12  2022      4722
    """
    save_path = kwargs.get('save_path', None)
    springer_api_key = "56580f5684a4934af904f1edf8f07706"
    base_url_springer = 'http://api.springer.com/metadata/json'
    date_list = np.arange(year_1, year_2 + 1, 1)
    url_params_springer = {}
    url_params_springer["api_key"] = springer_api_key
    url_params_springer["p"] = 200
    df = pd.DataFrame({'Year': [],
                       'Articles': []})
    for date_int in date_list:
        springer_keyword = "?q=("+ "%22" + keyword.replace(" ", "%20") + "%22"\
         + "%20AND%20year:" + str(date_int) + ")"

    # Building the Springer Metadata API parameters dictionary
        d_springer = requests.get(base_url_springer + springer_keyword,
                                  params=url_params_springer).json()
        articles = pd.DataFrame([d_springer])
        articles = articles.result
        articles = articles[0]
        articles = pd.DataFrame(articles)
        articles = int(articles.total[0])
        print(f'{date_int}:  {articles}')
        df.loc[len(df)] = [date_int, articles]

    if save_path:
        pathcsv = f"{save_path}/{keyword}_springer.csv"
        df.to_csv(path_or_buf=pathcsv)

    return df
