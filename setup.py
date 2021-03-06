#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path
from setuptools import setup


def version():
    init = path.join(path.dirname(__file__), 'leankitmocks', '__init__.py')
    line = list(filter(lambda l: l.startswith('__version__'), open(init)))[0]
    return line.split('=')[-1].strip(" '\"\n")


setup(name='leankitmocks',
      packages=['leankitmocks'],
      version=version(),
      author='Guillermo Guirao Aguilar',
      author_email='contact@guillermoguiraoaguilar.com',
      url='https://github.com/bitelio/leankitmocks',
      install_requires=['leankit'],
      include_package_data=True,
      classifiers=['Programming Language :: Python :: 3.6'])
