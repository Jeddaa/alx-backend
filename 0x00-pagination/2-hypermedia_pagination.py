#!/usr/bin/env python3
""" task 1 """

import csv
from math import ceil
from typing import List


index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """func that takes 2 arguments: page and page_size"""
        assert type(page) is int and page > 0
        assert type(page_size) is int and page_size > 0

        self.dataset()
        if self.__dataset is None:
            return []

        index_range_tuple = index_range(page, page_size)
        data_range = self.__dataset[index_range_tuple[0]:index_range_tuple[1]]

        return data_range

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """func that takes same argument as get_page
        and returns a dictionary"""
        data = self.get_page(page, page_size)

        dataset_length = len(self.dataset())
        try:
            total_pages = ceil(dataset_length / page_size)
        except Exception:
            total_pages = 0

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
