#!/usr/bin/env python3
""" task 0 """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ basic cache class """

    def __init__(self):
        """
        initialization function
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        function to pass item value to dictionary
        """
        if key is None or item is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        """
        function to get
        """
        if key is None and key not in self.cache_data:
            return None
        else:
            return self.cache_data.get(key)
