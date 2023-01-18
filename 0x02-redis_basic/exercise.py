#!/usr/bin/env python3
"""
Redis module
"""

import redis
from typing import Union
from uuid import uuid4


class Cache:
    """
    Class representing Redis cache

    Args:

    Attributes:
        _redis : redis instance

    """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = uuid4()
        self._redis.set(key, data)
        return key
