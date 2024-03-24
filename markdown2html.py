#!/usr/bin/python3

"""
This is a script that is built step by step in
order to convert Markdown text to HTML format
"""

import sys


def main():
    """
    Converts Markdown to HTML
    """
    if len(sys.args) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html")
        sys.exit(1)
    else:
        sys.exit(0)


if __name__ == "__main__":
    main()
