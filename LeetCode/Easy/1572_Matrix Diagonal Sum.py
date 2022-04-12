# https://leetcode.com/problems/matrix-diagonal-sum/

# Solution_1
class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        pri = 0
        sec = 0
        tem = len(mat[0]) - 1
        odd = len(mat[0]) % 2

        for i in range(len(mat[0])): # 0,1,2 3개
            pri += mat[i][i]
            sec += mat[i][tem-i]

        if odd != 0:  
            result = pri + sec - mat[len(mat[0]) - odd][len(mat[0]) - odd]
        else:
            result = pri + sec
            
        return result
    
    
# Solution_2
from collections import Counter

class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        zipped = zip(*indices)
        rows, cols = Counter(next(zipped)), Counter(next(zipped))

        odd_rows = sum([1 for x in rows.values() if x & 1])
        odd_cols = sum([1 for x in cols.values() if x & 1])
        even_rows = n - odd_rows
        even_cols = m - odd_cols

        return odd_rows * even_cols + even_rows * odd_cols