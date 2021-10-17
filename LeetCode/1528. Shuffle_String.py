# https://leetcode.com/problems/shuffle-string/

# Solution_1
class Solution:  
    def restoreString(self, s: str, indices: List[int]) -> str:
        A = [''] * len(s)  # 문자열 길이만큼 자리 만들기
        for i, c in zip(indices, s):
            A[i] = c
        return ''.join(A)
    

# Solution_2
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res[''] * len(s)
        for i, v in enumerate(indices):
            res[v] = s[i]
        return ''.join(s)