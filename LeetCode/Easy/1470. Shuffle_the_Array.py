# https://leetcode.com/problems/shuffle-the-array/submissions/

# Solution_1
class Solution:
    def shuffle(self, nums, n):
        new = []
        for i in range(len(nums)-n):
            new.append(nums[i])
            new.append(nums[i+n])
        return new
    
    
# Solution_2    
class Solution:
    def shuffle(self, nums, n):
        return list(sum(zip(nums[:n], nums[n:]), ()))
    
    
# Solution_3
from itertools import chain  # list, tuple 등을 연결

class Solution:
    def shuffle(self, nums, n):
        return list(chain(*zip(nums, nums[n:])))