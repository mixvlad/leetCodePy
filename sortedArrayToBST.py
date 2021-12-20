from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int], node = None) -> TreeNode:
        if not nums:
            return node
        if not node:
            node = TreeNode()
        lenn = len(nums)
        half = lenn // 2
        if lenn % 2 == 1:
            node.val = nums[half]
            node.left = self.sortedArrayToBST(nums[:half])
            node.right = self.sortedArrayToBST(nums[half+1:])
        else:
            node.val = nums[half]
            node.left = self.sortedArrayToBST(nums[:half])
            node.right = self.sortedArrayToBST(nums[half+1:])
        return node

    def test(self):
        assert self.sortedArrayToBST([-10,-3,0,5,9]) == TreeNode()

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")