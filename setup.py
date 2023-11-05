"""Materials Chempy: Materials chemistry python uttilities."""


from os.path import abspath, dirname
from setuptools import setup, find_packages
# import unittest

project_dir = abspath(dirname(__file__))


# def unit_tests():
# test_loader = unittest.TestLoader()
# test_suite = test_loader.discover('test', pattern='test*.py')
# return test_suite

if __name__ == "__main__":

    setup(
        name='materials-chempy',
        version='0.0.1',
        description='General python uttilities for materials chemistry and engineering',
        long_description="""
    Parse, treat and visualize different carachterization analysis data and results,
    focusing on matplotlib plottings and visualizations

    1. .mzML mass spectrum input files plotting.

    2. AscII fluorescence emission data plotting.

    3. AscII UV-VIS spectrophotommetry data plotting.

    4. Transmission electron microscopy (TEM) analysis and scripts.

    5. AscII Shimadzu gas-chromatography (GC) plotting.

    6. Edinburgh .FS fluorescnece emission files conversion to Ascii.

    7. Elsevier and PubMed articles Databases data analysis

    8. Other python useffull jupyter notebooks, on the material chemistry subarea.
    """,
        url="https://github.com/eduardotlc/materials_chempy",
        author="Eduardo Campos",
        author_email="eduardotcampos@usp.br",
        license='MIT',

        classifiers=[
            'Development Status :: 2 - Pre-Alpha',
            'Intended Audience :: Science/Research',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3.10',
            'Programming Language :: Python :: 3.11',
            'Topic :: Scientific/Engineering :: Chemistry',
            'Topic :: Scientific/Engineering :: Physics'
        ],
        keywords=(
            'spectroscopy spectra chemistry physics TEM microscopy UV-VIS \
             fluorescence emission gas-chromatography mass-spectrometry mzML \
             material-chemistry ESI-MS data-analysis Database articles machine-learning'
        ),
        include_package_data=True,
        packages=find_packages(exclude=['docs', 'default', 'dev']),
        install_requires=['numpy', 'scipy',
                          'matplotlib; python_version >= "3.7"',
                          'spectrum >= 0.8.1', 'astropy >= 5.0.6',
                          'specutils >= 1.10.0', 'distinnctipy >= 1.2.2',
                          ],
        extras_require={'docs': ["sphinx",
                                 "sphinx_rtd_theme",
                                 "sphinx-argparse",
                                 "sphinxcontrib-bibtex"],
                        'vasp': ['pymatgen;python_version >= "3.7"',
                                 'numpy >= 1.17'
                                 ]
                        },
        python_requires='!=3.7.*, !=3.8.*, !=3.9.*, !=3.10.*, !=3.11.*, <4',
        entry_points={
            'console_scripts': [
                'materials-chempy=materials-chempy.cli',
                'materials-chempy-general-utils=materials-chempy.cli.utils',
            ]
        },
        # test_suite='setup.unit_tests'
    )
