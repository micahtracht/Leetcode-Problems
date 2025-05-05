class Solution:
    def hammingWeight(self, n: int) -> int:
        '''
        Pretty easy:
        Just use the powers trick
        '''
        power = 0
        countOnes = 0
        
        while 2**power <= n:
            power += 1
        
        while n > 0:
            if 2**power <= n:
                n -= 2**power
                countOnes += 1
            power -= 1
        return countOnes