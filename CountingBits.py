class Solution():
    def countBits(self, n):
        '''
        For 1, n return array where:
        arr[i] = number of bits in i+1 (size = n)
        We can use bin.
        
        Okay, what about w/o bin? It's not too hard to basically simulate bin myself.
        And they do follow a recursive pattern, but probably simulating bin is best.
        '''
        res = []
        startingPower = 0
        for i in range(n+1):
            countOnes = 0
            while 2**startingPower <= i:
                startingPower += 1
            power = startingPower
            num = i
            while num > 0:
                if (2**power) <= num:
                    num -= (2**power)
                    countOnes += 1
                power -= 1
            res.append(countOnes)
        return res