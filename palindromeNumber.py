class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        Solve w/o string:
        Go in reverse order and mult by 10, see if you get same.
        '''
        original = x
        reversed = 0
        while x > 0:
            digit = x % 10
            reversed = reversed * 10 + digit
            x //= 10
        return original == reversed
        