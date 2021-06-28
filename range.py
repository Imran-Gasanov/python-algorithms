#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable, Sequence, Iterator


class RangeIterator(Iterator):

    def __init__(self, rangeobj):
        self.rangeobj = rangeobj
        self.curr = self.rangeobj.start

    def __next__(self):
        stop = self.rangeobj.stop
        step = self.rangeobj.step
        value = self.curr
        self.curr += step
        if value < stop and step > 0:
            return value
        elif value > stop and step < 0:
            return value

        else:
            raise StopIteration

    def __iter__(self):
        if not hasattr(self.rangeobj, "__getitem__"):
            raise TypeError(f"{self.__class__.__name__} "
                            f"object is not iterable")
        return self


class Range(Sequence, Iterable):

    def __init__(self, *args):
        if len(args) == 1:
            self.start = 0
            self.stop = args[0]
            self.step = 1
        if len(args) == 2:
            self.start = args[0]
            self.stop = args[1]
            self.step = 1
        if len(args) == 3:
            self.start = args[0]
            self.stop = args[1]
            self.step = args[2]
        if len(args) > 3:
            raise TypeError(f'range expected at most 3 arguments, got {len(args)}')
        for elem in [self.start, self.stop, self.step]:
            if isinstance(elem, float):
                raise TypeError("'float' object cannot be interpreted as an integer")
            if isinstance(elem, str):
                raise TypeError("'str' object cannot be interpreted as an integer")
        if self.step == 0:
            raise ValueError('range() arg 3 must not be zero', )

    def __eq__(self, other):
        if not isinstance(other, Range):
            return False
        if self.start == other.start and self.stop == other.stop and self.step == other.step:
            return True
        return False

    def __iter__(self):
        if not hasattr(self, "__getitem__"):
            raise TypeError(f"{self.__class__.__name__} "
                            f"object is not iterable")
        return RangeIterator(self)

    def __repr__(self):
        if self.step == 1:
            return f'range({self.start}, {self.stop})'
        else:
            return f'range({self.start}, {self.stop}, {self.step})'

    __str__ = __repr__

    def __getitem__(self, key):
        if abs((self.stop - self.start) / self.step) < key:
            raise IndexError('range object index out of range')
        return self.start + key * self.step

    def __len__(self):
        start = self.start
        step = self.step
        stop = self.stop
        curr_len = 1
        if stop > start and step <= 0:
            return 0
        if stop < start and step >= 0:
            return 0
        while True:
            start += step
            curr_len += 1
            if abs(stop - start) <= abs(step):
                break
        return curr_len

    def __contains__(self, value):
        for element in self:
            if element == value:
                return True

        return False


if __name__ == "__main__":
    import doctest

    doctest.testmod()
