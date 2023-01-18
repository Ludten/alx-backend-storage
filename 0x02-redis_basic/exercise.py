#!/usr/bin/env python3
"""
Redis module
"""

from functools import wraps
import redis
from typing import Any, Optional, Union, Callable
from uuid import uuid4


def count_calls(method: Callable) -> Callable:
    """
    take a single method Callable argument and
    returns a Callable
    """
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        '''Invokes the given method after incrementing its call counter.
        '''
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


def call_history(method: Callable) -> Callable:
    '''Tracks the call details of a method in a Cache class.
    '''
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        '''Returns the method's output after storing its inputs and output.
        '''
        in_key = '{}:inputs'.format(method.__qualname__)
        out_key = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return invoker


def replay(method: Callable) -> None:
    """
    Replays the history of a function
    Args:
        method: The function to be decorated
    Returns:
        None
    """
    name = method.__qualname__
    cache = redis.Redis()
    calls = cache.get(name).decode("utf-8")
    print("{} was called {} times:".format(name, calls))
    inputs = cache.lrange(name + ":inputs", 0, -1)
    outputs = cache.lrange(name + ":outputs", 0, -1)
    for i, o in zip(inputs, outputs):
        print("{}(*{}) -> {}".format(name, i.decode('utf-8'),
                                     o.decode('utf-8')))


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

    @call_history
    @count_calls
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
