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
