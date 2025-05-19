class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
        Strategy (worked out w/ pen and paper + hints):
        -make adj list
        -do post order DFS
        '''
        adjList = {c: set() for word in words for c in word}
        
        for w1, w2 in zip(words, words[1:]):
            minLen = min(len(w1), len(w2))
            
            if w1[:minLen] == w2[:minLen] and len(w1) > len(w2): # invalid ordering
                return ""

            for j in range(minLen):
                if w1[j] != w2[j]:
                    adjList[w1[j]].add(w2[j])
                    break
        
        # Three-color post order DFS. White: not visited. Black: visited. Gray: processing
        W, G, B = 0, 1, 2
        visited = {c: W for c in adjList}
        res = []
        
        def dfs(c):
            if visited[c] == B:
                return False
            if visited[c] == G:
                return True # we detected a cycle

            visited[c] = G
            
            for neighbor in adjList[c]:
                if dfs(neighbor):
                    return True
            
            visited[c] = B
            
            res.append(c)
        
        for c in adjList:
            if dfs(c):
                return "" # detected a loop
        return "".join(res[::-1])