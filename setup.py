#!/usr/bin/env python
# vim: sw=4 expandtab:
# pylint: disable=no-name-in-module
# pylint: disable=import-error

"""The haddock module have all glue code
between git/gerrit/go.cd/zuul and Jenkins
"""

from distutils.core import setup

setup(name='haddock',
      version='0.5',
      description='Zenuity Continuous Everything Toolchain',
      author='Zenuity',
      author_email='haddock@zenuity.com',
      url='https://www.zenuity.com/',
      packages=['haddock'], scripts=['scripts/ngsetupgocd.py',
                                     'scripts/ngsetupjenkins.py',
                                     'scripts/ngsetupzuul.py',
                                     'scripts/py_filter',
                                    ]
     )
