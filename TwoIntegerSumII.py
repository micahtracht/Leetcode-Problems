from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        '''
        Main constraint: O(1) space

        We're given that S is sorted in non-decreasing order
        We want index 1 < index 2, and s[i1] + s[i2] == target
        Only 1 sol.

        Two pointers. Easy.
        '''
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1, j+1] # 1 indexed
        
        return [-1, -1] # never reached