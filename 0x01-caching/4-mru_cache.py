#!/usr/bin/env python3
"""
MRUCache Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    Class that inherits from
    BaseCaching and is a caching system
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.access_tracker = []

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = self.access_tracker.pop()
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        self.access_tracker.insert(0, key)

    def get(self, key):
        """
        Get an item from the cache
        """
        if key is None or key not in self.cache_data:
            return None

        self.access_tracker.remove(key)
        self.access_tracker.insert(0, key)
        return self.cache_data[key]
