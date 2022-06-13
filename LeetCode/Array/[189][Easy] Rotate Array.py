# https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/646

"""
    조건 : 1. Do not return anything, modify nums in-place instead.
           2. Do it in-place with O(1) extra space.
"""

from typing import List

# Solution_1 -> pop & insert / 메모리 효율은 좋으나 속도가 느림
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for _ in range(k):
            a = nums.pop()
            nums.insert(0, a)


# Solution_2 -> Use Auxiliary Space
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        nums_copy = nums.copy()
        for i in range(len(nums)):
            nums[i] = nums_copy[i - k]


# Solution_3 -> Use Auxiliary Space / Time : O(n), Space : O(n) (*n : num's length)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        auxArr = [0] * len(nums)  # add another auxiliary to store moved nums
        k %= len(nums)
        for i in range(len(nums)):
            auxArr[(i + k) % len(nums)] = nums[i]
        nums[:] = auxArr          # replace nums[:] = auxiliary


# Solution_4 -> *Reverse Array / Time : O(2n) = O(n), Space : O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        self.reverseArray(0, len(nums) - 1, nums)  # Step 1: Reverse nums => [7, 6, 5, 4, 3, 2, 1]
        self.reverseArray(0, k - 1, nums)          # Step 2: Reverse from 0 ~ k and k+1 ~ len(nums) => nums = [5, 6, 7, 1, 2, 3, 4]
        self.reverseArray(k, len(nums) - 1, nums)

    def reverseArray(self, left, right, array):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left += 1
            right -= 1


# Solution_5 -> Cyclic Move elements / Time : O(n), Space : O(1)
# *Explanation : We divided nums by k groups, and each time we move one group to desire index.
#                Once counter == len(nums) means we have moved all elements so the array is in-place moved.
# *Eventually we have to move array's element n times, so we set a counter move = 0
#  -> Step 1 : Start from index 0
#              => Each time we move elements to index (current + k), 
#                 once we found our current == start, means we finished a cycle group
#     Step 2 : Increase start by 1 => Back to Step 1
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        start, move = 0, 0
        while move < len(nums):
            current, prev = start, nums[start]
            while True:
                nextIdx = (current + k) % len(nums)
                nums[nextIdx], prev = prev, nums[nextIdx]
                current = nextIdx
                move += 1
                if current == start:
                    break
            start += 1


# test_case
Solution().rotate([1, 2, 3, 4, 5, 6, 7], 3)  # [5, 6, 7, 1, 2, 3, 4]
Solution().rotate([-1, -100, 3, 99], 2)      # [3, 99, -1, -100]