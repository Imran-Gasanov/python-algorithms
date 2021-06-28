#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Sequence
from numbers import Number


def binary_search(array: Sequence[Number], value: Number) -> int:
    """
    Time Complexity: O(log n)
    Space Complexity: O(1)

    >>> binary_search([1, 2, 3, 4], 1) == 0
    True
    >>> binary_search([1, 1, 2, 2], 2) == 2
    True
    >>> binary_search([1, 1, 2, 2], 100500)
    Traceback (most recent call last):
        ...
    LookupError: 100500 not in array
    >>> binary_search([1, 1, 1, 2, 2], 1) == 0
    True
    """
    left, right = 0, len(array) - 1
    n = 0
    while left < right:
        mid = (left + right) // 2
        if array[mid] < value:
            left = mid
        else:
            right = mid
        n += 1
        if 2 ** n > len(array):
            if array[right] == value:
                return right
            else:
                raise LookupError(f'{value} not in array')
    return right


if __name__ == "__main__":
    import doctest

    doctest.testmod()
