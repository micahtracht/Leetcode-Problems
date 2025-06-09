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
        clones = {}

        def copyHelper(node):
            if not node or node in clones:
                return 
            
            clones[node] = Node(node.val)
            copyHelper(node.next)
            copyHelper(node.random)
        
        copyHelper(head)

        for orig, clone in clones.items():
            clone.next = clones.get(orig.next, None)
            clone.random = clones.get(orig.random, None)
        return clones.get(head, None)