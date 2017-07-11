#!/usr/bin/env python

# Project skeleton maintained at https://github.com/jaraco/skeleton

import io

import setuptools

with io.open('README.md', encoding='utf-8') as readme:
	long_description = readme.read()

name = 'jaraco.mongodb'
description = 'Routines and classes supporting MongoDB environments'

params = dict(
	name=name,
	use_scm_version=True,
	author="Jason R. Coombs",
	author_email="jaraco@jaraco.com",
	description=description or name,
	long_description=long_description,
	url="https://github.com/jaraco/" + name,
	packages=setuptools.find_packages(),
	include_package_data=True,
	namespace_packages=name.split('.')[:-1],
	python_requires='>=2.7,!=3.0,!=3.1,!=3.2',
	install_requires=[
		'pymongo>=3.0',
		'six',
		'python-dateutil',
		'jaraco.services',
		'portend',
		'jaraco.itertools>=1.8',
		'jaraco.functools',
		'jaraco.ui',
		'jaraco.context',
		'more_itertools',
		'jaraco.logging',
		'jaraco.timing',
		'pytimeparse',
		'jaraco.collections>=1.5',
	],
	extras_require={
		'testing': [
			'pytest>=2.8',
			'pytest-sugar',
			'cherrypy',
		],
		'docs': [
			'sphinx',
			'jaraco.packaging>=3.2',
			'rst.linker>=1.9',
			'cherrypy',
		],
	},
	setup_requires=[
		'setuptools_scm>=1.15.0',
	],
	classifiers=[
		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 2.7",
		"Programming Language :: Python :: 3",
		"Framework :: Pytest",
	],
	entry_points={
		'pytest11': [
			'MongoDB = jaraco.mongodb.fixtures',
		],
		'pmxbot_handlers': [
			'create in MongoDB shard = jaraco.mongodb.pmxbot',
		],
	},
)
if __name__ == '__main__':
	setuptools.setup(**params)