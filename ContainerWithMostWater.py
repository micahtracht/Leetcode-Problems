from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        We can run two pointers.

        Here's what we want to maximize:
        min(l, r) * (r - l)

        We could form two arrays, one of the max heights to the left,
        and one with the max heights to the right.

        Obviously this can be done in O(n^2). Why don't I start with that?

        Wait... that got accepted?
        Surely there's an O(n).
        Let me check the target time/space (this is O(n^2) time, O(1) space)

        Yeah, O(n) is optimal. I thought so. Let's find that solution.

        So we have two pointers, l and r.
        Maybe we try incrementing l if it'll help us, decrementing r if it'll help us.
        That feels wrong, but lets give it a shot.

        Okay, doesn't work.

        So the hint says to move the pointer at the smaller height value.
        Aha, that's because that pointer bounds us!
        Moving the larger would never help. It'll still be bounded, and we'll have less width.

        How would I have come up with that myself?
        I'd have said: okay, say we're at a position with l and r.
        I want to get more water. I know I'll have less width between.
        So to increase my water, I'd have to increase the heights.
        So I'll move the one with the smaller height, since that determines the water height.

        Or I'd have said: what's limiting me? Height is, so move the smaller one.

        Okay, now here's a detailed outline of the algorithm:
        Start with l = 0, r = len(h) - 1
        Move the one with the smaller height, and track your max.
        '''
        l, r = 0, len(heights) - 1
        res = -1

        while l < r:
            curr = min(heights[l], heights[r]) * (r - l)
            res = max(res, curr)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return res