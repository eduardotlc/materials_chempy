# Materials Chempy

---

**Python client tools utils on inorganic chemistry & materials science data handling.**

   [![Build](/.assets/build_badge.svg)](https://github.com/eduardotlc/materials_chempy/actions/workflows/build.yml)
   [![License](/.assets/mit_badge.svg)](https://opensource.org/license/mit)
   [![Python](/.assets/python_badge.svg)](https://www.python.org/downloads/release/python-3145/)
   [![Contact](/.assets/contact_badge.svg)](mailto:eduardotcampos@hotmail.com)

> [!CAUTION] Under development, not recomended cloning the repo yet. In case of interest, star it and wait stable release

> [!INFO] Tested on Linux (Fedora gnome) with [Kitty terminal](https://sw.kovidgoyal.net/kitty/)

1. [Features](#features)

2. [Installation](#installation)

  2.1 [Dependencies](#dependencies)

3. [Usage](#usage)

4. [TODO](#todo)

5. [Development](#development)

  5.1 [Tests](#tests)

6. [Acknowledgments](#acknowledgments)


## Features

- [Fluorescence Emission](#fluorescence-emission)

- [UV-Vis Absorption](#uv-vis-absorption)

- [Electron Microscopy](#electron-micsoscopy)

- [Articles Database Analysis](#articles-database-analysis)

- [Mass Spectrometry](#mass-spectrometry)

- [Structure Simulation and Visualization](#structure-simulation-and-vizualization)

## Installation

### Dependencies

#### Plotting

```
python -m pip install numpy pandas pytz six distinctipy astropy
```

#### Format parsing

```
python -m pip install pyyaml yaml pandas parse_binary_file
```

## Usage

### Fluorescence emission

### Articles Database Analysis

- PubMed NCBI Databasedata analysis and visualization script.

- Elsevier Escopus Database analysis and visualization script.

- This modules consists on fetching the number of published articles presenting a specific keyword, in each database,
  in every month from a user defined year range.

- It allows to save the queryied results to a csv file for later analysis.

- The obtained results can be plotted as a bar plot, to demonstrate this specific subject interest evolution,
  over the time.


### UV-Vis absorption

### Electron microscopy

- [Tensorflow](https://www.tensorflow.org) automatic identification and measure of nanoparticles.

- Model still needs to be finished and optimized.


### Mass spectrometry

- Accepts data from .mzML and .ascii files

- Plots the data, filtering from number of most intense peaks the user prefers to plot

- Allows custom labeling specifc peaks, as well as automatic labeling the n highest peaks,
  with their corresponding m/z value


### Structures simulation and visualization

- Examples of molecular structures simulation and visualization.

- Initially only in an example notebook, using the [ase](https://pypi.org/project/ase/) package




## TODO

---

- [ ] handle creation of docstring file tests dirs/files like "/tmp/materials_chempy/alt_stdout"

- [ ] handle Literal["repeat"] types from handlers

- [ ] Create fallback/check on matplotlib backend on to terminals other than kitty

- [ ] Implement ase notebook examples in the package client module.

- [ ] Finish tensorflow TEM image training

- [ ] Implement mass spectrometry fragmentations plotting

- [ ] Implement more complex data normalization and correction in spectrophotometry

- [ ] Implement a github building workflow to the project.

- [ ] Create a pypi releasing workflow

## Development

### Tests

on repo root dir:
```zsh
python -m pytest --doctest-modules \
src/materials_chempy/utils.py
```

### Documentation

- The documentation present in docs folder is not yet available on the internet, however it can be build locally.

- The docs folder contains a single html and a pdf version of the current early developement stages of the project.

## Acknowledgments

- [dracula.nvim](https://github.com/Mofiqul/dracula.nvim) theme, which served as foundation for this
  color scheme's structure.

- [cherry-kde](https://github.com/nullxception/cherry-kde) theme, from which the terminal color
  palette was inspired.

**Please consider supporting and checking out the original developers and their projects - without
their work, this theme wouldn’t have been possible.**
