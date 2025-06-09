'''
Hashmap for most of the functions
Use a LL for the orders?
Use a DLL. 
'''
class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # key -> Node pointer

        # Left = LRU, Right = MRU
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    
    # remove from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev  = prev

    
    # insert at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = node
        node.prev = prev
        node.next = nxt
        nxt.prev  = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.insert(node)

        if len(self.cache) > self.cap:
            # evict LRU
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



