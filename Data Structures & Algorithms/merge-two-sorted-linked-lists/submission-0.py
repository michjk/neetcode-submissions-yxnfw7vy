# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        head = None
        cur1 = list1
        cur2 = list2
        prev = None
        while cur1 and cur2:
            cur = None
            if cur1.val < cur2.val:
                cur = cur1
                cur1 = cur1.next
            else:
                cur = cur2
                cur2 = cur2.next
            if not head:
                head = cur
            if prev:
                prev.next = cur
            prev = cur
        
        if cur1:
            prev.next = cur1
        if cur2:
            prev.next = cur2
        
        return head
            