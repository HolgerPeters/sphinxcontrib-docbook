#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a skeleton file that can serve as a starting point for a Python
console script. To run this script uncomment the following line in the
console_scripts section in setup.cfg:

    hello_world = sphinxcontrib_docbook.skeleton:run

Then run `python setup.py install` which will install the command `hello_world`
inside your current environment.
Besides console scripts, the header (i.e. until _logger...) of this file can
also be used as template for Python modules.

Note: This skeleton file can be safely removed if not needed!
"""
from __future__ import division, print_function, absolute_import

import argparse
import sys
import logging

from sphinxcontrib_docbook import __version__

__author__ = "Holger Peters"
__copyright__ = "Holger Peters"
__license__ = "none"

_logger = logging.getLogger(__name__)


def parse_args(args):
    """
    Parse command line parameters

    :param args: command line parameters as list of strings
    :return: command line parameters as :obj:`argparse.Namespace`
    """
    parser = argparse.ArgumentParser(
        description="Just a Hello World demonstration")
    parser.add_argument(
        '-v',
        '--version',
        action='version',
        version='sphinxcontrib-docbook {ver}'.format(ver=__version__))
    return parser.parse_args(args)


def main(args):
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    args = parse_args(args)
    print("Hello World!")
    _logger.info("Script ends here")


def run():
    main(sys.argv[1:])


if __name__ == "__main__":
    run()
