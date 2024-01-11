#!/usr/bin/env python3
"""7. Complex types - string and int/float to tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of k and v ^ 2

    Args:
        k (str): a string.
        v (int | float): a number.

    Returns:
        tuple[str, float]: the result tuple.
    """
    return (k, v ** 2)
