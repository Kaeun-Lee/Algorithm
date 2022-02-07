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