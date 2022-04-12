# https://leetcode.com/problems/range-sum-of-bst/

# Solution_1
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.root = root
        self.low = low
        self.high = high