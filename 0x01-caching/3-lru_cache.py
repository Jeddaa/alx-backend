#!/usr/bin/env python3
""" LRU caching module
"""
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """class LRU cache"""

    def __init__(self):
        """constructor function"""
        super().__init__()
        self.cache_data = OrderedDict(self.cache_data)

    def put(self, key, item):
        """function to put the items"""
        dictlen = len(self.cache_data)
        if key is None or item is None:
            pass
        else:
            if dictlen >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                last = self.cache_data.popitem(last=False)
                print(f"DISCARD: {last[0]}")
            self.cache_data[key] = item

    def get(self, key):
        """function to get"""
        if key is None and key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
