from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Make a table of prefix and suffix products
        Use that to solve it
        '''
        prefix = []
        suffix = []
        
        prod = 1
        for num in nums:
            prod *= num
            prefix.append(prod)
        
        prod = 1
        for num in reversed(nums):
            prod *= num
            suffix.append(prod)
        suffix.reverse()
        
        output = [suffix[1]]
        for i in range(1, len(nums)-1):
            output.append(prefix[i-1] * suffix[i+1])
        output.append(prefix[len(nums)-2])

        return output