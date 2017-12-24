def checkSubarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if len(nums) < 2:
        return False
    
    if k == 0:
        for index in range(len(nums)-1):
            if nums[index] == 0 and nums[index+1] == 0:
                    return True
        return False
    
    k = abs(k)
    
    for i in range(len(nums)):
        if nums[i] <= k:
            index = i+1
            temp = nums[i]
            while index < len(nums):
                temp+= nums[index]
                if temp % k == 0:
                    return True
                index += 1
    return False

print(checkSubarraySum([23, 2, 4, 6, 7], -6))
print(checkSubarraySum([0, 0], 0))
print(checkSubarraySum([0], 0))
print(checkSubarraySum([1, 1], 1))