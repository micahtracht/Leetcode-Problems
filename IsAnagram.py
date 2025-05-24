class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        '''
        Hashmap with letter counts. See if the hashmaps are the same.
        '''
        sLetters = {} # letter -> freq
        tLetters = {} # letter -> freq
        for c in s:
            sLetters[c] = sLetters.get(c, 0) + 1
        for c in t:
            tLetters[c] = tLetters.get(c, 0) + 1
        if set(sLetters.keys()) != set(tLetters.keys()):
            return False
        
        for c in sLetters:
            if c not in tLetters:
                return False
            else:
                if tLetters[c] != sLetters[c]:
                    return False
        return True