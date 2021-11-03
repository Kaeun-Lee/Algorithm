# https://leetcode.com/problems/split-a-string-in-balanced-strings/

# Solution_1
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r_cnt = 0
        l_cnt = 0
        cnt = 0

        for i in s:
            if i == 'R':
                r_cnt += 1
            else:
                l_cnt += 1
            if r_cnt == l_cnt:
                cnt += 1

        return cnt


# Solution_2 -> 속도 빠름
from itertools import accumulate as acc  # list(acc([1,2,3])) -> [1, 3, 6]

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        return list(acc(1 if c == 'L' else -1 for c in s)).count(0)  # 리스트 중 0의 개수
    

# Solution_3
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = cnt = 0         
        for c in s:
            cnt += c == 'L'  # True + True = 2
            cnt -= c == 'R'
            res += cnt == 0
        return res  
    
    
# Solution_4
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        res = cnt = 0         
        for c in s:
            cnt += 1 if c == 'L' else -1            
            if cnt == 0:
                res += 1
        return res  