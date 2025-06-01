from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        As always with these questions, try to come up with a formula.

        For any point here, the amount of water trapped there is:
        min(max(l), max(r)) - h[i]

        So make two arrays:
        max to the left, and max to the right

        Go through and sum up those mins.

        Quick test:
        [0, 1, 3, 1]
        max left: [0, 1, 3, 3]
        max right: [3, 3, 3, 1]

        what does our max right give us?
        [1, 3, 3, 3]
        So I do have to reverse it.

        O(n) time and O(n) space.
        '''
        maxLeftList, maxRightList = [], []
        maxLeft = 0
        for h in height:
            maxLeft = max(maxLeft, h)
            maxLeftList.append(maxLeft)
        
        maxRight = 0
        for h in reversed(height):
            maxRight = max(maxRight, h)
            maxRightList.append(maxRight)
        maxRightList.reverse()

        res = 0
        for i in range(len(height)):
            res += min(maxLeftList[i], maxRightList[i]) - height[i]
        return res