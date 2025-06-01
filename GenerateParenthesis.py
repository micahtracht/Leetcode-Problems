class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        We need to use recursion, time complexity will be
        roughly 2^n.

        How would I generate this sequence?
        I'd start with an open paren.
        Then at each step, if o > c and o < n, I could add an o or a c
        
        So I have a helper function that tracks:
        num o, num c, and n
        Update accordingly.

        What's my base case?
        if o + c == n:
            return
        
        Use a helper function to compute it
        Let's try implementing it
        '''
        res = []
        def genHelper(curr, numOpen, numClose):
            if numOpen + numClose == 2*n and numOpen == numClose:
                res.append(curr)
                return 
            
            if numOpen == n:
                currCopy = curr + ')'
                genHelper(currCopy, numOpen, numClose + 1)
            elif numOpen == numClose:
                currCopy = curr + '('
                genHelper(currCopy, numOpen + 1, numClose)
            else:
                currCopyOpen = curr + '('
                currCopyClose = curr + ')'
                genHelper(currCopyOpen, numOpen+1, numClose)
                genHelper(currCopyClose, numOpen, numClose+1)
        genHelper('', 0, 0)
        return res