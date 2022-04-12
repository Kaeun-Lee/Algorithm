# https://leetcode.com/problems/shuffle-string/

# Solution_1
from typing import List
class Solution:  
    def restoreString(self, s: str, indices: List[int]) -> str:
        A = [''] * len(s)  # 문자열 길이만큼 자리 만들기
        for i, c in zip(indices, s):
            A[i] = c
        return ''.join(A)
    

# Solution_2
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for i, v in enumerate(indices):
            res[v] = s[i]
        return ''.join(res)
    
    

sol = Solution()
test_case1 = sol.restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3])
test_case2 = sol.restoreString(s = "abc", indices = [0,1,2])
print(test_case1)  # "leetcode"
print(test_case2)  # "abc"