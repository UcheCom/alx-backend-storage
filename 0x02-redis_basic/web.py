#!/usr/bin/env python3
"""Module with tools for request caching and tracking.
"""
import redis
import requests
from datetime import timedelta


def get_page(url: str) -> str:
    """Returns the content of a URL after caching the request's response,
    and tracking the request.
    """
    if url is None or len(url.strip()) == 0:
        return ""
    rd = redis.Redis()
    key = 'result:{}'.format(url)
    k_url = 'count:{}'.format(url)
    result = rd.get(key)
    if result is not None:
        rd.incr(k_url)
        return result
    result = requests.get(url).content.decode('utf-8')
    rd.setex(key, timedelta(seconds=10), result)
    return result
