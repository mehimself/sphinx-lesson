# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Sphinx-lesson'
copyright = '2020, CodeRefinery'
author = 'CodeRefinery'

# roundabout way to get version.  "import sphinx_lesson" would be easier, but
# then it becomes harder to have the same github action for this repo and
# the lessons themselves.
version_ns = { }
exec(open('../sphinx_lesson/_version.py').read(), version_ns)
version = version_ns['__version__']

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
import sys
sys.path.append('.')
extensions = [
    # githubpages just adds a .nojekyll file
    'sphinx.ext.githubpages',
    # myst_parser is not needed, because myst_nb replaces and conflicts with it
    # (provides all functionality and more).  But, myst_parser has fewer
    # dependencies so could be used instead.
    #'myst_parser',
    'sphinx_lesson',
    #'myst_nb',  # now done as part of sphinx_lesson
    #'sphinx.ext.intersphinx',
]

# Settings for myst_nb:
# https://myst-nb.readthedocs.io/en/latest/use/execute.html#triggering-notebook-execution
#jupyter_execute_notebooks = "off"
#jupyter_execute_notebooks = "auto"   # *only* execute if at least one output is missing.
#jupyter_execute_notebooks = "force"
jupyter_execute_notebooks = "cache"

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['README*', '_build', 'Thumbs.db', '.DS_Store',
                    'jupyter_execute', '*venv*']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_book_theme'
html_theme_options = {
    "repository_url": "https://github.com/coderefinery/sphinx-lesson/",
    "use_repository_button": True,
    "use_edit_page_button": True,
    "use_issues_button": True,
    }

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['_static']

# Intersphinx mapping.  For example, with this you can use
# :py:mod:`multiprocessing` to link straight to the Python docs of that module.
# List all available references:
#   python -msphinx.ext.intersphinx https://docs.python.org/3/objects.inv
#intersphinx_mapping = {
#    #'python': ('https://docs.python.org/3', None),
#    #'sphinx': ('https://www.sphinx-doc.org/', None),
#    }
