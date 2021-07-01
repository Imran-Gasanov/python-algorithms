def runningSum(nums):
    result = [0] * len(nums)
    result[0] = nums[0]
    for i in range(1, len(nums)):
        result[i] = result[i - 1] + nums[i]
    return result
