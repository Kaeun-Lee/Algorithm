# https://leetcode.com/problems/find-target-indices-after-sorting-array/

# Solution_1
from typing import List

class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        result = []
        for i in range(len(nums)):
            if nums[i] == target:
                result.append(i)
        return result
    
    
# Solution_2
class Solution:
    def targetIndices(self, nums, target):
        lt_count, eq_count = 0, 0
        for n in nums:
            if n < target:     # target이 시작되는 index 위치를 구함
                lt_count += 1
            elif n == target:  # 반복되는 target의 개수로 range의 크기를 정함
                eq_count += 1
        return list(range(lt_count, lt_count+eq_count))
    
    
    
sol = Solution()
test_case1 = sol.targetIndices([1,2,5,2,3], 2)
test_case2 = sol.targetIndices([1,2,5,2,3], 3)
test_case3 = sol.targetIndices([1,2,5,2,3], 5)
print(test_case1)  # [1,2]
print(test_case2)  # [3]
print(test_case3)  # [4]