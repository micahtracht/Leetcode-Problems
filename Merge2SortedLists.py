# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2

        curr = ListNode()
        dummy = curr

        while p1 or p2:
            if p1 and p2:
                if p1.val < p2.val:
                    curr.next = ListNode(p1.val)
                    curr = curr.next
                    p1 = p1.next
                else:
                    curr.next = ListNode(p2.val)
                    curr = curr.next
                    p2 = p2.next
            elif p1:
                curr.next = ListNode(p1.val)
                curr = curr.next
                p1 = p1.next
            else:
                curr.next = ListNode(p2.val)
                curr = curr.next
                p2 = p2.next
        return dummy.next