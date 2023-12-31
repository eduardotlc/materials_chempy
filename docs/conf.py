from __future__ import annotations

import sys
import doctest
import shutil
import os
from textwrap import dedent
import matplotlib.sphinxext
import bokeh.sphinxext
sys.path.append(os.path.abspath('sphinxext'))
# sys.path.append(os.path.abspath('static'))
# sys.path.append(os.path.abspath('../'))

# Basic
author = 'eduardotc'
copyright = '2023'
language = "en"
project = "Materials_Chempy"
release = '0.1'
sys.path.append('.')


# Extensions
extensions = [
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    'matplotlib.sphinxext.mathmpl',
    'matplotlib.sphinxext.plot_directive',
    'nbsphinx',
    'numpydoc',
    'pygments_pytest',
    'qiskit_sphinx_theme',
    'reno.sphinxext',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.extlinks',
    'sphinx.ext.inheritance_diagram',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_copybutton',
    'sphinx_design',
    'sphinx_remove_toctrees',
    'sphinx_reredirects',
    'sphinxcontrib.inkscapeconverter',
    'sphinx_toolbox.code',
    'bokeh.sphinxext.bokeh_dataframe',
]

if shutil.which("inkscape"):
    extensions.append("sphinxcontrib.inkscapeconverter")

# doctest_global_setup = """
# import pandas as pd
# import matplotlib.pyplot as plt
# import pytest
# import numpy
# import matplotlib
# import doctest

# matplotlib.use('agg', force=True)

# # Ignore matplotlib output such as `<matplotlib.image.AxesImage at
# # 0x7f956908c280>`. doctest monkeypatching inspired by
# # https://github.com/wooyek/pytest-doctest-ellipsis-markers (MIT license)
# OutputChecker = doctest.OutputChecker

# empty_line_markers = ['<matplotlib.', '<mpl_toolkits.mplot3d.']
# class SkipMatplotlibOutputChecker(doctest.OutputChecker):
    # def check_output(self, want, got, optionflags):
        # for marker in empty_line_markers:
            # if marker in got:
                # got = ''
                # break
        # return OutputChecker.check_output(self, want, got, optionflags)


# doctest.OutputChecker = SkipMatplotlibOutputChecker

# @pytest.fixture(autouse=True)
# def add_np(doctest_namespace):
    # numpy.random.seed(1)
    # doctest_namespace['np'] = numpy
# """

# Other configs
autoclass_content = 'both'
autodoc_default_options = {'members': None, 'undoc-members': None}
autodoc_docstring_signature = True
autodoc_mock_imports = ['kimpy']
autodoc_typehints = 'description'
autodoc_typehints_description_target = 'all'
autosummary_generate = True
coverage_show_missing_items = True
coverage_statistics_to_report = True
coverage_statistics_to_stdout = True
github_url = 'http://gtihub.com/eduardotlc/materials_chempy'
graphviz_dot = shutil.which('dot')

html_favicon = 'static/logo.png'
html_file_suffix = '.html'
html_index = 'index.html'
html_last_updated_fmt = "2023/10/13"
html_logo = 'static/logo.svg'
html_show_sphinx = False
html_static_path = ['./static']
html_theme = 'qiskit-ecosystem'


e = f"{project} {release}"

inheritance_edge_attrs = dict(penwidth=1)
inheritance_graph_attrs = dict(dpi=100, size='1000.0', splines='polyline')
inheritance_node_attrs = dict(height=0.02, margin=0.055, penwidth=1,
                              width=0.01)
panels_css_variables = {
    "tabs-color-label-active": "rgb(138, 63, 252)",
    "tabs-color-label-inactive": "rgb(221, 225, 230)",
}
plot_html_show_formats = True
unused_docs = []
latex_appendices = []
latex_elements = {'papersize': 'letter'}
latex_elements['babel'] = r'\usepackage{babel}'
latex_elements['fontenc'] = r''
latex_elements['maxlistdepth'] = '10'
latex_elements['pointsize'] = '11pt'
latex_elements['printindex'] = r'\footnotesize\raggedright\printindex'
# latex_engine = 'lualatex'
latex_logo = 'static/logo.png'
latex_show_urls = 'inline'
latex_show_pagerefs = True
latex_toplevel_sectioning = 'part'
latex_use_modindex = True
# latex_elements = {
    # "preamble": dedent(
        # r"""
        # \directlua{
            # luaotfload.add_fallback("fallbacks", {
                # "Noto Serif CJK SC:style=Regular;",
                # "Symbola:Style=Regular;"
            # })
        # }

        # \setmainfont{FreeSerif}[RawFeature={fallback=fallbacks}]
        # """
    # )
# }

latex_engine = 'xelatex'
latex_elements = {
    'fontpkg': r'''
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont{DejaVu Sans Mono}
''',
    'preamble': r'''
\usepackage[titles]{tocloft}
\cftsetpnumwidth {1.25cm}\cftsetrmarg{1.5cm}
\setlength{\cftchapnumwidth}{0.75cm}
\setlength{\cftsecindent}{\cftchapnumwidth}
\setlength{\cftsecnumwidth}{1.25cm}
''',
    'fncychap': r'\usepackage[Bjornstrup]{fncychap}',
    'printindex': r'\footnotesize\raggedright\printindex',
}
latex_show_urls = 'footnote'
makeindexfile = True
modindex_common_prefix = ["materials_chempy."]
nitpicky = True
os.environ.pop('DISPLAY', None)

pygments_style = 'colorful'
root_doc = master_doc = 'index'
source_suffix = '.rst', '.ipynb'
today_fmt = '%B %d, %Y'
unused_docs = []

napoleon_google_docstring = False
napoleon_numpy_docstring = True


# ----------------------------------------------------------------------------------
# Doctest
# ----------------------------------------------------------------------------------

doctest_default_flags = (
    doctest.ELLIPSIS
    | doctest.NORMALIZE_WHITESPACE
    | doctest.IGNORE_EXCEPTION_DETAIL
    | doctest.DONT_ACCEPT_TRUE_FOR_1
)

# Leaving this string empty disables testing of doctest blocks from docstrings.
# Doctest blocks are structures like this one:
# >> code
# output
doctest_test_doctest_blocks = "../utils.py ./cli.py \
                               ../database_analysis/dban_functions.py \
                               ../cli_utils.py"
addopts = '--doctest-modules'

doctest_encoding = 'latin1'

# doctest_optionflags = (doctest.NORMALIZE_WHITESPACE
                       # | doctest.IGNORE_EXCEPTION_DETAIL)
# ----------------------------------------------------------------------------------
# Plot directive
# ----------------------------------------------------------------------------------

# plot_html_show_formats = False
# nbsphinx_timeout = int(os.getenv("QISKIT_CELL_TIMEOUT", "300"))
# nbsphinx_execute = os.getenv("QISKIT_DOCS_BUILD_TUTORIALS", "never")
# nbsphinx_widgets_path = ""

nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=None) %}

.. only:: html

    .. role:: raw-html(raw)
        :format: html

    .. note::
        This page was generated from `{{ docname }}`__.

    __ https://github.com/Qiskit/qiskit-terra/blob/main/{{ docname }}

"""
