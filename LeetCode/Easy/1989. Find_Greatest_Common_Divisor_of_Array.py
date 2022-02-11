# https://leetcode.com/problems/find-greatest-common-divisor-of-array/
       
# Solution_1 -> Euclidean Algorithm
class Solution:
    def findGCD(self, nums):
        a, b = min(nums), max(nums)
        while a:             # a가 0이 되면 False
            a, b = b % a, a  # a : 큰 수를 작은 수로 나눈 나머지, b : 작은 수
        return b
    

# Solution_2
class Solution:
    def findGCD(self, nums):
        min_num = min(nums)
        max_num = max(nums)

        for i in range(min_num, 0, -1):  # 1씩 감소
            if max_num % i == 0 and min_num % i == 0:
                return i
            

# Solution_3 -> python 내장함수 중 math 모듈 사용. 속도가 더 빠름
from math import gcd

class Solution:
    def findGCD(self, nums):
        min_num = min(nums)
        max_num = max(nums)
        
        return gcd(min_num, max_num)



sol = Solution()
test_case1 = sol.findGCD([2,5,6,9,10])
test_case2 = sol.findGCD([7,5,6,8,3])
test_case3 = sol.findGCD([3,3])
print(test_case1)  # 2
print(test_case2)  # 1
print(test_case3)  # 3