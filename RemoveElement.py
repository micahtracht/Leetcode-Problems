from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        '''
        Keep track of when we delete for a total count
        '''
        found = False
        total = len(nums)
        i = 0
        while i < len(nums):
            num = nums[i]
            if num == val:
                del nums[i]
                i -= 1
                total -= 1
            i += 1
        return total