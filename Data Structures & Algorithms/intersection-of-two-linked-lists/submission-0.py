# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        cur_a = headA
        cur_b = headB
        mp = set()

        while cur_a != None:
            mp.add(cur_a)
            cur_a = cur_a.next
        
        while cur_b != None:
            if cur_b in mp:
                return cur_b
            cur_b = cur_b.next
        
        return None