class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        Here's the idea behind the algorithm:

        We should only compute the area of a rectangle when it is at its largest
        So we do so when it cannot be extended any further.

        We need to track when a rectangle could begin, which we do using the start variable
        We track the max area of the rectangles, and return it.

        So here's what each piece of the code does:
        maxArea is our result.
        Stack is our stack, which stores a pair: the starting index of the rectangle, and it's hegiht
        Note that by the starting index, and when it pops, we can find the width of it.

        Then we enumerate the indices and heights in the heights array.
        We initialize start to i, because it started at least at i.
        While the top element of the stack is taller, we know we can't extend it, so:
        we need to pop it, find the max area it was a part of (width = i - its start idx)
        and then set start to its start 
        (since it is taller, we know we can extend our rectangle back at least to it)

        But some may be left (could be extended all the way)
        so compute their areas, as (len(heights) - idx) * height,
        and return the max.
        '''
        maxArea = 0
        stack = []
        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h: # cannot be extended, pop elements
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                start = idx
            stack.append((start, h))
        
        for idx, height in stack:
            maxArea = max(maxArea, height * (len(heights) - idx))
        return maxArea