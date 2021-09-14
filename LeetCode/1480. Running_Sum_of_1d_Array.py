# https://leetcode.com/problems/running-sum-of-1d-array/

# Solution_1
class Solution:
    def runningSum(self, nums):
        result = []
        emp = 0
        for i in range(len(nums)):
            result.append(emp + nums[i])
            emp = result[i]
        return result


# Solution_2
class Solution:
    def runningSum(self, nums):
        for i in range(1, len(nums)):
            nums[i] += nums[i-1]
        return nums
    
    
# Solution_3
from itertools import accumulate

class Solution:
    def runningSum(self, nums):
        return list(accumulate(nums))


