#!/usr/bin/env python3
"""0. Async Generator"""
import random
import time
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Generator that yields 10 numbers between 0-10.

    Returns:
        Generator[float, None, None]: the resulting generator.
    """
    for _ in range(10):
        time.sleep(1)
        yield random.uniform(0, 10)
