from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        '''
        Just combine them. Iterate twice. Easy.
        '''
        ans = []
        for num in nums:
            ans.append(num)
        for num in nums:
            ans.append(num)
        
        return ans