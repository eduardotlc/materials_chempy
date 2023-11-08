Notebooks Modules Examples
==========================

articles_data_analysis
----------------------

**Notebok written to query, analyze, and plot different research related databases.**

This notebook presents code cells for querying the number of published papers , or google searches, containing a user
defined keyword, over a custom range of time, with subsequent plotting of this data, for demonstrating the interest
evolution on this topic over the years.

The notebook workflow is based on my personal preferences, managing most of the datas as pandas dataframes, with the
possibility of saving it as a csv, as well as reading a stored csv for analysis and plotting.

The code cells were designed based on a non-paid API key user, not being the most optimized case for
the user possesing one of these paids APIs.

More specifically, this notebook presents interactions with:

    - Google Trends

    - Scopus Database

    - PubMed Database

The Scopus database requires the user to `generate a free api`_, which requires an elsevier account.

.. _generate a free api: https://dev.elsevier.com/apikey/manage

This notebook require the following packages to be installed to be fully executed:

.. code-block:: bash

   python -m pip install pandas pytrends metapub matplotlib pybiometrics numpy


