from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        n = len(nums)
        a + b + c + d == target
        a, b, c, d are distinct
        
        find all
        
        Okay, how do I do this?
        I need to find the nums, not indices. That means sorting is possible.
        
        quadruplets have to be unique, meaning I should make them a tuple, sort them, and then add them to a set. Make a set a list at the end.
        
        Obviously O(n^4) works, but I can probably do much, much better. I'm unsure what's optimal, however (I'd guess, at best, it's O(nlogn) or worse).
        
        Let's see. I can solve 2 sum in O(n).
        3 sum to target I can solve in O(n^2) by running 2 sum on all n problems.
        So that gets me O(n^3) for this. But surely I can do better.
        
        Easier than that, I could iterate through n^2 pairs and run two sum (O(n)) giving me O(n^3). So that's somewhat better.
        
        What if I build a list of all n^2 sums of 2?
        Then I can iterate through it (O(n^2)) and check if other results exist within it. If so, add it to the list.
        
        The list would be: val -> [n[i], n[j]]
        Add duplicates freely because it's a set: they're removed automatically.
        
        So thats O(n^2). Can I do better? That would require me to abandon the list. Probably not? Maybe. I'll think on it.
        
        Here's the issue: It's very messy with a term appearing in the sum for val, and in target - val, which leads to duplicate answers. This is too hairy, probably a different approach is needed.
        
        Okay, say I sort it. Now what?
        Also say it's two pointers. Maybe that leads me somewhere.
        
        '''
        