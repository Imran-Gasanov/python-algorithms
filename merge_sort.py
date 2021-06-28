#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
from numbers import Real


def merge(left: List[Real], right: List[Real]) -> List[Real]:
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


def merge_sort(array: List[Real]) -> List[Real]:
    """
    >>> merge_sort([10, 7, 9, 4, 6, 3, 1]) == [1, 3, 4, 6, 7, 9, 10]
    True
    >>> merge_sort([1]) == [1]
    True
    >>> merge_sort([]) == []
    True
    >>> merge_sort([1, 2, 1, 2]) == [1, 1, 2, 2]
    True
    """
    if len(array) <= 1:
        return array
    mid = int(len(array) / 2)
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    return merge(left, right)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
