#!/usr/bin/env python3
"""11. More involved type annotations"""
from typing import Mapping, Any, TypeVar, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None
                     ) -> Union[Any, T]:
    """Sets a value safely in a dict

    Returns:
        the value
    """
    if key in dct:
        return dct[key]
    else:
        return default
