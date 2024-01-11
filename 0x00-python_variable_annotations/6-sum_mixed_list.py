#!/usr/bin/env python3
"""6. Complex types - mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums up a list of numbers.

    Args:
        mxd_lst (list[int | float]): a list of numbers.

    Returns:
        float: the sum of mxd_lst.
    """
    return sum(mxd_lst)
