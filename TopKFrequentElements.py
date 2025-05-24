from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        Use a heap?
        Let's remember what a heap does and how to use it.

        It's heapq.heap(push, pop, pushpop)(heap, element)

        A heap of size k (always a minheap) will store the k smallest elements
        If I try to add an element to the heap that is too big, it won't be added.
        The top element of the heap is always the smallest.

        This may be wrong, but let me try it and see if it's right.
        I'll use negatives to turn my minheap into a maxheap.

        The issue now is to determine whether to add an element.
        To solve this, I can keep two heaps:
        heapMax, which stores negatives, and heapMin, which stores the normal values.
        
        If I add to heapMax, I add to heapMin as well.

        Every parent node is less than or equal to its children for a minheap.

        In a maxheap, every parent node is >= its children.
        We have a maxheap.
        So the root of the maxheap is the biggest value (smallest frequency).
        So I can compare my new frequency to that, and if it is smaller (larger frequency), add it.
        
        Issue: my heap stores the frequencies, not the values themselves.
        So I could build an opposite list, freq -> num, and use that. Answer is always unique, so that works.
        
        Shoot. I'm not supposed to be negating at all.
        I got it all messed up.

        Let me thoroughly trace back my reasoning.

        I had said to use negatives because I wanted a maxheap.
        Why did I think I wanted a maxheap?
        I saw top k, and thought I wanted a heap that stored the largest elements.
        However, in a maxheap, you end up pushing off the largest elements and storing the smallest.
        That's the opposite of what we want.

        Consider what heapq.heappushpop does. In a maxheap, it'll add your new element, and kick out the largest!
        We want to kick out the smallest!
        So in a minheap, it'll behave exactly as we want.

        So with a minheap, here's how it works:
        Go through each frequency, add it to the minheap if it is larger than the top of the minheap (the smallest element)
        with heapq.heappushpop, that'll kick out the smallest, and add our next larger.
        Now our next smallest element is on the chopping block.

        Ah, so here's our next issue:
        freqToNum count be overridden, and that causes problems.
        We can have it store lists instead, and move through the list.
        But that could also cause problems: we might add more than k elements.
        Wait, that can't happen! Otherwise the answer wouldn't be unique.








        Okay, now time to rewrite the problem from scratch, with detailed comments.
        '''
        heap = []
        heapq.heapify(heap) # 1 p, not 2. This makes the heap into a heap.

        numToFreq = {}
        freqToNum = {}
        for num in nums: # build numToFreq list, use .get(num, 0) to default to 0
            numToFreq[num] = numToFreq.get(num, 0) + 1
        
        # used to recover answer later
        for num in numToFreq: # build freqToNum list, store lists so we don't have issues with overriding
            freq = numToFreq[num]
            if freq not in freqToNum:
                freqToNum[freq] = []
            freqToNum[freq].append(num)
        
        for num in numToFreq:
            freq = numToFreq[num]
            if len(heap) < k:
                heapq.heappush(heap, freq) # heap argument goes first
            else:
                if freq > heap[0]: # if we're larger than the smallest (minheap)
                    heapq.heappushpop(heap, freq) # pop smallest, add larger one
        
        res = set()
        while heap:
            for val in freqToNum[heapq.heappop(heap)]:
                res.add(val)
        return list(res)
        