SPHINXPROJ    = "Materials_Chempy"
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = build
TEST		  = '../mass_spectrometry/ms_functions.py' '../utils.py' '../spectrophotometry/spec_functions.py' '../database_analysis/dban_functions.py'
PYTHON		  = '/home/eduardotc/mambaforge/bin/python'
.PHONY: help Makefile
# @$(SPHINXBUILD) -M help '$(SOURCEDIR)' '$(BUILDDIR)' $(SPHINXOPTS) $(O)
# doctest:
# @$(SPHINXBUILD) -M $@ '$(SOURCEDIR)' '$(BUILDDIR)' $(SPHINXOPTS) $(O)
# docset:
# @doc2dash  -n '$(SPHINXPROJ)' -d './build/docset' -i './static/zif8.png' -a '_build/html'#
help:
		 @$(SPHINXBUILD) --version --color
		 @printf "Please use \`make \e[38;2;189;146;248mtarget\e[0m\' where \e[38;2;189;146;248mtarget\e[0m is one of\n"
		 @printf "\e[38;2;189;146;248m  html\e[0m        to make standalone HTML files\n"
		 @printf "\e[38;2;189;146;248m  singlehtml\e[0m  to make a single large HTML file\n"
		 @printf "\e[38;2;189;146;248m  latexpdf\e[0m    to make LaTeX and PDF files (default pdflatex)\n"
		 @printf "\e[38;2;189;146;248m  linkcheck\e[0m   to check all external links for integrity\n"
		 @printf "\e[38;2;189;146;248m  clean\e[0m       to remove everything in the build directory\n"
		 @printf "\e[38;2;189;146;248m  test\e[0m        Run all docstrings examples tests\n"
		 @printf "\e[38;2;189;146;248m  show\e[0m        Open html documentation in the browser\n"
		 @printf "\e[38;2;189;146;248m  coverage\e[0m    to run coverage check of the documentation\n"
clean:
		 @$(SPHINXBUILD) -M clean '$(SOURCEDIR)' '$(BUILDDIR)' $(SPHINXOPTS) $(O)
		 rm -rf '$(SOURCEDIR)/build/'
		 rm -rf '$(SOURCEDIR)/sphinxext/__pycache__'
show:
		 @python -c 'import webbrowser'
		 @python -m webbrowser -t '/home/eduardotc/Programação/my_gits/materials_chempy/docs/build/html/index.html'
html:
		 @$(SPHINXBUILD) -M $@ '$(SOURCEDIR)' '$(BUILDDIR)' $(SPHINXOPTS) $(O)
singlehtml:
		 @$(SPHINXBUILD) -M $@ '$(SOURCEDIR)' '$(BUILDDIR)' $(SPHINXOPTS) $(O)

latexpdf:
		 @$(SPHINXBUILD) -M $@ '$(SOURCEDIR)' '$(BUILDDIR)' $(SPHINXOPTS) $(O)
linkcheck:
		 @$(SPHINXBUILD) -M $@ '$(SOURCEDIR)' '$(BUILDDIR)' $(SPHINXOPTS) $(O)
coverage:
		 @$(SPHINXBUILD) -M $@ '$(SOURCEDIR)' '$(BUILDDIR)' $(SPHINXOPTS) $(O)
.PHONY: test
test:
		 mkdir -p './tmp'
		 @python -m pytest --doctest-modules -v $(TEST)
		 rm -rf './tmp'
