#!/usr/bin/env python2

from setuptools import setup

PACKAGE = 'Kinglet'
VERSION = '0.0'

setup(
    name=PACKAGE,
    version=VERSION,
    description='Kinglet plugin for Plover',
    packages=['kinglet'],
    entry_points="""

    [plover.plugins.system]
    Kinglet = kinglet.system

    [plover.plugins.dictionary]
    Kinglet = kinglet.dictionary

    [console_scripts]
    kinglet = kinglet.test:test

    [setuptools.installation]
    eggsecutable = kinglet.test:test

    """
)

