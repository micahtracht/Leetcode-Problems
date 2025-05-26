from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        Let's go for O(n) time, O(1) space.
        Isn't it just counter trick?

        Track curr, and track counter.
        Add 1 to counter if we see curr. If we don't, subtract 1.
        If counter goes below 0 (or equals 0?) we change curr to whatever we're at.

        21212
        '''
        counter = 0
        curr = nums[0]
        for num in nums:
            if num == curr:
                counter +=1
            else:
                counter -= 1
            
            if counter < 0: # maybe <=
                curr = num
        return curr