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
        for i,n in enumerate(sorted(nums)): # [1,2,2,3,8]
            if n not in dic:
                dic[n] = i                  # {0:0, 1:1, 3:2, 8:4}
        return [dic[n] for n in nums] 
    
    
    
sol = Solution()
test_case1 = sol.smallerNumbersThanCurrent(nums = [8,1,2,2,3])    
test_case2 = sol.smallerNumbersThanCurrent(nums = [6,5,4,8])   
test_case3 = sol.smallerNumbersThanCurrent(nums = [7,7,7,7])   
print(test_case1)  # [4,0,1,1,3]
print(test_case2)  # [2,1,0,3]
print(test_case3)  # [0,0,0,0]