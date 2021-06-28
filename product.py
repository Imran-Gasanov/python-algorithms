#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class OnlyProductInteger:
    def __init__(self, value):
        self._value = value

    def __str__(self):
        return str(self._value)

    def __eq__(self, other):
        return self._value == other._value

    def __mul__(self, other):
        return OnlyProductInteger(self._value * other._value)

    __repr__ = __str__


def product(array):
    """
    Time Complexity: O(n)
    Space Complexity: O(n)
    >>> product([OnlyProductInteger(1), OnlyProductInteger(2), OnlyProductInteger(3)]) == [OnlyProductInteger(6), OnlyProductInteger(3), OnlyProductInteger(2)]
    True
    >>> product([OnlyProductInteger(2), OnlyProductInteger(3), OnlyProductInteger(4)]) == [OnlyProductInteger(12), OnlyProductInteger(8), OnlyProductInteger(6)]
    True
    >>> product([OnlyProductInteger(2), OnlyProductInteger(3), OnlyProductInteger(4), OnlyProductInteger(5)]) == [OnlyProductInteger(60), OnlyProductInteger(40), OnlyProductInteger(30), OnlyProductInteger(24)]
    True
    """
    count_pref = OnlyProductInteger(1)
    count_suff = OnlyProductInteger(1)
    prefix, suffix = [OnlyProductInteger(1)], [OnlyProductInteger(1)]
    for elem in array[:len(array) - 1]:
        count_pref *= elem
        prefix.append(count_pref)
    for curr in list(reversed(array))[:len(array) - 1]:
        count_suff *= curr
        suffix.append(count_suff)
    result = []
    j = len(suffix) - 1
    for i in range(len(prefix)):
        result.append(prefix[i] * suffix[j])
        j -= 1
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
