#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding='utf-8').read()


setup(
    name='pytest-Inomaly',
    version='0.2.3',
    author='Oliver Marks',
    author_email='oly@digitaloctave.com',
    maintainer='Oliver Marks',
    maintainer_email='oly@digitaloctave.com',
    license='MIT',
    url='https://github.com/olymk2/pytest-Inomaly',
    description='A simple image diff plugin for pytest',
    long_description=read('README.md'),
    py_modules=['pytest_inomaly'],
    setup_requires=['numpy', 'scipy'],
    install_requires=['pytest>=2.9.2', 'scipy'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Pytest',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: MIT License',
    ],
    entry_points={
        'pytest11': [
            'inomaly = pytest_inomaly',
        ],
    },
)
