#!/usr/bin/env python3
"""Writing strings to Redis"""
import uuid
import redis
from typing import Union


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
