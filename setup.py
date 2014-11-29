#!/usr/bin/env python

from setuptools import setup

setup(name='plumbing-iplookup-server',
      version='0.2',
      description='',
      author='Cooper Hewitt Smithsonian Design Museum',
      url='https://github.com/cooperhewitt/plumbing-iplookup-server',
      requires=[
      ],
      dependency_links=[
          'https://github.com/cooperhewitt/py-cooperhewitt-flask/tarball/master#egg=cooperhewitt.flask-0.35',
      ],
      install_requires=[
          'cooperhewitt.flask',
          'pygeoip',
      ],
      packages=[],
      scripts=[
          'scripts/iplookup-server.py',
      ],
      download_url='https://github.com/cooperhewitt/plumbing-iplookup-server/tarball/master#egg=0.22',
      license='BSD')
