from setuptools import setup, find_packages

import terms


setup(
    name='terms',
    version=terms.version,
    packages=find_packages(),
    test_suite='terms.tests',
    install_requires=[
        'parsing==0.1',
    ],
    dependency_links=[
        'https://github.com/davesque/parsing.py/tarball/master#egg=parsing-0.1',
    ],
)
