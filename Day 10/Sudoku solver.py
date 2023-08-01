Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.



class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        
        def isValid(board:List[List[str]], row:int, col:int, val:str) -> bool:
            
            for i in range(0, 9):
                if board[i][col]==val: return False
                if board[row][i]==val: return False
            
            for limit in range(3, 10, 3):
                if row < limit: 
                    rowLimit = limit
                    break
            for limit in range(3, 10, 3):
                if col < limit:
                    colLimit = limit
                    break
            for i in range(rowLimit-3, rowLimit):
                for j in range(colLimit-3, colLimit):
                    if board[i][j]==val: return False
            
            return True

        def sudoku(board:List[List[str]]):
            for i in range(0, 9):
                for j in range(0, 9):
                    
                    if board[i][j] == ".":
                        for val in range(1, 10):
                            if isValid(board, i, j, str(val)):
                                board[i][j] = str(val)
                                if sudoku(board) == True:
                                    return True
                                board[i][j] = "."
                        return False
            return True
        sudoku(board)
        return board
    
    # time complexity: O(9^(n*n))
    # space complexity: O(n*n)
