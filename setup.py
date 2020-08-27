#!/usr/bin/env python

import setuptools



#!/usr/bin/env python
import os
from setuptools import setup


def slurp(filename):
    """
    Return whole file contents as string. File is searched relative to
    directory where this `setup.py` is located.
    """
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read()


setup(
    name                 = "sphinxcontrib.relative-link-corrector",
    version              = "0.0.1",
    packages             = ["sphinxcontrib", "sphinxcontrib.relative-link-corrector"],
    namespace_packages   = ["sphinxcontrib"],
    package_dir          = {'': "src"},
    author               = "Gergely Csatari",
    author_email         = "gergely.csatari@nokia.com",
    license              = "Apache License 2.0",
    url                  = "https://github.com/CNTT",
    keywords             = ["helpers"],
    requires             = ["six"],
    description          = ("Corrects relative links when generating documents  "
                            "from .md to .html with commonmark"),
    long_description     = slurp("README.rst"),
    classifiers          = ["Programming Language :: Python",
                            "Programming Language :: Python :: 2.6",
                            "Programming Language :: Python :: 2.7",
                            "Programming Language :: Python :: 3.3",
                            "Programming Language :: Python :: 3.4",
                            "Programming Language :: Python :: 3.5",
                            "Programming Language :: Python :: 3.7",
                            "Development Status :: 2 - Pre-Alpha",
                            "Topic :: Documentation",
                            "Intended Audience :: Developers",
                            "License :: OSI Approved :: Apache Software License",
                            "Operating System :: POSIX"])

