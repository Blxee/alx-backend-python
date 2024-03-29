#!/usr/bin/env python3
"""10. Duck typing - first element of a sequence"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element if it exists.

    Args:
        lst (Sequence[any]): a list.
    Returns:
        any | None: first element or None.
    """
    if lst:
        return lst[0]
    else:
        return None
