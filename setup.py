from setuptools import setup, find_packages

import terms


setup(
    name='terms',
    version=terms.version,
    packages=find_packages(),
    test_suite='terms.tests',
)
