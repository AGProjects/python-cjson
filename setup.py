#!/usr/bin/python

from distutils.core import setup, Extension

__version__ = "1.2.1"

macros = [('MODULE_VERSION', __version__)]

setup(name         = "python-cjson",
      version      = __version__,
      author       = "Dan Pascu",
      author_email = "dan@ag-projects.com",
      url          = "https://github.com/AGProjects/python-cjson",
      description  = "Fast JSON encoder/decoder for Python",
      long_description = open('README').read(),
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
      ext_modules  = [
        Extension(name='cjson', sources=['cjson.c'], define_macros=macros)
      ]
)
