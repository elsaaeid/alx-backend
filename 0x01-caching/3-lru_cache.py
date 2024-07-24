#!/usr/bin/python3
"""
LRUCache Module
"""

BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    Class that inherits from BaseCaching 
    and is a caching system
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()
        self.lru_keys = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Discard the least recently used item (LRU algorithm)
            if self.lru_keys:
                discarded_key = self.lru_keys.pop(0)
                del self.cache_data[discarded_key]
                print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item
        if key in self.lru_keys:
            self.lru_keys.remove(key)
        self.lru_keys.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        if key in self.lru_keys:
            self.lru_keys.remove(key)
        self.lru_keys.append(key)

        return self.cache_data[key]
