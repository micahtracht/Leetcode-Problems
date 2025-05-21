from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Sort and use two pointers.
        We need to sort and keep track of the original indices.
        
        So we make a sorted indices list which is sorted with the key being the val in nums
        Then we make a new list out of that.
        
        Comes out to O(nlogn).
        
        Faster method (O(n)) is using a hashmap as you go. So you iterate through, build a hashmap, check as you go.
        '''
        seen = {} # val -> index
        for i, num in enumerate(nums):
            if target - num in seen:
                return [i, seen[target-num]]
            seen[num] = i