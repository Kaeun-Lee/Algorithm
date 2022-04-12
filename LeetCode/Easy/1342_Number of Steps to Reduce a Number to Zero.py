# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/

# Solution_1
class Solution:
    def numberOfSteps(self, num: int) -> int:
        count = 0
        while num != 0:
            if num % 2 == 0:
                num = num // 2
                count += 1
            else:
                num = num - 1
                count += 1 
        return count
    
    
# Solution_2  # 코드 단순화
class Solution:
    def numberOfSteps (self, num: int) -> int:
        cnt = 0
        while num > 0:
            if num % 2 == 0: 
                num //= 2
            else:
                num -= 1
            cnt += 1 
        return cnt 
    

# Solution_3  # 속도와 효율성이 좋지는 않음
class Solution:
    def numberOfSteps(self, num: int) -> int:
        cnt = 0
        while num > 0:
            cnt += 1 if num % 2 == 0 or num == 1 else 2
            num //= 2
        return cnt
    
    
    
sol = Solution()
test_case1 = sol.numberOfSteps(num = 14)
test_case2 = sol.numberOfSteps(num = 8)
test_case3 = sol.numberOfSteps(num = 123)
print(test_case1)  # 6
print(test_case2)  # 4
print(test_case3)  # 12