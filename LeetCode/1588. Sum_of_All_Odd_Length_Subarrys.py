# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

# Solution_1

def sumOddLengthSubarrays(self, A):
    n = len(A)
    res = 0
    for l in xrange(1, n + 1, 2):
        for i in xrange(n - l + 1):
            res += sum(A[i:i + l])
    return res