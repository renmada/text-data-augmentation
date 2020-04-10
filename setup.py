#! -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='tda',
    version='1.0',
    author='renmada',
    packages=find_packages(),
    install_requires=['synonyms'],
    package_data={
        '': ['*.txt']
    }
)
