======
Client
======

The client cli.py file allows to run specific modules from a terminal (bash,zsh etc...).

The main flags triggers specific modules features, like histogram plotting, mass spectra plotting,
image analysis, etc... The others flags allows to parse values to this executed feature.

inside the package folder:

.. code-block:: bash

    python cli.py [-flags] [-args]


To print the help from this module exec:

.. code-block:: bash

   python cli.py -h


.. list-table:: Client
   :widths: 25 25 60 20
   :header-rows: 1

   * - Flag
     - Arguments
     - Description
     - Module
   * - -h --help
     - None
     - Print clien module help
     - General
   * - -i --input
     - str
     - Input to another executed flag, like the path to a file
     - General
   * - -o --output
     - str
     - Output to another executed flag, like path to saved file
     - General
   * - -M --mplcfg
     - None
     - Configure matplotlib style to the developer default
     - Matplotlib
   * - -S --subtitle
     - str
     - Plot subtitle
     - Matplotlib
   * - -t --title
     - str
     - Plot title
     - Matplotlib

|
|
|

Mass spectrometry
=================

**The flag -m triggers matplotlib spectra plotting from a .mzML file**

**The following flags takes the arguments:**

---

**-i    --input**

    *String* with the path to a .mzML file

    *Required*

    If not given, fallbacks to *default: './example_data/anad2.mzML'* example

**-S    --subtitle**

    *String* with the plot subtitle

    *Optional*

    If not given, fallbacks to *default: <input file name>*

**--resolution**

    *Float* with the minimum difference between 2 of the plot peaks, for both being plotted.
    Otherwise, if (peak 1 - peak 2) < argument, the lowest intensity peak is ignored.

    *Optional*

    If not given, fallbacks to *default: 0.3 m/z*

|
|
|

Articles databases analysis
===========================

Basic
-----

**only printing in terminal the results of the fetched database**

Prints 'plasmonic' keyword containing articles from pubmed, from 2013 to
 2014, without saving the results.

.. code-cell:: bash

   python cli.py --pubmed plasmonic 2013 2014


.. output-cell::

   2013-1:  57
   2013-2:  80
   ...
   ...
   2014-11:  182
   2014-12:  140


|

Prints 'MOF' keyword containing articles, from scopus, ranging 2018 to 2020.

.. code-cell:: bash

   python cli.py --scopus MOF 2018 2020


.. output-cell::

   2018-january:  263
   2018-february:  287
   ...
   ...
   2020-november:  866
   2020-december:  1024


|

Prints number of articles containing 'mechanochemistry' keyword, in
 springer-nature database, from 2015 to 2020.

.. code-cell::

   python cli.py --springer mechanochemistry 2015 2020


.. output-cell::

   2015:  200
   2016:  191
   ...
   ...
   2019:  285
   2020:  277


Functions
---------

.. automodule:: materials_chempy.utils
    :members:


.. automodule:: materials_chempy.cli
    :members:
