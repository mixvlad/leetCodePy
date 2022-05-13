# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        cur = root
        while cur:
            first, last = None, None
            
            while cur:
                if cur.left or cur.right:
                    if last:
                        last.next = cur.left or cur.right
                    else:
                        first = cur.left or cur.right

                    if cur.left and cur.right:
                        cur.left.next = cur.right
                    last = cur.right or cur.left

                cur = cur.next
            cur = first
        return root