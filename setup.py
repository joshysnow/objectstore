#!/usr/bin/env python3
from setuptools import setup

setup(
    name='objectstore',
    verison='0.0.1',
    author='Joshinux',
    description='A simple observer pattern implementation in Python.',
    license='Apache 2.0',
    url='',
    packages=['objectstore'],
    extras_requires={
        'test': [
            'pytest'
        ]
    }
)
