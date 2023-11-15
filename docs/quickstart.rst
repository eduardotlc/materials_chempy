===========
Quick Start
===========


Testing
=======

Modules functions tests are defined inside the functions docstring, and can be
availed by running inside the /docs folder:

.. code-block:: bash

   # materials_chempy/docs
   make test

For running such tests, `pytest`_ needs to be installed.

.. _pytest: https://pypi.org/project/pytest/

Docstrings relative paths consider they are runned from the documentation folder.

Individual modules can be tested by parsing each function to pytest, for example:

**Mass Spectrometry module**

.. code-block:: bash

   # /materials_chempy/docs
   pytest --doctest-modules ../mass_spectrometry/functions.py

**Client utils**

.. code-block:: bash

   # /materials_chempy/docs
   pytest --doctest-modules ../utils.py


Plotting mzML Mass Spectrometry
===============================


Transmission Electron Microscopy particles histogram
====================================================


Gas Chromatography Analysis
===========================


Fluorescence Emission Spectra
=============================


Notebooks Examples
==================
