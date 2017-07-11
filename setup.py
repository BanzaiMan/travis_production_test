#!/usr/bin/env python

# Project skeleton maintained at https://github.com/jaraco/skeleton

import io

import setuptools

with io.open('README.md', encoding='utf-8') as readme:
	long_description = readme.read()

params = dict()
if __name__ == '__main__':
	setuptools.setup(**params)