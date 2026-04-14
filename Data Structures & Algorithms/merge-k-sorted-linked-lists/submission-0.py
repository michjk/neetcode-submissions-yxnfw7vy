# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq

class ListNodeWrapper:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        
        res = ListNode(0)
        cur = res
        min_heap = []

        for l in lists:
            if l:
                heapq.heappush(min_heap, ListNodeWrapper(l))
        
        while min_heap:
            node_wrapper = heapq.heappop(min_heap)
            cur.next = node_wrapper.node
            cur = cur.next

            if node_wrapper.node.next:
                heapq.heappush(min_heap, ListNodeWrapper(node_wrapper.node.next))

        return res.next