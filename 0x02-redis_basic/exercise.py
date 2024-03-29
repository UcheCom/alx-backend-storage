#!/usr/bin/env python3
"""Writing strings to Redis"""
import uuid
import redis
from typing import Union, Callable, Optional
from functools import wraps


def replay(method: Callable) -> None:
    """This displays the history of calls of a particular function"""
    rd = redis.Redis()
    name = method.__qualname__
    count = rd.get(name)
    try:
        count = int(count.decode("utf-8"))
    except Exception:
        count = 0

    print("{} was called {} times:".format(name, count))
    inputs = rd.lrange("{}:inputs".format(name), 0, -1)
    outputs = rd.lrange("{}:outputs".format(name), 0, -1)

    for ip, ou in zip(inputs, outputs):
        try:
            ip = ip.decode("utf-8")
        except Exception:
            ip = ""

        try:
            ou = ou.decode("utf-8")
        except Exception:
            ou = ""

        print("{}(*{}) -> {}".format(name, ip, ou))


def call_history(method: Callable) -> Callable:
    """Stores the history of inputs and outputs for a particular function"""
    key_in = method.__qualname__ + ":inputs"
    key_ou = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """This is wrapper func for the decorator"""
        inputs = str(args)
        self._redis.rpush(key_in, inputs)
        outputs = str(method(self, *args, **kwargs))
        self._redis.rpush(key_ou, outputs)

        return outputs

    return wrapper


def count_calls(method: Callable) -> Callable:
    """This decorator used to count instances"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function for decorator"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache():
    """This stores an instance of Redis client and flushes the instance"""
    def __init__(self):
        """Same as above"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """This takes a data arg and returns a string"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int]:
        """This convert the data back to the desired format."""
        val = self._redis.get(key)
        if fn:
            val = fn(val)
        return val

    def get_str(self, key: str) -> str:
        """This Parametrizes Cache.get with the correct conversion function"""
        val = self._redis.get(key)
        return val.decode("utf-8")

    def get_int(self, key: str) -> int:
        """Also Parametrizes Cache.get with the correct conversion function"""
        val = self._redis.get(key)
        try:
            val = int(val.decode("utf-8"))
        except Exception:
            val = 0
        return val
