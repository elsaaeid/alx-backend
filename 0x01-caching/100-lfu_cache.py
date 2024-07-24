#!/usr/bin/env python3
"""LFUCache Module"""

BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Class that inherits from
    BaseCaching and is a caching system
    """
    def __init__(self):
        """Initialize"""
        super().__init__()
        self.frequency_list = defaultdict(OrderedDict)
        self.key_node = {
        self.frequency = {}

    def put(self, key, item):
        """
        Add item to cache system
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.update_frequency_of_key(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.discard_least_frequently_used_item()

            self.cache_data[key] = item
            self.frequency[key] = [1]
            self.add_key_to_frequency_list(key)

    def get(self, key):
        """
        Get item from cache system
        """
        if key is None or key not in self.cache_data:
            return None

        self.update_frequency_of_key(key)
        return self.cache_data[key]

    def update_frequency_of_key(self, key):
        """
        Update frequency key
        """
        frequency = self.frequency[key][0]
        del self.frequency_list[frequency][key]
        self.frequency[key][0] += 1
        self.add_key_to_frequency_list(key)

    def add_key_to_frequency_list(self, key):
        """
        Add key to frequency list
        """
        frequency = self.frequency[key][0]
        self.frequency_list[frequency][key] = None
        self.key_node[key] = next(iter(self.frequency_list[frequency]))

    def discard_least_frequently_used_item(self):
        """
        Delete min key which used frequently
        """
        min_frequency = min(self.frequency_list.keys())
        key_to_discard = self.key_node[min_frequency]
        del self.cache_data[key_to_discard]
        del self.frequency[key_to_discard]
        del self.key_node[key_to_discard]
        del self.frequency_list[min_frequency][key_to_discard]
        print("DISCARD:", key_to_discard)
