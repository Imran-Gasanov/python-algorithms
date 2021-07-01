def subarraysDivByK(nums, k):
    """
    >>> subarraysDivByK([4,5,0,-2,-3,1], 5) == 7
    True
    ([4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3])
    """
    sums = []
    result = 0
    for i in range(len(nums)):
        sums.append(sum(nums[:i + 1]))
    for index, summ in enumerate(sums):
        if summ % k == 0:
            result += 1
        for summ2 in sums[index + 1:]:
            if (summ2 - summ) % k == 0:
                result += 1
    return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()
