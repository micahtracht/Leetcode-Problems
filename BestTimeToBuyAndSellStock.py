from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        Build list of max future prices by going in reverse order.
        Then check max diff.
        O(n) time, O(n) space.
        
        By thinking about it in the reverse, that is, whats our cheapest buy in, we can do it in O(n) time and O(1) space. We update our min price seen so far, and track the max difference.
        '''
        minPrice = prices[0]
        maxProfit = -1
        for price in prices:
            minPrice = min(minPrice, price)
            maxProfit = max(maxProfit, price - minPrice)
        return maxProfit