#!/usr/bin/env python3
"""8. Complex types - functions"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Makes a function which multiplies a number by a scalar.

    Args:
        multiplier (float): a float.

    Returns:
        Callable: the resulting function.
    """
    def inner(n: float) -> float:
        return n * multiplier
    return inner
