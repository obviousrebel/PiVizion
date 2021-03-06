#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://pivizion.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

setup(
    name='pivizion',
    version='0.1.0',
    description='Python package for image recognition using Google Cloud Vision and Text to speech.',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Joshua Alexander',
    author_email='itzjoshy8@gmail.com',
    url='https://github.com/obviousrebel/pivizion',
    packages=[
        'pivizion',
    ],
    package_dir={'pivizion': 'pivizion'},
    include_package_data=True,
    python_requires='>3.6',
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='pivizion',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    entry_points = {
      'console_scripts': [
          'pivizion = pivizion.pivizion:main',
      ]
    },
)
