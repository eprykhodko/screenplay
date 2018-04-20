from lxml import html
from termcolor import colored

from .constants import SCRIPT_CONTAINER_XPATH


def colorize(match):
    return colored(match.group(), 'yellow')


def normalize(string):
    return ' '.join(string.split())


def process_pages(pages, regex, verbose):
    count = 0
    for page in pages:
        for line in html.fromstring(page).xpath(SCRIPT_CONTAINER_XPATH):
            sub_line, subs = regex.subn(colorize, normalize(line))
            count += subs
            if verbose and subs:
                print('--> ', sub_line)

    print('Total episodes:', len(pages))
    print('Total count:', count)
    if count is not 0:
        print(f'Per episode, average, {count / len(pages):.4f}')
