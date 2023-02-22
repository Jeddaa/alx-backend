#!/usr/bin/env python3
""" LFU caching module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """class LFU cache"""

    def __init__(self):
        """constructor function"""
        super().__init__()
        # self.used = []
        self.index = {}

    def put(self, key, item):
        """function to put the items"""
        dictlen = len(self.cache_data)
        if key is None or item is None:
            pass
        else:
            if dictlen >= BaseCaching.MAX_ITEMS and key not in self.cache_data:
                min_key = min(self.index, key=self.index.get)
                print(f"DISCARD: {min_key}")
                del self.cache_data[min_key]
                del self.index[min_key]
                # self.used.remove(min_key)
                # del self.used[0]
            if key in self.used:
                del self.used[self.used.index(key)]
            # self.used.append(key)
            self.index[key] = self.index.get(key, 0) + 1
            self.cache_data[key] = item

    def get(self, key):
        """function to get"""
        if key is not None and key in self.cache_data.keys():
            self.index[key] = self.index.get(key, 0) + 1
            # del self.used[self.used.index(key)]
            # self.used.append(key)
            return self.cache_data.get(key)
        return None
