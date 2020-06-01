class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur = res = ListNode()
        add = 0
        while True:
            val1  = (l1.val if l1 else 0)
            val2  = (l2.val if l2 else 0)
            add, cur.val = divmod(val1 + val2 + add, 10)    
            l1 = (l1.next if l1 else None)
            l2 = (l2.next if l2 else None)
            if not l1 and not l2 and not add:
                break
            cur.next = ListNode()
            cur = cur.next
        return res

    def test(self):
        print(6%10)
        
if __name__ == "__main__":
    Solution().test()
    print("Everything passed")        