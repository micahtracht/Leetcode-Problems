class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        newS = ""
        for c in s:
            #print(c)
            if c in 'abcdefghijklmnopqrstuvwxyz0123456789':
                newS += c
        #print(newS)
        l, r = 0, len(newS) - 1
        while l < r:
            if newS[l] != newS[r]:
                return False
            l += 1
            r -= 1
        return True