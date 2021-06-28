#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import Sequence, Tuple, List


def encode(sequence: Sequence) -> Tuple[List, List]:
    """
    >>> encode('1111122223333') == (['1', '2', '3'], [5, 4, 4])
    True

    >>> encode([1,2,11,11,11]) == ([1, 2, 11], [1, 1, 3])
    True

    >>> encode([1,2,1,1]) == ([1, 2, 1], [1, 1, 2])
    True

    >>> encode([1, 1, 1, 1]) == ([1], [4])
    True

    >>> encode([1, 2, 3,]) == ([1, 2, 3], [1 ,1 ,1])
    True
    """
    values = []
    counter = []
    curr = sequence[0]
    count = 1
    result = []
    for elem in sequence[1:]:
        if elem != curr:
            values.append(curr)
            counter.append(count)
            curr = elem
            count = 1
        else:
            count += 1
    values.append(curr)
    counter.append(count)
    return values, counter


if __name__ == "__main__":
    pass
