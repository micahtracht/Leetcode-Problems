class Solution:
    def reverseBits(self, n: int) -> int:
        '''
        We get n in binary, we need to output the decimal number of n's value when reversed.
        Pretty easy:
        -Make it a string.
        -Iterate through that string from right to left and add powers of 2 each time.
        '''
        res = 0
        for i in range(32):
            res = (res << 1) | ((n >> i) & 1)
        return res