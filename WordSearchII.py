from typing import List
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_end_of_word
    
    def contains_prefix(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        From my first try, here's what I know:
        We want to use a DFS approach to find the words.
        We also want to use a trie of some sort for efficient pruning.
        
        The naive approach is to search from every cell and find all the words from there.
        One cell can't be used more than once in a word, this is probably going to be a problem for my approach.
        I'd need to track visited with DFS, but if I'm finding multiple words in one search, that could be a problem.
        
        So the approach is to use DFS, if I have a prefix that doesn't exist (see trie), terminate that branch.
        I need to use a recursive approach where visited is a parameter that I pass in to avoid the conflicts.
        
        So:
        Recursive DFS with visited, prefix, r, and c as a parameter.
        Check for early termination with trie.
        Go from every square.
        
        Time complexity: O(m^2n^2), since we could find all mn tiles every mn search.
        
        Okay, Trie is now implemented. Let's chart the approach in finer detail:
        -Iterate through the board.
        -For each starting position, launch a recursive dfs(r, c, visited, prefix)
        -If the prefix doesn't exist, cancel.
        -Else, keep searching.
        
        Make sure to handle backtracking carefully.
        
        I'm noticing caching would save a lot of repeated work in searches in the tree.
        I could have DFS use the node it's at as a parameter and do the trie checks from there.
        That's creative, and could work.
        
        Let's implement!
        '''
        # Step 1: build trie
        tree = Trie()
        for word in words:
            tree.add(word)
        
        res = set()
        m, n = len(board), len(board[0])
        def dfs(row, col, visited, prefix, currNode):
            if currNode.is_end_of_word: # if we're done, add the finished  word
                res.add(prefix)
            
            neighbors = [[row+1, col], [row-1, col], [row, col+1], [row, col-1]]
            
            for r, c in neighbors:
                if 0 <= r < m and 0 <= c < n and (r,c) not in visited and board[r][c] in currNode.children:
                    visited.add((r, c))
                    prefix += board[r][c]
                    dfs(r, c, visited, prefix, currNode.children[board[r][c]])
                    visited.remove((r, c))
                    prefix = prefix[:len(prefix) - 1]
        
        for i in range(m):
            for j in range(n):
                ch = board[i][j]
                if ch not in tree.root.children:
                    continue
                visited = {(i,j)}
                dfs(i, j, visited, ch, tree.root.children[ch])
        return list(res)
                
