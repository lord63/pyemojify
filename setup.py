#!/usr/bin/env python
#  -*- coding: utf-8 -*-

from setuptools import setup

import pyemojify


try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    with open('README.md') as f:
        long_description = f.read()


setup(
    name='pyemojify',
    version=pyemojify.__version__,
    description=('Substitutes emoji aliases (like :sparkling_heart:) to '
                 'emoji raw characters.'),
    long_description=long_description,
    url='http://github.com/lord63/pyemojify',
    author='lord63',
    author_email='lord63.j@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
    keywords='emoji cli',
    packages=['pyemojify'],
    install_requires=[
        'click>=4.1'
    ],
    include_package_data=True,
    entry_points={
        'console_scripts': [
            'pyemojify=pyemojify.main:cli']
    }
)
