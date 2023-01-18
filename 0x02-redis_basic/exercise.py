#!/usr/bin/env python3
"""
Redis module
"""

import redis
from typing import Optional, Union, Callable
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
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(
        self, key: str, fn: Union[Callable[[Union[bytes, None]],
                                           Union[bytes, None, bytes]],
                                  None] = None
    ) -> Union[Optional[bytes], bytes]:
        if fn is not None:
            return fn(self._redis.get(key))
        return self._redis.get(key)

    def get_str(self, key: str) -> Optional[bytes]:
        """
        Get a int variable from redis
        """
        return self.get(key, str)

    def get_int(self, key: str) -> Optional[bytes]:
        """
        Get a int variable from redis
        """
        return self.get(key, int)
