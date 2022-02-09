# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

# Solution_1
class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num = min(nums)
        max_num = max(nums)
        
        
        result = []
        for i in range(2, 30):
            if min_num == max_num:
                result.append(min_num)
                break
            else:
                if (min_num % i == 0) & (max_num % i == 0):
                    result.append(i)
                
                elif (min_num % min_num != 0) & (max_num % max_num != 0):
                    result.append(1)
                else:
                    result.append(1)
        return max(result)