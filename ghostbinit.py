#!/usr/bin/python3
# ghostbinit.py
# Copyright (c) 2016 Chisight
# Licensed under the MIT License
# https://opensource.org/licenses/MIT

import paste_ghostbin
import sys
import argparse

def main():
    """read stdin, write paste url to stdout, errors to stderr, options on command line, see -h
    """
    parser = argparse.ArgumentParser(description='Paste to ghostbin.com from stdin.', 
             epilog='Example: echo "paste this"|./ghostbinit.py --title "my paste" --expire 10m')
    parser.add_argument('-e','--expire', dest='expiration', action='store', nargs=1,
                        help='paste longevity, valid suffixes: ns/us/ms/s/m/h/d/w (-1 for forever)')
    parser.add_argument('-l','--lang', dest='language', action='store', default=None, nargs=1,
                        help='language text is written in, i.e. Python3 or C')
    parser.add_argument('-t','--title', dest='title', action='store', default=None, nargs=1,
                        help='an optional title for your paste')
    parser.add_argument('-p','--passwd', dest='passwd', action='store', default=None, nargs=1,
                        help='protects your pastes, readers will be prompted for the password')
    parser.add_argument('--http', dest='http', action='store_const', const = 'http', default=None,
                        help='use http rather than https, ignored if --passwd is used')
    parser.add_argument('-f','--noff', dest='nocookies', action='store_true',
                        help='do not attempt to read firefox\'s ghostbin.com cookies')
    args=parser.parse_args()

    if args.http is not None and args.passwd is not None:
        print("--http not used")
        args.http = None

    text = sys.stdin.read()

    if not args.nocookies:
        paste_ghostbin.getFFCookies()
    print( paste_ghostbin.ghostpaste(text, args.expiration, args.language, args.title, args.passwd, args.http))


if __name__ == "__main__":
    main()

