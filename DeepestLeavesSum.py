# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = [0, 0]

        def recursive(root: Optional[TreeNode], level: int, res: List[int]):
            if not root:
                return

            recursive(root.left, level + 1, res)
            recursive(root.right, level + 1, res)

            if level > res[1]:
                res[0] = root.val
                res[1] = level
            elif level == res[1]:
                res[0] += root.val

            return

        recursive(root, 0, res)

        return res[0]
    
    def test(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4),TreeNode(5)), TreeNode(3))
        assert self.deepestLeavesSum(root) == 9

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")
