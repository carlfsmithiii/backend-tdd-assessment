#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility"""

__author__ = "Carl Smith"


import argparse
import sys


def create_parser():
    """Creates and returns an argparse cmd line option parser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.",
        usage='%(prog)s [-h] [-u] [-l] [-t] text')
    parser.add_argument('text', nargs="+", help="text to be manipulated")
    parser.add_argument('-u', '--upper', action="store_true",
                        help='convert text to uppercase')
    parser.add_argument('-l', '--lower', action="store_true",
                        help='convert text to lowercase')
    parser.add_argument('-t', '--title', action="store_true",
                        help='convert text to titlecase')
    return parser


def main(args):
    """Implementation of echo"""
    output_string = ' '.join(args.text)
    if args.upper:
        output_string = output_string.upper()
    if args.lower:
        output_string = output_string.lower()
    if args.title:
        output_string = output_string.title()

    print(output_string)


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args(sys.argv[1:])
    main(args)
