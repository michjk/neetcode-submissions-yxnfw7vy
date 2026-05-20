"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        dummy = Node(0)
        hash_node = {}
        
        cur = head
        prev = dummy
        while cur != None:
            new_node = Node(cur.val)
            hash_node[cur] = new_node
            prev.next = new_node
            prev = new_node
            cur = cur.next
        
        cur_old = head
        cur_new = dummy.next
        while cur_old != None:
            if cur_old.random:
                cur_new.random = hash_node[cur_old.random]
            cur_old = cur_old.next
            cur_new = cur_new.next
        
        return dummy.next

            


        