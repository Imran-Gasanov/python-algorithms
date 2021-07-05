def maxSumDivThree(nums):
    """
    >>> maxSumDivThree([3,6,5,1,8]) == 18
    True
    >>> maxSumDivThree([1,2,3,4,4]) == 12
    True
    """
    rem1 = []
    rem2 = []
    all_sum = sum(nums)
    rem = all_sum % 3
    if rem == 0:
        return sum(nums)
    for num in nums:
        if num % 3 == 1:
            rem1.append(num)
    for num in nums:
        if num % 3 == 2:
            rem2.append(num)
    if rem == 1:
        a = 0
        b = 0
        if len(rem1) > 0:
            a = all_sum - min(rem1)
        if len(rem2) > 1:
            b = all_sum - sum(sorted(rem2)[:2])
        return max(a, b)
    if rem == 2:
        a = 0
        b = 0
        if len(rem2) > 0:
            a = all_sum - min(rem2)
        if len(rem1) > 1:
            b = all_sum - sum(sorted(rem1)[:2])
        return max(a, b)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
