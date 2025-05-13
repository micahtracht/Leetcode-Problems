from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        '''
        Constraints: O(n) time, O(1) space.
        
        Trivial to do in O(n^2) with 2 pointers and 2 fors.
        What about tortoise/hare? That works for find duplicate, maybe it works here.
        
        That's usually used for cycle detection, which doesn't seem important here.
        
        XOR can also be used to solve that problem. Maybe it's useful here. a xor a = 0 always, so we can find what isn't zero after the xor.
        XOR is commutative, so this works. Everything will cancel. Also, 0 xor a = a, so that works too.
        Great, xor every element and return what remains.
        '''
        curr = 0
        for num in nums:
            curr ^= num
        return curr