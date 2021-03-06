#!/usr/bin/env python
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

version = '0.0.1'
setup(
    name='puppetdb',
    version=version,
    description='Python client for interacting with PuppetDB',
    url='http://github.com/arcus-io/puppetdb-python',
    download_url=('https://github.com/arcus-io/'
                  'puppetdb-python/archive/%s.tar.gz' % version),
    author='Arcus, Inc.',
    author_email='support@arcus.io',
    keywords=['puppet', 'puppetdb'],
    license='Apache 2.0',
    packages=['puppetdb','puppetdb/v2'],
    install_requires = [ 'requests' ],
    test_suite='tests.all_tests',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        ]
)
