# https://leetcode.com/problems/concatenation-of-array/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0 for i in range(2*n)] 
        
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans
    
    
# 다른 풀이
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums*2
        # return nums + nums