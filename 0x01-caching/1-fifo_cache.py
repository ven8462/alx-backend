#!/usr/bin/env python3
""" FIFO caching """

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFO cache class """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD:", first_key)

        self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
