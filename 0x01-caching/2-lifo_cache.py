#!/usr/bin/env python3
""" LIFO Caching """

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Caching system that inherits from BaseCaching"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache"""
        if key is None or item is None:
            return

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_item = self.get_last_item()
            del self.cache_data[last_item[0]]
            print("DISCARD:", last_item[0])

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]

    def get_last_item(self):
        """ Get the last item inserted into cache"""
        return list(self.cache_data.items())[-1]
