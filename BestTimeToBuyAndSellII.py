from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        I can buy and immediately sell on the same day.

        So just... Buy if the next day is higher, and sell if the next day is lower?
        Why doesn't that work?

        Let's try it and see... should work.
        '''
        profit = 0
        hasStock = False
        for i in range(len(prices) - 1):
            if not hasStock and prices[i] < prices[i+1]:
                hasStock = True
                profit -= prices[i]
            if hasStock and prices[i] > prices[i+1]:
                hasStock = False
                profit += prices[i]
        
        if hasStock:
            profit += prices[-1]
        return profit
