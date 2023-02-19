#!/usr/bin/env python3
""" task 0 """


def index_range(page: int, page_size: int) -> tuple:
    """ function returns a tuple of size two
    containing a start index and an end index"""

    end_index = page * page_size
    start_index = end_index - page_size

    return (start_index, end_index)
