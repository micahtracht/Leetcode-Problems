from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        We need to use backtracking to solve this.
        The basic approach is this: Fill in a valid number at a position, keep going until we have no more valid numbers to use.
        Once we reach that, we know our current solution can't be right, so we backtrack.

        Now how exactly do we implement this?
        I'll probably want a helper function for what moves are valid on a square given a board.
        That's not too hard to build.

        Then from there, how exactly does the backtracking structure work?
        Place a number down, call a solvinghelper on the new board.

        If no numbers available, we backtrack.
        So does the call look like:
        Place number
        Call solveHelper
        Remove number

        And our base cases are:
        if solved, return board
        if no moves, return None

        So:
        place number
        if solveHelper == None:
            remove number
        else:
            return solveHelper's call
        
        Okay, let's try it I guess.
        """
        def updateRowCol(row, col):
            if col == 8:
                return (row+1, 0)
            return (row, col + 1)

        row_used = [set() for _ in range(9)]
        col_used = [set() for _ in range(9)]
        box_used = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    row_used[r].add(val)
                    col_used[c].add(val)
                    box_used[(r//3) * 3 + (c // 3)].add(val)


        def solveHelper(board, row, col):
            if row == 9:
                return board
            
            newRow, newCol = updateRowCol(row, col)
            if board[row][col] != '.':
                return solveHelper(board, newRow, newCol)

            box_idx = 3*(row // 3) + (col // 3)
            potentialMoves = [str(d) for d in range(1,10) if str(d) not in row_used[row] and str(d) not in col_used[col] and str(d) not in box_used[box_idx]]

            if not potentialMoves:
                return

            if row == 8 and col == 8 and (potentialMoves or board[8][8] != '.'):
                if potentialMoves:
                    board[8][8] = str(potentialMoves[0])
                return board
            
            for move in potentialMoves:
                d = str(move)
                board[row][col] = d
                row_used[row].add(d)
                col_used[col].add(d)
                box_used[box_idx].add(d)
                returnVal = solveHelper(board, newRow, newCol)
                if returnVal:
                    return returnVal
                board[row][col] = '.'
                row_used[row].remove(d)
                col_used[col].remove(d)
                box_used[box_idx].remove(d)
            return None
        
        return solveHelper(board, 0, 0)

sol = Solution()
board = [[".",".",".",".",".",".",".",".","."],[".","9",".",".","1",".",".","3","."],[".",".","6",".","2",".","7",".","."],[".",".",".","3",".","4",".",".","."],["2","1",".",".",".",".",".","9","8"],[".",".",".",".",".",".",".",".","."],[".",".","2","5",".","6","4",".","."],[".","8",".",".",".",".",".","1","."],[".",".",".",".",".",".",".",".","."]]
print(sol.solveSudoku(board))