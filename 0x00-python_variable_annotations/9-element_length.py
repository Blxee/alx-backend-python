#!/usr/bin/env python3
"""9. Let's duck type an iterable object"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """I won't even pretend to know what this function does.

    Args:
        lst (Iterable[Sequence]): an iterable.
    Returns:
        List[Tuple[Sequence, int]]: idk
    """
    return [(i, len(i)) for i in lst]
