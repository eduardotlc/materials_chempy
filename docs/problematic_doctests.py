import materials_chempy.database_analysis.dban_functions as dbanfunc


def problematic_doctests():
    """

    Contain problematic_doctests, to isolate them from the rest of the
    projext modules.

    Examples
    --------
    dban_functions scopusfetcher function example.
    Querying, per month, the number of published articles containing the
    keyword 'Upconversion', in the year of 2015, in the Scopus database.

    >>> scopus_df = dbanfunc.scopusfetcher('Upconversion', 2015, 2015,
    ...                                    save_path='./tmp')
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
