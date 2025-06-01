class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Sliding window algorithm.

        Remember how this works:
        for:
            while:
                stuff
        for l in range(len(s)):
            while no duplicates:
                r += 1
                res = max(res, r-l)
        That's it.

        Has O(n) time, O(m) space, where m is the number of unique characters.
        '''
        if len(s) == 0 or len(s) == 1:
            return len(s)
        
        res = 1
        for l in range(len(s)):
            letters = ""
            letters += s[l]
            r = l + 1
            while r < len(s) and s[r] not in letters:
                letters += s[r]
                res = max(res, r-l+1)
                r += 1
        return res
            
        