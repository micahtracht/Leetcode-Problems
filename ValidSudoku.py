from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        '''
        Hashsets probs

        Keep 28 hashmaps:
        9 for each row
        9 for each col
        9 for each 3x3 square

        Add accordingly to them. If you get an element already in one, it isn't valid.
        Otherwise, it is.

        O(81) = O(1).
        '''
        n, m = len(board), len(board[0]) # 9, 9
        
        rows = [set() for i in range(n)]
        cols = [set() for i in range(n)]
        boxes = [set() for i in range(n)]

        for r in range(n):
            for c in range(m):
                boxIndex = (3*(r//3) + (c//3))
                if board[r][c] == '.':
                    continue
                val = int(board[r][c])
                if val in boxes[boxIndex] or val in rows[r] or val in cols[c]:
                    return False
                boxes[boxIndex].add(val)
                rows[r].add(val)
                cols[c].add(val)
        return True
