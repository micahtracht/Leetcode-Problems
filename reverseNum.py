class Solution:
    def reverse(self, x: int) -> int:
        '''
        Reversing is easy, use % 10 then //= 10.
        However, the constraints of 32 bit integer are a little harder.
        Well, no it's not. I can build res and track how close I am to the limit as I go.
        
        If I could only store 32-bit integers, I could rely on integer overflows to flag issues as follows:
        if res is negative, then return 0. The issue with this is if I multiply by say 9, I could overflow multiple times.
        
        I could track the number of iterations, this'll tell me the order my number is on.
        order = numIter - numLeadingZeros
        
        If I know the order, here's what I know:
        If order > 10, then return 0.
        If order == 10:
        if digit > 2, return 0.
        If digit == 2 and res > 147483648, return 0.
        
        If isNeg, we have to be a little more careful, since we change the >= to >
        '''
        intmax, intmin = 2**31-1, -2**31
        
        res = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x:
            digit = x % 10
            x //= 10
            
            if res > intmax // 10 or (res == intmax//10 and digit > 7):
                return 0
            
            res = res * 10 + digit
        return sign * res