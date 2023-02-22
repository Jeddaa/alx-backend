#!/usr/bin/env python3
""" FIFO caching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class fifo cache"""

    def __init__(self):
        """constructor function"""
        super().__init__()

    def put(self, key, item):
        """function to put the items"""
        dictlen = len(self.cache_data)
        if key is None or item is None:
            pass
        else:
            if dictlen >= BaseCaching.MAX_ITEMS:
                # self.cache_data[self.order]
                first = next(iter(self.cache_data))
                self.cache_data.pop(first)
                print(f"DISCARD: {first}")
            self.cache_data[key] = item

    def get(self, key):
        """function to get"""
        if key is None and key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
