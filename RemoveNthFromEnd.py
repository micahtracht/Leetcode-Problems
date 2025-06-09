# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        To remove a node, n,
        set n-1.next = n+1

        So here's an approach:
        find the length of the list
        then you know which to remove
        '''
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        if size == 1:
            return None
        
        toRemove = size - n

        if toRemove == 0:
            return head.next

        curr = head
        for i in range(toRemove - 1):
            curr = curr.next
        
        afterNode = curr
        afterNode = afterNode.next
        if afterNode:
            afterNode = afterNode.next
        curr.next = afterNode
        return head