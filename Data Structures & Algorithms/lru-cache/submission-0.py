class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):
        prev = self.tail.prev
        nxt = self.tail
        node.prev = prev
        node.next = nxt
        nxt.prev = prev.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            node.val = value
        else:
            node = Node(key, value)
            if self.capacity == len(self.cache):
                lru_node = self.head.next
                self.remove(lru_node)
                del self.cache[lru_node.key]
            self.cache[key] = node
            self.insert(node)
            
        