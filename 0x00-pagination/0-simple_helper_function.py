#!/usr/bin/env python3
"""This module contains a simple helper function for pagination.
The index_range function takes in two parameters: page and page_size.
It calculates the start and end indices for a given page and page size.
The start index is calculated as (page - 1) * page_size, and the end
index is calculated as page * page_size.
The function returns a tuple containing the start and end indices.

"""


def index_range(page: int, page_size: int) -> 'tuple[int, int]':
    """A simple helper function for pagination."""
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return start_index, end_index
