from typing import List


class Solution:
    '''
    Approach:
    If we start with saying how long the next string is, we get to the end, and can then tell from there.
    So we do length, #, and that lets us not get tricked by any special characters, since we never even consider them.
    '''
    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded += str(len(string))
            encoded += '#'
            encoded += string
        return encoded

    '''
    Goal here is to recover the strings. Probably we'll read the length of the string, up until the #, and in that range we read what the string is and append it. Then repeat.
    '''
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        i = 0
        strs = []
        while i < len(s):
            toAdd = ""
            size = 0
            while s[i] != '#':
                digit = int(s[i])
                size *= 10
                size += digit
                i += 1
            upTo = i + size
            while i < upTo:
                i += 1
                toAdd += s[i]
            i += 1
            strs.append(toAdd)
        return strs