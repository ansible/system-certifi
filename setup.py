#!/usr/bin/env python

from setuptools import setup, find_packages
setup(
    name="certifi",
    version="2038.12.31",
    description='Certifi replacement that uses system certificate store',
    long_description='This library provides a basic replacement for certifi, implementing '
                     'where() and contents() implementations that are hardcoded to the '
                     'Fedora/RHEL system certificate store. Intended for pip use when '
                     'system package is not suitable.',
    license='Mozilla Public License 2.0',
    packages=find_packages(),
)

