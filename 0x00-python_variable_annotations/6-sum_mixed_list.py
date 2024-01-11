#!/usr/bin/env python3
"""6. Complex types - mixed list"""


def sum_mixed_list(mxd_lst: list[int | float]) -> float:
    """Sums up a list of numbers.

    Args:
        mxd_lst (list[int | float]): a list of numbers.

    Returns:
        float: the sum of mxd_lst.
    """
    return sum(mxd_lst)
