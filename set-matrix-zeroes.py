def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows, cols = len(matrix), len(matrix[0])
    firstRow = False
    firstCol = False
    
    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] == 0:
                if row == 0:
                    firstRow = True
                if col == 0:
                    firstCol = True
                matrix[row][0] = matrix[0][col] = 0
                
    for row in range(1,rows):
        for col in range(1,cols):
            if matrix[0][col] == 0 or matrix[row][0] == 0:
                matrix[row][col] = 0
            
    if firstRow:
        for col in range(cols):
            matrix[0][col] = 0
            
    if firstCol:
        for row in range(rows):
            matrix[row][0] = 0