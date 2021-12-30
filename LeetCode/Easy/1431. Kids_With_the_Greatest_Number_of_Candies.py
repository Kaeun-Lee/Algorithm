# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

# Solution_1
class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        result = []
        max_num = 0
        for i in range(len(candies)):
            if candies[i] > max_num:
                max_num = candies[i]
        for j in range(len(candies)):
            if candies[j] + extraCandies >= max_num:
                result.append(True)
            else:
                result.append(False)
        return result
    
    
# Solution_2
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        return [candy + extraCandies >= maxCandies for candy in candies]
    
    
# Soution_3
from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        high_enough = max(candies) - extraCandies
        return [candy >= high_enough for candy in candies]  # 계산 수를 줄임