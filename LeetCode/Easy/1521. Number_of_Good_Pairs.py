# https://leetcode.com/problems/number-of-good-pairs/

# Solution_1
from typing import List

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if (nums[i] == nums[j]) and (i < j):
                    count += 1
        return count
    
    
# Solution_2
from collections import Counter  

class Solution:
    def numIdenticalPairs(self, nums):
       return sum(k * (k - 1) / 2 for k in Counter(nums).values())  # Counter(nums) : 요소의 개수가 많은 것부터 출력