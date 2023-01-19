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
    """
    Counts the number of times a function is called
    Args:
        method: The function to be decorated
    Returns:
        The decorated function
    """
    key = method.__qualname__
    inputs = key + ":inputs"
    outputs = key + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
        Wrapper function for the decorated function
        Args:
            self: The object instance
            *args: The arguments passed to the function
            **kwargs: The keyword arguments passed to the function
        Returns:
            The return value of the decorated function
        """
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data

    return wrapper


def replay(fn: Callable) -> None:
    """
    Display the history of calls of a particular function.
    Args:
        fn (Callable): a function whose history to display
    """
    display = ''
    fnName = fn.__qualname__
    ikey = '{}:inputs'.format(fn.__qualname__)
    okey = '{}:outputs'.format(fn.__qualname__)
    cache = redis.Redis()
    if not cache.exists(ikey):
        return
    display += '{} was called {} times:\n'.format(fnName, cache.llen(ikey))
    for i, o in zip(cache.lrange(ikey, 0, -1), cache.lrange(okey, 0, -1)):
        display += "{}(*{}) -> {}\n".format(
            fnName, i.decode('utf-8'), o.decode('utf-8'))
    print(display, end="")


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
        return self.get(key, lambda s: s.decode('utf-8'))

    def get_int(self, key: str) -> Optional[bytes]:
        """
        Get a int variable from redis
        """
        return self.get(key, lambda n: int(n))
