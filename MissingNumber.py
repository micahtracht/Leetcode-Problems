class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        Nums has all numbers [0, n] except one (len(nums) = n). Return what is missing.
        
        Let's aim for O(n) time, O(1) space. Should be possible. Of course, O(n) time and O(n) space with a hashmap is trivial.
        
        What if I try a binary-esque pattern? What about XORs?
        We could use a set trick:
        Sum nums. That sum would have result n(n+1)/2 if every number were present (or 0 were missing). We can then deduce what number is missing as:
        n(n+1)/2 - sum(nums).
        '''
        return (len(nums) * (len(nums)+1)//2) - sum(nums)