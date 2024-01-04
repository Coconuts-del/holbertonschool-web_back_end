#!/usr/bin/env python3
""" coroutine called async_generator """
import asyncio
from random import uniform
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """attribute a random number """
    for i in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
