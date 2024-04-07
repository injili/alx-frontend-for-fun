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
        ul_prev_list = False
        ol_prev_list = False
        paragraph = False
        with open(sys.argv[1], 'r', encoding='utf-8') as f:
            for line in f:
                h_match = re.match(r'^(#+)\s(.*)$', line)
                u_match = re.match(r'^-\s(.*)$', line)
                o_match = re.match(r'^\*\s?(.*)$', line)
                b_match = re.match(r'^\s*$', line)
                if h_match:
                    if ul_prev_list:
                        html_content.append("</ul>\n")
                        ul_prev_list = False
                    elif ol_prev_list:
                        html_content.append("</ol>\n")
                        ol_prev_list = False
                    h_level = len(h_match.group(1))
                    h_content = h_match.group(2)
                    html_content.append('<h{}>{}</h{}>\n'
                                        .format(h_level, h_content, h_level))
                elif u_match:
                    if not ul_prev_list:
                        html_content.append("<ul>\n")
                        ul_prev_list = True
                    u_content = u_match.group(1)
                    html_content.append("<li>{}</li>\n".format(u_content))
                elif o_match:
                    if not ol_prev_list:
                        html_content.append("<ol>\n")
                        ol_prev_list = True
                    o_content = o_match.group(1)
                    html_content.append("<li>{}</li>\n".format(o_content))

                elif b_match and paragraph:
                    html_content.append("</p>\n")
                    paragraph = False
                else:
                    if ul_prev_list:
                        html_content.append("</ul>\n")
                        ul_prev_list = False
                    elif ol_prev_list:
                        html_content.append("</ol>\n")
                        ol_prev_list = False
                    else:
                        if not paragraph:
                            html_content.append("<p>\n{}".format(line))
                            paragraph = True
                        else:
                            html_content.append("<br/>\n{}".format(line))
        if ul_prev_list:
            html_content.append("</ul>\n")
        elif ol_prev_list:
            html_content.append("</ol>\n")
        elif paragraph:
            html_content.append("</p>\n")

        with open(sys.argv[2], 'w', encoding='utf-8') as f:
            f.writelines(html_content)

        sys.exit(0)


if __name__ == "__main__":
    main()
