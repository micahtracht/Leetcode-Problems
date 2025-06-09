# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        '''
        We want:
        [0, n-1, 1, n02, 2, n-3, 3, n-4, 4 ...]

        So say we build a list of the nodes for easy accesss
        We pop from the start then from the end
        and add a .next at each step.

        Let's try that.

        The issue is that's O(n) space, I wonder how to do it in O(1)?
        Well, I would work backwards from the end and forwards from the start
        Besides the issue of going backwards, we'd need 2 for each
        so we don't get stuck

        Okay, so how do we go backwards?
        Feels recursive (backtracking), but I'd rather do it iteratively
        
        Okay, infinite loop. Let's trace it.
        Eh, let's focus on doing it O(1) to avoid the cycle stuff.

        Ah, hint was useful: reverse and merge second half
        '''
        if not head or not head.next:
            return
        # find second alf
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        second = slow.next
        slow.next = None # split the lists to avoid cycles
        
        # reverse second half
        prev = None
        curr = second
        while curr:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        
        second = prev
        
        # merge them
        first = head
        while first and second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
        

        

