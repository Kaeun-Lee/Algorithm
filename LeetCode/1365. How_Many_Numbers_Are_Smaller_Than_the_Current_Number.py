# https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/

# Solution_1
from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        smaller_count = []
        for i in nums:
            cnt = 0
            for j in nums:
                if i != j and i > j:
                    cnt += 1
                else:
                    continue
            smaller_count.append(cnt)
        return smaller_count
    

# Solution_2
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        for i,n in enumerate(sorted(nums)):
            if n not in dic:
                dic[n] = i
        return [dic[n] for n in nums] 