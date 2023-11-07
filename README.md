# Materials Chempy

**Python tools to analyze, simulate and plot results of chemical inorganic materials.**

|       build       |         PyPi          |      Documeantion      |        License         |    Update     |
| :---------------: | :-------------------: | :--------------------: | :--------------------: | :-----------: |
| [![ci-badge]][ci] | [![pypi-badge]][pypi] | [![documentation]][dc] | [![mitbadge]][license] | ![lastupdate] |

<!--[ci-badge]: https://github.com/eduardotlc/jupyterlab_ariakedark_theme/workflows/Build/badge.svg-->
<!--[ci]: https://github.com/eduardotlc/jupyterlab_ariakedark_theme/actions/workflows/build.yml-->
<!--[pypi-badge]: ./images/badge_pypi.svg-->
<!--[pypi]: https://badge.fury.io/py/jupyterlab-ariakedark-theme-->
[mitbadge]: ./docs/static/license.svg
[license]: https://opensource.org/licenses/MIT
[lastupdate]: ./docs/static/lastupdate.svg
[documentation]: https://github.com/eduardotlc/materials_chempy/actions/workflows/documentation.yml/badge.svg
[dc]: https://github.com/eduardotlc/materials_chempy/actions/workflows/documentation.yml

<eduardotcampos@usp.br> **[2023]**

**Package not yet available in Pypi and conda repos**

---

---


## Informations

---

- The codes in this repository are still in the early stages of developement, not being yet suited for general use.

- Initial focus in certain imaging and spectroscopy techniques.

- Developement mostly in python, matplotlib, pandas DataFrames and Qt backends, suited for using in jupyter notebooks for example

- Example notebooks of in progress work will be updated to the repository /notebooks folder

- Visualization and other analysis techniques are considered with a
  focus in nanoparticles and MOFs compounds class.


## Fluorescence emission

---

- wavelength x CPS (counts per second)


### Dependencies

#### Plotting

```
python -m pip install numpy pandas pytz six distinctipy astropy
```

#### Format parsing

```
python -m pip install pyyaml yaml pandas parse_binary_file
```


## Articles Database Analysis

---

- PubMed NCBI Databasedata analysis and visualization script.

- Elsevier Escopus Database analysis and visualization script.

- This modules consists on fetching the number of published articles presenting a specific keyword, in each database,
  in every month from a user defined year range.

- It allows to save the queryied results to a csv file for later analysis.

- The obtained results can be plotted as a bar plot, to demonstrate this specific subject interest evolution,
  over the time.


## UV-Vis absorption
---


## Electron microscopy

---

- [Tensorflow](https://www.tensorflow.org) automatic identification and measure of nanoparticles.

- Model still needs to be finished and optimized.


## Mass spectrometry
---

- Accepts data from .mzML and .ascii files

- Plots the data, filtering from number of most intense peaks the user prefers to plot

- Allows custom labeling specifc peaks, as well as automatic labeling the n highest peaks,
  with their corresponding m/z value


## Structures simulation and visualization

---

- Examples of molecular structures simulation and visualization.

- Initially only in an example notebook, using the [ase](https://pypi.org/project/ase/) package


## Documentation

---

- The documentation present in docs folder is not yet available on the internet, however it can be build locally.

- The docs folder contains a single html and a pdf version of the current early developement stages of the project.


## TODO

---

- Implement ase notebook examples in the package client module.

- Finish tensorflow TEM image training

- Implement mass spectrometry fragmentations plotting

- Implement more complex data normalization and correction in spectrophotometry

- Implement a github building workflow to the project.
