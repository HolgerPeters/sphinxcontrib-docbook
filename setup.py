from setuptools import setup

import sys

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []

setup(name="sphinxcontrib_docbook",
      use_scm_version=True,
      author='Holger Peters',
      setup_requires=['setuptools_scm'] + pytest_runner,
      tests_require=['pytest',
                     'pytest-cov',
                     'pytest-flake8',
                     'hypothesis-pytest',
                     'hypothesis'],
      packages=['sphinxcontrib_docbook'])
