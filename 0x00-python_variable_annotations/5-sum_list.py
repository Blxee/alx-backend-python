#!/usr/bin/env python3
"""5. Complex types - list of floats"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Sums up a list of floats.

    Args:
        input_list (list[float]@): a list of floats.

    Returns:
        float: the sum of input_list
    """
    return sum(input_list)
