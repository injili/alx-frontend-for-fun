#!/usr/bin/python3

"""
This is a script that is built step by step in
order to convert Markdown text to HTML format

Usage:
    ./markdown2html.py [input.md] [input.html]
"""

import re
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
        html_content = []
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            for line in f:
                match = re.match(r'^(#+)\s(.*)$', line)
                if match:
                    h_level = len(match.group(1))
                    h_content = match.group(2)
                    html_content.append('<h{}>{}</h{}>\n'
                                        .format(h_level, h_content, h_level))
                else:
                    html_content.append(line)

        with open(sys.argv[2], 'w', encoding='utf-8') as f:
            f.writelines(html_content)

        sys.exit(0)


if __name__ == "__main__":
    main()
