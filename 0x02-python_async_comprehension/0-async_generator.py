#!/usr/bin/env python3
"""0. Async Generator"""
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generator that yields 10 numbers between 0-10.

    Returns:
        Generator[float, None, None]: the resulting generator.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
