==========================
Articles Database Analysis
==========================

**Script written to query, analyze, and plot different research related databases.**

This module presents functions for querying the number of published papers , or google searches, containing a user
defined keyword, over a custom range of time, with subsequent plotting of this data, for demonstrating the interest
evolution on this topic over the years.

The module workflow is based on my personal preferences, managing most of the datas as pandas dataframes, with the
possibility of saving it as a csv, as well as reading a stored csv for analysis and plotting.

The code cells were designed based on a non-paid API key user, not being the most optimized case for
the user possesing one of these paids APIs.

More specifically, this notebook presents interactions with:

    - Google Trends

    - Scopus Database

    - PubMed Database

    - Springer Database

API_Keys
========

.. tab-set::

    .. tab-item:: NCBI

        PubMed NCBI API key is optional, and the script was developed aiming to a workflow without the key. Feel free to `dig further`_ the API if it interests you.

        .. _dig further: https://account.ncbi.nlm.nih.gov/

        .. qiskit-card::
           :header: PubMed NCBI Database
           :card_description: Fetch PubMed NCBI database, providing alternatives to analyze scientific articles interest over the time, on a specific subject.
           :image: _static/ncbi.svg
           :link: https://account.ncbi.nlm.nih.gov/

    .. tab-item:: Elsevier

       The Scopus database requires the user to `generate a free api`_, which requires an elsevier account.

       .. _generate a free api: https://dev.elsevier.com/apikey/manage

       .. qiskit-card::
           :header: Elsevier Scopus Database
           :card_description: Fetch Elsevier articles Scopus database, aiming data analysis of articles time evolution.
           :image: _static/Elsevier.svg
           :link: https://dev.elsevier.com/apikey/manage

    .. tab-item:: Springer

        Springernature `free api`_ is required to use this database functions.

        .. _free api: https://dev.springernature.com/signup?cannot_be_converted_to_param

        .. qiskit-card::
            :header: Springernature Database
            :card_description: Fetch Springernature database, aiming data analysis of articles subjects interest evolution.
            :image: _static/springernature.ico
            :link: https://dev.springernature.com

|
|
|

Packages Installation
=====================

.. tab-set::

    .. tab-item:: NCBI

       All interactions with PubMed NCBI Database is done through the python package `Metapub <https://pypi.org/project/metapub/>`__.

       This package can be installed running the following on a terminal:

       .. code-block:: sh

          python -m pip install metapub

       Other important requirements are present in the database_analysis module folder `requirements.txt`_.

       .. _requirements.txt: https://github.com/eduardotlc/materials_chempy/blob/fea9fd5124d1d058abbb3ed55b2c9fb70c923bf9/database_analysis/requirements.txt

        .. qiskit-card::
           :header: Metapub Package
           :card_description: Interaction with the NCBI Database is done through the Metapub package
           :image: _static/metapub.svg
           :link: https://pypi.org/project/metapub/

    .. tab-item:: Elsevier

       All interactions with Scopus Database is done through the python package `Pybliometrics <https://pypi.org/project/pybliometrics/>`__.


    .. tab-item:: Springer

       This DataBase interaction is done through the API key and the `requests`_ python package.

       .. _requests: https://pypi.org/project/requests/

|
|
|


Important informations
======================

.. tab-set::

    .. tab-item:: NCBI

       NCBI/PubMed database was created at 1996.

       Free API limits to the user to make 9999 calls per time, if querying a much used keyword,
        it may reach this limit, in this cases you can use the --dailypubmed function that fetch
        data to every day in the year range given, having the drawback of a longer running time.
        Even fetching daily data, depending of the keyword, it may still reach the free API limit.

    .. tab-item:: Elsevier/Scopus

        Database launched in 2004.

    .. tab-item:: Springer

        Fastest database to fetch data from.


Client usage
============

Saving results to csv
---------------------

