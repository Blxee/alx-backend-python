#!/usr/bin/env python3
"""0. The basics of async"""
from random import random
from time import sleep


async def wait_random(max_delay: int=10) -> float:
    """waits for a random delay between 0 and max_delay.

    Args:
        max_delay (int): maximun delay amount (in seconds).
    Returns:
        float: time (in seconds) it had to wait.
    """
    seconds = random() * max_delay
    sleep(seconds)
    return seconds
