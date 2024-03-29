#!/usr/bin/env python3
"""Writing strings to Redis"""
import uuid
import redis
from typing import Union, Callable


class Cache():
    """This stores an instance of Redis client and flushes the instance"""
    def __init__(self):
        """Same as above"""
        self._redis = redis.Redis()
        self._redis.flushdb()

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
