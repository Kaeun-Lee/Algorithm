# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646

"""
    Q. Given an array, rotate the array to the right by k steps, where k is non-negative.
    Idea : k 번만큼, nums의 맨 뒤 숫자를 pop으로 뽑아낸 뒤 0번 idx에 삽입
"""

from typing import List

# Solution_1 -> 메모리 효율은 좋으나 속도가 느림
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for _ in range(k):
            a = nums.pop()
            nums.insert(0, a)

# Solution_2 -> 보조 공간 사용 / Time : O(n), Space : O(n) *n : num's length
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        auxArr = [0] * len(nums)
        k %= len(nums)
        for i in range(len(nums)):
            auxArr[(i + k) % len(nums)] = nums[i]
        nums[:] = auxArr

sol = Solution()
sol.rotate([1,2,3,4,5,6,7], 3)