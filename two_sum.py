def two_sum(nums, target):
    """
    >>> two_sum([2, 7, 11, 15], 9) == [0, 1]
    True
    >>> two_sum([3, 2, 4], 6) == [1, 2]
    True
    >>> two_sum([3, 3], 6) == [0, 1]
    True
    """
    dict_of_add = {}
    for index, number in enumerate(nums):
        if target - number in dict_of_add:
            return [dict_of_add[target - number], index]
        else:
            dict_of_add[number] = index


if __name__ == "__main__":
    import doctest

    doctest.testmod()
