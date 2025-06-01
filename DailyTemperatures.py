class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        So we try a stack

        Say we push temperatures onto the stack
        If we push a warmer temperature, pop until either the stack
        is empty, or there's a warmer temperature before hand.

        We can track when we add things to the stack,
        so when we pop we know the time and what to add to res.

        It's a bit like sliding window max in that way.
        '''
        stack = []
        res = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                _, idx = stack.pop()
                res[idx] = i - idx
            stack.append((temp, i))
        return res

