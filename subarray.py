def subarraysDivByK(nums, k):
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


print(subarraysDivByK([4, 5, 0, -2, -3, 1], 5))

