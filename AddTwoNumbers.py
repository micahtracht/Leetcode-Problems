# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Okay, they're reversed. Nothing stopping me from reading
        the numbers, and updating a sum as I go.

        For each number, sum = sum * 10
        sum += num

        Then I have the number. Easy enough to reverse it (can use string
        or reversing algo)

        then make it a linked list. Okay, let's do this
        '''
        num1 = 0
        curr = l1
        power = 0
        while curr:
            num1 += (10 ** power) * curr.val
            power += 1
            curr = curr.next
        
        num2 = 0
        curr = l2
        power = 0
        while curr:
            num2 += (10 ** power) * curr.val
            power += 1
            curr = curr.next
        
        total = num1 + num2
        #print(num1, num2, total)
        
        reversedDigits = []
        while total:
            digit = total % 10
            reversedDigits.append(digit)
            total //= 10
        
        #print(reversedDigits)

        if not reversedDigits:
            return ListNode(0)

        head = ListNode(reversedDigits[0])
        
        curr = head
        for i in range(1, len(reversedDigits)):
            curr.next = ListNode(reversedDigits[i])
            curr = curr.next
        return head
        
