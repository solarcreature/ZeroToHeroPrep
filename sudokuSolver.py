def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        assert(self.backtrack(board,0,0))
        return
    
def backtrack(self,board,r,c):
    
    while board[r][c] != '.':
        c += 1
        if c == 9 :
            c, r = 0, r + 1
        if r == 9:
            return True
        
    for k in range(1,10):
        
        if self.isValidSudokuMove(board,r,c,str(k)):
            board[r][c] = str(k)
            
            if self.backtrack(board,r,c):
                return True
    board[r][c] = '.'
    return False

def isValidSudokuMove(self,board,r,c,number):
    
    for j in range(9):
        if board[r][j] == number:
            return False
    
    for i in range(9):
        if board[i][c] == number:
            return False
        
    blockRow = 3 * (r//3)
    blockCol = 3 * (c//3)
    
    for i in range(blockRow,blockRow + 3):
        for j in range(blockCol,blockCol + 3):
            if board[i][j] == number:
                return False
            
    return True