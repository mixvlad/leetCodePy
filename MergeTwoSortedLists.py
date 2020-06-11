import sys
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = res = ListNode()
        
        while l1 or l2:
            val1 = (l1.val if l1 else -sys.maxsize)
            val2 = (l2.val if l2 else -sys.maxsize)
            if val1 > val2:
                cur.next = l1
                cur = l1
                l1 = l1.next
            else:
                cur.next = l2
                cur = l2
                l2 = l2.next
        return res.next
    
    
    def test(self):
        # assert self.removeDuplicates([1,1,2]) == 2
        assert self.mergeTwoLists(ListNode(1), ListNode(2)) == ListNode(0)
        

if __name__ == "__main__":
    Solution().test()
    print("Everything passed")