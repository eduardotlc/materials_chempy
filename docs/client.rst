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

|
|
|

Mass spectrometry
-----------------

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
---------------------------

 .. tab-set::

    .. tab-item:: NCBI

        - Creating an API key is optional and can be made registering `here`_.

        .. _here: https://www.ncbi.nlm.nih.gov/account/

            - If desired to use api key, define an environemnt variable named
              NCBI_API_KEY with your key

        - The querying of NCBI pubmed database is made by the python
          package `metapub`_.

        .. _metapub: https://pypi.org/project/metapub/

        .. code:: text

            python3 -m pip install metapub

        - To generate a csv with published articles containing a keyword from 2000 t0 2023,
          with number of articles per month, run:

        .. code:: text

            python cli.py --pubmed -o <output_path> --interval 2000 2023

        - Note: PubMed database was created on january 1996

        - Default qurying interval if not inputted will be 2000-2023.



    .. tab-item:: Elsevier

        The following cloud vendors have Qiskit pre-installed in their environments:

       .. qiskit-card::
          :header: IBM Quantum Lab
          :card_description: Build quantum applications and experiments with Qiskit in a cloud programming environment.
          :image: _static/images/ibm_qlab.png
          :link: https://quantum-computing.ibm.com/

       .. qiskit-card::
          :header: Strangeworks
          :card_description: A platform that enables users and organizations to easily apply quantum computing to their most pressing problems and research.
          :image: _static/images/strangeworks.png
          :link: https://strangeworks.com/


|
|
|

Functions
---------

.. automodule:: materials_chempy.utils
    :members:

.. automodule:: materials_chempy.cli
    :members:
