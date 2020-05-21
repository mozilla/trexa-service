from trexa.helpers import clean_up
from trexa.helpers import get_alexa
from trexa.helpers import get_tranco
from trexa.helpers import build_trexa

"""Main entry method to manually create the Trexa list."""


def main():
    """Build the Trexa list.

    This script is intended to be run from cron, but it can be called
    manually. It will fetch the list for the day it was called,
    because that's the only free way to get the Alexa 1 million.zip.

    Just sit tight, it takes a few minutes. But you can watch a cool
    progress bar while it happens.
    """
    alexa = get_alexa()
    tranco = get_tranco()
    build_trexa(alexa, tranco)
    clean_up()


if __name__ == "__main__":
    main()
