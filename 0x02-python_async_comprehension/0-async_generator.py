#!/usr/bin/env python3
"""0. Async Generator"""
from random import uniform
from typing import Generator
from time import sleep


async def async_generator() -> Generator[float, None, None]:
    """Generator that yields 10 numbers between 0-10.

    Returns:
        Generator[float, None, None]: the resulting generator.
    """
    for _ in range(10):
        sleep(1)
        yield uniform(0, 10)
