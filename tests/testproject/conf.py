# Copyright 2020 Nokia
# Licensed under the Apache License 2.0.
# SPDX-License-Identifier: Apache-2.0

# -*- coding: utf-8 -*-

import sys
import six

from recommonmark.parser import CommonMarkParser
source_parsers = {
'.md': CommonMarkParser,
}
source_suffix = ['.rst', '.md']

import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

six.print_(">>> This python version is ", sys.version)

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinxcontrib.relative-link-corrector']

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project   = 'sphinxcontrib.relative-link-corrector.testproject'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

