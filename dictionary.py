from enum import Enum

from util import selectors

# General behaviour variables
debug = False


class Selector(Enum):
    # Perfectly matching word, including accentuation
    PERFECT = 1
    # Simplified matching word, unaccented and lowercase
    SIMPLE = 2
    # Perfectly matching prefix, including accentuation
    PREFIX = 3
    # Simplified matching prefix, unaccented and lowercase
    SIMPLE_PREFIX = 4
    # Perfectly matching suffix, including accentuation
    SUFFIX = 5
    # Simplified matching suffix, unaccented and lowercase
    SIMPLE_SUFFIX = 6


def select(query, selector):
    """Returns meaning of selected word in dictionary, using the desired selector"""
    if selector == Selector.PERFECT:
        return selectors.get_match(query)
    elif selector == Selector.SIMPLE:
        return selectors.get_simple_match(query)
    elif selector == Selector.PREFIX:
        return selectors.get_prefix_match(query)
    elif selector == Selector.SIMPLE_PREFIX:
        return selectors.get_simple_prefix_match(query)
    elif selector == Selector.SUFFIX:
        return selectors.get_suffix_match(query)
    elif selector == Selector.SIMPLE_SUFFIX:
        return selectors.get_simple_suffix_match(query)