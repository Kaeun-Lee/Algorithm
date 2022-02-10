# https://leetcode.com/problems/find-greatest-common-divisor-of-array/

# Solution_1 -> Time Limit Exceeded
# class Solution:
#     def findGCD(self, nums):
#         min_num = min(nums)
#         max_num = max(nums)
        
#         if max_num % min_num == 0: # 최댓값이 최솟값으로 나눠지는 경우, 최솟값이 최대공약수
#             return min_num
#         else:                      # 최댓값이 최솟값으로 나눠지지 않는 경우 최솟값을 절반으로 나누며 최솟값을 찾음
#             tmp = min_num
#             while tmp > 0:
#                 tmp = min_num - 1
#                 if  (tmp >= min_num) & (max_num % tmp == 0):
#                     return min_num 
#             return 1


# Solution_2
class Solution:
    def findGCD(self, nums):
        min_num = min(nums)
        max_num = max(nums)
        
        if max_num % min_num == 0:
            return min_num
        else:
            remain = max_num % min_num  # 나머지 값
            while True:
                if remain != 0 : 
                    if min_num % remain == 0:
                        print(min_num, remain)
                        return remain
                    else:
                        min_num = remain
                        remain = min_num % remain
                        
                        print(min_num, remain)
                else:
                    break   
            return 1