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


def replay(fn: Callable) -> None:
    '''Displays the call history of a Cache class' method.
    '''
    if fn is None or not hasattr(fn, '__self__'):
        return
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return
    fxn_name = fn.__qualname__
    in_key = '{}:inputs'.format(fxn_name)
    out_key = '{}:outputs'.format(fxn_name)
    fxn_call_count = 0
    if redis_store.exists(fxn_name) != 0:
        fxn_call_count = int(redis_store.get(fxn_name))
    print('{} was called {} times:'.format(fxn_name, fxn_call_count))
    fxn_inputs = redis_store.lrange(in_key, 0, -1)
    fxn_outputs = redis_store.lrange(out_key, 0, -1)
    for fxn_input, fxn_output in zip(fxn_inputs, fxn_outputs):
        print('{}(*{}) -> {}'.format(
            fxn_name,
            fxn_input.decode("utf-8"),
            fxn_output,
        ))


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
