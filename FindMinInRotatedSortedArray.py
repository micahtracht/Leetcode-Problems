class Solution:
    def findMin(self, nums: List[int]) -> int:
        '''
        Find the pivot.
        '''
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])
        
        l, r = 0, len(nums) - 1
        if nums[l] < nums[r]:
            return nums[l]
        
        res = float('inf')

        while l < r:
            m = (l + r)//2
            nl = nums[l]
            nm = nums[m]

            if nl <= nm:
                res = min(nl, res)
                l = m + 1
            else:
                res = min(nm, res)
                r = m - 1
        return min(res, nums[l])