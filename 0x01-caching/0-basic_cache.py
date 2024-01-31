#!/usr/bin/env python3
""" BasicCache module
"""
from typing import Any
from base_caching import BaseCaching

class BaseCaching:
    """ BaseCaching class """

    def __init__(self):
        """ Initialize """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache """
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data[key]))


class BasicCache(BaseCaching):
    """ BasicCache class """

    def put(self, key: Any, item: Any) -> None:
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key: Any) -> Any:
        """ Get an item from the cache """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
