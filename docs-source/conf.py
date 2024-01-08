# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
#sys.path.insert(0, os.path.abspath('../laceworksdk'))

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Lacework Python SDK'
copyright = '2023, Lacework'
author = 'Jon Stewart, Tim MacDonald'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.napoleon',
              'sphinx.ext.autodoc',
              'autoapi.extension',
              'sphinx.ext.doctest',
              'sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sphinx.ext.githubpages']

autoapi_dirs = ['../laceworksdk']
autoapi_type = "python"
autoapi_options = [
    "members",
    "show-inheritance",
    "show-module-summary",
    "imported-members",
    "inherited-members",
    "no-private-members"
]
autodoc_default_options = {"members": True, "show-inheritance": True}
autodoc_inherit_docstrings = True
# Napoleon settings
napoleon_google_docstring = True
napoleon_numpy_docstring = False
napoleon_include_init_with_doc = True
napoleon_include_private_with_doc = False
napoleon_include_special_with_doc = False
napoleon_use_admonition_for_examples = False
napoleon_use_admonition_for_notes = False
napoleon_use_admonition_for_references = False
napoleon_use_ivar = False
napoleon_use_param = True
napoleon_use_rtype = True

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = 'https://techally-content.s3-us-west-1.amazonaws.com/public-content/lacework_logo_full.png'
html_theme_options = {
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False,
    'vcs_pageview_mode': '',
    'style_nav_header_background': 'white',
    # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': False,
    'titles_only': False
}

