#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict
from .0_simple_helper_function import index_range

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        assert index is None or (isinstance(index, int) and index >= 0), "Index must be a non-negative integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must be a positive integer"

        indexed_dataset = self.indexed_dataset()

        if index is None:
            index = 0
        else:
            assert index < len(indexed_dataset), "Index out of range"

        start_index, end_index = index_range(index, page_size)

        if start_index >= len(indexed_dataset):
            return {
                'index': index,
                'next_index': index,
                'page_size': page_size,
                'data': []
            }

        data = [indexed_dataset[i] for i in range(start_index, end_index) if i in indexed_dataset]

        next_index = end_index if end_index < len(indexed_dataset) else index

        return {
            'index': index,
            'next_index': next_index,
            'page_size': page_size,
            'data': data
        }
