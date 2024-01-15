#!/usr/bin/env python3
"""4. Tasks"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """spawns wait_random n times with the specified max_delay.

    Args:
        n (int): amount of times to spawn wait_random.
        max_delay (int): maximun delay amount (in seconds).
    Returns:
        list[float]: list of all the delays.
    """
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*coroutines))
