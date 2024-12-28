# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: AGPL-3.0-only
#
# Copyright © 2021-2022 siddharth ravikumar <s@ricketyspace.net>
#

from setuptools import setup
from codecs import open
from os import path

from acmensse import __version__

here = path.abspath(path.dirname(__file__))
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

config = {
    "name": "acmensse",
    "version": __version__,
    "description": "An ACMEv2 client. Fork of github.com/r5d/acmens.",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://github.com/aldocassola/acmens",
    "author": "Aldo Cassola",
    "author_email": "aldocassola@gmail.com",
    "license": "GNU Affero General Public License v3",
    "classifiers": [
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX :: BSD",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
    "keywords": "acme letsencrypt acmensse",
    "py_modules": ["acmensse"],
    "python_requires": ">=3",
    "entry_points": {"console_scripts": ["acmensse = acmensse:main"]},
}
setup(**config)
