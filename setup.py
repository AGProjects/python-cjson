#!/usr/bin/python

import sys
from distutils.core import setup, Extension


sources = ['cjson.c']

setup(name         = "cjson",
      version      = "1.0.0",
      description  = "Fast JSON encoder/decoder for Python",
      author       = "Dan Pascu",
      author_email = "dan@ag-projects.com",
      license      = "GPL",
      ext_modules  = [Extension(name='cjson', sources=sources)])
