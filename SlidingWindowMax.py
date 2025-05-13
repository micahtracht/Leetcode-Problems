from collections import deque
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        Brute force checking is easy, but it's O(nk-k^2). O(n) is possible, however.
        Wait, let's just use a deque with size 3! I've tried this problem so many times, but just thought of this since I'm working on replay buffers lmao... well let's try it.
        No, that alone doesn't work.
        
        What I could maybe do though is take a queue that is always in increasing order. Whatever element I lose when I move I remove from that queue, and I add to it as I push elements.
        The element at the top is my maximum.
        That's just a monotonic queue.
        '''
        res = []
        l = r = 0
        q = deque() # indices
        
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            
            # if left oob, remove left val
            if l > q[0]:
                q.popleft()
            
            if r > k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res