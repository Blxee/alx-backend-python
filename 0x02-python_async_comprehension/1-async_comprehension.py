#!/usr/bin/env python3
"""1. Async Comprehensions"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns a list of 1 random number floats in range 0-10.

    Returns:
        list[float]: the generated list of floats.
    """
    return [i async for i in async_generator()]
