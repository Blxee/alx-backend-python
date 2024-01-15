#!/usr/bin/env python3
"""3. Tasks"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates a task from wait_random coroutine.

    Args:
        max_delay (int): maximun delay amount (in seconds).
    Returns:
        asyncio.Task: the newly created task object.
    """
    return asyncio.create_task(wait_random(max_delay))
