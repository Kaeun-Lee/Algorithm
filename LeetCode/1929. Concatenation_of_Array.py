# https://leetcode.com/problems/concatenation-of-array/

# Solution_1
class Solution:
    def getConcatenation(self, nums):
        n = len(nums)
        ans = [0 for i in range(2*n)] 
        
        for i in range(n):
            ans[i] = nums[i]
            ans[i+n] = nums[i]
        return ans
    
    
# Solutuion_2
class Solution:
    def getConcatenation(self, nums):
        return nums*2
        # return nums + nums