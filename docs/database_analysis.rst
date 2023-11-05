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

API_Keys
--------

.. tab-set::

    .. tab-item:: NCBI

       PubMed NCBI API key is optional, and the script was developed aiming to a workflow without the key. Feel free to `dig further`_ the API if it interests you.

       .. _dig further: https://www.ncbi.nlm.nih.gov/account/

       .. qiskit-card::
           :header: PubMed NCBI Database
           :card_description: Fetch PubMed NCBI database, providing alternatives to analyze scientific articles interest over the time, on a specific subject.
           :image: ../../../static/ncbi.svg
           :link: https://www.ncbi.nlm.nih.gov/account/

    .. tab-item:: Elsevier

       The Scopus database requires the user to `generate a free api`_, which requires an elsevier account.

       .. _generate a free api: https://dev.elsevier.com/apikey/manage

       .. qiskit-card::
           :header: Elsevier Scopus Database
           :card_description: Fetch Elsevier articles Scopus database, aiming data analysis of articles time evolution.
           :image: ./static/Elsevier.svg
           :link: https://dev.elsevier.com/apikey/manage

|
|
|

Packages Installation
---------------------

.. tab-set::

    .. tab-item:: NCBI

       All interactions with PubMed NCBI Database is done through the python package `Metapub <https://pypi.org/project/metapub/>`__.

       This package can be installed running the following on a terminal:

       .. code-block:: sh

          python -m pip install metapub

       Other important requirements are present in the database_analysis module folder `requirements.txt`_.

       .. _requirements.txt: ../../../database_analysis/requirements.txt

        .. qiskit-card::
           :header: Metapub Package
           :card_description: Interaction with the NCBI Database is done through the Metapub package
           :image: .../../../../static/metapub.jpg
           :link: https://pypi.org/project/metapub/

    .. tab-item:: Elsevier

       All interactions with Scopus Database is done through the python package `Pybliometrics <https://pypi.org/project/pybliometrics/>`__.

|
|
|

Client usage
------------

        - To generate a csv with published articles containing a keyword from 2000 t0 2023,
          with number of articles per month, run:

        .. code:: text

            python cli.py --pubmed '<keyword>' 2000 2023 -o <output_path>

        - Note: PubMed database was created on january 1996

        - Default qurying interval if not inputted will be 1996-2023.


This notebook require the following packages to be installed to be fully executed:

.. code-block:: bash

   python -m pip install pandas pytrends metapub matplotlib pybiometrics numpy

Basic workflow is executed by the client module, linke the following examples:
