#!/usr/bin/env python

""" listdir.py : List a file tree with os.walk

List all subdirectories and files from a starting directory with os.walk.
Directory names are printed with different colors to be more distinguishable.
"""

import sys
import os

__author__ = "Miroslav Vidović"
__email__ = "vidovic.miroslav@yahoo.com"
__date__ = "10.08.2017."
__version__ = "0.2"
__status__ = "Production"


def listdir(root):
    """
    List a file a file tree with os.walk

    Print the root directory content including subdirectories.

    :param root: the root directory for the file tree listing

    """
    for (thisdir, subshere, fileshere) in os.walk(root):
        print('\x1b[4;32;40m' + '[' + thisdir + ']' + '\x1b[0m')
        for fname in fileshere:
            print(fname)


def main():
    """
    Call the listdir function with the scripts first positional parameter
    sys.arargv[1] as the root directory for listdir.

    """
    try:
        listdir(sys.argv[1])
    except IndexError:
        print("No starting directory provided")


if __name__ == '__main__':
    main()
