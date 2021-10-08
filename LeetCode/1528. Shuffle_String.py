# https://leetcode.com/problems/shuffle-string/

# Solution_1
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        A = [''] * len(s)
        for i, c in zip(indices, s):
            A[i] = c
        return "".join(A)