class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        Here's how we do it:

        We can find how long it takes to eat a certain pile:
        size / k, rounded up

        So the sum(piles/k rounded up) is the number of hours.

        Then we perform binary search to find k:
        start l = 0, r = sum(piles), and binary search from there.
        '''
        def calculateHours(piles, k):
            total = 0
            for pile in piles:
                total += (pile + k - 1) // k
            return total

        l, r = 1, max(piles)
        res = r
        while l <= r:
            m = (l + r)//2
            hours = calculateHours(piles, m)

            if hours <= h:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res
        
