#!/usr/bin/env python3
""" Writing strings to Redis """
import redis
import uuid
from typing import Union, Callable, Optional
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ Method that takes a single method Callable argument and returns a Callable """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Method that takes a single method Callable argument and returns a Callable """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        self._redis.rpush("{}:inputs".format(method.__qualname__), str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush("{}:outputs".format(method.__qualname__), result)
        return result
    return wrapper


class Cache:
    """ Cache class """

    def __init__(self):
        """ Constructor """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ Method that takes a data argument and returns a string """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """ Method that takes a key string argument and an optional Callable argument
            and returns the converted data """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ Method that will automatically parametrize Cache.get """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ Method that will automatically parametrize Cache.get """
        return self.get(key, int)
