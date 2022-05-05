from typing import Optional

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right





class Solution:
    def inorderTraversalRec(self, res: List[int], root: Optional[TreeNode]) -> List[int]:
        if root is not None:
            if root.left != None:
                res = self.inorderTraversalRec(res, root.left)
                
            res.append(root.val)
            
            if root.right != None:
                res = self.inorderTraversalRec(res, root.right)
            
                
        return res

    def preorderTraversalRec(self, res: List[int], root: Optional[TreeNode]) -> List[int]:
        if root is not None:
            res.append(root.val)

            if root.left != None:
                res = self.preorderTraversalRec(res, root.left)
                
            
            
            if root.right != None:
                res = self.preorderTraversalRec(res, root.right)
            
                
        return res
    
    def postorderTraversalRec(self, res: List[int], root: Optional[TreeNode]) -> List[int]:
        if root is not None:
            

            if root.left != None:
                res = self.postorderTraversalRec(res, root.left)
                
            
            
            if root.right != None:
                res = self.postorderTraversalRec(res, root.right)
            
            res.append(root.val)
                
        return res
        
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root != None:
            res = self.inorderTraversalRec(res, root)
        return res
    
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root != None:
            res = self.preorderTraversalRec(res, root)
        return res
    
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if root != None:
            res = self.postorderTraversalRec(res, root)
        return res

    def test(self):
        assert self.inorderTraversal(None) == []
        
          

    
if __name__ == "__main__":
  Solution().test()
  print("Everything passed")

        