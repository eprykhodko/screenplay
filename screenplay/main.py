"""
Screenplay word counter.

Usage:
    swc <show> <regexp> [options]

Options:
    -h --help        Show this screen.
    -v --verbose     Output actual lines.
"""
import re

import colorama
import docopt

from .crawler import gather_pages
from .processors import process_pages


def main():
    args = docopt.docopt(__doc__)
    show = args["<show>"].replace(" ", "-").lower()
    regex = re.compile(f'({args["<regexp>"]})', re.IGNORECASE)

    pages = gather_pages(show)
    colorama.init()
    process_pages(pages, regex, args["--verbose"])
