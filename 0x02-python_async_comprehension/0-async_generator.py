#!/usr/bin/env python3
"""0. Async Generator"""
from random import uniform
from typing import AsyncGenerator
from time import sleep


async def async_generator() -> AsyncGenerator[float, None]:
    """Generator that yields 10 numbers between 0-10.

    Returns:
        Generator[float, None, None]: the resulting generator.
    """
    for _ in range(10):
        sleep(1)
        yield uniform(0, 10)
