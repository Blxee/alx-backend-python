#!/usr/bin/env python3
"""1. Let's execute multiple coroutines at the same time with async"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list[float]:
    """spawns wait_random n times with the specified max_delay.

    Args:
        n (int): amount of times to spawn wait_random.
        max_delay (int): maximun delay amount (in seconds).
    Returns:
        list[float]: list of all the delays.
    """
    coroutines = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*coroutines))
