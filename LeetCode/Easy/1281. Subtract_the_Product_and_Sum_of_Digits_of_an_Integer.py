# https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

# Solution_1
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        product_num = 1
        sum_num = 0
        for i in str(n):
            product_num *= int(i)
            sum_num += int(i)
        return product_num - sum_num
    

# Solution_2 : Runtime 감소

from functools import reduce
from operator import mul 

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        A = list(map(int, str(n)))  # 문자열의 모든 요소를 int로 변환한 뒤, 다시 list로 만든다
        return reduce(mul, A) - sum(A)