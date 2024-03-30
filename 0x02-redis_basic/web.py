#!/usr/bin/env python3
"""Implements a get_page function and
   uses the requests module to obtain the HTML
   content of a particular URL and returns it
"""

import requests
import redis
from functools import wraps
from typing import Callable

rd = redis.Redis()
exp_time = 10


def count_call_access(fn: Callable) -> Callable:
    """This decorator counts url access"""

    @wraps(fn)
    def wrapper(url):
        """Wrapper func for the decorator"""
        key = "cached:" + url
        if rd.get(key):
            return rd.get(key).decode("utf-8")

        k_url = "count:" + url
        html = fn(url)
        rd.incr(k_url)
        rd.setex(key, exp_time, html)

        return html

    return wrapper


@count_call_access
def get_page(url: str) -> str:
    """Obtains the HTML content of a particular URL and returns it."""

    resp = requests.get(url)
    return resp.text


if __name__ == "__main__":
    url = 'http://slowwly.robertomurray.co.uk'
    print(get_page(url))
