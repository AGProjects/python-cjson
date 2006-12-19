#!/usr/bin/python

import sys
from distutils.core import setup, Extension

setup(name         = "python-cjson",
      version      = "1.0.0",
      author       = "Dan Pascu",
      author_email = "dan@ag-projects.com",
      url          = "http://ag-projects.com/",
      download_url = "http://cheeseshop.python.org/pypi/python-cjson/1.0.0",
      description  = "Fast JSON encoder/decoder for Python",
      long_description = open('README', 'r').read(),
      license      = "LGPL",
      platforms    = ["Platform Independent"],
      classifiers  = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules"
      ],
      ext_modules  = [Extension(name='cjson', sources=['cjson.c'])])