.. tab-set::

   .. tab-item:: PubMed

       - Printing the number of articles in the pubmed database, from 2019 to 2020, containig
         the 'hypoxia' keyword, and saving the results to a csv file int the home folder

       .. code-block:: bash

           >>> python cli.py --pubmed hypoxia 2019 2020 docs/pyplots
           2019-1:  642
           2019-2:  791
           ...
           ...
           2020-11:  462
           2020-12:  2234

       .. list-table:: hypoxia_pubmed.csv
          :widths: 25 25 25 25
          :header-rows: 1

          * -
            - Month
            - Year
            - Articles
          * - 0
            - 1
            - 2019
            - 15
          * - 1
            - 2
            - 2019
            - 33
          * - 2
            - 3
            - 2019
            - 17
          * - 3
            - 4
            - 2019
            - 28
          * - 4
            - 5
            - 2019
            - 663
          * - 5
            - 6
            - 2019
            - 1
          * - 6
            - 7
            - 2019
            - 499
          * - 7
            - 8
            - 2019
            - 16
          * - 8
            - 9
            - 2019
            - 169
          * - 9
            - 10
            - 2019
            - 24
          * - 10
            - 11
            - 2019
            - 322
          * - 11
            - 12
            - 2019
            - 15
          * - 0
            - 1
            - 2020
            - 4
          * - 1
            - 2
            - 2020
            - 0
          * - 2
            - 3
            - 2020
            - 6
          * - 3
            - 4
            - 2020
            - 49
          * - 4
            - 5
            - 2020
            - 23
          * - 5
            - 6
            - 2020
            - 46
          * - 6
            - 7
            - 2020
            - 24
          * - 7
            - 8
            - 2020
            - 11
          * - 8
            - 9
            - 2020
            - 15
          * - 9
            - 10
            - 2020
            - 1301
          * - 10
            - 11
            - 2020
            - 18
          * - 11
            - 12
            - 2020
            - 36


   .. tab-item:: Springer

       - Printing the number of articles in the springer-nature database, containing the 'niobium'
         keyword, from 2010 to 2023

       .. code-block:: bash

           >>> python cli.py --springer niobium 2010 2023 docs/pyplots
           2010:  791
           2011:  883
           ...
           ...
           2022:  2185
           2023:  2323

       .. list-table:: hypoxia_pubmed.csv
          :widths: 25 25 25
          :header-rows: 1

          * -
            - Year
            - Articles
          * - 0
            - 2010
            - 791
          * - 1
            - 2011
            - 883
          * - 2
            - 2012
            - 927
          * - 3
            - 2013
            - 977
          * - 4
            - 2014
            - 1112
          * - 5
            - 2015
            - 1112
          * - 6
            - 2016
            - 1640
          * - 7
            - 2017
            - 1472
          * - 8
            - 2018
            - 1633
          * - 9
            - 2019
            - 1770
          * - 10
            - 2020
            - 1862
          * - 11
            - 2021
            - 2016
          * - 12
            - 2022
            - 2185
          * - 13
            - 2023
            - 2323


   .. tab-item:: Scopus

       - Printing the number of articles in the scopus database, from 2018 to 2019, containig
         the 'MOF' keyword, and saving the results to a csv file in the docs/pyplots folder.

       .. code-block:: bash

           >>> python cli.py --scopus MOF 2018 2019 docs/pyplots
           2018-january:  263
           2018-february:  287
           ...
           ...
           2019-november:  561
           2019-december:  609

       .. list-table:: MOF_scopus.csv
          :widths: 25 25 25 25
          :header-rows: 1

          * -
            - Month
            - Year
            - Articles
          * - 0
            - 1
            - 2018
            - 263
          * - 1
            - 2
            - 2018
            - 287
          * - 2
            - 3
            - 2018
            - 312
          * - 3
            - 4
            - 2018
            - 264
          * - 4
            - 5
            - 2018
            - 331
          * - 5
            - 6
            - 2018
            - 294
          * - 6
            - 7
            - 2018
            - 306
          * - 7
            - 8
            - 2018
            - 325
          * - 8
            - 9
            - 2018
            - 390
          * - 9
            - 10
            - 2018
            - 377
          * - 10
            - 11
            - 2018
            - 410
          * - 11
            - 12
            - 2018
            - 446
          * - 0
            - 1
            - 2019
            - 551
          * - 1
            - 2
            - 2019
            - 468
          * - 2
            - 3
            - 2019
            - 523
          * - 3
            - 4
            - 2019
            - 474
          * - 4
            - 5
            - 2019
            - 460
          * - 5
            - 6
            - 2019
            - 483
          * - 6
            - 7
            - 2019
            - 470
          * - 7
            - 8
            - 2019
            - 482
          * - 8
            - 9
            - 2019
            - 550
          * - 9
            - 10
            - 2019
            - 623
          * - 10
            - 11
            - 2019
            - 561
          * - 11
            - 12
            - 2019
            - 609

Bar plotting
------------

.. tab-set::

   .. tab-item:: PubMed fetched

      - Fetching and plotting the number of articles containing keyword
        'pdt', from 2012 to 2018, saving a csv and the plot png to ~/

      - Bar plotting from a saved csv file

      .. code-block:: bash

         python cli.py --barplot pyplots/MOF_pubmed.csv

      .. plot:: pyplots/bar_csv_pubmed_mof.py
         :context: reset
         :include-source:

   .. tab-item:: Springer/Scopus csv

      - Bar plotting the number of articles per year containing a keyword,
        from a csv fetched from springer/scopus saved file.


      .. code-block:: bash

         python cli.py --barplot pyplots/niobium_springer.csv

      .. plot:: pyplots/bar_csv_springer_niobium.py
         :context: reset
         :include-source:

Functions
---------

.. automodule:: materials_chempy.database_analysis.dban_functions
    :members:
