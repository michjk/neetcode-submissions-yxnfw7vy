# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        cur_1 = l1
        cur_2 = l2
        res = ListNode()
        prev = res
        carry = 0
        while cur_1 and cur_2:
            total = cur_1.val + cur_2.val + carry
            rem = total % 10
            carry = total // 10
            prev.next = ListNode(val=rem)
            prev = prev.next
            cur_1 = cur_1.next
            cur_2 = cur_2.next
        
        long_cur = cur_1 or cur_2
        while long_cur:
            total = long_cur.val + carry
            rem = total % 10
            carry = total // 10
            prev.next = ListNode(val=rem)
            prev = prev.next
            long_cur = long_cur.next

        if carry:
            prev.next = ListNode(val=carry)
        
        return res.next

        
