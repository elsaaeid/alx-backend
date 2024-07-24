#!/usr/bin/env python3
"""
LIFOCache Module
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    Class that implements the
    LIFO caching algorithm.
    """
    def __init__(self):
        """Initialize LIFO caching
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """Add key and item to the cache system
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.stack:
            discard = self.stack.pop()
            del self.cache_data[discard]
            print("DISCARD: {}".format(discard))
        if key and item:
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Get data from the cache system with key
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
