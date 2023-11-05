Introduction
============

General information
-------------------

Python materials chemistry different analysis techniques plotting and uttilities.

`The MIT License (MIT)`_

.. _The MIT License (MIT): https://opensource.org/license/mit/

**Copyright (c) [2023] [Eduardo Toledo Campos]**

`eduardotcampos@usp.br`_

.. _eduardotcampos@usp.br: mailto:eduardotcampos@usp.br

Implementation
--------------

Materials chempy requires python 3.7+, with it other necessary python packages contained in the project
requirement.txt respective files. The module is available on https://www.github.com/eduardotlc/Materials_Chempy
or pypi, published under the MIT license. This project is still in pre-release early development stages, any
code improvement commit is welcome and appreciated.

Download
--------

Get the latest version in the `github repository`_.

.. _github repository: https://www.github.com/eduardotlc/Materials_Chempy

|

An early stage version of this documentation can be checked in the project `documentation`_ (Since you are
here you must have noticed it.)
    
    .. _documentation: https://github.com/eduardotlc/materials_chempy/blob/6bfe8f6c8471e37cca7dbc7e6cac39dcd57885f8/docs/build/singlehtml/index.html


Installation
------------

Materials_Chempy requires `python`_ 3.7 or higher.

.. _python: https://www.python.org/downloads/

.. tab-set::

    .. tab-item:: Python

      You can install the general python `requirements`_ , or each submodule
        specific requirements (for example the `database analysis requirements`_).
         
      .. _requirements: https://github.com/eduardotlc/materials_chempy/blob/fea9fd5124d1d058abbb3ed55b2c9fb70c923bf9/requirements.txt

      .. _database analysis requirements: https://github.com/eduardotlc/materials_chempy/blob/fea9fd5124d1d058abbb3ed55b2c9fb70c923bf9/database_analysis/requirements.txt
       
      The package can be installed direct from source by cloning the repo
      
      .. code-block:: bash
      
         git clone git@github.com:eduardotlc/materials_chempy
         cd materials_chempy
         python -m pip install -r requirements.txt
         python -m pip install -ve .
         
    .. tab-item:: Conda
      
      You can also install the package in an conda virtual environment, which
        is highly recommende, to do so, with conda already installed, run
        
      .. code-block:: bash
              
         git clone git@github.com:eduardotlc/materials_chempy
         cd materials_chempy
         conda env update --file environment.yml --name materials_chempy
         python -m pip install -ve .
         
    .. tab-item:: Public repositories
    
       Due to the current early developement stage of this project, it is not 
         yet available in public repos like pypi or conda-forge. This constation
         is also a sign, to proceed with caution on the usage of this repo on
         its current state.
     


Testing
-------

This project functions tests are written in docstrings formats, as shown in this documentation 
functions autodocs. To run all project tests, inside `docs`_ folder, run:


.. code-block:: bash

   make tests

If you want to test only an specific file functions, you can run the following command, also inside `docs`_ folder    

.. _docs: https://github.com/eduardotlc/materials_chempy/tree/262a91c69302bb16e8af52f2add31b751801aacc/docs

.. code-block:: bash

   python -m pytest --doctest-utils <path_to_file>

Make sure to install the `tests requirements`_ before executing them.

.. _tests requirements: https://github.com/eduardotlc/materials_chempy/blob/262a91c69302bb16e8af52f2add31b751801aacc/docs/requirements.txt