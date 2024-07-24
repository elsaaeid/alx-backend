#!/usr/bin/env python3
"""LFUCache Module"""
from collections import defaultdict, deque
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    Class that inherits from
    BaseCaching and is a caching system
    """
    def __init__(self):
        """Initialize"""
        super().__init__()
        '''Dictionary to store
        the frequency of each key
        '''
        self.frequency = defaultdict(int)
        '''Dictionary to store
        keys based on frequency
        '''
        self.frequency_queue = defaultdict(deque)
        '''
        Minimum frequency in the cache
        '''
        self.min_frequency = 0

    def put(self, key, item):
        """
        Add item to cache system
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.discard_least_frequently_used_item()

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.frequency_queue[1].append(key)
            self.min_frequency = 1

    def get(self, key):
        """
        Get item from cache system
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.update_frequency_queue(key)
        return self.cache_data[key]

    def discard_least_frequently_used_item(self):
        """
        Delete min key which used frequently
        """
        while not self.frequency_queue[self.min_frequency]:
            self.min_frequency += 1

        key_to_discard = self.frequency_queue[self.min_frequency].popleft()
        del self.cache_data[key_to_discard]
        del self.frequency[key_to_discard]
        print("DISCARD:", key_to_discard)

    def update_frequency_queue(self, key):
        """
        Update frequency key
        """
        frequency = self.frequency[key]
        self.frequency_queue[frequency-1].remove(key)
        self.frequency_queue[frequency].append(key)
        if not self.frequency_queue[self.min_frequency]:
            self.min_frequency += 1
