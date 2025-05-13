from typing import List
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
            '''
            Full disclosure: Used an editorial for the solution idea, I couldn't come up with it myself. The implementation is mine, however
            '''
            back, res = {}, []
            for i, w in enumerate(words):
                back[w[::-1]] = i
            for i, w in enumerate(words):
                if w in back and back[w] != i:
                    res.append([i, back[w]])
                    
                if w != "" and "" in back:
                    if w == w[::-1]:
                        res.append([i, back[""]])
                        res.append([back[""], i])
                    
                for j in range(len(w)):
                    if w[j:] in back and w[:j] == w[j-1::-1]:
                        res.append([back[w[j:]], i])
                    if w[:j] in back and w[j:] == w[:j-1:-1]:
                        res.append([i, back[w[:j]]])
            
            return res