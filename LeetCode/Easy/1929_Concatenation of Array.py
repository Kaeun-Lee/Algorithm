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
        
        

sol = Solution()
test_case1 = sol.getConcatenation(nums = [1,2,1])
test_case2 = sol.getConcatenation(nums = [1,3,2,1])
print(test_case1)  # [1,2,1,1,2,1]
print(test_case2)  # [1,3,2,1,1,3,2,1]