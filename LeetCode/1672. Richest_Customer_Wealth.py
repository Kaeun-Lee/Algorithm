# https://leetcode.com/problems/richest-customer-wealth/

# Solution_1
from functools import reduce

class Solution:
    def maximumWealth(self, accounts):
        sum = [reduce(lambda x,y : x+y, i) for i in accounts]

        richest = 0
        for idx in range(len(sum)):
            if sum[idx] > richest:
                richest = sum[idx]
            else:
                continue
        return richest
    

# Solution_2
from functools import reduce

class Solution:
    def maximumWealth(self, accounts):
        richest = max([reduce(lambda x,y : x+y, i) for i in accounts])
        return richest
    

# Solution_3
class Solution:
  def maximumWealth(self, accounts):
    return max(map(sum, accounts))
