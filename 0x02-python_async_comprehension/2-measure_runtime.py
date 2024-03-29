#!/usr/bin/env python3
"""2. Run time for four parallel comprehensions"""
import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the time of 4 async_comprehension() calls.

    Returns:
        float: total time.
    """
    start = time()
    await asyncio.gather(*[async_comprehension()] * 4)
    end = time()
    return (end - start)
