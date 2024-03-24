#!/usr/bin/python3

"""
This is a script that is built step by step in
order to convert Markdown text to HTML format
"""

import os
import sys


def main():
    """
    Converts Markdown to HTML
    """
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)
    elif not os.path.exists(sys.argv[1]):
        sys.stderr.write("Missing {}\n".format(sys.argv[1]))
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
