# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

# Solution_1
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        res = 0
        for l in range(1, n + 1,2):     # l = 1, 3, 5.. 
            for i in range(n - l + 1):  # 0-5, 0-3, 0-1
                res += sum(arr[i:i + l])  # 0:1, 1:2.. / 0:3, 1:4.. / 0:5
        return res
    
    
# Solution_2 -> 속도 빠름
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        return sum(((i + 1) * (len(arr) - i) + 1) // 2 * a for i, a in enumerate(arr))