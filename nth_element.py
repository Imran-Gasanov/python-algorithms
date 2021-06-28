#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def nth_element(array, n):
    """
    Time Complexity: O(n)
    Space Complexity: O(1)

    >>> nth_element([1, 2, 3], 3)
    3
    >>> nth_element([-1, -2, 3], 2)
    -1
    >>> nth_element([-1, -2, 3, 10], 1)
    -2
    >>> nth_element([-1, -2, 3, 10], 3)
    3
    >>> nth_element([-1, -2, 3, 10], 4)
    10
    >>> nth_element([2, 4, 5, 6, 7, 8, 3, 1, 7, 4, 5], 5) == 4
    True
    >>> nth_element([2, 4, 5, 6, 7, 8, 3, 1, 7, 4, 5], 1) == 1
    True
    >>> nth_element([2, 4, 5, 6, 7, 8, 3, 1, 7, 4, 5], 2) == 2
    True
    >>> nth_element([2, 4, 5, 6, 7, 8, 3, 1, 7, 4, 5], 9) == 7
    True
    >>> nth_element([2, 4, 5, 6, 7, 8, 3, 1, 7, 4, 5], 8) == 6
    True
    >>> nth_element([2, 4, 5, 6, 7, 8, 3, 1, 7, 4, 5], 10) == 7
    True
    """
    import random
    if len(array) < n:
        raise ValueError('n must be less than the length of the array')
    if len(array) < 2:
        return array[0]
    index = random.randint(0, len(array) - 1)
    curr = array[index]
    array[index], array[-1] = array[-1], array[index]
    i = 0
    for j in range(len(array)):
        if array[j] < curr:
            array[j], array[i] = array[i], array[j]
            i += 1
    array[i], array[-1] = array[-1], array[i]
    index = i
    if index + 1 == n:
        return array[index]
    elif index < n - 1:
        return nth_element(array[index + 1:], n - index - 1)
    else:
        return nth_element(array[:index], n)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
